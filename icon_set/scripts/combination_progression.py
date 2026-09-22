"""Live relationships between progression decisions and editable combinations.

Views read primitive_status directly, including writes from an already-running
gallery server. No polling, copied flags, or build-time state synchronization.
"""
import sqlite3
from pathlib import Path


def init_links(db):
    from .primitive_status import init_primitive_status
    init_primitive_status(db)
    db.execute('''CREATE TABLE IF NOT EXISTS combination_source_references (
        uuid TEXT PRIMARY KEY, concept TEXT NOT NULL, path TEXT)''')
    db.execute('''CREATE INDEX IF NOT EXISTS pair_progression_source ON pairs
        (COALESCE(json_extract(definition_json,'$.source_id'),source_id),kind)''')
    db.execute('''CREATE VIEW IF NOT EXISTS progression_combination_requirements AS
        SELECT p.uuid, CASE p.reason WHEN 'container' THEN 'container' ELSE 'side' END AS kind,
            COALESCE(r.concept,p.uuid) AS concept, r.path AS reference_path,
            p.main_brief,p.sub_brief,p.sub_position,p.note,p.updated_by,p.updated_at
        FROM primitive_status p LEFT JOIN combination_source_references r ON r.uuid=p.uuid
        WHERE p.status='skip' AND p.reason IN ('container','combination')''')
    view_sql = '''CREATE VIEW combination_entries AS
        SELECT p.pair_id,p.kind,p.source_id,p.concept,p.main_id,p.sub_id,
            CASE WHEN p.kind=q.kind THEN COALESCE(q.sub_position,p.position)
                ELSE p.position END AS position,p.status,p.revision,
            CASE WHEN q.uuid IS NULL THEN 'catalog' ELSE 'catalog+progression' END AS origin,
            q.uuid AS progression_uuid,q.kind AS progression_kind,q.reference_path,
            q.main_brief,q.sub_brief,q.note AS progression_note,
            q.updated_by AS progression_updated_by,q.updated_at AS progression_updated_at,
            CASE WHEN json_array_length(json_extract(p.resolution_json,'$.main_generated'))>0
                THEN 'artwork_available' WHEN q.main_brief IS NOT NULL THEN 'brief_ready' ELSE 'needed' END AS main_status,
            CASE WHEN json_array_length(json_extract(p.resolution_json,'$.sub_generated'))>0
                THEN 'artwork_available' WHEN q.sub_brief IS NOT NULL THEN 'brief_ready' ELSE 'needed' END AS sub_status
        FROM pairs p LEFT JOIN progression_combination_requirements q
          ON q.uuid=COALESCE(json_extract(p.definition_json,'$.source_id'),p.source_id)
        UNION ALL
        SELECT 'progression:'||q.kind||':'||q.uuid,q.kind,q.uuid,q.concept,NULL,NULL,
            q.sub_position,'active',0,'progression',q.uuid,q.kind,q.reference_path,
            q.main_brief,q.sub_brief,q.note,q.updated_by,q.updated_at,
            CASE WHEN q.main_brief IS NOT NULL THEN 'brief_ready' ELSE 'needed' END,
            CASE WHEN q.sub_brief IS NOT NULL THEN 'brief_ready' ELSE 'needed' END
        FROM progression_combination_requirements q
        WHERE NOT EXISTS (SELECT 1 FROM pairs p WHERE p.kind=q.kind
            AND COALESCE(json_extract(p.definition_json,'$.source_id'),p.source_id)=+q.uuid)'''
    # Unary + removes column affinity so SQLite can use the expression index.
    previous = db.execute("SELECT sql FROM sqlite_master WHERE name='combination_entries' AND type='view'").fetchone()
    if previous is None or previous[0] != view_sql:
        db.execute('DROP VIEW IF EXISTS combination_entries')
        db.execute(view_sql)


def index_references(db, catalog):
    """Names/paths are catalog metadata; live decisions stay in primitive_status."""
    rows = [(r['uuid'], r.get('concept') or r['uuid'], r.get('path')) for r in catalog['rows']]
    db.executemany('''INSERT INTO combination_source_references VALUES (?,?,?)
        ON CONFLICT(uuid) DO UPDATE SET concept=excluded.concept,path=excluded.path''', rows)
    return dict(indexed=len(rows), flagged=db.execute('SELECT COUNT(*) FROM progression_combination_requirements').fetchone()[0],
                entries=db.execute('SELECT COUNT(*) FROM combination_entries').fetchone()[0])


def migrate_legacy(db, source, destination):
    """Transactional, exact-copy migration; retain the old database as a backup."""
    source = Path(source).resolve()
    if source == Path(destination).resolve():
        raise ValueError('Source and destination must be different databases.')
    if not source.is_file():
        raise ValueError('Legacy combination database does not exist.')
    old = sqlite3.connect(source.as_uri() + '?mode=ro', uri=True)
    counts = {}
    try:
        # Validate everything before copying. A nonidentical target row is never replaced.
        pending = {}
        for table, identity in (('components', 'id'), ('pairs', 'pair_id'), ('pair_history', 'id')):
            columns = [r[1] for r in old.execute(f'PRAGMA table_info({table})')]
            target = [r[1] for r in db.execute(f'PRAGMA table_info({table})')]
            if not columns or columns != target:
                raise ValueError(f'Incompatible legacy schema: {table}')
            pending[table] = []
            for row in old.execute(f'SELECT * FROM {table}'):
                existing = db.execute(f'SELECT * FROM {table} WHERE {identity}=?', (row[columns.index(identity)],)).fetchone()
                if existing is not None:
                    if tuple(existing) != tuple(row):
                        raise ValueError(f'Migration conflict in {table}; existing data was preserved.')
                else:
                    pending[table].append(row)
        for table, rows in pending.items():
            if rows:
                placeholders = ','.join('?' for _ in rows[0])
                db.executemany(f'INSERT INTO {table} VALUES ({placeholders})', rows)
            counts[table] = len(rows)
    finally:
        old.close()
    return dict(copied=counts, legacy_backup=str(source))
