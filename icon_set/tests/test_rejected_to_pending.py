import json
from contextlib import closing
from pathlib import Path
import sqlite3
import tempfile
import unittest
from unittest.mock import patch

from icon_set.scripts.rejected_to_pending import run


class RestoreTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        root = Path(self.temp.name)
        self.database = root / 'reviews.sqlite3'
        self.catalog = root / 'icons.json'
        self.catalog.write_text(json.dumps({'icons': [
            {'key': key, 'svg_sha256': 'current'}
            for key in ['solo/old-rejection', 'solo/split', 'solo/approved', 'solo/stale-split']
        ], 'failed_icons': [{'key': 'solo/failed', 'svg_sha256': 'current'}]}))
        with closing(sqlite3.connect(self.database)) as db, db:
            db.executescript('''
                CREATE TABLE reviews(icon TEXT,svg_sha256 TEXT,status TEXT,updated_at TEXT,updated_by TEXT,PRIMARY KEY(icon,svg_sha256));
                CREATE TABLE split_requests(icon TEXT,svg_sha256 TEXT,active INTEGER,restored_by TEXT,restored_at TEXT);
                CREATE TABLE activity_log(id INTEGER PRIMARY KEY,username TEXT,action TEXT,icon TEXT,details TEXT,created_at TEXT);
            ''')
            db.executemany('INSERT INTO reviews VALUES (?,?,?,"before","original")', [
                ('solo/old-rejection', 'old', 'rejected'),
                ('solo/old-rejection', 'current', 'approve'),
                ('solo/approved', 'current', 'approve'),
                ('solo/failed', 'current', 'rejected'),
                ('solo/absent', 'old', 'rejected'),
                ('solo/stale-split', 'current', 'approve'),
            ])
            db.executemany('INSERT INTO split_requests VALUES (?,?,1,NULL,NULL)', [
                ('solo/split', 'current'), ('solo/stale-split', 'old')])

    def snapshot(self):
        with closing(sqlite3.connect(self.database)) as db, db:
            return '\n'.join(db.iterdump())

    def test_dry_run_is_read_only(self):
        before = self.snapshot()
        count, backup = run(self.database, self.catalog, 'tester')
        self.assertEqual(count, 3)
        self.assertIsNone(backup)
        self.assertEqual(self.snapshot(), before)
        self.assertEqual(len(list(self.database.parent.iterdir())), 2)

    def test_restore_matches_app_and_is_idempotent(self):
        before = self.snapshot()
        count, backup = run(self.database, self.catalog, 'tester', apply=True)
        self.assertEqual(count, 3)
        with closing(sqlite3.connect(backup)) as db:
            self.assertEqual('\n'.join(db.iterdump()), before)
        with closing(sqlite3.connect(self.database)) as db, db:
            states = dict(db.execute("SELECT icon,status FROM reviews WHERE svg_sha256='current'"))
            self.assertEqual(states, {'solo/old-rejection': 'pending', 'solo/split': 'pending',
                                     'solo/failed': 'pending', 'solo/approved': 'approve',
                                     'solo/stale-split': 'approve'})
            self.assertEqual(db.execute("SELECT status FROM reviews WHERE icon='solo/old-rejection' AND svg_sha256='old'").fetchone()[0], 'pending')
            self.assertEqual(db.execute("SELECT active FROM split_requests WHERE icon='solo/split'").fetchone()[0], 0)
            events = db.execute('SELECT action,details FROM activity_log').fetchall()
            self.assertEqual(len(events), 3)
            self.assertTrue(all(action == 'restore' and json.loads(details)['svg_sha256'] == 'current' for action, details in events))
        self.assertEqual(run(self.database, self.catalog, 'tester', apply=True), (0, None))

    def test_failure_rolls_back_whole_operation(self):
        with closing(sqlite3.connect(self.database)) as db, db:
            db.execute("CREATE TRIGGER fail_restore BEFORE INSERT ON activity_log BEGIN SELECT RAISE(ABORT,'test failure'); END")
        before = self.snapshot()
        with self.assertRaises(sqlite3.IntegrityError):
            run(self.database, self.catalog, 'tester', apply=True)
        self.assertEqual(self.snapshot(), before)

    def test_backup_failure_prevents_updates(self):
        before = self.snapshot()
        with patch('icon_set.scripts.rejected_to_pending.backup_database', side_effect=OSError('disk full')):
            with self.assertRaises(OSError):
                run(self.database, self.catalog, 'tester', apply=True)
        self.assertEqual(self.snapshot(), before)

    def test_missing_database_is_not_created(self):
        missing = self.database.parent / 'missing.sqlite3'
        with self.assertRaises(ValueError):
            run(missing, self.catalog, 'tester', apply=True)
        self.assertFalse(missing.exists())


if __name__ == '__main__':
    unittest.main()
