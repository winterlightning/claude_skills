#!/usr/bin/env python3
"""Turn a feedback snapshot into a SQL file for the D1 schema.

    python3 cloud/migrate/build_d1_import.py cloud/exports/feedback-<time>.sqlite3
    wrangler d1 execute pictographic --local  --file cloud/exports/d1-import.sql   # rehearsal
    wrangler d1 execute pictographic --remote --file cloud/exports/d1-import.sql   # cutover

Workflow tables keep their columns in D1, so rows copy across unchanged. Uploaded icons are
also written to the catalog tables (``icons`` and ``revisions``) that the Worker reads.
Statements stay under D1's 100 KB limit. Only ever reads the snapshot.
"""
from __future__ import annotations

import argparse
from contextlib import closing
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import sqlite3

ROOT = Path(__file__).resolve().parents[2]
SCHEMA = ROOT / 'cloud' / 'worker' / 'migrations' / '0001_schema.sql'
MAX_STATEMENT = 90_000

# Workflow tables in dependency order (split_requests before pending_briefs).
TABLES = ('admin_sessions', 'reviews', 'feedback', 'activity_log', 'work_results', 'icon_types', 'icon_flags',
          'split_requests', 'pending_briefs', 'upload_families', 'uploaded_icons', 'primitive_status',
          'primitive_briefs', 'primitive_symbol_links', 'progression_imports', 'progression_reviews',
          'review_data_migrations')


def literal(value) -> str:
    if value is None:
        return 'NULL'
    if isinstance(value, bool):
        return str(int(value))
    if isinstance(value, (int, float)):
        return repr(value)
    if isinstance(value, bytes):
        return "X'" + value.hex() + "'"
    return "'" + str(value).replace("'", "''") + "'"


def d1_columns(table: str) -> list[str]:
    """Column names of a table in the D1 schema file."""
    with closing(sqlite3.connect(':memory:')) as scratch:
        scratch.executescript(SCHEMA.read_text())
        return [row[1] for row in scratch.execute(f'PRAGMA table_info("{table}")')]


KEYS = {'progression_reviews': ('path',), 'work_results': ('icon', 'svg_sha256', 'stage'),
        'uploaded_icons': ('icon',), 'feedback': ('id',), 'activity_log': ('id',)}
CHUNK = 60_000


def oversized(table: str, columns: list[str], row) -> list[str]:
    """A row too big for one statement: insert it with its largest text cut short, then append the rest."""
    keys = KEYS.get(table)
    if not keys:
        raise ValueError(f'a {table} row is larger than D1 allows in one statement and the table has no known key')
    big = max((i for i, v in enumerate(row) if isinstance(v, str)), key=lambda i: len(row[i]))
    text = row[big]
    first = list(row)
    first[big] = text[:CHUNK]
    statements = [f'INSERT INTO "{table}" ({", ".join(columns)}) VALUES (' + ', '.join(literal(v) for v in first) + ');']
    where = ' AND '.join(f'{k} = {literal(row[columns.index(k)])}' for k in keys)
    for start in range(CHUNK, len(text), CHUNK):
        statements.append(f'UPDATE "{table}" SET {columns[big]} = {columns[big]} || {literal(text[start:start + CHUNK])} WHERE {where};')
    return statements


def inserts(table: str, columns: list[str], rows) -> list[str]:
    """Multi-row INSERTs, each under MAX_STATEMENT bytes."""
    head = f'INSERT INTO "{table}" ({", ".join(columns)}) VALUES '
    statements, values, size = [], [], len(head)
    for row in rows:
        value = '(' + ', '.join(literal(v) for v in row) + ')'
        if len(head) + len(value) > MAX_STATEMENT:
            statements += oversized(table, columns, row)
            continue
        if values and size + len(value) + 2 > MAX_STATEMENT:
            statements.append(head + ',\n'.join(values) + ';')
            values, size = [], len(head)
        values.append(value)
        size += len(value) + 2
    if values:
        statements.append(head + ',\n'.join(values) + ';')
    return statements


def build(snapshot: Path) -> tuple[list[str], dict]:
    statements, counts = [], {}
    with closing(sqlite3.connect(snapshot.resolve().as_uri() + '?mode=ro', uri=True)) as source:
        existing = {row[0] for row in source.execute("SELECT name FROM sqlite_master WHERE type='table'")}
        for table in TABLES:
            if table not in existing:
                counts[table] = 0
                continue
            wanted = d1_columns(table)
            present = {row[1] for row in source.execute(f'PRAGMA table_info("{table}")')}
            columns = [c for c in wanted if c in present]
            order = 'rowid' if table not in ('reviews',) else 'icon, svg_sha256'
            rows = source.execute(f'SELECT {", ".join(columns)} FROM "{table}" ORDER BY {order}').fetchall()
            counts[table] = len(rows)
            statements += inserts(table, columns, rows)
        # Uploads also appear in the catalog the Worker reads.
        uploads = source.execute('SELECT icon, record, svg FROM uploaded_icons ORDER BY rowid').fetchall() \
            if 'uploaded_icons' in existing else []
    icon_rows, revision_rows = [], []
    now = datetime.now(timezone.utc).isoformat()
    for key, record_text, svg in uploads:
        record = json.loads(record_text)
        digest = record.get('svg_sha256') or hashlib.sha256(svg.encode()).hexdigest()
        icon_rows.append((key, record.get('icon_id'), record.get('name'), record.get('family'), record.get('category'),
                          record.get('profile'), record.get('canvas_size'), digest, record.get('preview_url'), '[]', 1,
                          record_text, record.get('created_at') or now))
        revision_rows.append((digest, key, svg, 'upload', record.get('created_at') or now))
    statements += inserts('icons', ['key', 'icon_id', 'name', 'family', 'category', 'profile', 'canvas_size', 'svg_sha256',
                                    'preview_url', 'original_sources', 'uploaded', 'record', 'pushed_at'], icon_rows)
    seen, unique = set(), []
    for row in revision_rows:
        if row[0] not in seen:
            seen.add(row[0])
            unique.append(row)
    statements += inserts('revisions', ['svg_sha256', 'icon', 'svg', 'origin', 'created_at'], unique)
    counts['icons (uploads)'] = len(icon_rows)
    counts['revisions (uploads)'] = len(unique)
    return statements, counts


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('snapshot', type=Path)
    parser.add_argument('--out', type=Path, default=ROOT / 'cloud' / 'exports' / 'd1-import.sql')
    args = parser.parse_args(argv)
    statements, counts = build(args.snapshot)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text('\n'.join(statements) + '\n', encoding='utf-8')
    (args.out.with_suffix('.counts.json')).write_text(json.dumps(counts, indent=2) + '\n')
    print(json.dumps({'out': str(args.out), 'statements': len(statements), 'bytes': args.out.stat().st_size,
                      'counts': counts}, indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
