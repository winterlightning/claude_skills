#!/usr/bin/env python3
"""One SQLite database for icon review and primitive progression.

python3 -m icon_set.scripts.state_db summary            # progress per category
python3 -m icon_set.scripts.state_db refresh            # re-mirror the published catalogs now
python3 -m icon_set.scripts.state_db import-legacy      # load old JSON state folders (runs once by itself)

The gallery database (icon_set/state/feedback.sqlite3) holds two kinds of tables:

Authoritative, written by the gallery, agents and CLIs
    reviews, feedback, activity_log, primitive_status, primitive_briefs, ... (deploy.py)
    icon_artwork, stroke_edits, discarded_icons, reference_images (formerly JSON folders)

Derived mirror of the published build, rebuilt when the JSON changes, never edited
    primitives, primitive_icons      published/gallery/primitives.json
    icons                            published/gallery/icons.json (index fields, no geometry)
    side_components, side_component_sources, side_component_pairs
                                     published/gallery/side-components.json
    side_progress                    published/gallery/side-combination-progress.json
    catalog_imports                  which file version each mirror holds

Views join them: primitive_progress (one row per primitive with category, TODO/SKIP
decision, linked icons and their review status), category_progress and
side_component_progress.
"""
from __future__ import annotations

import argparse
from contextlib import closing
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import shutil
import sqlite3
import sys
import threading

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from icon_set.scripts.workspace import DEFAULT_DATABASE, DEFAULT_DIST, STATE_ROOT  # noqa: E402

_UUID = re.compile(r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}')
_DATE = re.compile(r'\d{4}-\d{2}-\d{2}')
LEGACY_MIGRATION = 'legacy-json-stores-v1'
LEGACY_FOLDERS = ('icon-artwork', 'stroke-edits', 'discarded-icons')
MIRROR_TABLES = ('primitives', 'primitive_icons', 'icons', 'side_components', 'side_component_sources',
                 'side_component_pairs', 'side_progress', 'catalog_imports')
# One refresh at a time per process; each still re-checks its stamp inside the write transaction.
_REFRESH_LOCK = threading.Lock()

STORE_TABLES = (
    '''CREATE TABLE IF NOT EXISTS icon_artwork (
        icon TEXT PRIMARY KEY, revision INTEGER NOT NULL, source_mode TEXT,
        updated_by TEXT, updated_at TEXT, document TEXT NOT NULL)''',
    '''CREATE TABLE IF NOT EXISTS stroke_edits (
        icon TEXT NOT NULL, source_svg_sha256 TEXT NOT NULL, revision INTEGER NOT NULL, status TEXT,
        updated_by TEXT, updated_at TEXT, document TEXT NOT NULL,
        PRIMARY KEY(icon, source_svg_sha256))''',
    '''CREATE TABLE IF NOT EXISTS discarded_icons (
        id TEXT PRIMARY KEY, icon_key TEXT NOT NULL, family TEXT, icon_id TEXT,
        discarded_by TEXT, discarded_at TEXT NOT NULL, source_path TEXT, shared_module INTEGER NOT NULL DEFAULT 0,
        record TEXT NOT NULL, feedback TEXT NOT NULL DEFAULT '[]', python_source TEXT)''',
    'CREATE INDEX IF NOT EXISTS discarded_icons_key ON discarded_icons(icon_key)',
    '''CREATE TABLE IF NOT EXISTS reference_images (
        id TEXT PRIMARY KEY, kind TEXT NOT NULL, name TEXT NOT NULL, bytes INTEGER, created_at TEXT)''',
)

MIRROR_SCHEMA = (
    '''CREATE TABLE IF NOT EXISTS catalog_imports (
        source TEXT PRIMARY KEY, stamp TEXT NOT NULL, sha256 TEXT NOT NULL, generated_at TEXT,
        rows INTEGER NOT NULL, imported_at TEXT NOT NULL, meta TEXT NOT NULL DEFAULT '{}')''',
    '''CREATE TABLE IF NOT EXISTS primitives (
        uuid TEXT PRIMARY KEY, canonical_uuid TEXT NOT NULL, position INTEGER NOT NULL,
        category TEXT NOT NULL, batch TEXT NOT NULL DEFAULT '', path TEXT, concept TEXT, old_concept TEXT,
        state TEXT, match TEXT, models INTEGER NOT NULL DEFAULT 0, copies INTEGER NOT NULL DEFAULT 1,
        row_json TEXT)''',
    'CREATE INDEX IF NOT EXISTS primitives_canonical ON primitives(canonical_uuid, position)',
    'CREATE INDEX IF NOT EXISTS primitives_category ON primitives(category, batch)',
    '''CREATE TABLE IF NOT EXISTS primitive_icons (
        uuid TEXT NOT NULL, icon_key TEXT NOT NULL, icon_id TEXT, preview_url TEXT,
        PRIMARY KEY(uuid, icon_key))''',
    'CREATE INDEX IF NOT EXISTS primitive_icons_key ON primitive_icons(icon_key)',
    '''CREATE TABLE IF NOT EXISTS icons (
        key TEXT PRIMARY KEY, icon_id TEXT, name TEXT, family TEXT, profile TEXT, category TEXT,
        svg_sha256 TEXT, preview_url TEXT, validation_status TEXT, author TEXT, python_path TEXT,
        source_uuid TEXT, failed INTEGER NOT NULL DEFAULT 0, created_at TEXT, modified_at TEXT)''',
    'CREATE INDEX IF NOT EXISTS icons_source ON icons(source_uuid)',
    '''CREATE TABLE IF NOT EXISTS side_components (
        role TEXT NOT NULL CHECK(role IN ('main','sub')), id TEXT NOT NULL, position INTEGER NOT NULL,
        concept TEXT, reference_url TEXT, source_path TEXT, uses INTEGER, status TEXT,
        drawings INTEGER NOT NULL DEFAULT 0, failing_variants INTEGER NOT NULL DEFAULT 0, row_json TEXT NOT NULL,
        PRIMARY KEY(role, id))''',
    '''CREATE TABLE IF NOT EXISTS side_component_sources (
        role TEXT NOT NULL, id TEXT NOT NULL, source_uuid TEXT NOT NULL, PRIMARY KEY(role, id, source_uuid))''',
    'CREATE INDEX IF NOT EXISTS side_component_sources_uuid ON side_component_sources(source_uuid)',
    '''CREATE TABLE IF NOT EXISTS side_component_pairs (
        role TEXT NOT NULL, id TEXT NOT NULL, pair_id TEXT NOT NULL, concept TEXT, PRIMARY KEY(role, id, pair_id))''',
    '''CREATE TABLE IF NOT EXISTS side_progress (metric TEXT PRIMARY KEY, value TEXT NOT NULL)''',
)

# Views are recreated on every migrate so a code change to them always lands.
VIEWS = {
    'primitive_icon_reviews': '''
        SELECT pi.uuid, pi.icon_key, i.svg_sha256, i.failed,
               COALESCE(r.status, CASE WHEN i.key IS NULL THEN 'missing' ELSE 'ready' END) AS review_status,
               r.updated_by AS reviewed_by, r.updated_at AS reviewed_at
        FROM primitive_icons pi
        LEFT JOIN icons i ON i.key = pi.icon_key
        LEFT JOIN reviews r ON r.icon = pi.icon_key AND r.svg_sha256 = i.svg_sha256''',
    # A canonical primitive uses its own decision, else the first folded alias that has one
    # (primitive_status.row_decision). Generated wins over SKIP and is flagged as a conflict.
    'primitive_progress': '''
        WITH decided AS (
            SELECT p.*, COALESCE(
                (SELECT s.uuid FROM primitive_status s WHERE s.uuid = p.uuid),
                (SELECT s.uuid FROM primitives a JOIN primitive_status s ON s.uuid = a.uuid
                 WHERE a.canonical_uuid = p.uuid AND a.uuid <> p.uuid ORDER BY a.position LIMIT 1)) AS decision_uuid
            FROM primitives p WHERE p.canonical_uuid = p.uuid)
        SELECT d.uuid, d.category, d.batch, d.path, d.concept, d.old_concept, d.state, d.match, d.models, d.copies,
               CASE WHEN d.state = 'generated' THEN 'generated'
                    WHEN d.decision_uuid IS NOT NULL THEN 'skip'
                    WHEN d.models > 0 OR d.state IN ('model_only', 'build_failed', 'work_only') THEN 'drawn'
                    ELSE 'todo' END AS status,
               (d.decision_uuid IS NOT NULL AND d.state = 'generated') AS conflict,
               d.decision_uuid, s.reason AS skip_reason, s.note AS skip_note,
               s.updated_by AS decided_by, s.updated_at AS decided_at,
               s.main_brief, s.sub_brief, s.sub_position,
               (SELECT COUNT(*) FROM primitive_icon_reviews v WHERE v.uuid = d.uuid) AS icons,
               (SELECT COUNT(*) FROM primitive_icon_reviews v WHERE v.uuid = d.uuid AND v.review_status = 'approve') AS icons_approved,
               (SELECT COUNT(*) FROM primitive_icon_reviews v WHERE v.uuid = d.uuid AND v.review_status = 'pending') AS icons_disapproved,
               (SELECT COUNT(*) FROM primitive_icon_reviews v WHERE v.uuid = d.uuid AND v.review_status = 'rejected') AS icons_rejected,
               (SELECT COUNT(*) FROM primitive_icon_reviews v WHERE v.uuid = d.uuid AND v.review_status = 'claimed') AS icons_claimed,
               (SELECT COUNT(*) FROM primitive_icon_reviews v WHERE v.uuid = d.uuid AND v.review_status = 'ready') AS icons_ready,
               (SELECT group_concat(v.icon_key, ' ') FROM primitive_icon_reviews v WHERE v.uuid = d.uuid) AS icon_keys
        FROM decided d LEFT JOIN primitive_status s ON s.uuid = d.decision_uuid''',
    'category_progress': '''
        SELECT category, COUNT(*) AS total,
               SUM(status = 'generated') AS generated, SUM(status = 'skip') AS skip,
               SUM(status = 'drawn') AS drawn, SUM(status = 'todo') AS todo,
               SUM(state = 'build_failed') AS build_failed, SUM(conflict) AS conflict,
               SUM(status = 'skip' AND skip_reason = 'combination') AS skip_combination,
               SUM(status = 'skip' AND skip_reason = 'container') AS skip_container,
               SUM(status = 'skip' AND skip_reason = 'text_number') AS skip_text_number,
               SUM(status = 'skip' AND skip_reason = 'other') AS skip_other,
               SUM(icons_approved > 0) AS approved, SUM(icons_disapproved > 0) AS disapproved,
               SUM(icons_rejected > 0) AS rejected,
               ROUND(100.0 * SUM(status IN ('generated', 'skip')) / COUNT(*), 1) AS percent_done
        FROM primitive_progress GROUP BY category''',
    'side_component_progress': '''
        SELECT c.role, c.id, c.concept, c.uses, c.status, c.drawings, c.failing_variants, c.source_path,
               (SELECT group_concat(x.source_uuid, ' ') FROM side_component_sources x
                WHERE x.role = c.role AND x.id = c.id) AS source_uuids,
               (SELECT COUNT(*) FROM side_component_pairs x WHERE x.role = c.role AND x.id = c.id) AS pairs,
               s.reason AS skip_reason, s.note AS skip_note
        FROM side_components c LEFT JOIN primitive_status s ON s.uuid = c.id''',
}


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def connect(path, timeout: float = 10) -> sqlite3.Connection:
    connection = sqlite3.connect(path, timeout=timeout)
    connection.execute(f'PRAGMA busy_timeout={int(timeout * 1000)}')
    return connection


def init_store_tables(connection) -> None:
    """The tables that replaced the JSON state folders; safe to call on every open."""
    for statement in STORE_TABLES:
        connection.execute(statement)


def migrate(connection) -> None:
    """Every table and view this module owns; idempotent. deploy.init_database calls it."""
    init_store_tables(connection)
    for statement in MIRROR_SCHEMA:
        connection.execute(statement)
    connection.execute('CREATE TABLE IF NOT EXISTS progression_reviews(path TEXT PRIMARY KEY,content TEXT NOT NULL)')
    columns = {row[1] for row in connection.execute('PRAGMA table_info(progression_reviews)')}
    for column in ('category', 'review_date'):
        if column not in columns:
            connection.execute(f'ALTER TABLE progression_reviews ADD COLUMN {column} TEXT')
    tag_category_reviews(connection)
    for name, body in VIEWS.items():
        connection.execute(f'DROP VIEW IF EXISTS {name}')
        connection.execute(f'CREATE VIEW {name} AS {body}')


def review_path_parts(path: str) -> tuple[str | None, str | None]:
    """'apps/2026-09-15/review.json' or 'batch-2026-09-15/Uncategorized/checkpoint-001/review.json'."""
    parts = [part for part in Path(path).parts[:-1]]
    date = next((match.group(0) for part in parts if (match := _DATE.search(part))), None)
    category = next((part for part in parts if not _DATE.search(part) and not part.startswith('checkpoint-')), None)
    return category, date


def tag_category_reviews(connection) -> None:
    rows = connection.execute('SELECT path FROM progression_reviews WHERE category IS NULL').fetchall()
    for (path,) in rows:
        connection.execute('UPDATE progression_reviews SET category=?, review_date=? WHERE path=?',
                           (*review_path_parts(path), path))


# ---------------------------------------------------------------- catalog mirror

def _stamp(path: Path) -> str:
    stat = path.stat()
    return f'{stat.st_size}:{stat.st_mtime_ns}'


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open('rb') as stream:
        while chunk := stream.read(1024 * 1024):
            digest.update(chunk)
    return digest.hexdigest()


def _dump(value) -> str:
    return json.dumps(value, ensure_ascii=False, separators=(',', ':'))


def _load_primitives(connection, data: dict) -> tuple[int, dict]:
    connection.execute('DELETE FROM primitives')
    connection.execute('DELETE FROM primitive_icons')
    position = 0
    for row in data.get('rows', []):
        uid = row['uuid']
        connection.execute('INSERT OR REPLACE INTO primitives VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)', (
            uid, uid, position, row.get('category') or '', row.get('batch') or '', row.get('path'),
            row.get('concept'), row.get('old_concept'), row.get('state'), row.get('match'),
            len(row.get('models') or []), row.get('copies', 1), _dump(row)))
        position += 1
        for alias in row.get('aliases', []):
            connection.execute('INSERT OR IGNORE INTO primitives VALUES (?,?,?,?,?,?,?,?,?,?,?,?,NULL)', (
                alias['uuid'], uid, position, alias.get('category') or '', alias.get('batch') or '',
                alias.get('path'), alias.get('concept'), alias.get('old_concept'), row.get('state'), 'alias', 0, 1))
            position += 1
        for icon in row.get('generated') or []:
            connection.execute('INSERT OR IGNORE INTO primitive_icons VALUES (?,?,?,?)',
                               (uid, icon['key'], icon.get('icon_id'), icon.get('preview_url')))
    meta = {key: value for key, value in data.items() if key != 'rows'}
    return len(data.get('rows', [])), meta


def _source_uuid(record: dict) -> str | None:
    for source in record.get('original_sources') or []:
        match = _UUID.search(str(source.get('source_path') or '').lower())
        if match:
            return match.group(0)
    python = record.get('python_source') if isinstance(record.get('python_source'), dict) else {}
    match = _UUID.search(str(python.get('path') or record.get('source_path') or '').lower().replace('_', '-'))
    return match.group(0) if match else None


def _load_icons(connection, data: dict) -> tuple[int, dict]:
    connection.execute('DELETE FROM icons')
    count = 0
    for failed, rows in ((0, data.get('icons', [])), (1, data.get('failed_icons', []))):
        for record in rows:
            key = record.get('key') or f"{record.get('family')}/{record.get('icon_id')}"
            validation = record.get('validation') if isinstance(record.get('validation'), dict) else {}
            python = record.get('python_source') if isinstance(record.get('python_source'), dict) else {}
            # A key that passed wins over a failed duplicate.
            connection.execute('INSERT OR IGNORE INTO icons VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', (
                key, record.get('icon_id'), record.get('name'), record.get('family'), record.get('profile'),
                record.get('category'), record.get('svg_sha256'), record.get('preview_url'),
                validation.get('status') or record.get('status') or ('fail' if failed else None),
                record.get('author'), python.get('path') or record.get('source_path'), _source_uuid(record),
                failed, record.get('created_at'), record.get('modified_at')))
            count += 1
    return count, {}


def _load_side_components(connection, data: dict) -> tuple[int, dict]:
    for table in ('side_components', 'side_component_sources', 'side_component_pairs'):
        connection.execute(f'DELETE FROM {table}')
    count = 0
    for role, rows in (('main', data.get('mains', [])), ('sub', data.get('subs', []))):
        for position, row in enumerate(rows):
            connection.execute('INSERT OR REPLACE INTO side_components VALUES (?,?,?,?,?,?,?,?,?,?,?)', (
                role, row['id'], position, row.get('concept'), row.get('reference_url'), row.get('source_path'),
                row.get('uses'), row.get('status'), len(row.get('drawings') or []), row.get('failing_variants') or 0,
                _dump(row)))
            for uid in row.get('source_ids') or []:
                connection.execute('INSERT OR IGNORE INTO side_component_sources VALUES (?,?,?)', (role, row['id'], uid))
            for pair in row.get('pairs') or []:
                connection.execute('INSERT OR IGNORE INTO side_component_pairs VALUES (?,?,?,?)',
                                   (role, row['id'], pair.get('id'), pair.get('concept')))
            count += 1
    meta = {key: value for key, value in data.items() if key not in ('mains', 'subs')}
    return count, meta


def _load_side_progress(connection, data: dict) -> tuple[int, dict]:
    connection.execute('DELETE FROM side_progress')
    for metric, value in data.items():
        connection.execute('INSERT INTO side_progress VALUES (?,?)', (metric, _dump(value)))
    return len(data), {}


SOURCES = {
    'primitives': ('primitives.json', _load_primitives),
    'icons': ('icons.json', _load_icons),
    'side_components': ('side-components.json', _load_side_components),
    'side_progress': ('side-combination-progress.json', _load_side_progress),
}


def refresh_catalog(connection, gallery, *, sources=None, force=False) -> dict:
    """Mirror the published gallery JSON; a source whose file is unchanged is skipped.

    Missing files are left alone (a small test dist, or a build that has not staged them yet).
    Returns {source: rows} for the sources that were reloaded.
    """
    gallery = Path(gallery)
    reloaded = {}
    with _REFRESH_LOCK:
        for source in sources or SOURCES:
            filename, loader = SOURCES[source]
            path = gallery / filename
            if not path.is_file():
                continue
            stamp = _stamp(path)
            row = connection.execute('SELECT stamp, sha256 FROM catalog_imports WHERE source=?', (source,)).fetchone()
            if row and row[0] == stamp and not force:
                continue
            digest = _sha256(path)
            if row and row[1] == digest and not force:
                with connection:
                    connection.execute('UPDATE catalog_imports SET stamp=? WHERE source=?', (stamp, source))
                continue
            data = json.loads(path.read_text(encoding='utf-8'))
            with connection:
                connection.execute('BEGIN IMMEDIATE')
                count, meta = loader(connection, data)
                connection.execute(
                    'INSERT INTO catalog_imports VALUES (?,?,?,?,?,?,?) ON CONFLICT(source) DO UPDATE SET '
                    'stamp=excluded.stamp, sha256=excluded.sha256, generated_at=excluded.generated_at, '
                    'rows=excluded.rows, imported_at=excluded.imported_at, meta=excluded.meta',
                    (source, stamp, digest, data.get('generated_at') if isinstance(data, dict) else None,
                     count, utc_now(), _dump(meta)))
            reloaded[source] = count
    return reloaded


def clear_mirror(connection) -> None:
    """Drop derived rows, e.g. from an exported copy; the receiver re-mirrors its own build."""
    tables = {row[0] for row in connection.execute("SELECT name FROM sqlite_master WHERE type='table'")}
    for table in MIRROR_TABLES:
        if table in tables:
            connection.execute(f'DELETE FROM {table}')


def _meta(connection, source: str) -> dict | None:
    row = connection.execute('SELECT meta FROM catalog_imports WHERE source=?', (source,)).fetchone()
    return json.loads(row[0]) if row else None


def load_primitives_catalog(connection) -> dict | None:
    """primitives.json, exactly as published, rebuilt from the mirror; None before the first refresh."""
    meta = _meta(connection, 'primitives')
    if meta is None:
        return None
    rows = [json.loads(text) for (text,) in connection.execute(
        'SELECT row_json FROM primitives WHERE canonical_uuid = uuid ORDER BY position')]
    return {**meta, 'rows': rows}


def load_side_components(connection) -> dict | None:
    """side-components.json, exactly as published, rebuilt from the mirror."""
    meta = _meta(connection, 'side_components')
    if meta is None:
        return None
    result = {key: meta[key] for key in ('generated_at',) if key in meta}
    for role, name in (('main', 'mains'), ('sub', 'subs')):
        result[name] = [json.loads(text) for (text,) in connection.execute(
            'SELECT row_json FROM side_components WHERE role=? ORDER BY position', (role,))]
    result.update({key: value for key, value in meta.items() if key != 'generated_at'})
    return result


def category_progress(connection) -> list[dict]:
    cursor = connection.execute('SELECT * FROM category_progress ORDER BY category COLLATE NOCASE')
    names = [column[0] for column in cursor.description]
    return [dict(zip(names, row)) for row in cursor]


# ---------------------------------------------------------------- legacy JSON folders

def _read_json(path: Path):
    try:
        return json.loads(path.read_text(encoding='utf-8'))
    except (OSError, ValueError):
        return None


def put_artwork(connection, document: dict) -> None:
    connection.execute(
        'INSERT INTO icon_artwork VALUES (?,?,?,?,?,?) ON CONFLICT(icon) DO UPDATE SET revision=excluded.revision, '
        'source_mode=excluded.source_mode, updated_by=excluded.updated_by, updated_at=excluded.updated_at, '
        'document=excluded.document',
        (document['icon'], document.get('revision', 0), document.get('source_mode'), document.get('updated_by'),
         document.get('updated_at'), json.dumps(document, ensure_ascii=False)))


def put_stroke_edit(connection, document: dict) -> None:
    connection.execute(
        'INSERT INTO stroke_edits VALUES (?,?,?,?,?,?,?) ON CONFLICT(icon, source_svg_sha256) DO UPDATE SET '
        'revision=excluded.revision, status=excluded.status, updated_by=excluded.updated_by, '
        'updated_at=excluded.updated_at, document=excluded.document',
        (document['icon'], document['source_svg_sha256'], document.get('revision', 0), document.get('status'),
         document.get('updated_by'), document.get('updated_at'), json.dumps(document, ensure_ascii=False)))


def put_discard(connection, stem: str, meta: dict, python_source: str | None) -> None:
    record = meta.get('record') or {}
    key = record.get('key') or f"{record.get('family')}/{record.get('icon_id')}"
    connection.execute('INSERT OR REPLACE INTO discarded_icons VALUES (?,?,?,?,?,?,?,?,?,?,?)', (
        stem, key, record.get('family'), record.get('icon_id'), meta.get('discarded_by'),
        meta.get('discarded_at') or '', meta.get('source_path'), int(bool(meta.get('shared_module'))),
        json.dumps(record, ensure_ascii=False), json.dumps(meta.get('feedback') or [], ensure_ascii=False),
        python_source))


def import_store_folders(connection, state_root, names=LEGACY_FOLDERS + ('reference-images',)) -> dict:
    """Load old JSON state folders into their tables (rows already present are replaced)."""
    state_root = Path(state_root)
    counts = {}
    if 'icon-artwork' in names:
        counts['icon-artwork'] = 0
        for path in sorted((state_root / 'icon-artwork').glob('*/artwork.json')):
            document = _read_json(path)
            if isinstance(document, dict) and document.get('icon'):
                put_artwork(connection, document)
                counts['icon-artwork'] += 1
    if 'stroke-edits' in names:
        counts['stroke-edits'] = 0
        for path in sorted((state_root / 'stroke-edits').glob('*/*.json')):
            document = _read_json(path)
            if isinstance(document, dict) and document.get('icon') and document.get('source_svg_sha256'):
                put_stroke_edit(connection, document)
                counts['stroke-edits'] += 1
    if 'discarded-icons' in names:
        counts['discarded-icons'] = 0
        for path in sorted((state_root / 'discarded-icons').glob('*.json')):
            meta = _read_json(path)
            if not isinstance(meta, dict):
                continue
            source = path.with_suffix('.py')
            put_discard(connection, path.stem, meta, source.read_text(encoding='utf-8') if source.is_file() else None)
            counts['discarded-icons'] += 1
    if 'reference-images' in names:
        counts['reference-images'] = 0
        for path in sorted((state_root / 'reference-images').glob('*.json')):
            meta = _read_json(path)
            if not isinstance(meta, dict) or not meta.get('id') or not meta.get('kind'):
                continue
            image = path.with_name(f"{meta['id']}.{meta['kind']}")
            connection.execute('INSERT OR IGNORE INTO reference_images VALUES (?,?,?,?,?)', (
                meta['id'], meta['kind'], meta.get('name') or f"reference.{meta['kind']}",
                image.stat().st_size if image.is_file() else None, None))
            counts['reference-images'] += 1
    return counts


def import_legacy_json(connection, state_root=STATE_ROOT, *, move=True) -> dict | None:
    """Run once per database: load the JSON folders, then park them in state/legacy-json-<date>/.

    Returns the counts, or None when this database already ran the import. Nothing is deleted.
    """
    connection.execute('CREATE TABLE IF NOT EXISTS review_data_migrations (id TEXT PRIMARY KEY, applied_at TEXT NOT NULL, details TEXT NOT NULL)')
    init_store_tables(connection)
    if connection.execute('SELECT 1 FROM review_data_migrations WHERE id=?', (LEGACY_MIGRATION,)).fetchone():
        return None
    state_root = Path(state_root)
    with connection:
        counts = import_store_folders(connection, state_root)
        connection.execute('INSERT INTO review_data_migrations VALUES (?,?,?)',
                           (LEGACY_MIGRATION, utc_now(), json.dumps(counts)))
    if move:
        parked = state_root / f"legacy-json-{datetime.now(timezone.utc).strftime('%Y%m%d')}"
        for name in LEGACY_FOLDERS:
            folder = state_root / name
            if folder.is_dir():
                parked.mkdir(parents=True, exist_ok=True)
                target = parked / name
                suffix = 1
                while target.exists():
                    suffix += 1
                    target = parked / f'{name}-{suffix}'
                shutil.move(str(folder), str(target))
    return counts


# ---------------------------------------------------------------- CLI

def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--database', type=Path, default=DEFAULT_DATABASE)
    parser.add_argument('--dist', type=Path, default=DEFAULT_DIST)
    commands = parser.add_subparsers(dest='command', required=True)
    summary = commands.add_parser('summary', help='Primitive progress per category')
    summary.add_argument('--format', choices=('table', 'json'), default='table')
    refresh = commands.add_parser('refresh', help='Re-mirror the published gallery JSON')
    refresh.add_argument('--force', action='store_true', help='Reload even when the files are unchanged')
    commands.add_parser('import-legacy', help='Load the old JSON state folders (runs once by itself)')
    args = parser.parse_args(argv)

    from icon_set.scripts.deploy import init_database
    init_database(args.database)
    with closing(connect(args.database)) as connection:
        if args.command == 'import-legacy':
            result = import_legacy_json(connection, args.database.parent)
            print(json.dumps(result) if result is not None else 'Already imported.')
            return 0
        reloaded = refresh_catalog(connection, args.dist / 'gallery', force=getattr(args, 'force', False))
        if args.command == 'refresh':
            print(json.dumps(reloaded or 'Mirror is current.'))
            return 0
        rows = category_progress(connection)
    if args.format == 'json':
        print(json.dumps(rows, indent=1))
        return 0
    columns = ('category', 'total', 'generated', 'skip', 'drawn', 'todo', 'build_failed', 'approved', 'disapproved', 'percent_done')
    print('\t'.join(columns))
    for row in rows:
        print('\t'.join(str(row[column] if row[column] is not None else '') for column in columns))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
