"""Removing one feedback entry preserves icons, reviews, and other feedback."""
import json
import sqlite3
import tempfile
import unittest
from email.message import Message
from io import BytesIO
from pathlib import Path
from unittest.mock import patch
from icon_set.scripts.deploy import GalleryHandler, init_database


class FeedbackDeleteTests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name)
        self.database = self.root / 'feedback.sqlite3'
        init_database(self.database)
        self.db = sqlite3.connect(self.database)
        self.addCleanup(self.db.close)
        with self.db:
            self.db.execute("INSERT INTO feedback(icon,feedback,svg_sha256,created_at) VALUES ('solo/example','Make round','old','2026-09-15')")
            self.db.execute("INSERT INTO feedback(icon,feedback,svg_sha256,created_at) VALUES ('solo/example','Keep this','old','2026-09-15')")
            self.db.execute("INSERT INTO reviews VALUES ('solo/example','new','approve','2026-09-15','jakes')")
        self.payload = {'id': 1, 'previous_feedback': 'Make round', 'previous_edited_at': None}

    def request(self, payload=None, user='jakes', origin=None):
        handler = GalleryHandler.__new__(GalleryHandler)
        handler.root, handler.database = self.root, self.database
        handler.current_user = lambda: user
        handler.path = '/api/feedback/delete'
        body = json.dumps(self.payload if payload is None else payload).encode()
        handler.rfile = BytesIO(body)
        handler.headers = Message()
        handler.headers['Host'] = 'localhost'
        handler.headers['Content-Type'] = 'application/json'
        handler.headers['Content-Length'] = str(len(body))
        if origin:
            handler.headers['Origin'] = origin
        responses = []
        handler.json_response = lambda data, status=200: responses.append((status, data))
        handler.do_POST()
        return responses[0]

    def test_removes_only_selected_feedback_and_records_actor(self):
        reviews = self.db.execute('SELECT * FROM reviews').fetchall()
        remaining = self.db.execute('SELECT * FROM feedback WHERE id=2').fetchall()
        status, result = self.request()
        self.assertEqual(status, 200)
        self.assertEqual(result, {'deleted': True, 'id': 1, 'icon': 'solo/example'})
        self.assertEqual(self.db.execute('SELECT * FROM feedback').fetchall(), remaining)
        self.assertEqual(self.db.execute('SELECT * FROM reviews').fetchall(), reviews)
        actor, action, icon, details = self.db.execute('SELECT username,action,icon,details FROM activity_log').fetchone()
        self.assertEqual((actor, action, icon), ('jakes', 'feedback_delete', 'solo/example'))
        self.assertEqual(json.loads(details)['feedback_id'], 1)
        self.assertEqual(self.request()[0], 404)

    def test_changed_feedback_is_not_removed(self):
        for text, timestamp in [('Revised request', None), ('Make round', '2026-09-16T01:00:00Z')]:
            with self.subTest(text=text, timestamp=timestamp):
                with self.db:
                    self.db.execute('UPDATE feedback SET feedback=?,edited_at=? WHERE id=1', (text, timestamp))
                self.assertEqual(self.request()[0], 409)
                self.assertEqual(self.db.execute('SELECT COUNT(*) FROM feedback').fetchone()[0], 2)

    def test_requires_login_same_origin_and_valid_id(self):
        self.assertEqual(self.request(user=None)[0], 401)
        self.assertEqual(self.request(origin='https://elsewhere.test')[0], 403)
        for id in (True, '1', 0, -1, None):
            self.assertEqual(self.request(dict(self.payload, id=id))[0], 400)
        self.assertEqual(self.request({'id': 1})[0], 400)
        self.assertEqual(self.db.execute('SELECT COUNT(*) FROM feedback').fetchone()[0], 2)

    def test_activity_failure_rolls_back_delete(self):
        with patch('icon_set.scripts.deploy.record_activity', side_effect=sqlite3.OperationalError('unavailable')):
            self.assertEqual(self.request()[0], 503)
        self.assertEqual(self.db.execute('SELECT COUNT(*) FROM feedback').fetchone()[0], 2)


if __name__ == '__main__':
    unittest.main()
