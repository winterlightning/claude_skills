#!/usr/bin/env python3
"""Restore every rejected icon in the production catalog to Pending.

Standard library only. Defaults to a read-only dry run. --apply creates a SQLite
backup and performs one transaction, matching the app's Restore behavior.
Use the database and icons.json from the same production deployment.
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
        'split_requests': {'icon', 'svg_sha256', 'active', 'restored_by', 'restored_at'},
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


def rejected_keys(db, catalog):
    rejected = {row[0] for row in db.execute("SELECT DISTINCT icon FROM reviews WHERE status='rejected'")}
    splits = db.execute('SELECT icon,svg_sha256 FROM split_requests WHERE active=1').fetchall()
    targets = (rejected & catalog.keys()) | {
        key for key, sha in splits if catalog.get(key) == sha
    }
    return sorted(targets), sorted(rejected - catalog.keys())


def backup_database(database):
    stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    fd, filename = tempfile.mkstemp(prefix=database.name + '.before-pending-' + stamp + '-',
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


def run(database, catalog_path, actor, apply=False):
    database, catalog_path = Path(database).resolve(), Path(catalog_path).resolve()
    if not database.is_file():
        raise ValueError('Database does not exist: ' + str(database))
    if not actor.strip():
        raise ValueError('Actor must not be empty.')
    catalog, catalog_bytes = read_catalog(catalog_path)
    backup = None
    with closing(connect_existing(database, writable=apply)) as db:
        db.execute('BEGIN IMMEDIATE' if apply else 'BEGIN')
        try:
            validate_schema(db)
            keys, absent = rejected_keys(db, catalog)
            print('Database:', database)
            print('Rejected catalog icons to restore:', len(keys))
            if absent:
                print('Skipped rejected records outside the current catalog:', len(absent))
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
            for key in keys:
                sha = catalog[key]
                db.execute('UPDATE split_requests SET active=0,restored_by=?,restored_at=? '
                           'WHERE icon=? AND svg_sha256=? AND active=1', (actor, now, key, sha))
                db.execute("UPDATE reviews SET status='pending',updated_by=?,updated_at=? "
                           "WHERE icon=? AND status='rejected'", (actor, now, key))
                db.execute("INSERT INTO reviews(icon,svg_sha256,status,updated_at,updated_by) "
                           "VALUES (?,?,'pending',?,?) ON CONFLICT(icon,svg_sha256) DO UPDATE SET "
                           "status='pending',updated_at=excluded.updated_at,updated_by=excluded.updated_by",
                           (key, sha, now, actor))
                # 'restore' is required: the API otherwise changes pending parents
                # with published variants back to Re-generated automatically.
                db.execute('INSERT INTO activity_log(username,action,icon,details,created_at) '
                           "VALUES (?,'restore',?,?,?)", (actor, key, json.dumps({
                               'svg_sha256': sha, 'source': 'rejected_to_pending.py',
                               'previous_status': 'rejected', 'status': 'pending',
                           }), now))
            if catalog_path.read_bytes() != catalog_bytes:
                raise ValueError('Catalog changed during the operation. Rolled back; retry after the build finishes.')
            if rejected_keys(db, catalog)[0]:
                raise ValueError('Rejected catalog icons remain. Rolled back.')
            db.commit()
        except BaseException:
            db.rollback()
            if backup:
                print('Changes rolled back. Backup retained:', backup, file=sys.stderr)
            raise
    print('Restored', len(keys), 'icons to Pending. Refresh the review page; no rebuild is needed.')
    return len(keys), backup


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--database', type=Path, required=True, help='Production feedback.sqlite3')
    parser.add_argument('--catalog', type=Path, required=True, help='Matching production gallery/icons.json')
    parser.add_argument('--actor', required=True, help='Your name for the audit log, e.g. jakes')
    parser.add_argument('--apply', action='store_true', help='Back up the database and apply the changes')
    args = parser.parse_args()
    try:
        run(args.database, args.catalog, args.actor, args.apply)
    except (OSError, ValueError, sqlite3.Error) as error:
        print('Error:', error, file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
