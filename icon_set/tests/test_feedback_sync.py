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
from icon_set.scripts.deploy import GalleryHandler, export_feedback_snapshot, init_database


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
        export = self.root / 'export.sqlite3'
        export_feedback_snapshot(self.production, export)
        self.export = export.read_bytes()

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

    def test_sync_replaces_database_backs_up_and_keeps_local_login(self):
        with patch('urllib.request.urlopen', return_value=FakeResponse(self.export)) as opened:
            status, result = self.request({'source': 'https://prod.example/gallery/icons.html?page=1&page_size=48'})
        self.assertEqual(status, 200, result)
        self.assertEqual(opened.call_args[0][0].full_url, 'https://prod.example/api/feedback-db/export')
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

    def test_refuses_self_invalid_downloads_and_guests(self):
        before = self.rows('SELECT * FROM feedback')
        self.assertEqual(self.request({'source': 'http://localhost:8000/gallery/'})[0], 400)
        self.assertEqual(self.request({'source': 'ftp://prod.example'})[0], 400)
        self.assertEqual(self.request({'source': 'https://prod.example'}, user=None)[0], 401)
        with patch('urllib.request.urlopen', return_value=FakeResponse(b'<html>tunnel offline</html>')):
            self.assertEqual(self.request({'source': 'https://prod.example'})[0], 502)
        self.assertEqual(self.rows('SELECT * FROM feedback'), before)
        self.assertFalse((self.root / 'local/feedback-sync-backups').exists())


def closing_db(path):
    return closing(sqlite3.connect(path))


if __name__ == '__main__':
    unittest.main()
