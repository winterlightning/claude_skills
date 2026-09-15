#!/usr/bin/env python3
"""TODO / SKIP decisions for Pictographic primitives, shared by the gallery and agents.

python3 icon_set/scripts/primitive_status.py summary
python3 icon_set/scripts/primitive_status.py list --category computers --status todo --format json
python3 icon_set/scripts/primitive_status.py skip --reason container --note "glyph in a screen" UUID [UUID ...]
python3 icon_set/scripts/primitive_status.py skip --reason text_number --from-file uuids.txt
python3 icon_set/scripts/primitive_status.py todo UUID [UUID ...]

TODO is the default: a primitive without a row is TODO, and marking TODO deletes
the row. GENERATED is never stored; it comes from the catalog
(primitives_catalog.py) and wins over SKIP, which is then reported as a conflict.
Every change is written to the gallery database's activity log.
"""
from __future__ import annotations

import argparse
import collections
from contextlib import closing
from datetime import datetime, timezone
import json
from pathlib import Path
import re
import sqlite3
import sys

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

REASONS = ('combination', 'container', 'text_number', 'other')
STATUSES = ('todo', 'skip')
MAX_BATCH = 500
MAX_NOTE = 2000
_UUID = re.compile(r'^[0-9a-f]{8}(?:-[0-9a-f]{4}){3}-[0-9a-f]{12}$')


def init_primitive_status(connection) -> None:
    connection.execute(f'''CREATE TABLE IF NOT EXISTS primitive_status (
        uuid TEXT PRIMARY KEY, status TEXT NOT NULL CHECK(status IN ('skip')),
        reason TEXT NOT NULL CHECK(reason IN ({",".join(repr(r) for r in REASONS)})),
        note TEXT NOT NULL DEFAULT '', updated_by TEXT NOT NULL, updated_at TEXT NOT NULL)''')


def validate(uuids, status, reason=None, note='', known=None) -> tuple[list[str], str | None, str]:
    if status not in STATUSES:
        raise ValueError("Status must be 'todo' or 'skip'.")
    if not isinstance(uuids, list) or not uuids:
        raise ValueError('Choose at least one primitive.')
    if len(uuids) > MAX_BATCH:
        raise ValueError(f'Update at most {MAX_BATCH} primitives at a time.')
    cleaned = []
    for uid in uuids:
        if not isinstance(uid, str) or not _UUID.match(uid.strip().lower()):
            raise ValueError(f'Invalid primitive id: {uid!r}')
        uid = uid.strip().lower()
        if known is not None and uid not in known:
            raise ValueError(f'Unknown primitive: {uid}')
        if uid not in cleaned:
            cleaned.append(uid)
    note = note or ''
    if not isinstance(note, str) or len(note) > MAX_NOTE:
        raise ValueError(f'Notes must be text of at most {MAX_NOTE} characters.')
    note = note.strip()
    if status == 'skip':
        if reason not in REASONS:
            raise ValueError('Choose a skip reason: ' + ', '.join(REASONS) + '.')
        if reason == 'other' and not note:
            raise ValueError("A skip for 'other' needs a note explaining why.")
    else:
        reason, note = None, ''
    return cleaned, reason, note


def set_status(connection, uuids, status, reason=None, note='', *, user, record, known=None) -> dict:
    """Apply one decision to many primitives inside the caller's transaction.
    `record` is deploy.record_activity; unchanged primitives are not logged."""
    uuids, reason, note = validate(uuids, status, reason, note, known)
    now = datetime.now(timezone.utc).isoformat()
    changed = []
    for uid in uuids:
        current = connection.execute('SELECT reason, note FROM primitive_status WHERE uuid=?', (uid,)).fetchone()
        if status == 'todo':
            if current is None:
                continue
            connection.execute('DELETE FROM primitive_status WHERE uuid=?', (uid,))
            record(connection, user, 'primitive_todo', 'primitive:' + uid, previous_reason=current[0])
        else:
            if current == (reason, note):
                continue
            connection.execute(
                "INSERT INTO primitive_status(uuid,status,reason,note,updated_by,updated_at) VALUES (?,'skip',?,?,?,?) "
                'ON CONFLICT(uuid) DO UPDATE SET reason=excluded.reason, note=excluded.note, '
                'updated_by=excluded.updated_by, updated_at=excluded.updated_at',
                (uid, reason, note, user, now))
            record(connection, user, 'primitive_skip', 'primitive:' + uid, reason=reason, note=note)
        changed.append(uid)
    return {'status': status, 'reason': reason, 'changed': len(changed), 'unchanged': len(uuids) - len(changed)}


def load_status(connection) -> dict:
    rows = connection.execute('SELECT uuid, status, reason, note, updated_by, updated_at FROM primitive_status')
    return {uid: {'status': status, 'reason': reason, 'note': note, 'updated_by': by, 'updated_at': at}
            for uid, status, reason, note, by, at in rows}


def effective(row: dict, decision: dict | None) -> str:
    return 'generated' if row.get('state') == 'generated' else 'skip' if decision else 'todo'


def merge(rows: list[dict], statuses: dict) -> list[dict]:
    merged = []
    for row in rows:
        decision = statuses.get(row['uuid'])
        merged.append({**row, 'status': effective(row, decision), 'decision': decision,
                       'conflict': bool(decision) and row.get('state') == 'generated'})
    return merged


def summarize(merged: list[dict]) -> dict:
    categories = collections.OrderedDict()
    for row in merged:
        counts = categories.setdefault(row['category'], collections.Counter())
        counts['total'] += 1
        counts[row['status']] += 1
        counts['build_failed'] += row.get('state') == 'build_failed'
        counts['conflict'] += row['conflict']
        if row['status'] == 'skip':  # a conflict counts as generated, not under its skip reason
            counts['skip_' + row['decision']['reason']] += 1
    overall = collections.Counter()
    for counts in categories.values():
        overall.update(counts)
    return {'overall': dict(overall), 'categories': {name: dict(counts) for name, counts in categories.items()}}


def filter_rows(merged, category=None, status=None, batch=None, reason=None):
    category = (category or '').lower()
    for row in merged:
        if category and row['category'].lower() != category:
            continue
        if status and status != 'all' and row['status'] != status:
            continue
        if batch and row['batch'] != batch:
            continue
        if reason and (row['decision'] or {}).get('reason') != reason:
            continue
        yield row


def _load_catalog(dist: Path) -> dict:
    path = dist / 'gallery' / 'primitives.json'
    if not path.is_file():
        raise SystemExit(f'error: {path} is missing; run icon_set/scripts/primitives_catalog.py first')
    return json.loads(path.read_text(encoding='utf-8'))


def main(argv=None) -> int:
    from icon_set.scripts.deploy import DEFAULT_DB, DEFAULT_DIST, init_database, record_activity
    from icon_set.scripts.primitives_catalog import primitives_root

    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--database', type=Path, default=DEFAULT_DB)
    parser.add_argument('--dist', type=Path, default=DEFAULT_DIST)
    commands = parser.add_subparsers(dest='command', required=True)
    commands.add_parser('summary', help='Counts per category and overall')
    listing = commands.add_parser('list', help='Primitives with their effective status')
    listing.add_argument('--category')
    listing.add_argument('--status', choices=('todo', 'skip', 'generated', 'all'), default='todo')
    listing.add_argument('--batch')
    listing.add_argument('--reason', choices=REASONS)
    listing.add_argument('--primitives', type=Path, help='Original primitives folder, for absolute file paths')
    listing.add_argument('--format', choices=('json', 'tsv', 'uuids'), default='json')
    for name in ('skip', 'todo'):
        command = commands.add_parser(name, help=f'Mark primitives {name.upper()}')
        command.add_argument('uuids', nargs='*')
        command.add_argument('--from-file', type=Path, help='One UUID per line')
        command.add_argument('--user', default='agent', help='Recorded as the actor in the activity log')
        if name == 'skip':
            command.add_argument('--reason', choices=REASONS, required=True)
            command.add_argument('--note', default='')
    args = parser.parse_args(argv)

    catalog = _load_catalog(args.dist)
    init_database(args.database)
    with closing(sqlite3.connect(args.database, timeout=10)) as connection:
        if args.command in ('skip', 'todo'):
            uuids = list(args.uuids)
            if args.from_file:
                uuids += [line.strip() for line in args.from_file.read_text().splitlines() if line.strip()]
            known = {row['uuid'] for row in catalog['rows']}
            total = collections.Counter()
            try:
                with connection:
                    for start in range(0, len(uuids), MAX_BATCH):
                        result = set_status(connection, uuids[start:start + MAX_BATCH], args.command,
                                            getattr(args, 'reason', None), getattr(args, 'note', ''),
                                            user=args.user, record=record_activity, known=known)
                        total.update(changed=result['changed'], unchanged=result['unchanged'])
            except ValueError as error:
                parser.exit(2, f'error: {error}\n')
            print(json.dumps({'status': args.command, **total}))
            return 0
        merged = merge(catalog['rows'], load_status(connection))
    if args.command == 'summary':
        print(json.dumps(summarize(merged), indent=2))
        return 0
    root = primitives_root(args.primitives)
    rows = list(filter_rows(merged, args.category, args.status, args.batch, args.reason))
    if args.format == 'uuids':
        print('\n'.join(row['uuid'] for row in rows))
    elif args.format == 'tsv':
        print('uuid\tstatus\tcategory\tbatch\tconcept\tfile')
        for row in rows:
            print('\t'.join([row['uuid'], row['status'], row['category'], row['batch'], row['concept'], str(root / row['path'])]))
    else:
        print(json.dumps([{**{k: row[k] for k in ('uuid', 'status', 'category', 'batch', 'concept', 'old_concept',
                                                   'state', 'models', 'decision', 'conflict')},
                           'file': str(root / row['path'])} for row in rows], ensure_ascii=False, indent=1))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
