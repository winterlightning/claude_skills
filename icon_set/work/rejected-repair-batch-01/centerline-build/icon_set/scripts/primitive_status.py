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
UNSET = object()
SUB_POSITIONS = ('top-left', 'top', 'top-right', 'left', 'center', 'right', 'bottom-left', 'bottom', 'bottom-right')
_UUID = re.compile(r'^[0-9a-f]{8}(?:-[0-9a-f]{4}){3}-[0-9a-f]{12}$')


def init_primitive_status(connection) -> None:
    connection.execute(f'''CREATE TABLE IF NOT EXISTS primitive_status (
        uuid TEXT PRIMARY KEY, status TEXT NOT NULL CHECK(status IN ('skip')),
        reason TEXT NOT NULL CHECK(reason IN ({",".join(repr(r) for r in REASONS)})),
        note TEXT NOT NULL DEFAULT '', updated_by TEXT NOT NULL, updated_at TEXT NOT NULL)''')
    columns = {row[1] for row in connection.execute('PRAGMA table_info(primitive_status)')}
    for column in ('combination_brief', 'main_brief', 'sub_brief', 'sub_position'):
        if column not in columns:
            connection.execute(f'ALTER TABLE primitive_status ADD COLUMN {column} TEXT')
    # Migrate the old paired field once, retaining each component independently.
    for uid, value in connection.execute('SELECT uuid, combination_brief FROM primitive_status WHERE combination_brief IS NOT NULL').fetchall():
        brief = validate_brief(json.loads(value))
        main, sub = brief['components']
        connection.execute('UPDATE primitive_status SET main_brief=COALESCE(main_brief,?), sub_brief=COALESCE(sub_brief,?), combination_brief=NULL WHERE uuid=?',
                           (json.dumps(main, sort_keys=True), json.dumps(sub, sort_keys=True), uid))


def validate_component(component, field):
    if component is None:
        return None
    allowed = ('sub',) if field == 'sub_brief' else ('solo', 'container')
    if not isinstance(component, dict) or component.get('family') not in allowed:
        raise ValueError('The main brief must be solo/container; the sub brief must be sub.')
    item = {'family': component['family']}
    for key, limit in (('name', 200), ('description', MAX_NOTE)):
        value = component.get(key)
        if not isinstance(value, str) or not value.strip() or len(value) > limit:
            raise ValueError(f'Component {key} must be nonempty text of at most {limit} characters.')
        item[key] = value.strip()
    return item


def validate_brief(brief):
    """A saved plan for two independently generated components; null clears it."""
    if brief is None:
        return None
    if not isinstance(brief, dict) or brief.get('combination_type') not in ('container', 'side'):
        raise ValueError('Choose a container + sub or main + sub combination brief.')
    components = brief.get('components')
    if not isinstance(components, list) or len(components) != 2:
        raise ValueError('A combination brief needs exactly two components.')
    cleaned = []
    for index, component in enumerate(components):
        allowed = ('sub',) if index else ('container',) if brief['combination_type'] == 'container' else ('solo', 'container')
        if not isinstance(component, dict) or component.get('family') not in allowed:
            raise ValueError('Choose the correct family for each component: container/main first, sub second.')
        item = {'family': component['family']}
        for key, limit in (('name', 200), ('description', MAX_NOTE)):
            value = component.get(key)
            if not isinstance(value, str) or not value.strip() or len(value) > limit:
                raise ValueError(f'Component {key} must be nonempty text of at most {limit} characters.')
            item[key] = value.strip()
        cleaned.append(item)
    return {'combination_type': brief['combination_type'], 'components': cleaned}


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


def set_status(connection, uuids, status, reason=None, note='', *, user, record, known=None,
               combination_brief=UNSET, main_brief=UNSET, sub_brief=UNSET, sub_position=UNSET) -> dict:
    """Update either component independently; omitted fields preserve saved values."""
    uuids, reason, note = validate(uuids, status, reason, note, known)
    if combination_brief is not UNSET:
        if main_brief is not UNSET or sub_brief is not UNSET:
            raise ValueError('Use separate component fields or the legacy paired brief, not both.')
        paired = validate_brief(combination_brief)
        main_brief, sub_brief = paired['components'] if paired else (None, None)
    updates = {}
    for field, value in (('main_brief', main_brief), ('sub_brief', sub_brief)):
        if value is not UNSET:
            updates[field] = validate_component(value, field)
    if updates and (status != 'skip' or reason not in ('container', 'combination') or len(uuids) != 1):
        raise ValueError('Save a component brief for one skipped container or combination at a time.')
    if sub_position is not UNSET:
        if sub_position is not None and sub_position not in SUB_POSITIONS:
            raise ValueError('Choose a valid sub-icon position relative to the main icon.')
        if status != 'skip' or reason != 'combination' or len(uuids) != 1:
            raise ValueError('Set a sub-icon position for one skipped side combination at a time.')
    now = datetime.now(timezone.utc).isoformat()
    changed = []
    encode = lambda value: json.dumps(value, ensure_ascii=False, sort_keys=True) if value else None
    for uid in uuids:
        current = connection.execute('SELECT reason, note, main_brief, sub_brief, sub_position FROM primitive_status WHERE uuid=?', (uid,)).fetchone()
        if status == 'todo':
            if current is None:
                continue
            connection.execute('DELETE FROM primitive_status WHERE uuid=?', (uid,))
            record(connection, user, 'primitive_todo', 'primitive:' + uid, previous_reason=current[0])
        else:
            main, sub, position = current[2:] if current else (None, None, None)
            if sub_position is not UNSET:
                position = sub_position
            if reason != 'combination':
                position = None
            if 'main_brief' in updates:
                main = encode(updates['main_brief'])
            if 'sub_brief' in updates:
                sub = encode(updates['sub_brief'])
            if reason not in ('container', 'combination'):
                main = sub = None
            if current == (reason, note, main, sub, position):
                continue
            connection.execute(
                "INSERT INTO primitive_status(uuid,status,reason,note,updated_by,updated_at,main_brief,sub_brief,sub_position) VALUES (?,'skip',?,?,?,?,?,?,?) "
                'ON CONFLICT(uuid) DO UPDATE SET reason=excluded.reason, note=excluded.note, '
                'updated_by=excluded.updated_by, updated_at=excluded.updated_at, '
                'main_brief=excluded.main_brief, sub_brief=excluded.sub_brief, sub_position=excluded.sub_position, combination_brief=NULL',
                (uid, reason, note, user, now, main, sub, position))
            record(connection, user, 'primitive_skip', 'primitive:' + uid, reason=reason, note=note,
                   main_brief=json.loads(main) if main else None, sub_brief=json.loads(sub) if sub else None, sub_position=position)
        changed.append(uid)
    return {'status': status, 'reason': reason, 'changed': len(changed), 'unchanged': len(uuids) - len(changed)}


def load_status(connection) -> dict:
    rows = connection.execute('SELECT uuid, status, reason, note, updated_by, updated_at, main_brief, sub_brief, sub_position FROM primitive_status')
    result = {}
    for uid, status, reason, note, by, at, main, sub, position in rows:
        main, sub = json.loads(main) if main else None, json.loads(sub) if sub else None
        result[uid] = {'status': status, 'reason': reason, 'note': note, 'updated_by': by, 'updated_at': at,
                       'main_brief': main, 'sub_brief': sub, 'sub_position': position,
                       # Compatibility for older agent exports; storage uses the separate fields above.
                       'combination_brief': {'combination_type': 'container' if reason == 'container' else 'side',
                                             'components': [main, sub]} if main and sub else None}
    return result


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
            command.add_argument('--brief-file', type=Path, help='JSON component brief for one primitive; JSON null clears it')
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
                brief_path = getattr(args, 'brief_file', None)
                brief = json.loads(brief_path.read_text()) if brief_path else UNSET
                if brief is not UNSET and len(set(uuids)) != 1:
                    raise ValueError('--brief-file requires exactly one primitive.')
                with connection:
                    for start in range(0, len(uuids), MAX_BATCH):
                        result = set_status(connection, uuids[start:start + MAX_BATCH], args.command,
                                            getattr(args, 'reason', None), getattr(args, 'note', ''),
                                            user=args.user, record=record_activity, known=known, combination_brief=brief)
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
