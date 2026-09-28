#!/usr/bin/env python3
"""Take a consistent, read-only snapshot of a feedback database.

    python3 cloud/migrate/export_snapshot.py                         # ./feedback.sqlite3
    python3 cloud/migrate/export_snapshot.py --database /srv/pictographic/state/feedback.sqlite3

The source is opened with ``mode=ro`` and copied with SQLite's backup API, so a running
server can keep writing while the copy is taken and the source file is never modified.
The snapshot lands in cloud/exports/ (git-ignored). Prints the row count of every table.
"""
from __future__ import annotations

import argparse
from contextlib import closing
from datetime import datetime, timezone
import json
from pathlib import Path
import sqlite3
import sys

ROOT = Path(__file__).resolve().parents[2]
EXPORTS = ROOT / 'cloud' / 'exports'


def snapshot(database: Path, target: Path) -> dict:
    database = database.resolve()
    before = database.stat()
    target.parent.mkdir(parents=True, exist_ok=True)
    with closing(sqlite3.connect(database.as_uri() + '?mode=ro', uri=True, timeout=30)) as source, \
            closing(sqlite3.connect(target)) as copy:
        source.backup(copy)
        tables = [row[0] for row in copy.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")]
        counts = {table: copy.execute(f'SELECT count(*) FROM "{table}"').fetchone()[0] for table in tables}
        check = copy.execute('PRAGMA integrity_check').fetchone()[0]
    after = database.stat()
    if (before.st_mtime_ns, before.st_size) != (after.st_mtime_ns, after.st_size) and not _has_wal(database):
        print('note: the source changed while copying (a live server wrote to it); the snapshot is still consistent.',
              file=sys.stderr)
    return {'source': str(database), 'snapshot': str(target), 'integrity': check, 'counts': counts,
            'taken_at': datetime.now(timezone.utc).isoformat()}


def _has_wal(database: Path) -> bool:
    return database.with_name(database.name + '-wal').exists()


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--database', type=Path, default=ROOT / 'feedback.sqlite3')
    parser.add_argument('--out', type=Path, help='snapshot path (default cloud/exports/feedback-<time>.sqlite3)')
    args = parser.parse_args(argv)
    if not args.database.is_file():
        parser.error(f'{args.database} does not exist')
    stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    target = args.out or EXPORTS / f'feedback-{stamp}.sqlite3'
    if target.exists():
        parser.error(f'{target} already exists; choose another --out')
    report = snapshot(args.database, target)
    if report['integrity'] != 'ok':
        print(json.dumps(report, indent=2))
        print('error: the snapshot failed its integrity check', file=sys.stderr)
        return 1
    print(json.dumps(report, indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
