#!/usr/bin/env python3
"""Serve the built icon gallery and persist feedback in SQLite.

python3 icon_set/scripts/deploy.py --host 0.0.0.0 --port 8000
Use --open for local browser preview. Put a TLS reverse proxy in front on a server.
"""
from __future__ import annotations

import argparse
import base64
import binascii
from contextlib import closing
from datetime import datetime, timezone
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import json
import hashlib
import secrets
import re
import time
from http.cookies import SimpleCookie, CookieError
from pathlib import Path
import sqlite3
import threading
import sys
import os
import shutil
import tempfile
import zipfile
import urllib.error
import urllib.request
from urllib.parse import parse_qs, unquote, urlsplit
import webbrowser

if __package__:
    from .attribute_legacy_reviews import migrate as migrate_legacy_reviewers
    from .reviewer_stats import current_reviews, reviewer_stats
    from .upload_validation import validate_upload
    from .icon_artwork import ArtworkStore, baseline, resolve_artwork, icon_from_graph, sha, safe_svg
    from .stroke_edits import StrokeEditStore, EditConflict, GRAPH_FIELDS
    from .generation import GenerationManager
    from .review_icon import FeedbackReviewManager
    from .brief_queue import init_brief_queue, enqueue_split, list_briefs, validate_split, brief_archive
    from .reference_images import ReferenceStore, LIMITS as REFERENCE_LIMITS
    from .discard_icon import discard_many
    from .qa_evidence import EvidenceStore
    from .primitive_briefs import init_primitive_briefs, load_primitive_briefs, save_primitive_brief, generation_queue
    from .primitive_status import init_primitive_status, set_status, load_status, merge, summarize, filter_rows, canonical_map
    from .progression import import_snapshot
    from .primitives_catalog import primitives_root
else:
    from attribute_legacy_reviews import migrate as migrate_legacy_reviewers
    from reviewer_stats import current_reviews, reviewer_stats
    from upload_validation import validate_upload
    from icon_artwork import ArtworkStore, baseline, resolve_artwork, icon_from_graph, sha, safe_svg
    from stroke_edits import StrokeEditStore, EditConflict, GRAPH_FIELDS
    from generation import GenerationManager
    from review_icon import FeedbackReviewManager
    from brief_queue import init_brief_queue, enqueue_split, list_briefs, validate_split, brief_archive
    from reference_images import ReferenceStore, LIMITS as REFERENCE_LIMITS
    from discard_icon import discard_many
    from qa_evidence import EvidenceStore
    from primitive_briefs import init_primitive_briefs, load_primitive_briefs, save_primitive_brief, generation_queue
    from primitive_status import init_primitive_status, set_status, load_status, merge, summarize, filter_rows, canonical_map
    from progression import import_snapshot
    from primitives_catalog import primitives_root

if __package__:
    from .workspace import DEFAULT_DIST, DEFAULT_DATABASE
else:
    from workspace import DEFAULT_DIST, DEFAULT_DATABASE

PACKAGE_ROOT = Path(__file__).resolve().parents[1]
# Resolve the shared validator package when launched as a script.
if str(PACKAGE_ROOT.parent) not in sys.path:
    sys.path.insert(0, str(PACKAGE_ROOT.parent))

DEFAULT_DB = DEFAULT_DATABASE
MAX_BODY = 65536
# Base64 inflates by 4/3; leave room for the JSON wrapper around the largest image.
MAX_REFERENCE_BODY = max(REFERENCE_LIMITS.values()) * 4 // 3 + 4096
ADMIN_USERS = {"jakes": "1", "hina": "1", "ray": "1", "phuong": "1"}
SESSION_TTL = 12 * 60 * 60
# Discards rewrite icons.json and manifests; one at a time.
DISCARD_LOCK = threading.Lock()
MAX_DISCARD_BATCH = 500
# Where the developer machine pulls reviewing data from; the quick tunnel URL changes on restart.
DEFAULT_SYNC_SOURCE = os.environ.get('PICTOGRAPHIC_SYNC_SOURCE', 'https://suffered-scored-nicole-default.trycloudflare.com')
MAX_SYNC_BYTES = 1024 * 1024 * 1024
SYNC_TIMEOUT = 120
SYNC_COUNTED_TABLES = ('feedback', 'reviews', 'icon_flags', 'activity_log')
# Review decisions point at artwork kept beside the database: an approved upload or
# gallery edit changes the icon's svg_sha256, so these folders travel with the database.
SYNC_STORES = ('icon-artwork', 'stroke-edits', 'reference-images')


def init_database(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with closing(sqlite3.connect(path)) as connection, connection:
        connection.execute("CREATE TABLE IF NOT EXISTS admin_sessions (token TEXT PRIMARY KEY, username TEXT NOT NULL, expires REAL NOT NULL)")
        connection.execute("""CREATE TABLE IF NOT EXISTS uploaded_icons (
            icon TEXT PRIMARY KEY, record TEXT NOT NULL, svg TEXT NOT NULL)""")
        init_brief_queue(connection)
        connection.execute('''CREATE TABLE IF NOT EXISTS icon_types (
            icon TEXT PRIMARY KEY, icon_type TEXT NOT NULL,
            updated_at TEXT NOT NULL, updated_by TEXT NOT NULL)''')
        connection.execute("""CREATE TABLE IF NOT EXISTS icon_flags (
            icon TEXT PRIMARY KEY, flag TEXT NOT NULL CHECK(flag IN ('container_combination','combination','other','exception')),
            updated_at TEXT NOT NULL)""")
        # Rebuild the flag constraint while preserving old reviewer attribution.
        schema = connection.execute("SELECT sql FROM sqlite_master WHERE name='icon_flags'").fetchone()[0]
        if "'text'" not in schema or "'number'" not in schema:
            columns = {row[1] for row in connection.execute('PRAGMA table_info(icon_flags)')}
            connection.execute('ALTER TABLE icon_flags RENAME TO icon_flags_legacy')
            connection.execute("""CREATE TABLE icon_flags (
                icon TEXT PRIMARY KEY, flag TEXT NOT NULL CHECK(flag IN
                ('container_combination','combination','text','number','other','exception')),
                updated_at TEXT NOT NULL, updated_by TEXT)""")
            actor = 'updated_by' if 'updated_by' in columns else 'NULL'
            connection.execute('INSERT INTO icon_flags SELECT icon,flag,updated_at,' + actor + ' FROM icon_flags_legacy')
            connection.execute('DROP TABLE icon_flags_legacy')
        connection.execute('''CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY, icon TEXT NOT NULL, feedback TEXT NOT NULL,
            svg_sha256 TEXT NOT NULL, created_at TEXT NOT NULL)''')
        connection.execute('CREATE INDEX IF NOT EXISTS feedback_icon ON feedback(icon, id)')
        if 'reason' not in {row[1] for row in connection.execute('PRAGMA table_info(feedback)')}:
            connection.execute("ALTER TABLE feedback ADD COLUMN reason TEXT NOT NULL DEFAULT 'other'")
            connection.execute("UPDATE feedback SET reason='bad-stroke' WHERE feedback LIKE 'Bad draw%' OR feedback LIKE 'Bad stroke%'")
            connection.execute("UPDATE feedback SET reason='meaning' WHERE feedback LIKE 'Does not convey the meaning%'")
        if 'reference_images' not in {row[1] for row in connection.execute('PRAGMA table_info(feedback)')}:
            connection.execute("ALTER TABLE feedback ADD COLUMN reference_images TEXT NOT NULL DEFAULT '[]'")
        connection.execute('''CREATE TABLE IF NOT EXISTS reviews (
            icon TEXT NOT NULL, svg_sha256 TEXT NOT NULL,
            status TEXT NOT NULL CHECK(status IN ('ready', 'pending', 're-generated', 'approve', 'rejected')),
            updated_at TEXT NOT NULL, PRIMARY KEY(icon, svg_sha256))''')
        schema = connection.execute("SELECT sql FROM sqlite_master WHERE name='reviews'").fetchone()[0]
        if 'rejected' not in schema:
            connection.execute('ALTER TABLE reviews RENAME TO reviews_legacy')
            connection.execute("""CREATE TABLE reviews (
                icon TEXT NOT NULL, svg_sha256 TEXT NOT NULL,
                status TEXT NOT NULL CHECK(status IN ('ready', 'pending', 're-generated', 'approve', 'rejected')),
                updated_at TEXT NOT NULL, PRIMARY KEY(icon, svg_sha256))""")
            connection.execute('INSERT INTO reviews SELECT * FROM reviews_legacy')
            connection.execute('DROP TABLE reviews_legacy')
        # Keep the legacy pending storage value for existing Python consumers;
        # the review UI calls it Disapprove. Re-generated is retired.
        connection.execute("UPDATE reviews SET status='ready' WHERE status='re-generated'")
        # Existing feedback starts pending; never overwrite an explicit decision.
        connection.execute('''INSERT OR IGNORE INTO reviews(icon, svg_sha256, status, updated_at)
            SELECT icon, svg_sha256, 'pending', MAX(created_at)
            FROM feedback GROUP BY icon, svg_sha256''')
        # Who did what: an actor on each current record (NULL for rows saved before
        # logins were required), plus an append-only log of every action.
        for table, column in (('feedback', 'author'), ('feedback', 'edited_by'), ('feedback', 'edited_at'),
                              ('reviews', 'updated_by'), ('icon_flags', 'updated_by')):
            if column not in {row[1] for row in connection.execute(f'PRAGMA table_info({table})')}:
                connection.execute(f'ALTER TABLE {table} ADD COLUMN {column} TEXT')
        connection.execute('''CREATE TABLE IF NOT EXISTS activity_log (
            id INTEGER PRIMARY KEY, username TEXT NOT NULL, action TEXT NOT NULL, icon TEXT,
            details TEXT NOT NULL DEFAULT '{}', created_at TEXT NOT NULL)''')
        connection.execute('CREATE INDEX IF NOT EXISTS activity_log_user ON activity_log(username, id)')
        connection.execute('CREATE INDEX IF NOT EXISTS activity_log_icon ON activity_log(icon, id)')
        init_primitive_status(connection)
        init_primitive_briefs(connection)
    # Data migrations run against this installation's live database after its
    # schema is committed; no local database copy or manual attribution command.
    migrate_legacy_reviewers(path)


def utc_now():
    return datetime.now(timezone.utc).isoformat()


def record_activity(connection, username, action, icon=None, **details):
    """Append one action to the log; call inside the transaction that makes the change."""
    connection.execute('INSERT INTO activity_log(username, action, icon, details, created_at) VALUES (?, ?, ?, ?, ?)',
                       (username, action, icon, json.dumps(details, ensure_ascii=False), utc_now()))


def clear_ready_feedback(connection, key, user):
    """Resolve all saved requests when an icon is explicitly returned to Ready."""
    deleted = connection.execute('DELETE FROM feedback WHERE icon=?', (key,)).rowcount
    if deleted:
        record_activity(connection, user, 'feedback_resolved', key, deleted_count=deleted)


def review_detail(connection, key, sha):
    """Who set the icon's current review state, following the same precedence as /api/reviews."""
    split = connection.execute('SELECT created_by, created_at FROM split_requests WHERE icon=? AND svg_sha256=? AND active=1',
                               (key, sha)).fetchone()
    if split:
        return {'status': 'rejected', 'updated_by': split[0], 'updated_at': split[1]}
    rejected = connection.execute("SELECT updated_by, updated_at FROM reviews WHERE icon=? AND status='rejected' "
                                  'ORDER BY updated_at DESC LIMIT 1', (key,)).fetchone()
    if rejected:
        return {'status': 'rejected', 'updated_by': rejected[0], 'updated_at': rejected[1]}
    row = connection.execute('SELECT status, updated_by, updated_at FROM reviews WHERE icon=? AND svg_sha256=?',
                             (key, sha)).fetchone()
    return {'status': 'ready' if row[0] == 're-generated' else row[0], 'updated_by': row[1], 'updated_at': row[2]} if row else \
        {'status': 'ready', 'updated_by': None, 'updated_at': None}


PROGRESSION_TABLES = ('primitive_status', 'primitive_briefs', 'progression_imports', 'progression_reviews')
PROGRESSION_ACTIVITY = "action GLOB 'primitive_*' OR icon GLOB 'primitive:*'"


def export_feedback_snapshot(database: Path, target: Path) -> None:
    """Consistent review data copy without login sessions or progression data."""
    with closing(sqlite3.connect(database, timeout=30)) as source, closing(sqlite3.connect(target)) as copy:
        source.backup(copy)
        copy.execute('DELETE FROM admin_sessions')
        tables = {row[0] for row in copy.execute("SELECT name FROM sqlite_master WHERE type='table'")}
        for table in PROGRESSION_TABLES:
            if table in tables:
                copy.execute(f'DELETE FROM {table}')
        copy.execute(f'DELETE FROM activity_log WHERE {PROGRESSION_ACTIVITY}')
        copy.commit()
        copy.execute('VACUUM')


def sync_origin(source) -> str:
    """Reduce any pasted production URL to scheme://host."""
    parts = urlsplit(source.strip()) if isinstance(source, str) else None
    if not parts or parts.scheme not in ('http', 'https') or not parts.netloc:
        raise ValueError('Enter the production URL, for example https://example.trycloudflare.com.')
    return f'{parts.scheme}://{parts.netloc}'


def export_review_bundle(database: Path, target: Path) -> None:
    """Zip the database snapshot with the artwork, stroke-edit and reference folders."""
    snapshot = target.with_name(target.name + '.sqlite3')
    try:
        export_feedback_snapshot(database, snapshot)
        with zipfile.ZipFile(target, 'w', zipfile.ZIP_DEFLATED) as bundle:
            bundle.write(snapshot, 'feedback.sqlite3')
            bundle.writestr('stores.json', json.dumps(list(SYNC_STORES)))
            for store in SYNC_STORES:
                root = database.parent / store
                for path in sorted(root.rglob('*')) if root.is_dir() else ():
                    relative = path.relative_to(root)
                    # Skip lock files and half-written temporaries.
                    if path.is_file() and not any(part.startswith('.') for part in relative.parts) and path.suffix != '.tmp':
                        bundle.write(path, f'{store}/{relative.as_posix()}')
    finally:
        snapshot.unlink(missing_ok=True)


def extract_review_bundle(bundle: Path, folder: Path) -> list:
    """Unpack a downloaded bundle safely; returns the stores it carries."""
    try:
        with zipfile.ZipFile(bundle) as archive:
            names = archive.namelist()
            stores = json.loads(archive.read('stores.json')) if 'stores.json' in names else []
            if 'feedback.sqlite3' not in names or not isinstance(stores, list) or not set(stores) <= set(SYNC_STORES):
                raise ValueError('Production did not send a valid review data bundle.')
            for name in names:
                parts = Path(name).parts
                if name.endswith('/') or name in ('feedback.sqlite3', 'stores.json'):
                    continue
                if (name.startswith('/') or '..' in parts or '\\' in name or len(parts) < 2 or parts[0] not in stores):
                    raise ValueError('Production sent an unsafe file path: ' + name)
            archive.extractall(folder)
            return stores
    except (zipfile.BadZipFile, KeyError, UnicodeDecodeError, json.JSONDecodeError):
        raise ValueError('Production did not send a valid review data bundle.')


def replace_review_stores(data_dir: Path, incoming: Path, stores: list, backup: Path) -> dict:
    """Move each local store into the backup folder, then move production's copy into place."""
    counts = {}
    for store in stores:
        live, new = data_dir / store, incoming / store
        if live.exists():
            backup.mkdir(parents=True, exist_ok=True)
            live.rename(backup / store)
        if new.is_dir():
            new.rename(live)
        counts[store] = sum(1 for path in live.rglob('*') if path.is_file()) if live.is_dir() else 0
    return counts


def download_snapshot(origin: str, target: Path, route: str = '/api/feedback-db/export') -> str:
    """Fetch one of production's exports into target; returns its export time."""
    request = urllib.request.Request(origin + route, headers={'User-Agent': 'pictographic-sync'})
    with urllib.request.urlopen(request, timeout=SYNC_TIMEOUT) as response, target.open('wb') as stream:
        written = 0
        while chunk := response.read(1024 * 1024):
            written += len(chunk)
            if written > MAX_SYNC_BYTES:
                raise ValueError('The production database is larger than the sync limit.')
            stream.write(chunk)
        return response.headers.get('X-Feedback-Exported-At') or ''


def replace_feedback_database(database: Path, snapshot: Path, user: str, origin: str, exported_at: str = '',
                              stores_dir: Path = None, stores=()) -> dict:
    """Validate a downloaded snapshot, back up the local database and stores, then put production's copy in place."""
    try:
        with closing(sqlite3.connect(snapshot.as_uri() + '?mode=rw', uri=True)) as check:
            ok = check.execute('PRAGMA integrity_check').fetchone()
            tables = {row[0] for row in check.execute("SELECT name FROM sqlite_master WHERE type='table'")}
    except sqlite3.DatabaseError:
        raise ValueError('Production did not send a valid feedback database.')
    if not ok or ok[0] != 'ok' or not {'feedback', 'reviews'} <= tables:
        raise ValueError('Production did not send a valid feedback database.')
    # Bring an older production schema up to this code's schema before it goes live.
    init_database(snapshot)
    backups = database.parent / 'feedback-sync-backups'
    backups.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%f')
    backup = backups / f'feedback.sqlite3.before-sync-{stamp}.bak'
    with DISCARD_LOCK:
        with closing(sqlite3.connect(database, timeout=30)) as live, closing(sqlite3.connect(snapshot, timeout=30)) as incoming:
            with closing(sqlite3.connect(backup)) as copy:
                live.backup(copy)
            # Keep whoever is logged in on this machine logged in.
            incoming.execute('DELETE FROM admin_sessions')
            incoming.executemany('INSERT INTO admin_sessions VALUES (?,?,?)',
                                 live.execute('SELECT token, username, expires FROM admin_sessions').fetchall())
            # Progression belongs to this installation, even when syncing an older export.
            for table in PROGRESSION_TABLES:
                schema = live.execute("SELECT sql FROM sqlite_master WHERE type='table' AND name=?", (table,)).fetchone()
                incoming.execute(f'DROP TABLE IF EXISTS {table}')
                if schema:
                    incoming.execute(schema[0])
                    columns = [row[1] for row in live.execute(f'PRAGMA table_info({table})')]
                    incoming.executemany(f'INSERT INTO {table} VALUES ({",".join("?" for _ in columns)})',
                                         live.execute(f'SELECT * FROM {table}').fetchall())
            incoming.execute(f'DELETE FROM activity_log WHERE {PROGRESSION_ACTIVITY}')
            incoming.executemany('INSERT INTO activity_log(username,action,icon,details,created_at) VALUES (?,?,?,?,?)',
                                 live.execute(f'SELECT username,action,icon,details,created_at FROM activity_log WHERE {PROGRESSION_ACTIVITY} ORDER BY id').fetchall())
            record_activity(incoming, user, 'feedback_sync', source=origin, backup=backup.name, exported_at=exported_at)
            incoming.commit()
            counts = {table: incoming.execute(f'SELECT COUNT(*) FROM {table}').fetchone()[0] for table in SYNC_COUNTED_TABLES}
            incoming.backup(live)
        files = replace_review_stores(database.parent, stores_dir, stores, backups / f'stores.before-sync-{stamp}') if stores else {}
    return {'synced': True, 'source': origin, 'backup': backup.name, 'exported_at': exported_at, 'counts': counts,
            'stores': files}


def last_sync(connection):
    row = connection.execute("SELECT username, details, created_at FROM activity_log WHERE action='feedback_sync' ORDER BY id DESC LIMIT 1").fetchone()
    if not row:
        return None
    try:
        details = json.loads(row[1])
    except ValueError:
        details = {}
    return {'user': row[0], 'created_at': row[2], 'source': details.get('source'), 'backup': details.get('backup')}


def feedback_row(row):
    data = dict(row)
    try:
        data['reference_images'] = json.loads(data.get('reference_images') or '[]')
    except ValueError:
        data['reference_images'] = []
    return data


def live_directory(initial, releases):
    """Select one complete catalog for each request, without restarting the server."""
    if releases is None:
        return initial
    marker = Path(releases) / 'active.json'
    if not marker.exists():
        return initial
    name = json.loads(marker.read_text())['release']
    if not isinstance(name, str) or Path(name).name != name or name in ('.', '..'):
        raise ValueError('Invalid active release name.')
    assets = (Path(releases) / name / 'assets').resolve()
    if not assets.is_relative_to(Path(releases).resolve()) or not (assets / 'gallery/icons.json').is_file():
        raise ValueError('Active gallery is missing or outside release storage.')
    return assets


class GalleryServer(ThreadingHTTPServer):
    # The default backlog of 5 drops connections when a page requests hundreds of icons at once.
    request_queue_size = 256


class GalleryHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, directory, database, **kwargs):
        self.root = Path(directory() if callable(directory) else directory).resolve()
        self.database = database
        super().__init__(*args, directory=str(self.root), **kwargs)

    @property
    def evidence(self):
        if getattr(self.server, 'live_release_root', None):
            return EvidenceStore(self.root, self.database.parent / 'qa-evidence')
        return self.server.evidence

    @property
    def stroke_edits(self):
        if getattr(self.server, 'live_release_root', None):
            return StrokeEditStore(self.database.parent / 'stroke-edits', self.root / 'gallery/laboratory.json')
        return self.server.stroke_edits

    def handle(self):
        try:
            super().handle()
        except (BrokenPipeError, ConnectionResetError):
            # A browser refresh or cancelled download can close a response early.
            self.close_connection = True

    def setup(self):
        super().setup()
        self.connection.settimeout(15)

    def end_headers(self):
        self.send_header('X-Content-Type-Options', 'nosniff')
        # Static files revalidate (Last-Modified -> 304) so a grid of hundreds of SVGs and the
        # 50 MB icons.json are not refetched on every view; API responses are never cached.
        self.send_header('Cache-Control', 'no-cache' if self.__dict__.pop('static_file', False) else 'no-store')
        super().end_headers()

    def json_response(self, data, status=200):
        content = json.dumps(data, ensure_ascii=False).encode('utf-8')
        self.send_response(status)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(content)))
        self.end_headers()
        if self.command != 'HEAD':
            self.wfile.write(content)

    def current_user(self):
        cookie = SimpleCookie()
        try:
            cookie.load(self.headers.get('Cookie', ''))
            token = cookie.get('pictographic_session')
            if not token:
                return None
            digest = hashlib.sha256(token.value.encode()).hexdigest()
            with closing(sqlite3.connect(self.database, timeout=10)) as connection:
                row = connection.execute('SELECT username FROM admin_sessions WHERE token=? AND expires>?',
                                         (digest, time.time())).fetchone()
            return row[0] if row else None
        except (ValueError, CookieError, sqlite3.Error):
            return None

    def auth_action(self, route, data):
        cookie = SimpleCookie()
        try:
            cookie.load(self.headers.get('Cookie', ''))
        except CookieError:
            cookie = SimpleCookie()
        old = cookie.get('pictographic_session')
        username = data.get('username')
        if route.endswith('/login'):
            password = data.get('password')
            if (not isinstance(username, str) or not isinstance(password, str) or
                    username not in ADMIN_USERS or not secrets.compare_digest(password, ADMIN_USERS[username])):
                return self.json_response({'error': 'Incorrect username or password.'}, 401)
        with closing(sqlite3.connect(self.database, timeout=10)) as connection, connection:
            connection.execute('DELETE FROM admin_sessions WHERE expires<=?', (time.time(),))
            if old:
                digest = hashlib.sha256(old.value.encode()).hexdigest()
                ended = connection.execute('SELECT username FROM admin_sessions WHERE token=?', (digest,)).fetchone()
                connection.execute('DELETE FROM admin_sessions WHERE token=?', (digest,))
                if ended and route.endswith('/logout'):
                    record_activity(connection, ended[0], 'logout')
            token = secrets.token_urlsafe(32) if route.endswith('/login') else ''
            if token:
                connection.execute('INSERT INTO admin_sessions VALUES (?,?,?)',
                                   (hashlib.sha256(token.encode()).hexdigest(), username, time.time()+SESSION_TTL))
                record_activity(connection, username, 'login')
        content = json.dumps({'user': username if token else None}).encode()
        self.send_response(200)
        self.send_header('Set-Cookie', f'pictographic_session={token}; Path=/; HttpOnly; SameSite=Strict; Max-Age={SESSION_TTL if token else 0}')
        self.send_header('Content-Type', 'application/json')
        self.send_header('Content-Length', str(len(content)))
        self.end_headers()
        self.wfile.write(content)

    def catalog_data(self):
        path = self.root / 'gallery/icons.json'
        stat = path.stat()
        stamp = (stat.st_mtime_ns, stat.st_size)
        cached = getattr(self.server, 'catalog_cache', None)
        if not cached or cached[0] != stamp:
            cached = (stamp, json.loads(path.read_text(encoding='utf-8')))
            self.server.catalog_cache = cached
        data = dict(cached[1])
        with closing(sqlite3.connect(self.database, timeout=10)) as connection:
            uploads = [dict(json.loads(record), uploaded_svg=svg)
                       for record, svg in connection.execute('SELECT record, svg FROM uploaded_icons')]
        data['icons'] = data['icons'] + uploads
        return data

    def catalog(self, *, include_failed=False):
        data = self.catalog_data()
        rows = data['icons'] + (data.get('failed_icons', []) if include_failed else [])
        return {item['key']: self.artwork_record(item) for item in rows}

    def catalog_icon(self, key):
        data = self.catalog_data()
        record = next((row for row in data['icons'] + data.get('failed_icons', []) if row['key'] == key), None)
        return self.artwork_record(record) if record else None

    def artwork_record(self, record):
        from urllib.parse import quote
        source = baseline(record)
        choice = self.server.artwork.get(record['key'])
        result = dict(record)
        if not choice:
            return result
        result['generated_graph'] = {k: source[k] for k in GRAPH_FIELDS if k in source}
        result['generated_svg_sha256'] = source['svg_sha256']
        result['artwork_source'] = (choice or {}).get('source_mode', 'use_org')
        # A server choice takes precedence over a previous build's selection.
        selected = resolve_artwork(source, choice)
        if selected:
            if selected['graph']:
                result.update(selected['graph'])
            else:
                result.update(result['generated_graph'])
            result['svg_sha256'] = selected['svg_sha256']
            result['validation'] = {'status': 'human-selected' if selected['source_mode']=='use_upload' or selected['validation_override'] else 'valid',
                                    'automatic_status': selected['automatic_status']}
        elif record.get('artwork_source', 'use_org') != 'use_org':
            result.update(result['generated_graph'])
            result['svg_sha256'] = source['svg_sha256']
            result['validation'] = {'status': 'original'}
        if choice or record.get('artwork_source', 'use_org') != 'use_org':
            result['preview_url'] = '../api/icon-artwork/svg?icon='+quote(record['key'], safe='')+'&v='+result['svg_sha256']
        result['artwork_revision'] = (choice or {}).get('revision', 0)
        return result

    def artwork_response(self, icon):
        from urllib.parse import quote
        source = baseline(icon)
        choice = self.server.artwork.get(icon['key'])
        edit = self.stroke_edits.get(icon['key'], source['svg_sha256'])
        return {'choice': choice, 'source_mode': (choice or {}).get('source_mode', icon.get('artwork_source', 'use_org')), 'svg_sha256': source['svg_sha256'],
                'edit_revision': (edit or (choice or {}).get('edited') or {}).get('revision'),
                'preview_url': '../api/icon-artwork/svg?icon='+quote(icon['key'], safe='')+'&v='+str((choice or {}).get('revision', 0)),
                'record': self.artwork_record(icon)}

    def primitives_catalog(self):
        """gallery/primitives.json, reparsed only when a build or refresh replaces it."""
        path = self.root / 'gallery/primitives.json'
        stamp = path.stat().st_mtime_ns
        cached = getattr(self.server, 'primitives_cache', None)
        if not cached or cached[0] != stamp:
            cached = (stamp, json.loads(path.read_text(encoding='utf-8')))
            self.server.primitives_cache = cached
        return cached[1]

    def serve_primitive(self, path):
        """Original primitive artwork, from outside dist; SVG only, sandboxed like reference images."""
        base = self.server.primitives_root
        relative = unquote(path[len('/primitives/'):])
        parts = Path(relative).parts
        candidate = (base / relative).resolve()
        if (not relative or any(part.startswith('.') or part == '..' for part in parts) or
                not candidate.is_relative_to(base) or candidate.suffix.lower() != '.svg' or not candidate.is_file()):
            return self.json_response({'error': 'Not found'}, 404)
        content = candidate.read_bytes()
        self.send_response(200)
        self.send_header('Content-Type', 'image/svg+xml')
        self.send_header('Content-Length', str(len(content)))
        self.send_header('Content-Security-Policy', "default-src 'none'; style-src 'unsafe-inline'; sandbox")
        self.end_headers()
        if self.command != 'HEAD':
            self.wfile.write(content)

    def is_rejected(self, connection, key, sha):
        return bool(connection.execute(
            "SELECT 1 FROM reviews WHERE icon=? AND status='rejected' "
            "UNION ALL SELECT 1 FROM split_requests WHERE icon=? AND svg_sha256=? AND active=1",
            (key, key, sha),
        ).fetchone())

    def production_blocked(self, route):
        if not getattr(getattr(self, 'server', None), 'production', False):
            return False
        return (route.startswith('/api/generation') or route.startswith('/api/ai-feedback')
                or route in ('/api/icons/discard', '/api/feedback-db/sync',
                             '/api/combination-refresh', '/api/combination-experiment'))

    def do_GET(self):
        parsed = urlsplit(self.path)
        if parsed.path == '/api/runtime':
            production = getattr(self.server, 'production', False)
            return self.json_response({'mode': 'production' if production else 'development',
                                       'can_generate': not production, 'can_edit': True, 'can_upload': True})
        if self.production_blocked(parsed.path):
            return self.json_response({'error': 'This action belongs to the development workspace.'}, 403)
        if parsed.path == '/api/combination-refresh':
            from icon_set.scripts.combination_refresh_job import status
            return self.json_response(status())
        if parsed.path == '/api/icon-categories':
            try:
                data = self.catalog_data()
                categories = {'manual_upload'}
                for row in data.get('icons', []) + data.get('failed_icons', []):
                    category = row.get('category')
                    if isinstance(category, str) and category.strip():
                        categories.add(category.strip())
                return self.json_response({'categories': sorted(categories, key=lambda value: (value.casefold(), value))})
            except (OSError, ValueError, sqlite3.Error):
                return self.json_response({'error': 'Could not load categories. You can still type a category.'}, 503)
        if parsed.path == '/gallery/icons.json':
            try:
                data = dict(self.catalog_data())
                for field in ('icons', 'failed_icons'):
                    data[field] = [{k: v for k, v in self.artwork_record(row).items() if k != 'uploaded_svg'} for row in data.get(field, [])]
                return self.json_response(data)
            except (OSError, ValueError):
                return self.json_response({'error': 'Artwork storage is unavailable.'}, 503)
        if parsed.path in ('/api/icon-artwork', '/api/icon-artwork/svg'):
            key = parse_qs(parsed.query).get('icon', [''])[0]
            try:
                icon = self.catalog_icon(key)
                if not icon:
                    return self.json_response({'error': 'Icon not found.'}, 404)
                if parsed.path == '/api/icon-artwork':
                    return self.json_response(self.artwork_response(icon))
                variant = parse_qs(parsed.query).get('variant', [None])[0]
                choice = self.server.artwork.get(key)
                if variant == 'browser_edit':
                    edit = self.stroke_edits.get(key, baseline(icon)['svg_sha256']) or (choice or {}).get('edited')
                    if not edit:
                        raise ValueError('No browser edit has been saved yet.')
                    selected = {'svg': icon_from_graph(edit['edited_graph']).to_svg()}
                else:
                    selected = resolve_artwork(icon, choice, variant=variant)
                if not choice and not icon.get('uploaded_icon') and variant is None and icon.get('artwork_source', 'use_org') != 'use_org':
                    # A published manual SVG still displays when only dist was copied.
                    # Editing its source choice requires restoring persistent storage.
                    path = (self.root / 'gallery' / unquote(urlsplit(icon['preview_url']).path)).resolve()
                    if not path.is_relative_to(self.root) or path.suffix != '.svg':
                        raise ValueError('Published artwork path is invalid.')
                    document = path.read_text(encoding='utf-8')
                else:
                    document = selected['svg'] if selected else icon_from_graph(baseline(icon)).to_svg()
                content = document.encode('utf-8')
                self.send_response(200)
                self.send_header('Content-Type', 'image/svg+xml')
                self.send_header('Content-Length', str(len(content)))
                self.send_header('Cache-Control', 'no-store')
                self.send_header('X-Content-Type-Options', 'nosniff')
                self.send_header('Content-Security-Policy', "default-src 'none'; style-src 'unsafe-inline'; sandbox")
                self.end_headers(); self.wfile.write(content)
                return
            except (ValueError, KeyError, TypeError) as error:
                return self.json_response({'error': str(error)}, 400)
            except (OSError, ImportError):
                return self.json_response({'error': 'Artwork is unavailable on this server.'}, 503)
        if parsed.path == '/api/stroke-edits':
            key = parse_qs(parsed.query).get('icon', [''])[0]
            icon = self.catalog_icon(key)
            if not icon:
                return self.json_response({'error': 'Icon not found.'}, 404)
            icon = baseline(icon)
            try:
                return self.json_response({
                    'svg_sha256': icon['svg_sha256'],
                    'edit': self.stroke_edits.get(key, icon['svg_sha256']),
                    'previous_versions': self.stroke_edits.previous_versions(key, icon['svg_sha256']),
                })
            except (OSError, ValueError):
                return self.json_response({'error': 'Saved edits are unavailable. Try loading them again.'}, 503)
        if parsed.path == '/api/auth/session':
            return self.json_response({'user': self.current_user()})
        if parsed.path == '/api/ai-feedback':
            user = self.current_user() or 'system'
            try:
                row = self.server.ai_feedback.read(parse_qs(parsed.query).get('id', [''])[0])
                if row['created_by'] != user:
                    return self.json_response({'error': 'This review belongs to another user.'}, 403)
                current = self.catalog(include_failed=True).get(row['icon'])
                if not current or current['svg_sha256'] != row['svg_sha256']:
                    row = {k: v for k, v in row.items() if k not in ('feedback', 'verdict')}
                    row.update(status='stale', error='The artwork changed during review. Ask again for this version.')
                return self.json_response(row)
            except ValueError as error:
                return self.json_response({'error': str(error)}, 400)
            except OSError:
                return self.json_response({'error': 'AI feedback is temporarily unavailable.'}, 503)
        if parsed.path.startswith('/api/generation'):
            try:
                manager = self.server.generation
                if parsed.path == '/api/generation':
                    return self.json_response(manager.listing())
                if parsed.path in ('/api/generation/preview', '/api/generation/log'):
                    content, mime = manager.artifact(parse_qs(parsed.query).get('id', [''])[0], parsed.path.rsplit('/',1)[1])
                    self.send_response(200)
                    self.send_header('Content-Type', mime)
                    self.send_header('Content-Length', str(len(content)))
                    self.send_header('Content-Security-Policy', "default-src 'none'; style-src 'unsafe-inline'; sandbox")
                    self.end_headers()
                    self.wfile.write(content)
                    return
                return self.json_response({'error': 'Unknown generation route.'}, 404)
            except (OSError, ValueError) as error:
                return self.json_response({'error': str(error)}, 400)
        if parsed.path == '/api/reference-images':
            try:
                content, mime = self.server.references.read(parse_qs(parsed.query).get('id', [''])[0])
            except (OSError, ValueError) as error:
                return self.json_response({'error': str(error)}, 404)
            self.send_response(200)
            self.send_header('Content-Type', mime)
            self.send_header('Content-Length', str(len(content)))
            self.send_header('Content-Security-Policy', "default-src 'none'; style-src 'unsafe-inline'; sandbox")
            self.end_headers()
            self.wfile.write(content)
            return
        if parsed.path.startswith('/primitives/'):
            return self.serve_primitive(parsed.path)
        if parsed.path == '/api/combinations/container/results':
            try:
                from icon_set.scripts.container_combination_results import listing
                return self.json_response(listing(self.root, PACKAGE_ROOT / 'data', self.database.parent))
            except (OSError, ValueError, sqlite3.Error):
                return self.json_response({'error': 'Combination results are temporarily unavailable'}, 503)
        if parsed.path in ('/api/combinations/container/latest', '/api/combinations/container/svg'):
            try:
                from icon_set.scripts.latest_container_combinations import LatestContainerPairs
                query = parse_qs(parsed.query)
                if parsed.path.endswith('/svg') and not query.get('id', [''])[0]:
                    raise ValueError('A combination id is required')
                if parsed.path.endswith('/svg'):
                    from icon_set.scripts.container_combination_results import saved_svg
                    cached_svg = saved_svg(self.root, PACKAGE_ROOT / 'data', self.database.parent, query['id'][0])
                else:
                    cached_svg = None
                result = ({'pairs': [{'svg': cached_svg}]} if cached_svg else
                          LatestContainerPairs(self.root, PACKAGE_ROOT / 'data').response(query))
                if parsed.path.endswith('/svg'):
                    if not result['pairs']:
                        return self.json_response({'error': 'Combination not found'}, 404)
                    pair = result['pairs'][0]
                    if 'svg' not in pair:
                        return self.json_response(pair, 409)
                    content = pair['svg'].encode('utf-8')
                    self.send_response(200)
                    self.send_header('Content-Type', 'image/svg+xml')
                    self.send_header('Content-Length', str(len(content)))
                    self.send_header('Content-Security-Policy', "default-src 'none'; style-src 'unsafe-inline'; sandbox")
                    self.end_headers()
                    self.wfile.write(content)
                    return
                for pair in result['pairs']:
                    pair.pop('svg', None)
                return self.json_response(result)
            except ValueError as error:
                return self.json_response({'error': str(error)}, 400)
            except OSError:
                return self.json_response({'error': 'Container combinations are temporarily unavailable'}, 503)
        if parsed.path == '/api/combinations/generation-queue':
            try:
                from icon_set.scripts.container_symbol_queue import generation_queue as symbol_queue
                combinations = json.loads((self.root / 'gallery/combinations.json').read_text())
                manifest = json.loads((self.root / 'symbol32/manifest.json').read_text())
                return self.json_response(symbol_queue(
                    combinations, manifest, self.primitives_catalog(), parse_qs(parsed.query)))
            except ValueError as error:
                return self.json_response({'error': str(error)}, 400)
            except OSError:
                return self.json_response({'error': 'Container symbol queue is temporarily unavailable'}, 503)
        if parsed.path == '/api/primitives/generation-queue':
            try:
                from icon_set.scripts.primitive_decision_history import load_history
                with closing(sqlite3.connect(self.database, timeout=10)) as connection:
                    statuses = load_status(connection)
                    briefs = load_primitive_briefs(connection)
                    classification_history = load_history(connection, ADMIN_USERS)
                return self.json_response(generation_queue(
                    self.primitives_catalog(), statuses, briefs, parse_qs(parsed.query), classification_history))
            except ValueError as error:
                return self.json_response({'error': str(error)}, 400)
            except (OSError, sqlite3.Error):
                return self.json_response({'error': 'Generation queue is temporarily unavailable'}, 503)
        if parsed.path == '/api/primitives/briefs':
            try:
                with closing(sqlite3.connect(self.database, timeout=10)) as connection:
                    return self.json_response(load_primitive_briefs(connection))
            except sqlite3.Error:
                return self.json_response({'error': 'Primitive briefs are temporarily unavailable'}, 503)
        if parsed.path in ('/api/primitives', '/api/primitives/status', '/api/primitives/summary'):
            try:
                with closing(sqlite3.connect(self.database, timeout=10)) as connection:
                    statuses = load_status(connection)
                if parsed.path == '/api/primitives/status':
                    return self.json_response(statuses)
                merged = merge(self.primitives_catalog()['rows'], statuses)
                if parsed.path == '/api/primitives/summary':
                    return self.json_response(summarize(merged))
                query = parse_qs(parsed.query)
                one = lambda name: query.get(name, [None])[0]  # noqa: E731
                return self.json_response(list(filter_rows(merged, one('category'), one('status'),
                                                           one('batch'), one('reason'))))
            except (OSError, ValueError, sqlite3.Error):
                return self.json_response({'error': 'Primitive progress is temporarily unavailable'}, 503)
        if parsed.path in ('/api/qa-evidence', '/api/qa-evidence/image'):
            query = parse_qs(parsed.query)
            key = query.get('icon', [''])[0]
            try:
                if parsed.path == '/api/qa-evidence':
                    return self.json_response(self.evidence.evidence(key))
                content = self.evidence.image(key, query.get('kind', [''])[0])
            except KeyError:
                return self.json_response({'error': 'Unknown icon'}, 404)
            except (FileNotFoundError, ValueError) as error:
                return self.json_response({'error': str(error) or 'Evidence image unavailable.'}, 404)
            except Exception as error:  # a checker crash must surface, never read as a pass
                return self.json_response({'error': f'Validation evidence failed: {error}'}, 500)
            self.send_response(200)
            self.send_header('Content-Type', 'image/png')
            self.send_header('Content-Length', str(len(content)))
            self.end_headers()
            self.wfile.write(content)
            return
        if parsed.path == '/api/icon-types':
            query = parse_qs(parsed.query)
            wanted = query.get('type', [None])[0]
            try:
                catalog = self.catalog(include_failed=True)
                with closing(sqlite3.connect(self.database, timeout=10)) as connection:
                    types = connection.execute('SELECT icon,icon_type,updated_at,updated_by FROM icon_types WHERE icon_type != \'\'').fetchall()
                    result = []
                    for key, icon_type, at, actor in types:
                        if key not in catalog or (wanted is not None and icon_type != wanted):
                            continue
                        icon = catalog[key]
                        review = review_detail(connection, key, icon['svg_sha256'])
                        status = 'disapprove' if review['status'] == 'pending' else review['status']
                        if query.get('status') and query['status'][0] != status:
                            continue
                        feedback = connection.execute('SELECT reason,feedback FROM feedback WHERE icon=? AND svg_sha256=? ORDER BY id DESC LIMIT 1', (key, icon['svg_sha256'])).fetchone()
                        result.append({'icon': key, 'icon_type': icon_type, 'status': status,
                                       'python_source': icon.get('python_source'), 'svg_sha256': icon['svg_sha256'],
                                       'reason': feedback[0] if feedback else None, 'feedback': feedback[1] if feedback else None,
                                       'updated_at': at, 'updated_by': actor})
                return self.json_response({'icons': result})
            except (OSError, ValueError, sqlite3.Error):
                return self.json_response({'error': 'Icon types are temporarily unavailable.'}, 503)
        if parsed.path == '/api/icon-type':
            key = parse_qs(parsed.query).get('icon', [''])[0]
            try:
                if key not in self.catalog():
                    return self.json_response({'error': 'Unknown icon'}, 404)
                with closing(sqlite3.connect(self.database, timeout=10)) as connection:
                    row = connection.execute('SELECT icon_type, updated_by, updated_at FROM icon_types WHERE icon=?', (key,)).fetchone()
                return self.json_response({'icon_type': row[0], 'updated_by': row[1], 'updated_at': row[2]} if row
                                          else {'icon_type': '', 'updated_by': None, 'updated_at': None})
            except (OSError, ValueError, sqlite3.Error):
                return self.json_response({'error': 'Could not load icon type.'}, 503)
        if parsed.path == '/api/icon-flag':
            key = parse_qs(parsed.query).get('icon', [''])[0]
            try:
                if key not in self.catalog():
                    return self.json_response({'error': 'Unknown icon'}, 404)
                with closing(sqlite3.connect(self.database, timeout=10)) as connection:
                    row = connection.execute('SELECT flag, updated_by, updated_at FROM icon_flags WHERE icon=?', (key,)).fetchone()
                return self.json_response({'flag': row[0], 'updated_by': row[1], 'updated_at': row[2]} if row
                                          else {'flag': '', 'updated_by': None, 'updated_at': None})
            except (OSError, ValueError, sqlite3.Error):
                return self.json_response({'error': 'Could not load icon flag.'}, 503)
        if parsed.path == '/api/pending-briefs/download':
            try:
                with closing(sqlite3.connect(self.database, timeout=10)) as connection:
                    rows = list_briefs(connection)
                if not rows:
                    return self.json_response({'error': 'No briefs to download yet.'}, 404)
                content = brief_archive(rows, self.catalog(), self.root, PACKAGE_ROOT.parent)
            except (OSError, ValueError, sqlite3.Error):
                return self.json_response({'error': 'Could not prepare the brief download. Please retry.'}, 503)
            self.send_response(200)
            self.send_header('Content-Type', 'application/zip')
            self.send_header('Content-Disposition', 'attachment; filename="pending-briefs.zip"')
            self.send_header('Content-Length', str(len(content)))
            self.end_headers()
            self.wfile.write(content)
            return
        if parsed.path == '/api/pending-briefs':
            try:
                with closing(sqlite3.connect(self.database, timeout=10)) as connection:
                    return self.json_response(list_briefs(connection))
            except sqlite3.Error:
                return self.json_response({'error': 'Pending briefs unavailable'}, 503)
        if parsed.path == '/api/feedback-db/export':
            return self.export_feedback_db()
        if parsed.path == '/api/review-data/export':
            return self.export_feedback_db(bundle=True)
        if parsed.path == '/api/feedback-db/sync':
            try:
                with closing(sqlite3.connect(self.database, timeout=10)) as connection:
                    latest = last_sync(connection)
                return self.json_response({'default_source': getattr(self.server, 'sync_source', DEFAULT_SYNC_SOURCE), 'last_sync': latest})
            except sqlite3.Error:
                return self.json_response({'error': 'Sync status is temporarily unavailable.'}, 503)
        if parsed.path == '/api/feedback-feed':
            try:
                with closing(sqlite3.connect(self.database, timeout=10)) as connection:
                    connection.row_factory = sqlite3.Row
                    rows = connection.execute(
                        "SELECT f.*, COALESCE(t.icon_type, '') AS icon_type FROM feedback f LEFT JOIN icon_types t ON t.icon=f.icon ORDER BY f.id DESC"
                    ).fetchall()
                return self.json_response([feedback_row(row) for row in rows])
            except sqlite3.Error:
                return self.json_response({'error': 'Feedback is temporarily unavailable'}, 503)
        if parsed.path == '/api/reviewer-stats':
            try:
                with closing(sqlite3.connect(self.database, timeout=10)) as connection:
                    result = reviewer_stats(connection, parse_qs(parsed.query), ADMIN_USERS, self.catalog(include_failed=True))
                return self.json_response(result)
            except ValueError as error:
                return self.json_response({'error': str(error)}, 400)
            except (OSError, sqlite3.Error):
                return self.json_response({'error': 'Reviewer activity is temporarily unavailable. Try again.'}, 503)
        if parsed.path == '/api/reviews':
            try:
                catalog = self.catalog(include_failed=True)
                with closing(sqlite3.connect(self.database, timeout=10)) as connection:
                    statuses, approved_by, disapproved_by, rejected_by = current_reviews(connection, catalog)
                    if parse_qs(parsed.query).get('include_approvers') == ['1']:
                        authors = connection.execute('SELECT DISTINCT icon, author FROM feedback WHERE author IS NOT NULL ORDER BY icon, author').fetchall()
                        feedback_by = {}
                        for key, actor in authors:
                            if key in catalog and actor:
                                feedback_by.setdefault(key, []).append(actor)
                        return self.json_response({'statuses': statuses, 'approved_by': approved_by,
                                                   'rejected_by': rejected_by,
                                                   'disapproved_by': disapproved_by, 'feedback_by': feedback_by})
                return self.json_response(statuses)
            except (OSError, ValueError, sqlite3.Error):
                return self.json_response({'error': 'Review statuses are temporarily unavailable'}, 503)
        if parsed.path == '/api/review-detail':
            key = parse_qs(parsed.query).get('icon', [''])[0]
            try:
                catalog = self.catalog()
                if key not in catalog:
                    return self.json_response({'error': 'Unknown icon'}, 404)
                with closing(sqlite3.connect(self.database, timeout=10)) as connection:
                    return self.json_response(review_detail(connection, key, catalog[key]['svg_sha256']))
            except (OSError, ValueError, sqlite3.Error):
                return self.json_response({'error': 'Review details are temporarily unavailable'}, 503)
        if parsed.path == '/api/feedback':
            key = parse_qs(parsed.query).get('icon', [''])[0]
            try:
                if key not in self.catalog(include_failed=True):
                    return self.json_response({'error': 'Unknown icon'}, 404)
                with closing(sqlite3.connect(self.database, timeout=10)) as connection, connection:
                    connection.row_factory = sqlite3.Row
                    rows = connection.execute(
                        'SELECT id, feedback, svg_sha256, created_at, reference_images, author, edited_by, edited_at, reason FROM feedback WHERE icon=? ORDER BY id DESC LIMIT 100',
                        (key,),
                    ).fetchall()
                return self.json_response([feedback_row(row) for row in rows])
            except (OSError, ValueError, sqlite3.Error):
                return self.json_response({'error': 'Feedback is temporarily unavailable'}, 503)
        return super().do_GET()

    def send_head(self):
        path = unquote(urlsplit(self.path).path)
        if path == '/':
            self.send_response(302)
            self.send_header('Location', '/gallery/home.html')
            self.send_header('Content-Length', '0')
            self.end_headers()
            return None
        parts = Path(path.lstrip('/')).parts
        candidate = (self.root / path.lstrip('/')).resolve()
        if candidate == self.root / 'gallery/generate.html' and not self.current_user():
            self.send_response(302)
            self.send_header('Location', '/gallery/login.html')
            self.send_header('Content-Length', '0')
            self.end_headers()
            return None
        # No directory listings, hidden build stages, traversal or symlink escapes.
        if (any(part.startswith('.') for part in parts) or
                not candidate.is_relative_to(self.root) or not candidate.is_file() or
                candidate.suffix.lower() not in {'.html', '.json', '.svg', '.png', '.css', '.js'}):
            self.send_error(404)
            return None
        self.static_file = True
        return super().send_head()

    def do_POST(self):
        route = urlsplit(self.path).path
        if self.production_blocked(route):
            return self.json_response({'error': 'This action belongs to the development workspace.'}, 403)
        original_route = route
        if route not in ('/api/combinations/container/combine', '/api/combination-refresh', '/api/combination-experiment', '/api/icons/upload', '/api/ai-feedback', '/api/icon-artwork', '/api/stroke-edits/validate', '/api/stroke-edits', '/api/auth/login', '/api/auth/logout', '/api/generation', '/api/generation/accept', '/api/generation/discard', '/api/icon-type', '/api/icon-flag', '/api/feedback/delete', '/api/feedback/edit', '/api/feedback', '/api/reviews', '/api/reject-combination', '/api/pending-briefs/complete', '/api/reject-combination/restore', '/api/reference-images', '/api/icons/discard', '/api/primitives/status', '/api/primitives/briefs', '/api/feedback-db/sync'):
            return self.json_response({'error': 'Not found'}, 404)
        # Login identifies a human reviewer; sessionless API calls are system actions.
        user = self.current_user() or 'system'
        origin = self.headers.get('Origin')
        if origin and (urlsplit(origin).scheme not in ('http', 'https') or
                       urlsplit(origin).netloc != self.headers.get('Host')):
            return self.json_response({'error': 'Cross-origin feedback is not allowed'}, 403)
        if self.headers.get_content_type() != 'application/json':
            return self.json_response({'error': 'Expected application/json'}, 415)
        try:
            size = int(self.headers.get('Content-Length', '0'))
        except ValueError:
            size = 0
        limit = {'/api/combination-experiment': 3 * 1024 * 1024, '/api/icons/upload': 2 * 1024 * 1024, '/api/icon-artwork': 2 * 1024 * 1024, '/api/generation': 131072, '/api/reference-images': MAX_REFERENCE_BODY}.get(route, MAX_BODY)
        if self.headers.get('Transfer-Encoding') or not 0 < size <= limit:
            return self.json_response({'error': 'Invalid request size' if route != '/api/reference-images' else 'Reference image is too large.'}, 413)
        try:
            data = json.loads(self.rfile.read(size))
            if not isinstance(data, dict):
                raise ValueError()
            if route == '/api/combinations/container/combine':
                from icon_set.scripts.container_combination_results import combine
                try:
                    query = {k: [str(v)] for k, v in data.items()}
                    return self.json_response(combine(self.root, PACKAGE_ROOT / 'data', self.database.parent, query))
                except ValueError as error:
                    return self.json_response({'error': str(error)}, 400)
                except (OSError, sqlite3.Error):
                    return self.json_response({'error': 'Could not save combination previews'}, 503)
            if route == '/api/combination-refresh':
                from icon_set.scripts.combination_refresh_job import start
                return self.json_response(start(), 202)
            if route == '/api/combination-experiment':
                from icon_set.scripts.combination_experiment import render
                try:
                    return self.json_response(render(data))
                except (ValueError, OSError) as error:
                    return self.json_response({'error': str(error)}, 422)
            if route == '/api/icons/upload':
                return self.upload_icon(data, user)
            if route == '/api/ai-feedback':
                try:
                    key = data.get('icon')
                    if not isinstance(key, str):
                        raise ValueError('Choose an icon to review.')
                    icon = self.catalog_icon(key)
                    if not icon or icon['svg_sha256'] != data.get('svg_sha256'):
                        return self.json_response({'error': 'The icon changed. Refresh before asking for feedback.'}, 409)
                    chosen = resolve_artwork(icon, self.server.artwork.get(key))
                    if chosen:
                        document = chosen['svg']
                    else:
                        # Match the displayed export, even if its Python source changed later.
                        preview = (self.root/'gallery'/urlsplit(icon.get('preview_url', '')).path).resolve()
                        document = (preview.read_text() if preview.is_relative_to(self.root) and preview.is_file()
                                    else icon_from_graph(baseline(icon)).to_svg())
                    result = self.server.ai_feedback.start(data, icon, document, user)
                    return self.json_response(result, 202)
                except (ValueError, KeyError, TypeError) as error:
                    return self.json_response({'error': str(error)}, 400)
                except (OSError, ImportError):
                    return self.json_response({'error': 'Could not start AI feedback. Check the server and try again.'}, 503)
            if route == '/api/icon-artwork':
                return self.save_artwork(data, user)
            if route in ('/api/stroke-edits', '/api/stroke-edits/validate'):
                return self.save_stroke_edits(data, user, validate_only=route.endswith('/validate'))
            if route == '/api/reference-images':
                return self.upload_reference(data, user)
            if route in ('/api/auth/login', '/api/auth/logout'):
                return self.auth_action(route, data)
            if route in ('/api/reject-combination', '/api/pending-briefs/complete', '/api/reject-combination/restore'):
                return self.brief_action(route, data, user)
            if route in ('/api/generation', '/api/generation/accept', '/api/generation/discard'):
                try:
                    if route == '/api/generation' and data.get('mode') == 'fix':
                        icon = self.catalog().get(data.get('icon'))
                        if icon:
                            with closing(sqlite3.connect(self.database, timeout=10)) as connection:
                                if self.is_rejected(connection, icon['key'], icon['svg_sha256']):
                                    return self.json_response({'error': 'Restore this rejected icon before regenerating it.'}, 409)
                    manager = self.server.generation
                    if route == '/api/generation':
                        result = manager.start(data, self.catalog(), user)
                        action, details = result['mode'], {'job': result['id'], 'name': result['name']}
                    else:
                        result = manager.decide(data.get('id'), route.endswith('/accept'), user)
                        action, details = 'generation_' + route.rsplit('/', 1)[1], {'job': result['id'], 'name': result['name']}
                    with closing(sqlite3.connect(self.database, timeout=10)) as connection, connection:
                        record_activity(connection, user, action, (result.get('source') or {}).get('key'), **details)
                    return self.json_response(result, 202)
                except (OSError, ValueError) as error:
                    return self.json_response({'error': str(error)}, 400)
                except sqlite3.Error:
                    return self.json_response({'error': 'Review statuses are temporarily unavailable'}, 503)
            if route == '/api/icons/discard':
                return self.discard_icon(data, user)
            if route == '/api/feedback-db/sync':
                return self.sync_feedback(data, user)
            if route == '/api/primitives/briefs':
                return self.save_primitive_brief(data, user)
            if route == '/api/primitives/status':
                return self.save_primitive_status(data, user)
            if route == '/api/icon-flag':
                return self.save_icon_flag(data, user)
            if route == '/api/icon-type':
                return self.save_icon_type(data, user)
            if route == '/api/feedback/delete':
                return self.delete_feedback(data, user)
            if route == '/api/feedback/edit':
                return self.edit_feedback(data, user)
            key, feedback = data.get('icon'), data.get('feedback')
            if not isinstance(data.get('status', ''), str) or not isinstance(data.get('reason', ''), str):
                raise ValueError()
            status = {'disapprove': 'pending', 're-generated': 'ready'}.get(data.get('status'), data.get('status'))
            reason = {'bad-draw': 'bad-stroke'}.get(data.get('reason'), data.get('reason', 'other'))
            if not isinstance(key, str):
                raise ValueError()
            if route == '/api/reviews' and status == 'pending' and ('reason' in data or 'feedback' in data):
                labels = {'bad-stroke': 'Bad stroke drawn', 'meaning': 'Does not convey the intended meaning', 'manual-fix-request': 'Manual fix request'}
                details = data.get('feedback', '')
                if not isinstance(details, str) or reason not in ('bad-stroke', 'meaning', 'manual-fix-request', 'other') or (reason == 'other' and not details.strip()):
                    return self.json_response({'error': 'Choose a disapproval reason; Other requires feedback.'}, 400)
                feedback = '\n\n'.join(filter(None, (labels.get(reason), details.strip())))
                route = '/api/feedback'
            if route == '/api/feedback':
                if data.get('feedback_id') is not None and (type(data['feedback_id']) is not int or not isinstance(data.get('previous_feedback'), str)):
                    raise ValueError()
                if reason not in ('bad-stroke', 'meaning', 'manual-fix-request', 'other'):
                    return self.json_response({'error': 'Choose a valid disapproval reason.'}, 400)
                if not isinstance(feedback, str) or not 1 <= len(feedback.strip()) <= 10000:
                    raise ValueError()
                try:
                    references = self.server.references.resolve(data.get('reference_images'))
                except ValueError as error:
                    return self.json_response({'error': str(error)}, 400)
                status = 'pending'
            elif status not in ('ready', 'pending', 're-generated', 'approve', 'rejected'):
                raise ValueError()
            icon = self.catalog(include_failed=route == '/api/feedback').get(key)
            if icon is None:
                return self.json_response({'error': 'Unknown icon'}, 404)
            sha = icon.get('svg_sha256') or ''
            if (data.get('svg_sha256') or '') != sha:
                return self.json_response({'error': 'Icon changed; reload the gallery before submitting'}, 409)
        except (ValueError, UnicodeError):
            return self.json_response({'error': 'Invalid feedback or review status'}, 400)
        except OSError:
            return self.json_response({'error': 'Gallery is temporarily unavailable'}, 503)
        try:
            with closing(sqlite3.connect(self.database, timeout=10)) as connection, connection:
                if original_route == '/api/reviews' and connection.execute(
                    'SELECT 1 FROM split_requests WHERE icon=? AND svg_sha256=? AND active=1',
                    (key, sha),
                ).fetchone():
                    return self.json_response({'error': 'This combined icon is rejected. Restore it before changing its review status.'}, 409)
                if self.is_rejected(connection, key, sha):
                    if original_route == '/api/feedback':
                        status = 'rejected'
                    elif status != 'rejected':
                        return self.json_response({'error': 'Restore this rejected icon before changing its review status.'}, 409)
                now = datetime.now(timezone.utc).isoformat()
                if route == '/api/feedback':
                    feedback_id = data.get('feedback_id')
                    if feedback_id is not None:
                        updated = connection.execute(
                            '''UPDATE feedback SET feedback=?, reason=?, reference_images=?, edited_by=?, edited_at=?
                               WHERE id=? AND icon=? AND svg_sha256=? AND feedback=? AND author=?''',
                            (feedback.strip(), reason, json.dumps(references), user, now, feedback_id, key, sha, data['previous_feedback'], user))
                        if not updated.rowcount:
                            return self.json_response({'error': 'Feedback changed. Reopen the icon before editing again.'}, 409)
                    else:
                        feedback_id = connection.execute(
                            'INSERT INTO feedback(icon, feedback, svg_sha256, created_at, reference_images, author, reason) VALUES (?, ?, ?, ?, ?, ?, ?)',
                            (key, feedback.strip(), sha, now, json.dumps(references), user, reason),
                        ).lastrowid
                    record_activity(connection, user, 'feedback_edit' if data.get('feedback_id') is not None else 'feedback', key, feedback_id=feedback_id, status=status, reason=reason,
                                    reference_images=[ref['id'] for ref in references])
                else:
                    record_activity(connection, user, 'review', key, status=status, svg_sha256=sha)
                connection.execute(
                    '''INSERT INTO reviews(icon, svg_sha256, status, updated_at, updated_by) VALUES (?, ?, ?, ?, ?)
                       ON CONFLICT(icon, svg_sha256) DO UPDATE SET
                       status=excluded.status, updated_at=excluded.updated_at, updated_by=excluded.updated_by''',
                    (key, sha, status, now, user),
                )
                if status == 'ready':
                    clear_ready_feedback(connection, key, user)
            result = {'saved': True, 'status': status, 'updated_by': user}
            if route == '/api/feedback':
                result.update(id=feedback_id, feedback=feedback.strip())
            return self.json_response(result, 201)
        except sqlite3.Error:
            return self.json_response({'error': 'Could not save feedback'}, 503)

    def upload_icon(self, data, user):
        """Create a persistent SVG-only icon and its initial review atomically."""
        try:
            name, family = data.get('name'), data.get('family')
            if not isinstance(name, str) or not 1 <= len(name.strip()) <= 120:
                raise ValueError('Enter an icon name up to 120 characters.')
            if not isinstance(family, str) or family not in ('sub', 'symbol', 'solo', 'container'):
                raise ValueError('Choose sub, solo, or container.')
            category = data.get('category', 'manual_upload')
            if not isinstance(category, str) or len(category) > 100:
                raise ValueError('Enter a category up to 100 characters.')
            bypass = data.get('bypass_validation', True)
            if type(bypass) is not bool:
                raise ValueError('bypass_validation must be a JSON boolean: true or false.')
            canvas = {'sub': 32, 'symbol': 32, 'solo': 48, 'container': 64}[family]
            document = safe_svg(data.get('svg'), canvas)
            validation = validate_upload(document, canvas, bypass=bypass)
            if validation['status'] in ('fail', 'error'):
                return self.json_response({'error': 'Upload validation failed.' if validation['status']=='fail' else 'Upload validation is unavailable.',
                                           'validation': validation}, 422 if validation['status']=='fail' else 503)
            digest = sha(document)
            slug = re.sub(r'[^a-z0-9]+', '-', name.lower()).strip('-')[:80] or 'icon'
            icon_id = slug + '-upload-' + secrets.token_hex(8)
            key = family + '/' + icon_id
            now = utc_now()
            record = dict(key=key, icon_id=icon_id, name=name.strip(), family=family,
                          profile=family.upper()+str(canvas), canvas_size=canvas,
                          category=category.strip() or 'manual_upload', icon_type='uploaded', keywords=[], aliases=[],
                          svg_sha256=digest, uploaded_icon=True, artwork_source='use_org',
                          preview_url='../api/icon-artwork/svg?icon='+key+'&v='+digest,
                          author=user, created_at=now, modified_at=now, original_sources=[],
                          primitives=[], contours=[], relationships=[], anchors={},
                          style={'stroke_width': 4}, keyshape='FREE', keyshape_bounds=[0, 0, canvas, canvas],
                          bypass_validation=bypass, validation=validation)
            with DISCARD_LOCK:
                with closing(sqlite3.connect(self.database, timeout=10)) as connection, connection:
                    connection.execute('INSERT INTO uploaded_icons VALUES (?,?,?)',
                                       (key, json.dumps(record), document))
                    connection.execute("INSERT INTO reviews(icon,svg_sha256,status,updated_at,updated_by) VALUES (?,?,'ready',?,?)",
                                       (key, digest, now, user))
                    connection.execute('INSERT INTO icon_types(icon,icon_type,updated_at,updated_by) VALUES (?,?,?,?)',
                                       (key, 'uploaded', now, user))
                    record_activity(connection, user, 'upload', key, svg_sha256=digest, status='ready',
                                    category=record['category'], icon_type='uploaded')
            return self.json_response({'record': record, 'status': 'ready'}, 201)
        except ValueError as error:
            return self.json_response({'error': str(error)}, 400)
        except (OSError, ImportError, sqlite3.Error):
            return self.json_response({'error': 'Could not save the upload. Check storage and SVG rendering dependencies.'}, 503)

    def export_feedback_db(self, bundle=False):
        handle, name = tempfile.mkstemp(prefix='.feedback-export-', suffix='.zip' if bundle else '.sqlite3', dir=self.database.parent)
        os.close(handle)
        target = Path(name)
        try:
            exported_at = utc_now()
            if bundle:
                # Artwork saves hold this lock, so the database and folders match.
                with DISCARD_LOCK:
                    export_review_bundle(self.database, target)
            else:
                export_feedback_snapshot(self.database, target)
            size = target.stat().st_size
            self.send_response(200)
            self.send_header('Content-Type', 'application/zip' if bundle else 'application/vnd.sqlite3')
            self.send_header('Content-Disposition', 'attachment; filename="review-data.zip"' if bundle else 'attachment; filename="feedback.sqlite3"')
            self.send_header('Content-Length', str(size))
            self.send_header('X-Feedback-Exported-At', exported_at)
            self.end_headers()
            if self.command != 'HEAD':
                with target.open('rb') as stream:
                    while chunk := stream.read(1024 * 1024):
                        self.wfile.write(chunk)
        except (OSError, sqlite3.Error):
            return self.json_response({'error': 'Could not export the feedback database. Please retry.'}, 503)
        finally:
            target.unlink(missing_ok=True)

    def sync_feedback(self, data, user):
        """Replace this machine's feedback database with production's copy."""
        try:
            origin = sync_origin(data.get('source'))
        except ValueError as error:
            return self.json_response({'error': str(error)}, 400)
        if urlsplit(origin).netloc == self.headers.get('Host'):
            return self.json_response({'error': 'That URL is this server. Enter the production URL to sync from.'}, 400)
        work = Path(tempfile.mkdtemp(prefix='.feedback-sync-', dir=self.database.parent))
        snapshot, stores, warning = work / 'feedback.sqlite3', [], None
        try:
            try:
                try:
                    exported_at = download_snapshot(origin, work / 'bundle.zip', '/api/review-data/export')
                    stores = extract_review_bundle(work / 'bundle.zip', work / 'bundle')
                    (work / 'bundle' / 'feedback.sqlite3').rename(snapshot)
                    (work / 'bundle.zip').unlink()
                except urllib.error.HTTPError as error:
                    if error.code != 404:
                        raise
                    # Production predates artwork sync: take the database alone and say so.
                    exported_at = download_snapshot(origin, snapshot)
                    warning = ('Production has not been updated, so uploaded and edited artwork was not synced. '
                               'Icons with that artwork may show different statuses. Update deploy.py on production and sync again.')
            except urllib.error.HTTPError as error:
                return self.json_response({'error': f'Production refused the export (HTTP {error.code}). Is it running the latest deploy.py?'}, 502)
            except (urllib.error.URLError, TimeoutError, OSError) as error:
                return self.json_response({'error': f'Could not reach production: {getattr(error, "reason", error)}'}, 502)
            except ValueError as error:
                return self.json_response({'error': str(error)}, 502)
            try:
                result = replace_feedback_database(self.database, snapshot, user, origin, exported_at,
                                                   work / 'bundle', stores)
            except ValueError as error:
                return self.json_response({'error': str(error)}, 502)
            if warning:
                result['warning'] = warning
            return self.json_response(result)
        except (OSError, sqlite3.Error):
            return self.json_response({'error': 'Could not replace the local feedback database. It was left unchanged or backed up; retry.'}, 503)
        finally:
            shutil.rmtree(work, ignore_errors=True)

    def upload_reference(self, data, user):
        encoded = data.get('data')
        try:
            if not isinstance(encoded, str):
                raise ValueError('Choose an SVG or PNG file.')
            try:
                content = base64.b64decode(encoded, validate=True)
            except (binascii.Error, ValueError):
                raise ValueError('Could not read the uploaded file.')
            meta = self.server.references.save(data.get('name'), content)
            with closing(sqlite3.connect(self.database, timeout=10)) as connection, connection:
                record_activity(connection, user, 'reference_upload', image=meta['id'], name=meta['name'])
            return self.json_response(meta, 201)
        except ValueError as error:
            return self.json_response({'error': str(error)}, 400)
        except (OSError, sqlite3.Error):
            return self.json_response({'error': 'Could not store the reference image. Please retry.'}, 503)

    def save_artwork(self, data, user):
        with DISCARD_LOCK:
            try:
                icon = self.catalog_icon(data.get('icon'))
                if not icon:
                    return self.json_response({'error': 'Icon not found.'}, 404)
                if data.get('action') == 'upload':
                    self.server.artwork.save(icon, data, user, self.stroke_edits)
                    return self.json_response(self.artwork_response(icon))
                with closing(sqlite3.connect(self.database, timeout=10)) as connection, connection:
                    connection.execute('BEGIN IMMEDIATE')
                    if self.is_rejected(connection, icon['key'], icon['svg_sha256']):
                        return self.json_response({'error': 'Restore this rejected icon before picking and approving its artwork.'}, 409)
                    self.server.artwork.save(icon, data, user, self.stroke_edits)
                    result = self.artwork_response(icon)
                    record = result['record']
                    now = utc_now()
                    connection.execute(
                        '''INSERT INTO reviews(icon, svg_sha256, status, updated_at, updated_by) VALUES (?, ?, 'approve', ?, ?)
                           ON CONFLICT(icon, svg_sha256) DO UPDATE SET
                           status=excluded.status, updated_at=excluded.updated_at, updated_by=excluded.updated_by''',
                        (icon['key'], record['svg_sha256'], now, user))
                    record_activity(connection, user, 'review', icon['key'], status='approve',
                                    svg_sha256=record['svg_sha256'], artwork_source=result['source_mode'])
                    record.update(review_status='approve', review_updated_by=user, review_updated_at=now)
                return self.json_response(result)
            except EditConflict as error:
                return self.json_response({'error': str(error)}, 409)
            except (ValueError, TypeError, KeyError) as error:
                return self.json_response({'error': str(error)}, 400)
            except sqlite3.Error:
                return self.json_response({'error': 'Could not save approval. Reload the source choices and try again.'}, 503)
            except (OSError, ImportError):
                return self.json_response({'error': 'Could not store artwork. Check the persistent storage and SVG rendering dependencies.'}, 503)

    def save_stroke_edits(self, data, user, validate_only=False):
        if not isinstance(data.get('icon'), str):
            return self.json_response({'error': 'An icon key is required.'}, 400)
        with DISCARD_LOCK:
            icon = self.catalog(include_failed=True).get(data['icon'])
            if not icon:
                return self.json_response({'error': 'Icon not found.'}, 404)
            try:
                result = self.stroke_edits.validate(baseline(icon), data) if validate_only else self.stroke_edits.save(baseline(icon), data, user)
                return self.json_response(result)
            except EditConflict as error:
                return self.json_response({'error': str(error)}, 409)
            except ValueError as error:
                return self.json_response({'error': str(error)}, 400)
            except ImportError:
                return self.json_response({'error': 'Validation is unavailable on this server. Install the shared icon model, validation package, schemas, contracts, and QA dependencies.'}, 503)
            except (KeyError, TypeError) as error:
                return self.json_response({'error': 'The catalog is missing geometry metadata required for validation: '+str(error)}, 400)
            except OSError:
                return self.json_response({'error': 'Could not write edits to server storage. Your draft has not been saved.'}, 503)

    def discard_icon(self, data, user):
        """Permanently remove rejected icons: Python models, published files and their review rows.

        Accepts {icon, svg_sha256} or {icons: [{icon, svg_sha256}, ...]}. A batch discards every
        icon that passes its checks and lists the rest under `failed`.
        """
        batch = 'icons' in data
        requests = data.get('icons') if batch else [data]
        if not isinstance(requests, list) or not 1 <= len(requests) <= MAX_DISCARD_BATCH or \
                not all(isinstance(item, dict) and isinstance(item.get('icon'), str) for item in requests):
            return self.json_response({'error': f'Choose between 1 and {MAX_DISCARD_BATCH} icons to discard.'}, 400)
        with DISCARD_LOCK:
            try:
                catalog = self.catalog(include_failed=True)
                with closing(sqlite3.connect(self.database, timeout=10)) as connection, connection:
                    icons, failed = [], []
                    for item in requests:
                        key, icon = item['icon'], catalog.get(item['icon'])
                        error = ('Unknown icon' if icon is None else
                                 'Icon changed. Refresh before discarding.' if item.get('svg_sha256') != icon.get('svg_sha256') else
                                 'Only rejected icons can be discarded. Reject it first.'
                                 if not icon.get('build_failed') and not self.is_rejected(connection, key, icon.get('svg_sha256')) else None)
                        if error:
                            failed.append({'icon': key, 'name': icon['name'] if icon else key, 'error': error})
                        elif all(existing['key'] != key for existing in icons):
                            icons.append(icon)
                    if not batch and failed:
                        return self.json_response({'error': failed[0]['error']}, 404 if failed[0]['error'] == 'Unknown icon' else 409)
                    source_root = getattr(self.server, 'source_root', PACKAGE_ROOT.parent)
                    result = discard_many(icons, source_root=source_root, dist=self.root,
                                          archive=self.database.parent / 'discarded-icons',
                                          connection=connection, user=user)
                    for row in result['discarded']:
                        record_activity(connection, user, 'discard', row['icon'], svg_sha256=catalog[row['icon']].get('svg_sha256'),
                                        source=row['source'], archive=row['archive'])
                    result['failed'] = failed + result['failed']
                if not batch and result['failed']:
                    return self.json_response({'error': result['failed'][0]['error']}, 409)
                return self.json_response(result)
            except (OSError, SyntaxError, sqlite3.Error):
                return self.json_response({'error': 'Could not discard. Refresh to see what changed, then retry.'}, 503)

    def _canonical_uuids(self, uuids):
        """Folded alias uuids act on their canonical primitive; unknown ids pass through to validation."""
        canonical = canonical_map(self.primitives_catalog()['rows'])
        resolved = [canonical.get(uid.strip().lower(), uid) if isinstance(uid, str) else uid for uid in uuids]
        return resolved, set(canonical)

    def save_primitive_brief(self, data, user):
        try:
            (uid,), known = self._canonical_uuids([data.get('uuid')])
            with closing(sqlite3.connect(self.database, timeout=10)) as connection, connection:
                result = save_primitive_brief(connection, uid, data.get('family'), data.get('brief'),
                                              known=known, user=user, record=record_activity, authority='user')
            return self.json_response(result)
        except ValueError as error:
            return self.json_response({'error': str(error)}, 400)
        except (OSError, sqlite3.Error):
            return self.json_response({'error': 'Could not save the brief. Please retry.'}, 503)

    def save_primitive_status(self, data, user):
        try:
            uuids = data.get('uuids')
            if isinstance(uuids, list):
                uuids, known = self._canonical_uuids(uuids)
            else:
                known = {row['uuid'] for row in self.primitives_catalog()['rows']}
            with closing(sqlite3.connect(self.database, timeout=10)) as connection, connection:
                result = set_status(connection, uuids, data.get('status'), data.get('reason'),
                                    data.get('note', ''), user=user, record=record_activity, known=known, authority='user',
                                    **{key: data[key] for key in ('combination_brief', 'main_brief', 'sub_brief', 'sub_position') if key in data})
                statuses = load_status(connection)
            result['decisions'] = {uid.strip().lower(): statuses.get(uid.strip().lower()) for uid in uuids}
            return self.json_response(result)
        except ValueError as error:
            return self.json_response({'error': str(error)}, 400)
        except (OSError, sqlite3.Error):
            return self.json_response({'error': 'Could not save primitive status. Please retry.'}, 503)

    def save_icon_type(self, data, user):
        key, icon_type = data.get('icon'), data.get('icon_type')
        if not isinstance(key, str) or not isinstance(icon_type, str) or len(icon_type) > 200:
            return self.json_response({'error': 'Enter an icon type of up to 200 characters.'}, 400)
        icon_type = icon_type.strip()
        try:
            if key not in self.catalog():
                return self.json_response({'error': 'Unknown icon'}, 404)
            with closing(sqlite3.connect(self.database, timeout=10)) as connection, connection:
                now = utc_now()
                connection.execute('INSERT INTO icon_types(icon,icon_type,updated_at,updated_by) VALUES (?,?,?,?) '
                    'ON CONFLICT(icon) DO UPDATE SET icon_type=excluded.icon_type,updated_at=excluded.updated_at,updated_by=excluded.updated_by',
                    (key, icon_type, now, user))
                record_activity(connection, user, 'icon_type', key, icon_type=icon_type)
            return self.json_response({'icon_type': icon_type, 'updated_by': user, 'updated_at': now})
        except (OSError, ValueError, sqlite3.Error):
            return self.json_response({'error': 'Could not save icon type. Please retry.'}, 503)

    def save_icon_flag(self, data, user):
        key, flag = data.get('icon'), data.get('flag')
        if not isinstance(key, str) or flag not in ('', 'container_combination', 'combination', 'text', 'number', 'other', 'exception'):
            return self.json_response({'error': 'Choose a valid icon flag.'}, 400)
        try:
            if key not in self.catalog():
                return self.json_response({'error': 'Unknown icon'}, 404)
            with closing(sqlite3.connect(self.database, timeout=10)) as connection, connection:
                now = utc_now()
                if flag:
                    connection.execute('INSERT INTO icon_flags(icon,flag,updated_at,updated_by) VALUES (?,?,?,?) '
                        'ON CONFLICT(icon) DO UPDATE SET flag=excluded.flag,updated_at=excluded.updated_at,updated_by=excluded.updated_by',
                        (key, flag, now, user))
                else:
                    connection.execute('DELETE FROM icon_flags WHERE icon=?', (key,))
                record_activity(connection, user, 'flag' if flag else 'unflag', key, flag=flag)
            return self.json_response({'flag': flag, 'updated_by': user if flag else None, 'updated_at': now if flag else None})
        except (OSError, ValueError, sqlite3.Error):
            return self.json_response({'error': 'Could not save icon flag. Please retry.'}, 503)

    def delete_feedback(self, data, user):
        feedback_id, previous = data.get('id'), data.get('previous_feedback')
        edited_at = data.get('previous_edited_at')
        if (type(feedback_id) is not int or feedback_id <= 0 or not isinstance(previous, str)
                or (edited_at is not None and not isinstance(edited_at, str))):
            return self.json_response({'error': 'Choose a feedback entry to remove.'}, 400)
        try:
            with closing(sqlite3.connect(self.database, timeout=10)) as connection, connection:
                connection.execute('BEGIN IMMEDIATE')
                row = connection.execute('SELECT icon,feedback,edited_at FROM feedback WHERE id=?', (feedback_id,)).fetchone()
                if not row:
                    return self.json_response({'error': 'Feedback not found. Refresh the page.'}, 404)
                if (row[1], row[2]) != (previous, edited_at):
                    return self.json_response({'error': 'Feedback changed. Refresh before removing it.'}, 409)
                connection.execute('DELETE FROM feedback WHERE id=?', (feedback_id,))
                record_activity(connection, user, 'feedback_delete', row[0], feedback_id=feedback_id)
            return self.json_response({'deleted': True, 'id': feedback_id, 'icon': row[0]})
        except sqlite3.Error:
            return self.json_response({'error': 'Could not remove feedback. Please retry.'}, 503)

    def edit_feedback(self, data, user):
        feedback_id, feedback, previous = data.get('id'), data.get('feedback'), data.get('previous_feedback')
        if (type(feedback_id) is not int or not isinstance(feedback, str)
                or not 1 <= len(feedback.strip()) <= 10000 or not isinstance(previous, str)):
            return self.json_response({'error': 'Enter feedback between 1 and 10,000 characters.'}, 400)
        try:
            with closing(sqlite3.connect(self.database, timeout=10)) as connection, connection:
                # Compare and update together to avoid silently overwriting another editor.
                now = utc_now()
                updated = connection.execute(
                    'UPDATE feedback SET feedback=?, edited_by=?, edited_at=? WHERE id=? AND feedback=?',
                    (feedback.strip(), user, now, feedback_id, previous))
                if not updated.rowcount:
                    exists = connection.execute('SELECT 1 FROM feedback WHERE id=?', (feedback_id,)).fetchone()
                    return self.json_response({'error': 'Feedback changed. Refresh before editing again.' if exists else 'Feedback not found.'}, 409 if exists else 404)
                icon = connection.execute('SELECT icon FROM feedback WHERE id=?', (feedback_id,)).fetchone()[0]
                record_activity(connection, user, 'feedback_edit', icon, feedback_id=feedback_id, previous_feedback=previous)
            return self.json_response({'saved': True, 'feedback': feedback.strip(), 'edited_by': user, 'edited_at': now})
        except sqlite3.Error:
            return self.json_response({'error': 'Could not save feedback. Please retry.'}, 503)

    def brief_action(self, route, data, user):
        try:
            catalog = self.catalog()
            with closing(sqlite3.connect(self.database, timeout=10)) as connection, connection:
                if route == '/api/pending-briefs/complete':
                    brief_id = data.get('brief_id')
                    key = data.get('generated_icon')
                    if not isinstance(brief_id, int) or not isinstance(key, str):
                        raise ValueError('Choose a generated component icon.')
                    brief = connection.execute('SELECT b.family,s.icon FROM pending_briefs b JOIN split_requests s ON s.id=b.split_id WHERE b.id=? AND s.active=1', (brief_id,)).fetchone()
                    icon = catalog.get(key)
                    if not brief or not icon or icon['family'] != brief[0] or key == brief[1]:
                        raise ValueError('Choose a built standalone icon in this component family, not the rejected combination.')
                    if self.is_rejected(connection, key, icon['svg_sha256']):
                        raise ValueError('A rejected icon cannot fulfill a component brief.')
                    connection.execute("UPDATE pending_briefs SET status='generated',generated_icon=?,completed_by=?,completed_at=? WHERE id=?",
                                       (key, user, utc_now(), brief_id))
                    record_activity(connection, user, 'brief_complete', brief[1], brief_id=brief_id, generated_icon=key)
                    return self.json_response({'saved': True})
                key = data.get('icon')
                if not isinstance(key, str) or key not in catalog:
                    return self.json_response({'error': 'Unknown icon'}, 404)
                icon = catalog[key]
                if data.get('svg_sha256') != icon['svg_sha256']:
                    return self.json_response({'error': 'Icon changed. Refresh before rejecting or restoring.'}, 409)
                now = utc_now()
                if route == '/api/reject-combination/restore':
                    connection.execute('UPDATE split_requests SET active=0, restored_by=?, restored_at=? WHERE icon=? AND svg_sha256=? AND active=1',
                                       (user, now, key, icon['svg_sha256']))
                    connection.execute("UPDATE reviews SET status='ready', updated_by=?, updated_at=? WHERE icon=? AND status='rejected'", (user, now, key))
                    # Explicit restore returns the icon to review, never silently approves it.
                    connection.execute("INSERT INTO reviews(icon,svg_sha256,status,updated_at,updated_by) VALUES (?,?,'ready',?,?) ON CONFLICT(icon,svg_sha256) DO UPDATE SET status='ready',updated_at=excluded.updated_at,updated_by=excluded.updated_by", (key,icon['svg_sha256'],now,user))
                    clear_ready_feedback(connection, key, user)
                    record_activity(connection, user, 'restore', key, svg_sha256=icon['svg_sha256'])
                    return self.json_response({'saved': True, 'status': 'ready'})
                validate_split(data)
                sources = icon.get('original_sources', [])
                reference = sources[0]['source_path'] if sources else ''
                already = connection.execute('SELECT 1 FROM split_requests WHERE icon=? AND svg_sha256=? AND active=1',
                                             (key, icon['svg_sha256'])).fetchone()
                split_id = enqueue_split(connection,key,icon['svg_sha256'],reference,data,user)
                if not already:  # a repeated click changes nothing, so it records nothing
                    record_activity(connection, user, 'reject_combination', key, split_id=split_id,
                                    combination_type=data.get('combination_type'))
                return self.json_response({'saved': True, 'status': 'rejected', 'split_id': split_id}, 201)
        except (ValueError, TypeError) as error:
            return self.json_response({'error': str(error)}, 400)
        except (OSError, sqlite3.Error):
            return self.json_response({'error': 'Could not update pending briefs.'}, 503)


def create_server(dist: Path, database: Path, host='127.0.0.1', port=8000, primitives=None, sync_source=DEFAULT_SYNC_SOURCE, *, production=False, live_release_root=None):
    dist, database = dist.resolve(), database.resolve()
    if live_release_root is not None:
        dist = live_directory(dist, live_release_root)
    if not (dist / 'gallery/index.html').is_file() or not (dist / 'gallery/icons.json').is_file():
        raise ValueError('Gallery is missing. Run icon_set/scripts/build.py first.')
    from icon_set.scripts.workspace import PUBLISHED_DIST
    if not production and (dist / 'release.json').is_file() and dist != PUBLISHED_DIST.resolve():
        raise ValueError('An exported release must be served with --production, not the development server.')
    if database.is_relative_to(dist):
        raise ValueError('Keep the feedback database outside the publicly served dist folder.')
    if production:
        if database.is_relative_to(PACKAGE_ROOT.parent):
            raise ValueError('Production database must be outside the source checkout.')
        if dist.is_relative_to(PACKAGE_ROOT.parent) and dist != PUBLISHED_DIST.resolve():
            raise ValueError('Production dist must be published/ or outside the source checkout.')
        if dist == PUBLISHED_DIST.resolve() and not (dist / 'release.json').is_file():
            raise ValueError('Run python3 -m icon_set publish before serving published/.')
        if dist.is_relative_to(database.parent):
            raise ValueError('Keep production releases outside the persistent state directory.')
    if live_release_root is not None:
        if not production:
            raise ValueError('Live catalog updates require production mode.')
        from icon_set.scripts.automatic_deploy import validate_paths
        live_release_root, _ = validate_paths(PACKAGE_ROOT.parent, live_release_root, database)
    init_database(database)
    if not production:
        with closing(sqlite3.connect(database, timeout=10)) as connection, connection:
            import_snapshot(connection)
    server = GalleryServer((host, port), partial(GalleryHandler, directory=lambda: live_directory(dist, live_release_root), database=database))
    server.production = production
    server.live_release_root = live_release_root
    server.references = ReferenceStore(database.parent / 'reference-images')
    server.artwork = ArtworkStore(database.parent / 'icon-artwork')
    server.stroke_edits = StrokeEditStore(database.parent / 'stroke-edits', dist / 'gallery/laboratory.json')
    server.evidence = EvidenceStore(dist, database.parent / 'qa-evidence')
    server.primitives_root = primitives_root(primitives)
    server.sync_source = sync_source
    if not production:
        server.generation = GenerationManager(PACKAGE_ROOT.parent, dist, database.parent / 'generation-jobs', server.references)
        server.ai_feedback = FeedbackReviewManager(server.generation, database.parent / 'ai-feedback-jobs')
    return server


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--live-release-root', type=Path, help='Follow completed gallery updates without restarting the server')
    parser.add_argument('--production', action='store_true', help='Review/upload server; serves published/ or an external release with an external database')
    parser.add_argument('--dist', type=Path, default=DEFAULT_DIST)
    parser.add_argument('--database', type=Path, default=DEFAULT_DB)
    parser.add_argument('--host', default='127.0.0.1')
    parser.add_argument('--port', type=int, default=8000)
    parser.add_argument('--open', action='store_true', help='Open the local browser')
    parser.add_argument('--primitives', type=Path, help='Original primitives folder for the Primitives page '
                                                        '(default $PICTOGRAPHIC_PRIMITIVES or claude_skills/pictographic-primitives)')
    parser.add_argument('--sync-source', default=DEFAULT_SYNC_SOURCE,
                        help='Production gallery to pull reviewing data from (default $PICTOGRAPHIC_SYNC_SOURCE)')
    args = parser.parse_args(argv)
    try:
        server = create_server(args.dist, args.database, args.host, args.port, args.primitives, args.sync_source, production=args.production, live_release_root=args.live_release_root)
    except (OSError, ValueError, sqlite3.Error) as error:
        parser.exit(1, f'error: {error}\n')
    port = server.server_address[1]
    browser_host = '127.0.0.1' if args.host == '0.0.0.0' else args.host
    url = f'http://{browser_host}:{port}/'
    print(f'Gallery: {url}\nListening on {args.host}:{port}\nFeedback: {args.database.resolve()}', flush=True)
    if args.open:
        webbrowser.open(url)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\nServer stopped.')
    finally:
        server.server_close()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
