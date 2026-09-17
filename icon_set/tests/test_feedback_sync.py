"""Syncing replaces the local feedback database with production's export, after a backup."""
import json
import sqlite3
from contextlib import closing
import tempfile
import unittest
from email.message import Message
from io import BytesIO
from pathlib import Path
from unittest.mock import patch
import urllib.error
from icon_set.scripts.deploy import GalleryHandler, export_feedback_snapshot, export_review_bundle, init_database


class FakeResponse(BytesIO):
    def __init__(self, content, exported_at='2026-09-16T10:00:00+00:00'):
        super().__init__(content)
        self.headers = {'X-Feedback-Exported-At': exported_at}


class FeedbackSyncTests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name)
        (self.root / 'prod').mkdir()
        (self.root / 'local').mkdir()
        self.production = self.root / 'prod/feedback.sqlite3'
        self.database = self.root / 'local/feedback.sqlite3'
        for path in (self.production, self.database):
            init_database(path)
        with closing_db(self.production) as db, db:
            db.execute("INSERT INTO feedback(icon,feedback,svg_sha256,created_at,author) VALUES ('solo/cat','Ears too big','abc','2026-09-16','ray')")
            db.execute("INSERT INTO reviews VALUES ('solo/cat','abc','pending','2026-09-16','ray')")
            db.execute("INSERT INTO admin_sessions VALUES ('prod-token','ray',9999999999)")
        with closing_db(self.database) as db, db:
            db.execute("INSERT INTO feedback(icon,feedback,svg_sha256,created_at) VALUES ('solo/old','Local only','old','2026-09-10')")
            db.execute("INSERT INTO admin_sessions VALUES ('local-token','jakes',9999999999)")
        # Production approved an uploaded drawing; the local machine has an older edit and reference.
        write(self.root / 'prod/icon-artwork/abc123/artwork.json', '{"source_mode": "use_upload"}')
        write(self.root / 'prod/icon-artwork/abc123/.lock', '')
        write(self.root / 'prod/reference-images/ref.json', '{}')
        write(self.root / 'local/stroke-edits/old/edit.json', '{"local": true}')
        write(self.root / 'local/reference-images/local.json', '{}')
        export = self.root / 'export.sqlite3'
        export_feedback_snapshot(self.production, export)
        self.export = export.read_bytes()
        bundle = self.root / 'export.zip'
        export_review_bundle(self.production, bundle)
        self.bundle = bundle.read_bytes()

    def serve(self, bundle=True, database=True):
        def urlopen(request, timeout=None):
            if request.full_url.endswith('/api/review-data/export'):
                if bundle is True:
                    return FakeResponse(self.bundle)
                if bundle is False:
                    raise urllib.error.HTTPError(request.full_url, 404, 'Not Found', {}, None)
                return FakeResponse(bundle)
            return FakeResponse(self.export if database is True else database)
        return patch('urllib.request.urlopen', side_effect=urlopen)

    def request(self, payload, user='jakes', host='localhost:8000'):
        handler = GalleryHandler.__new__(GalleryHandler)
        handler.root, handler.database = self.root, self.database
        handler.current_user = lambda: user
        handler.path = '/api/feedback-db/sync'
        body = json.dumps(payload).encode()
        handler.rfile = BytesIO(body)
        handler.headers = Message()
        handler.headers['Host'] = host
        handler.headers['Content-Type'] = 'application/json'
        handler.headers['Content-Length'] = str(len(body))
        responses = []
        handler.json_response = lambda data, status=200: responses.append((status, data))
        handler.do_POST()
        return responses[0]

    def rows(self, sql, path=None):
        with closing_db(path or self.database) as db:
            return db.execute(sql).fetchall()

    def test_export_omits_login_sessions(self):
        path = self.root / 'check.sqlite3'
        path.write_bytes(self.export)
        self.assertEqual(self.rows('SELECT feedback FROM feedback', path), [('Ears too big',)])
        self.assertEqual(self.rows('SELECT * FROM admin_sessions', path), [])

    def seed_progression(self, path, label):
        with closing_db(path) as db, db:
            db.execute("INSERT INTO primitive_status(uuid,status,reason,updated_by,updated_at) VALUES (?,'skip','container','jakes','2026-09-17')", (label,))
            db.execute("INSERT INTO primitive_briefs VALUES (?,'solo',?,'jakes','2026-09-17')", (label, label))
            db.execute('CREATE TABLE progression_imports(uuid TEXT PRIMARY KEY, updated_at TEXT NOT NULL)')
            db.execute('INSERT INTO progression_imports VALUES (?,?)', (label, '2026-09-17'))
            db.execute('CREATE TABLE progression_reviews(path TEXT PRIMARY KEY, content TEXT NOT NULL)')
            db.execute('INSERT INTO progression_reviews VALUES (?,?)', (label, '{}'))
            db.execute("INSERT INTO activity_log(username,action,icon,created_at) VALUES ('jakes','primitive_todo',?,'2026-09-17')", ('primitive:' + label,))

    def test_export_excludes_progression(self):
        self.seed_progression(self.production, 'production')
        path = self.root / 'without-progression.sqlite3'
        export_feedback_snapshot(self.production, path)
        for table in ('primitive_status', 'primitive_briefs', 'progression_imports', 'progression_reviews'):
            self.assertEqual(self.rows(f'SELECT * FROM {table}', path), [])
        self.assertEqual(self.rows("SELECT * FROM activity_log WHERE action='primitive_todo'", path), [])

    def test_sync_preserves_local_progression_even_from_legacy_exports(self):
        self.seed_progression(self.production, 'production')
        self.seed_progression(self.database, 'local')
        tables = ('primitive_status', 'primitive_briefs', 'progression_imports', 'progression_reviews')
        before = {table: self.rows(f'SELECT * FROM {table}') for table in tables}
        # A legacy server sends progression as part of its whole database.
        self.export = self.production.read_bytes()
        import zipfile
        bundle = self.root / 'legacy.zip'
        with zipfile.ZipFile(bundle, 'w') as archive:
            archive.writestr('feedback.sqlite3', self.export)
            archive.writestr('stores.json', '[]')
        self.bundle = bundle.read_bytes()
        for bundled in (True, False):
            with self.subTest(bundled=bundled), self.serve(bundle=bundled):
                status, result = self.request({'source': 'https://prod.example'})
            self.assertEqual(status, 200, result)
            for table in tables:
                self.assertEqual(self.rows(f'SELECT * FROM {table}'), before[table])
            self.assertEqual(self.rows("SELECT icon FROM activity_log WHERE action='primitive_todo'"), [('primitive:local',)])
            self.assertEqual(self.rows('SELECT feedback FROM feedback'), [('Ears too big',)])

    def test_sync_replaces_database_backs_up_and_keeps_local_login(self):
        with self.serve() as opened:
            status, result = self.request({'source': 'https://prod.example/gallery/icons.html?page=1&page_size=48'})
        self.assertEqual(status, 200, result)
        self.assertEqual(opened.call_args[0][0].full_url, 'https://prod.example/api/review-data/export')
        self.assertNotIn('warning', result)
        self.assertEqual(result['source'], 'https://prod.example')
        self.assertEqual(result['counts']['feedback'], 1)
        self.assertEqual(self.rows('SELECT icon,feedback,author FROM feedback'), [('solo/cat', 'Ears too big', 'ray')])
        self.assertEqual(self.rows('SELECT icon,status,updated_by FROM reviews'), [('solo/cat', 'pending', 'ray')])
        self.assertEqual(self.rows('SELECT token,username FROM admin_sessions'), [('local-token', 'jakes')])
        user, details = self.rows("SELECT username,details FROM activity_log WHERE action='feedback_sync'")[0]
        self.assertEqual((user, json.loads(details)['source']), ('jakes', 'https://prod.example'))
        backup = self.root / 'local/feedback-sync-backups' / result['backup']
        self.assertEqual(self.rows('SELECT feedback FROM feedback', backup), [('Local only',)])
        self.assertEqual([p.name for p in (self.root / 'local').iterdir() if p.name.startswith('.feedback-')], [])

    def test_sync_mirrors_artwork_edits_and_references(self):
        with self.serve():
            status, result = self.request({'source': 'https://prod.example'})
        self.assertEqual(status, 200, result)
        local = self.root / 'local'
        self.assertEqual((local / 'icon-artwork/abc123/artwork.json').read_text(), '{"source_mode": "use_upload"}')
        self.assertFalse((local / 'icon-artwork/abc123/.lock').exists())
        self.assertTrue((local / 'reference-images/ref.json').is_file())
        self.assertFalse((local / 'reference-images/local.json').exists())
        self.assertFalse((local / 'stroke-edits').exists())
        self.assertEqual(result['stores'], {'icon-artwork': 1, 'stroke-edits': 0, 'reference-images': 1})
        saved = next((local / 'feedback-sync-backups').glob('stores.before-sync-*'))
        self.assertEqual((saved / 'stroke-edits/old/edit.json').read_text(), '{"local": true}')
        self.assertTrue((saved / 'reference-images/local.json').is_file())

    def test_older_production_syncs_database_with_warning(self):
        with self.serve(bundle=False):
            status, result = self.request({'source': 'https://prod.example'})
        self.assertEqual(status, 200, result)
        self.assertIn('artwork was not synced', result['warning'])
        self.assertEqual(self.rows('SELECT feedback FROM feedback'), [('Ears too big',)])
        self.assertTrue((self.root / 'local/stroke-edits/old/edit.json').is_file())

    def test_rejects_unsafe_bundle_paths(self):
        import io, zipfile
        buffer = io.BytesIO()
        with zipfile.ZipFile(buffer, 'w') as archive:
            archive.writestr('feedback.sqlite3', self.export)
            archive.writestr('stores.json', '["icon-artwork"]')
            archive.writestr('icon-artwork/../../escape.txt', 'x')
        with self.serve(bundle=buffer.getvalue()):
            self.assertEqual(self.request({'source': 'https://prod.example'})[0], 502)
        self.assertFalse((self.root / 'escape.txt').exists())
        self.assertEqual(self.rows('SELECT feedback FROM feedback'), [('Local only',)])

    def test_refuses_self_invalid_downloads_and_guests(self):
        before = self.rows('SELECT * FROM feedback')
        self.assertEqual(self.request({'source': 'http://localhost:8000/gallery/'})[0], 400)
        self.assertEqual(self.request({'source': 'ftp://prod.example'})[0], 400)
        self.assertEqual(self.request({'source': 'https://prod.example'}, user=None)[0], 401)
        with self.serve(bundle=b'<html>tunnel offline</html>'):
            self.assertEqual(self.request({'source': 'https://prod.example'})[0], 502)
        with self.serve(bundle=False, database=b'<html>tunnel offline</html>'):
            self.assertEqual(self.request({'source': 'https://prod.example'})[0], 502)
        self.assertEqual(self.rows('SELECT * FROM feedback'), before)
        self.assertFalse((self.root / 'local/feedback-sync-backups').exists())


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)


def closing_db(path):
    return closing(sqlite3.connect(path))


if __name__ == '__main__':
    unittest.main()
