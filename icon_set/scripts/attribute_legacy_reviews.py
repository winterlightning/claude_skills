#!/usr/bin/env python3
"""Attribute existing unnamed icon decisions to Hina, as confirmed by the owner.

Runs automatically once when the gallery initializes its configured database.
The CLI remains available for diagnostics (dry run by default).
Only approved, disapproved and rejected review rows are affected. Existing names,
Ready rows, feedback authors and primitive/reference review records are preserved.
Historical dashboard entries retain the original saved decision timestamp and
explicitly record the attribution source and time. Re-running is a no-op.
"""
import argparse
from collections import Counter
from contextlib import closing
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import sqlite3
import tempfile

SOURCE = 'attribute_legacy_reviews.py'
MIGRATION = '2026-09-16-legacy-reviewers-hina-v1'
# When the owner confirmed the attribution. Later unnamed reviews are not Hina
# by default, even if a production deployment is updated much later.
LEGACY_CUTOFF = '2026-09-16T07:40:44.370999+00:00'


def targets(db):
    return db.execute("""SELECT icon,svg_sha256,status,updated_at FROM reviews
        WHERE TRIM(COALESCE(updated_by,''))=''
        AND status IN ('approve','pending','disapprove','rejected')
        AND (julianday(updated_at)<=julianday(?) OR julianday(updated_at) IS NULL)
        ORDER BY updated_at,icon,svg_sha256""", (LEGACY_CUTOFF,)).fetchall()


def attribute(db, rows):
    """Run inside a caller-owned transaction; never invent missing review dates."""
    assigned_at = datetime.now(timezone.utc).isoformat()
    for icon, sha, status, stamp in rows:
        try:
            datetime.fromisoformat(stamp.replace('Z', '+00:00'))
        except (ValueError, TypeError, AttributeError):
            raise ValueError('Invalid saved review date for ' + icon) from None
        result = db.execute("""UPDATE reviews SET updated_by='hina'
            WHERE icon=? AND svg_sha256=? AND status=? AND updated_at=?
            AND TRIM(COALESCE(updated_by,''))=''""", (icon, sha, status, stamp))
        if result.rowcount != 1:
            raise ValueError('Review changed during attribution: ' + icon)
        db.execute('''INSERT INTO activity_log(username,action,icon,details,created_at)
            VALUES ('hina','review',?,?,?)''', (icon, json.dumps({
                'status': status, 'svg_sha256': sha, 'source': SOURCE, 'migration': MIGRATION,
                'attributed_at': assigned_at,
                'attribution_basis': 'Owner confirmed existing unnamed reviews belong to Hina',
                'legacy_snapshot': True,
            }), stamp))


def run(database, apply=False):
    database = Path(database).resolve()
    with closing(sqlite3.connect(database.as_uri() + ('?mode=rw' if apply else '?mode=ro'),
                                 uri=True, timeout=30, isolation_level=None)) as db:
        db.execute('BEGIN IMMEDIATE' if apply else 'BEGIN')
        try:
            has_ledger = db.execute("SELECT 1 FROM sqlite_master WHERE type='table' AND name='review_data_migrations'").fetchone()
            if has_ledger and db.execute('SELECT 1 FROM review_data_migrations WHERE id=?', (MIGRATION,)).fetchone():
                db.rollback()
                return {'records': 0, 'icons': 0, 'statuses': {}, 'applied': False, 'already_applied': True}
            rows = targets(db)
            result = {'records': len(rows), 'icons': len({row[0] for row in rows}),
                      'statuses': dict(Counter(row[2] for row in rows)), 'applied': False}
            if not apply:
                db.rollback()
                return result
            if rows:
                fd, filename = tempfile.mkstemp(prefix=database.name + '.before-hina-attribution-',
                                                suffix='.sqlite3', dir=database.parent)
                os.close(fd)
                with closing(sqlite3.connect(database.as_uri() + '?mode=ro', uri=True)) as source, \
                        closing(sqlite3.connect(filename)) as backup:
                    source.backup(backup)
                    if backup.execute('PRAGMA quick_check').fetchone()[0] != 'ok':
                        raise ValueError('Database backup failed its integrity check.')
                result['backup'] = filename
            attribute(db, rows)
            if targets(db):
                raise ValueError('Unnamed reviews remain; changes rolled back.')
            db.execute('''CREATE TABLE IF NOT EXISTS review_data_migrations (
                id TEXT PRIMARY KEY, applied_at TEXT NOT NULL, details TEXT NOT NULL)''')
            result['applied'] = True
            db.execute('INSERT INTO review_data_migrations VALUES (?,?,?)',
                       (MIGRATION, datetime.now(timezone.utc).isoformat(), json.dumps(result)))
            db.commit()
            return result
        except BaseException:
            db.rollback()
            raise


def migrate(database):
    """Use the actual server database, including a custom --database path."""
    return run(database, apply=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--database', type=Path, required=True)
    parser.add_argument('--apply', action='store_true')
    args = parser.parse_args()
    print(json.dumps(run(args.database, args.apply), indent=2))
