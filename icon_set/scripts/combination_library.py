"""Editable combination database. Imports are explicit; builds never modify it."""
from __future__ import annotations

import argparse
from contextlib import contextmanager
from datetime import datetime, timezone
import json
from pathlib import Path
import sqlite3
import uuid

from .workspace import DEFAULT_COMBINATION_DATABASE, LEGACY_COMBINATION_DATABASE, REPO_ROOT, build_dist

KINDS = ('container', 'side')
POSITIONS = {'br', 'tr', 'bl', 'tl', 'to', 'bo', 'ri', 'le', 'top',
             'bottom', 'left', 'right', 'top-left', 'top-right',
             'bottom-left', 'bottom-right', 'center'}


def encoded(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':'))


def timestamp():
    return datetime.now(timezone.utc).isoformat()


@contextmanager
def connect(path):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    db = sqlite3.connect(path)
    db.row_factory = sqlite3.Row
    db.execute('PRAGMA foreign_keys=ON')
    try:
        db.executescript('''
            CREATE TABLE IF NOT EXISTS components (
                id TEXT PRIMARY KEY, concept TEXT NOT NULL, reference_url TEXT,
                artwork_json TEXT NOT NULL DEFAULT '[]');
            CREATE TABLE IF NOT EXISTS pairs (
                pair_id TEXT PRIMARY KEY,
                kind TEXT NOT NULL CHECK(kind IN ('container','side')),
                source_id TEXT NOT NULL, concept TEXT NOT NULL,
                main_id TEXT REFERENCES components(id),
                sub_id TEXT REFERENCES components(id), position TEXT,
                status TEXT NOT NULL CHECK(status IN ('active','archived')),
                revision INTEGER NOT NULL DEFAULT 1,
                definition_json TEXT NOT NULL, imported_json TEXT,
                resolution_json TEXT NOT NULL DEFAULT '{}',
                ordinal INTEGER NOT NULL, created_at TEXT NOT NULL, updated_at TEXT NOT NULL,
                UNIQUE(kind, source_id));
            CREATE INDEX IF NOT EXISTS pair_main ON pairs(main_id, kind);
            CREATE INDEX IF NOT EXISTS pair_sub ON pairs(sub_id, kind);
            CREATE INDEX IF NOT EXISTS pair_status ON pairs(kind, status, ordinal);
            CREATE TABLE IF NOT EXISTS pair_history (
                id INTEGER PRIMARY KEY, pair_id TEXT NOT NULL REFERENCES pairs(pair_id),
                revision INTEGER NOT NULL, action TEXT NOT NULL, actor TEXT NOT NULL,
                snapshot_json TEXT NOT NULL, created_at TEXT NOT NULL,
                UNIQUE(pair_id, revision));
        ''')
        from .combination_progression import init_links
        init_links(db)
        db.commit()
        with db:
            yield db
    finally:
        db.close()


def component(db, identity, reference=None):
    if identity is None:
        return
    reference = reference or {}
    db.execute('INSERT OR IGNORE INTO components VALUES (?,?,?,?)',
               (identity, reference.get('concept') or identity,
                reference.get('reference_url'), encoded(reference.get('generated', []))))


def validate(kind, definition):
    if kind not in KINDS:
        raise ValueError('Kind must be container or side.')
    for field in ('id', 'concept'):
        if not isinstance(definition.get(field), str) or not definition[field].strip():
            raise ValueError(f'{field} must be a nonempty string.')
    for field in ('main_id', 'sub_id'):
        value = definition.get(field)
        if value is not None and (not isinstance(value, str) or not value.strip()):
            raise ValueError(f'{field} must be a component ID or null.')
    if kind == 'side' and definition.get('position') not in POSITIONS:
        raise ValueError('Side pairs need a supported position: ' + ', '.join(sorted(POSITIONS)))
    if kind == 'container' and definition.get('position') is not None:
        raise ValueError('Container pairs use placement metadata, not a side position.')
    # Exact keys are distinct from source references. Do not coerce one into the other.
    if definition.get('component_selection') == 'explicit':
        for role in ('main', 'sub'):
            identity = definition.get(role + '_id')
            if not identity or '/' not in identity:
                raise ValueError('Explicit selections require family/icon keys for both components.')
            if definition.get(role + '_key', identity) != identity:
                raise ValueError(f'{role}_key must match {role}_id.')
        if kind == 'container' and not definition['main_id'].startswith('container/'):
            raise ValueError('A container pair requires a container main.')


def get_pair(db, pair_id):
    row = db.execute('SELECT * FROM pairs WHERE pair_id=?', (pair_id,)).fetchone()
    if row is None:
        raise ValueError('Unknown pair ID.')
    result = dict(row)
    for name in ('definition', 'imported', 'resolution'):
        value = result.pop(name + '_json')
        result[name] = json.loads(value) if value is not None else None
    return result


def record_history(db, pair_id, action, actor):
    row = get_pair(db, pair_id)
    db.execute('INSERT INTO pair_history(pair_id,revision,action,actor,snapshot_json,created_at) VALUES (?,?,?,?,?,?)',
               (pair_id, row['revision'], action, actor, encoded(row), timestamp()))


def seed(db, definitions, catalog):
    """Import every existing pair once. Never reset edits, archives or history."""
    published = {(r['kind'], r['id']): r for r in catalog['rows']}
    references = catalog['references']
    counts = dict(inserted=0, unchanged=0, conflicts=[])
    seen = set()
    for kind in KINDS:
        for ordinal, definition in enumerate(definitions.get(kind, [])):
            validate(kind, definition)
            identity = (kind, definition['id'])
            if identity in seen:
                raise ValueError(f'Duplicate source pair: {identity}')
            seen.add(identity)
            pair_id = str(uuid.uuid5(uuid.NAMESPACE_URL, 'pictographic:combination:' + kind + ':' + definition['id']))
            prior = db.execute('SELECT imported_json FROM pairs WHERE pair_id=?', (pair_id,)).fetchone()
            if prior:
                if prior['imported_json'] != encoded(definition):
                    counts['conflicts'].append(dict(kind=kind, source_id=definition['id'], pair_id=pair_id))
                else:
                    counts['unchanged'] += 1
                continue
            current = published.get(identity)
            if current is None:
                raise ValueError(f'Published catalog is missing {identity}; refresh it before importing.')
            for key, value in definition.items():
                if key in ('main_id', 'sub_id') and value is None:
                    continue  # The gallery may contain a reviewed remapping.
                if current.get(key) != value:
                    raise ValueError(f'Published catalog is stale for {identity}: {key}')
            for role in ('main', 'sub'):
                uid = current.get(role + '_id')
                component(db, uid, references.get(uid))
            resolution = {key: current[key] for key in
                          ('main_generated', 'sub_generated', 'main_icon_id', 'remappings') if key in current}
            for role in ('main', 'sub'):
                resolution.setdefault(role + '_generated', references.get(current.get(role + '_id'), {}).get('generated', []))
            now = timestamp()
            db.execute('''INSERT INTO pairs VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                       (pair_id, kind, definition['id'], definition['concept'], current.get('main_id'),
                        current.get('sub_id'), definition.get('position'), 'active', 1,
                        encoded(definition), encoded(definition), encoded(resolution), ordinal, now, now))
            record_history(db, pair_id, 'import', 'catalog import')
            counts['inserted'] += 1
    return counts


def save_pair(db, kind, definition, *, pair_id=None, revision=None, status='active', actor='local'):
    """Create or replace a definition, using a revision to prevent lost updates."""
    validate(kind, definition)
    if status not in ('active', 'archived'):
        raise ValueError('Status must be active or archived.')
    old = get_pair(db, pair_id) if pair_id else None
    if old and (old['revision'] != revision or old['kind'] != kind or old['source_id'] != definition['id']):
        raise ValueError('Revision conflict or changed identity; reload the pair before editing.')
    for role in ('main', 'sub'):
        component(db, definition.get(role + '_id'))
    now = timestamp()
    if old:
        # Keep reviewed remaps/artwork only while the component definition is unchanged.
        same = all(old['definition'].get(k) == definition.get(k) for k in
                   ('main_id', 'sub_id', 'main_key', 'sub_key', 'component_selection'))
        changed = db.execute('''UPDATE pairs SET concept=?,main_id=?,sub_id=?,position=?,status=?,
                      revision=revision+1,definition_json=?,resolution_json=?,updated_at=?
                      WHERE pair_id=? AND revision=?''',
                   (definition['concept'], old['main_id'] if same else definition.get('main_id'),
                    old['sub_id'] if same else definition.get('sub_id'), definition.get('position'),
                    status, encoded(definition), encoded(old['resolution'] if same else {}), now, pair_id, revision))
        if changed.rowcount != 1:
            raise ValueError('Revision conflict; reload the pair before editing.')
    else:
        pair_id = str(uuid.uuid4())
        ordinal = db.execute('SELECT COALESCE(MAX(ordinal),-1)+1 FROM pairs WHERE kind=?', (kind,)).fetchone()[0]
        db.execute('''INSERT INTO pairs VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                   (pair_id, kind, definition['id'], definition['concept'], definition.get('main_id'),
                    definition.get('sub_id'), definition.get('position'), status, 1,
                    encoded(definition), None, '{}', ordinal, now, now))
    record_history(db, pair_id, 'edit' if old else 'create', actor)
    return get_pair(db, pair_id)


def export_definitions(db, include_archived=False):
    """Lossless legacy-compatible definitions, excluding generated preview state."""
    result = {kind: [] for kind in KINDS}
    for row in db.execute("SELECT kind,definition_json FROM pairs WHERE status='active' OR ? ORDER BY kind,ordinal,pair_id", (include_archived,)):
        result[row['kind']].append(json.loads(row['definition_json']))
    return result


def summary(db):
    counts = [dict(r) for r in db.execute('''SELECT kind,status,COUNT(*) AS total,
        SUM(main_id IS NULL) AS missing_main_reference,SUM(sub_id IS NULL) AS missing_sub_reference
        FROM pairs GROUP BY kind,status ORDER BY kind,status''')]
    live = [dict(r) for r in db.execute('SELECT kind,origin,COUNT(*) AS total FROM combination_entries GROUP BY kind,origin')]
    return dict(pairs=counts, live_entries=live, components=db.execute('SELECT COUNT(*) FROM components').fetchone()[0],
                history_entries=db.execute('SELECT COUNT(*) FROM pair_history').fetchone()[0])


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--database', type=Path, default=DEFAULT_COMBINATION_DATABASE)
    commands = parser.add_subparsers(dest='command', required=True)
    importer = commands.add_parser('import-current', help='Seed once from current definitions and gallery')
    importer.add_argument('--root', type=Path, default=REPO_ROOT)
    commands.add_parser('summary')
    migration = commands.add_parser('migrate-legacy', help='Copy the former standalone library into the shared database')
    migration.add_argument('--source', type=Path, default=LEGACY_COMBINATION_DATABASE)
    sync = commands.add_parser('sync-progression', help='Index progression reference names; flags remain live')
    sync.add_argument('--dist', type=Path, default=build_dist())
    listing = commands.add_parser('list')
    listing.add_argument('--kind', choices=KINDS)
    listing.add_argument('--query', default='')
    listing.add_argument('--status', choices=('active', 'archived'), default='active')
    listing.add_argument('--limit', type=int, default=50)
    listing.add_argument('--offset', type=int, default=0)
    for name in ('show', 'history'):
        commands.add_parser(name).add_argument('pair_id')
    save = commands.add_parser('save', help='Add or replace a pair from a JSON definition')
    save.add_argument('definition', type=Path)
    save.add_argument('--kind', required=True, choices=KINDS)
    save.add_argument('--pair-id')
    save.add_argument('--revision', type=int)
    save.add_argument('--status', choices=('active', 'archived'), default='active')
    save.add_argument('--actor', default='local')
    exporter = commands.add_parser('export', help='Write definitions for review; never overwrite an existing file')
    exporter.add_argument('output', type=Path)
    exporter.add_argument('--include-archived', action='store_true')
    args = parser.parse_args(argv)
    try:
        if args.command not in ('import-current', 'migrate-legacy', 'sync-progression') and not args.database.is_file():
            raise ValueError('Database does not exist. Run import-current first.')
        with connect(args.database) as db:
            if args.command == 'migrate-legacy':
                from .combination_progression import migrate_legacy
                result = migrate_legacy(db, args.source, args.database)
            elif args.command == 'sync-progression':
                from .combination_progression import index_references
                result = index_references(db, json.loads((args.dist / 'gallery/primitives.json').read_text()))
            elif args.command == 'import-current':
                source = json.loads((args.root / 'combination_data.json').read_text())
                catalog = json.loads((build_dist(args.root) / 'gallery/combinations.json').read_text())
                result = seed(db, source, catalog)
            elif args.command == 'summary':
                result = summary(db)
            elif args.command == 'list':
                if not 1 <= args.limit <= 1000 or args.offset < 0:
                    raise ValueError('Use a limit from 1 to 1000 and a nonnegative offset.')
                result = [dict(r) for r in db.execute('''SELECT *
                    FROM combination_entries WHERE (? IS NULL OR kind=?) AND status=? AND
                    (instr(lower(concept),lower(?))>0 OR instr(source_id,?)>0)
                    ORDER BY kind,concept,pair_id LIMIT ? OFFSET ?''',
                    (args.kind, args.kind, args.status, args.query, args.query, args.limit, args.offset))]
            elif args.command == 'show':
                live = db.execute('SELECT * FROM combination_entries WHERE pair_id=?', (args.pair_id,)).fetchone()
                if args.pair_id.startswith('progression:'):
                    if live is None:
                        raise ValueError('Unknown progression requirement.')
                    result = dict(live)
                else:
                    result = get_pair(db, args.pair_id)
                    result['progression'] = dict(live) if live else None
            elif args.command == 'history':
                get_pair(db, args.pair_id)
                result = [dict(r) for r in db.execute('SELECT * FROM pair_history WHERE pair_id=? ORDER BY revision', (args.pair_id,))]
            elif args.command == 'save':
                result = save_pair(db, args.kind, json.loads(args.definition.read_text()), pair_id=args.pair_id,
                                   revision=args.revision, status=args.status, actor=args.actor)
            else:
                result = export_definitions(db, args.include_archived)
                with args.output.open('x') as output:
                    output.write(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
                result = dict(output=str(args.output), counts={kind: len(rows) for kind, rows in result.items()})
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (ValueError, OSError, sqlite3.Error) as error:
        parser.exit(1, str(error) + '\n')


if __name__ == '__main__':
    raise SystemExit(main())
