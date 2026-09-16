"""Review semantics, structured reasons, exclusions and developer type lookup."""
import json
from pathlib import Path
import sqlite3
import tempfile
import unittest

from icon_set.scripts.deploy import init_database
from icon_set.tests import test_stroke_edits as fixture


class ReviewWorkflowTests(unittest.TestCase):
    setUp = fixture.StrokeEditAPITests.setUp
    start = fixture.StrokeEditAPITests.start
    call = fixture.StrokeEditAPITests.call

    def login(self):
        self.assertEqual(self.call('POST', '/api/auth/login', {'username': 'jakes', 'password': '1'})[0], 200)

    def test_disapproval_saves_immediately_and_reasons_are_exposed_to_developers(self):
        self.login()
        data = {'icon': 'sub/example', 'svg_sha256': 'version-a', 'status': 'disapprove'}
        self.assertEqual(self.call('POST', '/api/reviews', data)[0], 201)
        self.assertEqual(self.call('GET', '/api/feedback?icon=sub%2Fexample')[1], [])
        for reason in ('bad-stroke', 'meaning', 'other'):
            payload = dict(data, reason=reason)
            if reason == 'other':
                self.assertEqual(self.call('POST', '/api/reviews', payload)[0], 400)
                payload['feedback'] = 'Separate the two lower strokes.'
            status, row = self.call('POST', '/api/reviews', payload)
            self.assertEqual(status, 201)
            self.assertEqual(row['status'], 'pending')  # Existing consumer-compatible storage value.
            status, feedback = self.call('GET', '/api/feedback?icon=sub%2Fexample')
            self.assertEqual(feedback[0]['reason'], reason)
            self.assertTrue(feedback[0]['feedback'])
        self.assertEqual(self.call('POST', '/api/icon-type', {'icon': 'sub/example', 'icon_type': 'avatar'})[0], 200)
        status, rows = self.call('GET', '/api/icon-types?type=avatar&status=disapprove')
        self.assertEqual(status, 200)
        self.assertEqual(rows['icons'][0]['reason'], 'other')
        self.assertEqual(rows['icons'][0]['status'], 'disapprove')
        self.assertEqual(rows['icons'][0]['svg_sha256'], 'version-a')
        self.assertEqual(self.call('GET', '/api/icon-types?type=human')[1]['icons'], [])
        self.assertEqual(self.call('GET', '/api/feedback-feed')[1][0]['icon_type'], 'avatar')
        self.assertEqual(self.call('POST', '/api/reviews', dict(data, status='re-generated'))[0], 201)
        self.assertEqual(self.call('GET', '/api/reviews')[1]['sub/example'], 'ready')
        self.assertEqual(self.call('GET', '/api/icon-types?type=avatar&status=disapprove')[1]['icons'], [])

    def test_reject_text_and_number_and_restore_to_ready(self):
        self.login()
        data = {'icon': 'sub/example', 'svg_sha256': 'version-a', 'status': 'rejected'}
        self.assertEqual(self.call('POST', '/api/reviews', data)[0], 201)
        for flag in ('text', 'number', 'combination'):
            self.assertEqual(self.call('POST', '/api/icon-flag', {'icon': 'sub/example', 'flag': flag})[0], 200)
            self.assertEqual(self.call('GET', '/api/icon-flag?icon=sub%2Fexample')[1]['flag'], flag)
        self.assertEqual(self.call('POST', '/api/reviews', dict(data, status='approve'))[0], 409)
        self.assertEqual(self.call('POST', '/api/reject-combination/restore', data)[1]['status'], 'ready')
        self.assertEqual(self.call('GET', '/api/reviews')[1]['sub/example'], 'ready')


class ReviewMigrationTests(unittest.TestCase):
    def test_migration_preserves_flag_actors_and_retires_regenerated(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'feedback.sqlite3'
            init_database(path)
            with sqlite3.connect(path) as db:
                db.execute('DROP TABLE icon_flags')
                db.execute("CREATE TABLE icon_flags (icon TEXT PRIMARY KEY, flag TEXT CHECK(flag IN ('combination','exception')), updated_at TEXT, updated_by TEXT)")
                db.execute("INSERT INTO icon_flags VALUES ('sub/example','combination','old','hina')")
                db.execute("INSERT INTO reviews(icon,svg_sha256,status,updated_at,updated_by) VALUES ('sub/example','v1','re-generated','old','hina')")
            init_database(path)
            init_database(path)
            with sqlite3.connect(path) as db:
                self.assertEqual(db.execute('SELECT * FROM icon_flags').fetchone(), ('sub/example', 'combination', 'old', 'hina'))
                self.assertEqual(db.execute('SELECT status,updated_by FROM reviews').fetchone(), ('ready', 'hina'))
                db.execute("UPDATE icon_flags SET flag='text'")
