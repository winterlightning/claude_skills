import json
from contextlib import closing
import unittest
import sqlite3
import tempfile
from pathlib import Path
from icon_set.tests import test_gallery
from icon_set.scripts.deploy import init_database


class FlagMigrationTests(unittest.TestCase):
    def test_existing_database_preserves_flags_and_accepts_exception(self):
        with tempfile.TemporaryDirectory() as folder:
            database = Path(folder) / 'feedback.sqlite3'
            with closing(sqlite3.connect(database)) as connection, connection:
                connection.execute("""CREATE TABLE icon_flags (
                    icon TEXT PRIMARY KEY, flag TEXT NOT NULL CHECK(flag IN
                    ('container_combination','combination','other')),
                    updated_at TEXT NOT NULL)""")
                connection.execute("INSERT INTO icon_flags VALUES ('solo/mug','other','before')")
            init_database(database)
            init_database(database)
            with closing(sqlite3.connect(database)) as connection, connection:
                self.assertEqual(connection.execute('SELECT icon, flag, updated_at FROM icon_flags').fetchall(),
                                 [('solo/mug', 'other', 'before')])
                connection.execute("INSERT INTO icon_flags(icon, flag, updated_at) VALUES ('solo/hat','exception','after')")
                with self.assertRaises(sqlite3.IntegrityError):
                    connection.execute("INSERT INTO icon_flags(icon, flag, updated_at) VALUES ('solo/bad','unknown','after')")

class IconFlagTests(unittest.TestCase):
    setUp = test_gallery.ServerTests.setUp
    request = test_gallery.ServerTests.request

    def test_flags_persist_clear_and_leave_reviews_alone(self):
        endpoint='/api/icon-flag'
        self.assertEqual(json.loads(self.request('GET',endpoint+'?icon=sub/square')[1]),{'flag':'','updated_by':None,'updated_at':None})
        for flag in ('container_combination','combination','other','exception'):
            self.assertEqual(self.request('POST',endpoint,{'icon':'sub/square','flag':flag})[0],200)
            init_database(self.database)
            saved=json.loads(self.request('GET',endpoint+'?icon=sub/square')[1])
            self.assertEqual((saved['flag'],saved['updated_by']),(flag,'jakes'),'The flag records who set it')
        self.assertEqual(json.loads(self.request('GET','/api/reviews')[1])['sub/square'],'ready')
        self.assertEqual(self.request('POST',endpoint,{'icon':'sub/square','flag':''})[0],200)
        self.assertEqual(json.loads(self.request('GET',endpoint+'?icon=sub/square')[1])['flag'],'')
        self.assertEqual(self.request('POST',endpoint,{'icon':'sub/square','flag':'bad'})[0],400)
        self.assertEqual(self.request('POST',endpoint,{'icon':'missing','flag':'other'})[0],404)
        self.assertEqual(self.request('POST',endpoint,{'icon':'sub/square','flag':'other'}, {'Content-Type':'application/json','Origin':'http://elsewhere.test'})[0],403)


class IconTypeTests(unittest.TestCase):
    setUp = test_gallery.ServerTests.setUp
    request = test_gallery.ServerTests.request

    def test_type_round_trip_and_validation(self):
        endpoint = '/api/icon-type'
        query = endpoint + '?icon=sub/square'
        self.assertEqual(json.loads(self.request('GET', query)[1])['icon_type'], '')
        for value in ('human', 'avatar', 'custom portrait', ''):
            self.assertEqual(self.request('POST', endpoint, {'icon': 'sub/square', 'icon_type': value})[0], 200)
            init_database(self.database)
            saved = json.loads(self.request('GET', query)[1])
            self.assertEqual(saved['icon_type'], value)
            self.assertEqual(saved['updated_by'], 'jakes')
        for value in (None, 3, [], 'x' * 201):
            self.assertEqual(self.request('POST', endpoint, {'icon': 'sub/square', 'icon_type': value})[0], 400)
        self.assertEqual(self.request('POST', endpoint, {'icon': 'missing', 'icon_type': 'human'})[0], 404)
        self.assertEqual(self.request('GET', endpoint + '?icon=missing')[0], 404)
        self.assertEqual(self.request('POST', endpoint, {'icon': 'sub/square', 'icon_type': 'human'}, anonymous=True)[0], 401)
        self.assertEqual(self.request('POST', endpoint, {'icon': 'sub/square', 'icon_type': 'human'},
                                     {'Content-Type': 'application/json', 'Origin': 'http://elsewhere.test'})[0], 403)
        self.assertEqual(json.loads(self.request('GET', '/api/reviews')[1])['sub/square'], 'ready')
