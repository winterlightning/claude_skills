#!/usr/bin/env python3
"""Attribute existing unnamed icon decisions to Hina, as confirmed by the owner.

Dry run by default; --apply saves a database backup and updates one transaction.
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


def targets(db):
    return db.execute("""SELECT icon,svg_sha256,status,updated_at FROM reviews
        WHERE TRIM(COALESCE(updated_by,''))=''
        AND status IN ('approve','pending','disapprove','rejected')
        ORDER BY updated_at,icon,svg_sha256""").fetchall()


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
                'status': status, 'svg_sha256': sha, 'source': SOURCE,
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
            rows = targets(db)
            result = {'records': len(rows), 'icons': len({row[0] for row in rows}),
                      'statuses': dict(Counter(row[2] for row in rows)), 'applied': False}
            if not apply or not rows:
                db.rollback()
                return result
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
            db.commit()
            result['applied'] = True
            return result
        except BaseException:
            db.rollback()
            raise


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--database', type=Path, required=True)
    parser.add_argument('--apply', action='store_true')
    args = parser.parse_args()
    print(json.dumps(run(args.database, args.apply), indent=2))
