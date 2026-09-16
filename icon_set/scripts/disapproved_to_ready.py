#!/usr/bin/env python3
"""Return every icon disapproved by one reviewer to Ready.

The review UI's Disapprove button stores status='pending', so this moves the
'pending' reviews that reviewer owns back to 'ready'. Standard library only.
Defaults to a read-only dry run. --apply creates a SQLite backup and performs
one transaction. Use the database and icons.json from the same production
deployment.

Rejected icons are left alone: the app refuses review changes on them and
/api/reviews would show them as rejected regardless. Feedback entries are not
deleted, so the Feedback page still lists the requested changes.
"""
import argparse
from contextlib import closing
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import sqlite3
import sys
import tempfile


def connect_existing(path, writable=False):
    return sqlite3.connect(path.as_uri() + ('?mode=rw' if writable else '?mode=ro'),
                           uri=True, timeout=30, isolation_level=None)


def validate_schema(db):
    required = {
        'reviews': {'icon', 'svg_sha256', 'status', 'updated_at', 'updated_by'},
        'split_requests': {'icon', 'svg_sha256', 'active'},
        'feedback': {'icon', 'svg_sha256'},
        'activity_log': {'username', 'action', 'icon', 'details', 'created_at'},
    }
    for table, columns in required.items():
        found = {row[1] for row in db.execute('PRAGMA table_info(' + table + ')')}
        if not columns <= found:
            raise ValueError('Unsupported database schema: ' + table + ' is missing ' +
                             ', '.join(sorted(columns - found)))


def read_catalog(path):
    raw = path.read_bytes()
    data = json.loads(raw)
    if not isinstance(data, dict) or not isinstance(data.get('icons'), list):
        raise ValueError('Catalog must be the production gallery/icons.json file.')
    failed = data.get('failed_icons', [])
    if not isinstance(failed, list):
        raise ValueError('Invalid failed_icons list in catalog.')
    catalog = {}
    for row in data['icons'] + failed:
        key, sha = row.get('key'), row.get('svg_sha256')
        if not isinstance(key, str) or not key or not isinstance(sha, str) or not sha:
            raise ValueError('Every catalog icon must have a key and svg_sha256.')
        if key in catalog and catalog[key] != sha:
            raise ValueError('Conflicting revisions for catalog icon: ' + key)
        catalog[key] = sha
    return catalog, raw


def disapproved_keys(db, catalog, reviewer):
    """Current-revision icons this reviewer disapproved, plus what was skipped and why."""
    rows = db.execute('SELECT icon, svg_sha256 FROM reviews '
                      'WHERE status=? AND LOWER(COALESCE(updated_by,?))=LOWER(?)',
                      ('pending', '', reviewer)).fetchall()
    # 'rejected' outranks every other review state, on the icon or on this revision.
    rejected = {row[0] for row in db.execute("SELECT DISTINCT icon FROM reviews WHERE status='rejected'")}
    splits = {(row[0], row[1]) for row in db.execute('SELECT icon,svg_sha256 FROM split_requests WHERE active=1')}
    targets, skipped = [], {'absent': [], 'superseded': [], 'rejected': []}
    for key, sha in rows:
        if key not in catalog:
            skipped['absent'].append(key)
        elif catalog[key] != sha:
            # A newer build replaced the revision that was disapproved; the stale
            # row no longer drives the icon's status, so leave it as history.
            skipped['superseded'].append(key)
        elif key in rejected or (key, sha) in splits:
            skipped['rejected'].append(key)
        else:
            targets.append((key, sha))
    return sorted(set(targets)), {name: sorted(set(keys)) for name, keys in skipped.items()}


def backup_database(database):
    stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    fd, filename = tempfile.mkstemp(prefix=database.name + '.before-ready-' + stamp + '-',
                                    suffix='.sqlite3', dir=database.parent)
    os.close(fd)  # mkstemp creates a private, unique file (mode 0600).
    backup = Path(filename)
    try:
        # A separate reader can take a consistent snapshot while our writer holds
        # BEGIN IMMEDIATE. Backing up the writer connection itself would block.
        with closing(connect_existing(database)) as source, closing(sqlite3.connect(backup)) as target:
            source.backup(target)
            if target.execute('PRAGMA quick_check').fetchone()[0] != 'ok':
                raise ValueError('Backup failed its integrity check.')
    except BaseException:
        backup.unlink(missing_ok=True)
        raise
    return backup


def run(database, catalog_path, actor, reviewer='jakes', apply=False):
    database, catalog_path = Path(database).resolve(), Path(catalog_path).resolve()
    if not database.is_file():
        raise ValueError('Database does not exist: ' + str(database))
    if not actor.strip() or not reviewer.strip():
        raise ValueError('Actor and reviewer must not be empty.')
    actor, reviewer = actor.strip(), reviewer.strip()
    catalog, catalog_bytes = read_catalog(catalog_path)
    backup = None
    with closing(connect_existing(database, writable=apply)) as db:
        db.execute('BEGIN IMMEDIATE' if apply else 'BEGIN')
        try:
            validate_schema(db)
            targets, skipped = disapproved_keys(db, catalog, reviewer)
            keys = [key for key, _ in targets]
            print('Database:', database)
            print('Disapproved by ' + reviewer + ', moving to Ready:', len(keys))
            for label, note in (('rejected', 'rejected icons (restore them first)'),
                                ('superseded', 'older revisions replaced by a newer build'),
                                ('absent', 'records outside the current catalog')):
                if skipped[label]:
                    print('Skipped ' + note + ':', len(skipped[label]))
            for key in keys[:10]:
                print('  ' + key)
            if len(keys) > 10:
                print('  ... and', len(keys) - 10, 'more')
            if not apply or not keys:
                db.rollback()
                print('Dry run: no changes made. Add --apply to execute.' if not apply else 'Nothing to change.')
                return len(keys), None
            backup = backup_database(database)
            print('Backup:', backup, flush=True)
            now = datetime.now(timezone.utc).isoformat()
            for key, sha in targets:
                db.execute('UPDATE reviews SET status=?,updated_by=?,updated_at=? WHERE icon=? AND svg_sha256=? '
                           'AND status=? AND LOWER(COALESCE(updated_by,?))=LOWER(?)',
                           ('ready', actor, now, key, sha, 'pending', '', reviewer))
                db.execute('INSERT INTO activity_log(username,action,icon,details,created_at) '
                           "VALUES (?,'review',?,?,?)", (actor, key, json.dumps({
                               'svg_sha256': sha, 'source': 'disapproved_to_ready.py',
                               'previous_status': 'pending', 'status': 'ready',
                               'disapproved_by': reviewer,
                           }), now))
            if catalog_path.read_bytes() != catalog_bytes:
                raise ValueError('Catalog changed during the operation. Rolled back; retry after the build finishes.')
            if disapproved_keys(db, catalog, reviewer)[0]:
                raise ValueError('Disapproved catalog icons remain. Rolled back.')
            db.commit()
        except BaseException:
            db.rollback()
            if backup:
                print('Changes rolled back. Backup retained:', backup, file=sys.stderr)
            raise
    print('Moved', len(keys), 'icons to Ready. Refresh the review page; no rebuild is needed.')
    print('Their feedback entries were kept and still appear on the Feedback page.')
    return len(keys), backup


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--database', type=Path, required=True, help='Production feedback.sqlite3')
    parser.add_argument('--catalog', type=Path, required=True, help='Matching production gallery/icons.json')
    parser.add_argument('--actor', required=True, help='Your name for the audit log, e.g. jakes')
    parser.add_argument('--disapproved-by', default='jakes', dest='reviewer',
                        help="Whose disapprovals to move (default: jakes)")
    parser.add_argument('--apply', action='store_true', help='Back up the database and apply the changes')
    args = parser.parse_args()
    try:
        run(args.database, args.catalog, args.actor, args.reviewer, args.apply)
    except (OSError, ValueError, sqlite3.Error) as error:
        print('Error:', error, file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
