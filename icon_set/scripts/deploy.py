#!/usr/bin/env python3
"""Serve the built icon gallery and persist feedback in SQLite.

python3 icon_set/scripts/deploy.py --host 0.0.0.0 --port 8000
Use --open for local browser preview. Put a TLS reverse proxy in front on a server.
"""
from __future__ import annotations

import argparse
from contextlib import closing
from datetime import datetime, timezone
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path
import sqlite3
from urllib.parse import parse_qs, unquote, urlsplit
import webbrowser

if __package__:
    from .generation import GenerationManager
    from .brief_queue import init_brief_queue, enqueue_split, list_briefs, validate_split, brief_archive
else:
    from generation import GenerationManager
    from brief_queue import init_brief_queue, enqueue_split, list_briefs, validate_split, brief_archive

PACKAGE_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DIST = PACKAGE_ROOT / 'dist'
DEFAULT_DB = PACKAGE_ROOT / 'data' / 'feedback.sqlite3'
MAX_BODY = 65536


def init_database(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with closing(sqlite3.connect(path)) as connection, connection:
        init_brief_queue(connection)
        connection.execute("""CREATE TABLE IF NOT EXISTS icon_flags (
            icon TEXT PRIMARY KEY, flag TEXT NOT NULL CHECK(flag IN ('container_combination','combination','other')),
            updated_at TEXT NOT NULL)""")
        connection.execute('''CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY, icon TEXT NOT NULL, feedback TEXT NOT NULL,
            svg_sha256 TEXT NOT NULL, created_at TEXT NOT NULL)''')
        connection.execute('CREATE INDEX IF NOT EXISTS feedback_icon ON feedback(icon, id)')
        connection.execute('''CREATE TABLE IF NOT EXISTS reviews (
            icon TEXT NOT NULL, svg_sha256 TEXT NOT NULL,
            status TEXT NOT NULL CHECK(status IN ('ready', 'pending', 'approve')),
            updated_at TEXT NOT NULL, PRIMARY KEY(icon, svg_sha256))''')
        # Existing feedback starts pending; never overwrite an explicit decision.
        connection.execute('''INSERT OR IGNORE INTO reviews(icon, svg_sha256, status, updated_at)
            SELECT icon, svg_sha256, 'pending', MAX(created_at)
            FROM feedback GROUP BY icon, svg_sha256''')


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
        self.send_header('Cache-Control', 'no-cache')
        super().end_headers()

    def json_response(self, data, status=200):
        content = json.dumps(data, ensure_ascii=False).encode('utf-8')
        self.send_response(status)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(content)))
        self.end_headers()
        if self.command != 'HEAD':
            self.wfile.write(content)

    def catalog(self):
        data = json.loads((self.root / 'gallery/icons.json').read_text(encoding='utf-8'))
        return {item['key']: item for item in data['icons']}

    def do_GET(self):
        parsed = urlsplit(self.path)
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
        if parsed.path == '/api/icon-flag':
            key = parse_qs(parsed.query).get('icon', [''])[0]
            try:
                if key not in self.catalog():
                    return self.json_response({'error': 'Unknown icon'}, 404)
                with closing(sqlite3.connect(self.database, timeout=10)) as connection:
                    row = connection.execute('SELECT flag FROM icon_flags WHERE icon=?', (key,)).fetchone()
                return self.json_response({'flag': row[0] if row else ''})
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
                        'SELECT id, icon, feedback, svg_sha256, created_at FROM feedback ORDER BY id DESC'
                    ).fetchall()
                return self.json_response([dict(row) for row in rows])
            except sqlite3.Error:
                return self.json_response({'error': 'Feedback is temporarily unavailable'}, 503)
        if parsed.path == '/api/reviews':
            try:
                catalog = self.catalog()
                with closing(sqlite3.connect(self.database, timeout=10)) as connection:
                    rows = connection.execute('SELECT icon, svg_sha256, status FROM reviews').fetchall()
                statuses = {key: 'ready' for key in catalog}
                for key, sha, status in rows:
                    if key in catalog and catalog[key]['svg_sha256'] == sha:
                        statuses[key] = status
                with closing(sqlite3.connect(self.database, timeout=10)) as connection:
                    rejected = connection.execute('SELECT icon,svg_sha256 FROM split_requests WHERE active=1').fetchall()
                for key, sha in rejected:
                    if key in catalog and catalog[key]['svg_sha256'] == sha:
                        statuses[key] = 'rejected'
                return self.json_response(statuses)
            except (OSError, ValueError, sqlite3.Error):
                return self.json_response({'error': 'Review statuses are temporarily unavailable'}, 503)
        if parsed.path == '/api/feedback':
            key = parse_qs(parsed.query).get('icon', [''])[0]
            try:
                if key not in self.catalog():
                    return self.json_response({'error': 'Unknown icon'}, 404)
                with closing(sqlite3.connect(self.database, timeout=10)) as connection, connection:
                    connection.row_factory = sqlite3.Row
                    rows = connection.execute(
                        'SELECT id, feedback, svg_sha256, created_at FROM feedback WHERE icon=? ORDER BY id DESC LIMIT 100',
                        (key,),
                    ).fetchall()
                return self.json_response([dict(row) for row in rows])
            except (OSError, ValueError, sqlite3.Error):
                return self.json_response({'error': 'Feedback is temporarily unavailable'}, 503)
        return super().do_GET()

    def send_head(self):
        path = unquote(urlsplit(self.path).path)
        if path == '/':
            self.send_response(302)
            self.send_header('Location', 'gallery/index.html')
            self.send_header('Content-Length', '0')
            self.end_headers()
            return None
        parts = Path(path.lstrip('/')).parts
        candidate = (self.root / path.lstrip('/')).resolve()
        # No directory listings, hidden build stages, traversal or symlink escapes.
        if (any(part.startswith('.') for part in parts) or
                not candidate.is_relative_to(self.root) or not candidate.is_file() or
                candidate.suffix.lower() not in {'.html', '.json', '.svg', '.png', '.css', '.js'}):
            self.send_error(404)
            return None
        return super().send_head()

    def do_POST(self):
        route = urlsplit(self.path).path
        if route not in ('/api/generation', '/api/generation/accept', '/api/generation/discard', '/api/icon-flag', '/api/feedback/edit', '/api/feedback', '/api/reviews', '/api/reject-combination', '/api/pending-briefs/complete', '/api/reject-combination/restore'):
            return self.json_response({'error': 'Not found'}, 404)
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
        if self.headers.get('Transfer-Encoding') or not 0 < size <= (131072 if route == '/api/generation' else MAX_BODY):
            return self.json_response({'error': 'Invalid request size'}, 413)
        try:
            data = json.loads(self.rfile.read(size))
            if not isinstance(data, dict):
                raise ValueError()
            if route in ('/api/reject-combination', '/api/pending-briefs/complete', '/api/reject-combination/restore'):
                return self.brief_action(route, data)
            if route in ('/api/generation', '/api/generation/accept', '/api/generation/discard'):
                try:
                    manager = self.server.generation
                    result = manager.start(data, self.catalog()) if route == '/api/generation' else manager.decide(data.get('id'), route.endswith('/accept'))
                    return self.json_response(result, 202)
                except (OSError, ValueError) as error:
                    return self.json_response({'error': str(error)}, 400)
            if route == '/api/icon-flag':
                return self.save_icon_flag(data)
            if route == '/api/feedback/edit':
                return self.edit_feedback(data)
            key, feedback = data.get('icon'), data.get('feedback')
            status = data.get('status')
            if not isinstance(key, str):
                raise ValueError()
            if route == '/api/feedback':
                if not isinstance(feedback, str) or not 1 <= len(feedback.strip()) <= 10000:
                    raise ValueError()
                status = 'pending'
            elif status not in ('ready', 'pending', 'approve'):
                raise ValueError()
            icon = self.catalog().get(key)
            if icon is None:
                return self.json_response({'error': 'Unknown icon'}, 404)
            if data.get('svg_sha256') != icon['svg_sha256']:
                return self.json_response({'error': 'Icon changed; reload the gallery before submitting'}, 409)
        except (ValueError, UnicodeError):
            return self.json_response({'error': 'Invalid feedback or review status'}, 400)
        except OSError:
            return self.json_response({'error': 'Gallery is temporarily unavailable'}, 503)
        try:
            with closing(sqlite3.connect(self.database, timeout=10)) as connection, connection:
                if route == '/api/reviews' and connection.execute(
                    'SELECT 1 FROM split_requests WHERE icon=? AND svg_sha256=? AND active=1',
                    (key, icon['svg_sha256']),
                ).fetchone():
                    return self.json_response({'error': 'This combined icon is rejected. Restore it before changing its review status.'}, 409)
                now = datetime.now(timezone.utc).isoformat()
                if route == '/api/feedback':
                    connection.execute(
                        'INSERT INTO feedback(icon, feedback, svg_sha256, created_at) VALUES (?, ?, ?, ?)',
                        (key, feedback.strip(), icon['svg_sha256'], now),
                    )
                connection.execute(
                    '''INSERT INTO reviews(icon, svg_sha256, status, updated_at) VALUES (?, ?, ?, ?)
                       ON CONFLICT(icon, svg_sha256) DO UPDATE SET
                       status=excluded.status, updated_at=excluded.updated_at''',
                    (key, icon['svg_sha256'], status, now),
                )
            return self.json_response({'saved': True, 'status': status}, 201)
        except sqlite3.Error:
            return self.json_response({'error': 'Could not save feedback'}, 503)

    def save_icon_flag(self, data):
        key, flag = data.get('icon'), data.get('flag')
        if not isinstance(key, str) or flag not in ('', 'container_combination', 'combination', 'other'):
            return self.json_response({'error': 'Choose a valid icon flag.'}, 400)
        try:
            if key not in self.catalog():
                return self.json_response({'error': 'Unknown icon'}, 404)
            with closing(sqlite3.connect(self.database, timeout=10)) as connection, connection:
                if flag:
                    connection.execute('INSERT INTO icon_flags(icon,flag,updated_at) VALUES (?,?,?) '
                        'ON CONFLICT(icon) DO UPDATE SET flag=excluded.flag,updated_at=excluded.updated_at',
                        (key, flag, datetime.now(timezone.utc).isoformat()))
                else:
                    connection.execute('DELETE FROM icon_flags WHERE icon=?', (key,))
            return self.json_response({'flag': flag})
        except (OSError, ValueError, sqlite3.Error):
            return self.json_response({'error': 'Could not save icon flag. Please retry.'}, 503)

    def edit_feedback(self, data):
        feedback_id, feedback, previous = data.get('id'), data.get('feedback'), data.get('previous_feedback')
        if (type(feedback_id) is not int or not isinstance(feedback, str)
                or not 1 <= len(feedback.strip()) <= 10000 or not isinstance(previous, str)):
            return self.json_response({'error': 'Enter feedback between 1 and 10,000 characters.'}, 400)
        try:
            with closing(sqlite3.connect(self.database, timeout=10)) as connection, connection:
                # Compare and update together to avoid silently overwriting another editor.
                updated = connection.execute(
                    'UPDATE feedback SET feedback=? WHERE id=? AND feedback=?',
                    (feedback.strip(), feedback_id, previous))
                if not updated.rowcount:
                    exists = connection.execute('SELECT 1 FROM feedback WHERE id=?', (feedback_id,)).fetchone()
                    return self.json_response({'error': 'Feedback changed. Refresh before editing again.' if exists else 'Feedback not found.'}, 409 if exists else 404)
            return self.json_response({'saved': True, 'feedback': feedback.strip()})
        except sqlite3.Error:
            return self.json_response({'error': 'Could not save feedback. Please retry.'}, 503)

    def brief_action(self, route, data):
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
                    if connection.execute('SELECT 1 FROM split_requests WHERE icon=? AND svg_sha256=? AND active=1', (key,icon['svg_sha256'])).fetchone():
                        raise ValueError('A rejected combination cannot fulfill a component brief.')
                    connection.execute("UPDATE pending_briefs SET status='generated',generated_icon=? WHERE id=?", (key,brief_id))
                    return self.json_response({'saved': True})
                key = data.get('icon')
                if not isinstance(key, str) or key not in catalog:
                    return self.json_response({'error': 'Unknown icon'}, 404)
                icon = catalog[key]
                if data.get('svg_sha256') != icon['svg_sha256']:
                    return self.json_response({'error': 'Icon changed. Refresh before rejecting or restoring.'}, 409)
                if route == '/api/reject-combination/restore':
                    connection.execute('UPDATE split_requests SET active=0 WHERE icon=? AND svg_sha256=?', (key,icon['svg_sha256']))
                    # Explicit restore returns the icon to review, never silently approves it.
                    connection.execute("INSERT INTO reviews(icon,svg_sha256,status,updated_at) VALUES (?,?,'ready',?) ON CONFLICT(icon,svg_sha256) DO UPDATE SET status='ready',updated_at=excluded.updated_at", (key,icon['svg_sha256'],datetime.now(timezone.utc).isoformat()))
                    return self.json_response({'saved': True, 'status': 'ready'})
                validate_split(data)
                sources = icon.get('original_sources', [])
                reference = sources[0]['source_path'] if sources else ''
                split_id = enqueue_split(connection,key,icon['svg_sha256'],reference,data)
                return self.json_response({'saved': True, 'status': 'rejected', 'split_id': split_id}, 201)
        except (ValueError, TypeError) as error:
            return self.json_response({'error': str(error)}, 400)
        except (OSError, sqlite3.Error):
            return self.json_response({'error': 'Could not update pending briefs.'}, 503)


def create_server(dist: Path, database: Path, host='127.0.0.1', port=8000):
    dist, database = dist.resolve(), database.resolve()
    if not (dist / 'gallery/index.html').is_file() or not (dist / 'gallery/icons.json').is_file():
        raise ValueError('Gallery is missing. Run icon_set/scripts/build.py first.')
    if database.is_relative_to(dist):
        raise ValueError('Keep the feedback database outside the publicly served dist folder.')
    init_database(database)
    server = ThreadingHTTPServer((host, port), partial(GalleryHandler, directory=dist, database=database))
    server.generation = GenerationManager(PACKAGE_ROOT.parent, dist, database.parent / 'generation-jobs')
    return server


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dist', type=Path, default=DEFAULT_DIST)
    parser.add_argument('--database', type=Path, default=DEFAULT_DB)
    parser.add_argument('--host', default='127.0.0.1')
    parser.add_argument('--port', type=int, default=8000)
    parser.add_argument('--open', action='store_true', help='Open the local browser')
    args = parser.parse_args(argv)
    try:
        server = create_server(args.dist, args.database, args.host, args.port)
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
