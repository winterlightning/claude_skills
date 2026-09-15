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
import time
from http.cookies import SimpleCookie, CookieError
from pathlib import Path
import sqlite3
import threading
from urllib.parse import parse_qs, unquote, urlsplit
import webbrowser

if __package__:
    from .generation import GenerationManager
    from .brief_queue import init_brief_queue, enqueue_split, list_briefs, validate_split, brief_archive
    from .reference_images import ReferenceStore, LIMITS as REFERENCE_LIMITS
    from .discard_icon import discard_many
    from .qa_evidence import EvidenceStore
    from .primitive_status import init_primitive_status, set_status, load_status, merge, summarize, filter_rows
    from .progression import import_snapshot
    from .primitives_catalog import primitives_root
else:
    from generation import GenerationManager
    from brief_queue import init_brief_queue, enqueue_split, list_briefs, validate_split, brief_archive
    from reference_images import ReferenceStore, LIMITS as REFERENCE_LIMITS
    from discard_icon import discard_many
    from qa_evidence import EvidenceStore
    from primitive_status import init_primitive_status, set_status, load_status, merge, summarize, filter_rows
    from progression import import_snapshot
    from primitives_catalog import primitives_root

PACKAGE_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DIST = PACKAGE_ROOT / 'dist'
DEFAULT_DB = PACKAGE_ROOT / 'data' / 'feedback.sqlite3'
MAX_BODY = 65536
# Base64 inflates by 4/3; leave room for the JSON wrapper around the largest image.
MAX_REFERENCE_BODY = max(REFERENCE_LIMITS.values()) * 4 // 3 + 4096
ADMIN_USERS = {"jakes": "1", "hina": "1", "ray": "1", "phuong": "1"}
SESSION_TTL = 12 * 60 * 60
# Discards rewrite icons.json and manifests; one at a time.
DISCARD_LOCK = threading.Lock()
MAX_DISCARD_BATCH = 500


def init_database(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with closing(sqlite3.connect(path)) as connection, connection:
        connection.execute("CREATE TABLE IF NOT EXISTS admin_sessions (token TEXT PRIMARY KEY, username TEXT NOT NULL, expires REAL NOT NULL)")
        init_brief_queue(connection)
        connection.execute("""CREATE TABLE IF NOT EXISTS icon_flags (
            icon TEXT PRIMARY KEY, flag TEXT NOT NULL CHECK(flag IN ('container_combination','combination','other','exception')),
            updated_at TEXT NOT NULL)""")
        # SQLite cannot alter a CHECK constraint; preserve existing flags while
        # upgrading databases created before the manual-review exception flag.
        schema = connection.execute("SELECT sql FROM sqlite_master WHERE name='icon_flags'").fetchone()[0]
        if "'exception'" not in schema:
            connection.execute('ALTER TABLE icon_flags RENAME TO icon_flags_legacy')
            connection.execute("""CREATE TABLE icon_flags (
                icon TEXT PRIMARY KEY, flag TEXT NOT NULL CHECK(flag IN
                ('container_combination','combination','other','exception')),
                updated_at TEXT NOT NULL)""")
            connection.execute('INSERT INTO icon_flags SELECT * FROM icon_flags_legacy')
            connection.execute('DROP TABLE icon_flags_legacy')
        connection.execute('''CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY, icon TEXT NOT NULL, feedback TEXT NOT NULL,
            svg_sha256 TEXT NOT NULL, created_at TEXT NOT NULL)''')
        connection.execute('CREATE INDEX IF NOT EXISTS feedback_icon ON feedback(icon, id)')
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


def utc_now():
    return datetime.now(timezone.utc).isoformat()


def record_activity(connection, username, action, icon=None, **details):
    """Append one action to the log; call inside the transaction that makes the change."""
    connection.execute('INSERT INTO activity_log(username, action, icon, details, created_at) VALUES (?, ?, ?, ?, ?)',
                       (username, action, icon, json.dumps(details, ensure_ascii=False), utc_now()))


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
    return {'status': row[0], 'updated_by': row[1], 'updated_at': row[2]} if row else \
        {'status': 'ready', 'updated_by': None, 'updated_at': None}


def feedback_row(row):
    data = dict(row)
    try:
        data['reference_images'] = json.loads(data.get('reference_images') or '[]')
    except ValueError:
        data['reference_images'] = []
    return data


class GalleryServer(ThreadingHTTPServer):
    # The default backlog of 5 drops connections when a page requests hundreds of icons at once.
    request_queue_size = 256


class GalleryHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, directory, database, **kwargs):
        self.root = Path(directory).resolve()
        self.database = database
        super().__init__(*args, directory=str(self.root), **kwargs)

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

    def catalog(self, *, include_failed=False):
        data = json.loads((self.root / 'gallery/icons.json').read_text(encoding='utf-8'))
        rows = data['icons'] + (data.get('failed_icons', []) if include_failed else [])
        return {item['key']: item for item in rows}

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

    def do_GET(self):
        parsed = urlsplit(self.path)
        if parsed.path == '/api/auth/session':
            return self.json_response({'user': self.current_user()})
        if parsed.path.startswith('/api/generation'):
            if not self.current_user():
                return self.json_response({'error': 'Log in as an admin to generate icons.'}, 401)
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
                    return self.json_response(self.server.evidence.evidence(key))
                content = self.server.evidence.image(key, query.get('kind', [''])[0])
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
        if parsed.path == '/api/feedback-feed':
            try:
                with closing(sqlite3.connect(self.database, timeout=10)) as connection:
                    connection.row_factory = sqlite3.Row
                    rows = connection.execute(
                        'SELECT id, icon, feedback, svg_sha256, created_at, reference_images, author, edited_by, edited_at FROM feedback ORDER BY id DESC'
                    ).fetchall()
                return self.json_response([feedback_row(row) for row in rows])
            except sqlite3.Error:
                return self.json_response({'error': 'Feedback is temporarily unavailable'}, 503)
        if parsed.path == '/api/reviews':
            try:
                catalog = self.catalog(include_failed=True)
                with closing(sqlite3.connect(self.database, timeout=10)) as connection:
                    rows = connection.execute('SELECT icon, svg_sha256, status, updated_by FROM reviews').fetchall()
                    # Preserve an explicit restore until the next review or feedback action.
                    latest_actions = connection.execute("SELECT icon,action,details FROM activity_log WHERE id IN (SELECT MAX(id) FROM activity_log WHERE action IN ('restore','review','feedback') GROUP BY icon)").fetchall()
                    restored = {key: json.loads(details).get('svg_sha256') for key, action, details in latest_actions if action == 'restore'}
                statuses = {key: 'ready' for key in catalog}
                for key, sha, status, actor in rows:
                    if key in catalog and catalog[key]['svg_sha256'] == sha:
                        statuses[key] = status
                for key, sha, status, actor in rows:
                    if key in catalog and status == 'rejected':
                        statuses[key] = 'rejected'
                # A published child variant means the pending original has been regenerated.
                for icon in catalog.values():
                    parent = icon.get('variant_of')
                    if parent:
                        key = icon['family'] + '/' + parent
                        if statuses.get(key) == 'pending' and restored.get(key) != catalog[key]['svg_sha256']:
                            statuses[key] = 're-generated'
                with closing(sqlite3.connect(self.database, timeout=10)) as connection:
                    rejected = connection.execute('SELECT icon,svg_sha256 FROM split_requests WHERE active=1').fetchall()
                for key, sha in rejected:
                    if key in catalog and catalog[key]['svg_sha256'] == sha:
                        statuses[key] = 'rejected'
                if parse_qs(parsed.query).get('include_approvers') == ['1']:
                    approved_by = {key: actor for key, sha, status, actor in rows
                                   if key in catalog and catalog[key]['svg_sha256'] == sha
                                   and status == 'approve' and statuses[key] == 'approve' and actor}
                    return self.json_response({'statuses': statuses, 'approved_by': approved_by})
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
                        'SELECT id, feedback, svg_sha256, created_at, reference_images, author, edited_by, edited_at FROM feedback WHERE icon=? ORDER BY id DESC LIMIT 100',
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
        if route not in ('/api/auth/login', '/api/auth/logout', '/api/generation', '/api/generation/accept', '/api/generation/discard', '/api/icon-flag', '/api/feedback/edit', '/api/feedback', '/api/reviews', '/api/reject-combination', '/api/pending-briefs/complete', '/api/reject-combination/restore', '/api/reference-images', '/api/icons/discard', '/api/primitives/status'):
            return self.json_response({'error': 'Not found'}, 404)
        # Every change is attributed to a logged-in user; only logging in is anonymous.
        user = None
        if route not in ('/api/auth/login', '/api/auth/logout'):
            user = self.current_user()
            if not user:
                return self.json_response({'error': 'Log in to make changes.'}, 401)
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
        limit = {'/api/generation': 131072, '/api/reference-images': MAX_REFERENCE_BODY}.get(route, MAX_BODY)
        if self.headers.get('Transfer-Encoding') or not 0 < size <= limit:
            return self.json_response({'error': 'Invalid request size' if route != '/api/reference-images' else 'Reference image is too large.'}, 413)
        try:
            data = json.loads(self.rfile.read(size))
            if not isinstance(data, dict):
                raise ValueError()
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
            if route == '/api/primitives/status':
                return self.save_primitive_status(data, user)
            if route == '/api/icon-flag':
                return self.save_icon_flag(data, user)
            if route == '/api/feedback/edit':
                return self.edit_feedback(data, user)
            key, feedback = data.get('icon'), data.get('feedback')
            status = data.get('status')
            if not isinstance(key, str):
                raise ValueError()
            if route == '/api/feedback':
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
                if route == '/api/reviews' and connection.execute(
                    'SELECT 1 FROM split_requests WHERE icon=? AND svg_sha256=? AND active=1',
                    (key, sha),
                ).fetchone():
                    return self.json_response({'error': 'This combined icon is rejected. Restore it before changing its review status.'}, 409)
                if self.is_rejected(connection, key, sha):
                    if route == '/api/feedback':
                        status = 'rejected'
                    elif status != 'rejected':
                        return self.json_response({'error': 'Restore this rejected icon before changing its review status.'}, 409)
                now = datetime.now(timezone.utc).isoformat()
                if route == '/api/feedback':
                    feedback_id = connection.execute(
                        'INSERT INTO feedback(icon, feedback, svg_sha256, created_at, reference_images, author) VALUES (?, ?, ?, ?, ?, ?)',
                        (key, feedback.strip(), sha, now, json.dumps(references), user),
                    ).lastrowid
                    record_activity(connection, user, 'feedback', key, feedback_id=feedback_id, status=status,
                                    reference_images=[ref['id'] for ref in references])
                else:
                    record_activity(connection, user, 'review', key, status=status, svg_sha256=sha)
                connection.execute(
                    '''INSERT INTO reviews(icon, svg_sha256, status, updated_at, updated_by) VALUES (?, ?, ?, ?, ?)
                       ON CONFLICT(icon, svg_sha256) DO UPDATE SET
                       status=excluded.status, updated_at=excluded.updated_at, updated_by=excluded.updated_by''',
                    (key, sha, status, now, user),
                )
            return self.json_response({'saved': True, 'status': status, 'updated_by': user}, 201)
        except sqlite3.Error:
            return self.json_response({'error': 'Could not save feedback'}, 503)

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

    def save_primitive_status(self, data, user):
        try:
            known = {row['uuid'] for row in self.primitives_catalog()['rows']}
            with closing(sqlite3.connect(self.database, timeout=10)) as connection, connection:
                result = set_status(connection, data.get('uuids'), data.get('status'), data.get('reason'),
                                    data.get('note', ''), user=user, record=record_activity, known=known,
                                    **{key: data[key] for key in ('combination_brief', 'main_brief', 'sub_brief', 'sub_position') if key in data})
                statuses = load_status(connection)
            result['decisions'] = {uid.strip().lower(): statuses.get(uid.strip().lower()) for uid in data['uuids']}
            return self.json_response(result)
        except ValueError as error:
            return self.json_response({'error': str(error)}, 400)
        except (OSError, sqlite3.Error):
            return self.json_response({'error': 'Could not save primitive status. Please retry.'}, 503)

    def save_icon_flag(self, data, user):
        key, flag = data.get('icon'), data.get('flag')
        if not isinstance(key, str) or flag not in ('', 'container_combination', 'combination', 'other', 'exception'):
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
                    connection.execute("UPDATE reviews SET status='pending', updated_by=?, updated_at=? WHERE icon=? AND status='rejected'", (user, now, key))
                    # Explicit restore returns the icon to review, never silently approves it.
                    connection.execute("INSERT INTO reviews(icon,svg_sha256,status,updated_at,updated_by) VALUES (?,?,'pending',?,?) ON CONFLICT(icon,svg_sha256) DO UPDATE SET status='pending',updated_at=excluded.updated_at,updated_by=excluded.updated_by", (key,icon['svg_sha256'],now,user))
                    record_activity(connection, user, 'restore', key, svg_sha256=icon['svg_sha256'])
                    return self.json_response({'saved': True, 'status': 'pending'})
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


def create_server(dist: Path, database: Path, host='127.0.0.1', port=8000, primitives=None):
    dist, database = dist.resolve(), database.resolve()
    if not (dist / 'gallery/index.html').is_file() or not (dist / 'gallery/icons.json').is_file():
        raise ValueError('Gallery is missing. Run icon_set/scripts/build.py first.')
    if database.is_relative_to(dist):
        raise ValueError('Keep the feedback database outside the publicly served dist folder.')
    init_database(database)
    with closing(sqlite3.connect(database, timeout=10)) as connection, connection:
        import_snapshot(connection)
    server = GalleryServer((host, port), partial(GalleryHandler, directory=dist, database=database))
    server.references = ReferenceStore(database.parent / 'reference-images')
    server.evidence = EvidenceStore(dist, database.parent / 'qa-evidence')
    server.primitives_root = primitives_root(primitives)
    server.generation = GenerationManager(PACKAGE_ROOT.parent, dist, database.parent / 'generation-jobs', server.references)
    return server


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dist', type=Path, default=DEFAULT_DIST)
    parser.add_argument('--database', type=Path, default=DEFAULT_DB)
    parser.add_argument('--host', default='127.0.0.1')
    parser.add_argument('--port', type=int, default=8000)
    parser.add_argument('--open', action='store_true', help='Open the local browser')
    parser.add_argument('--primitives', type=Path, help='Original primitives folder for the Primitives page '
                                                        '(default $PICTOGRAPHIC_PRIMITIVES or claude_skills/pictographic-primitives)')
    args = parser.parse_args(argv)
    try:
        server = create_server(args.dist, args.database, args.host, args.port, args.primitives)
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
