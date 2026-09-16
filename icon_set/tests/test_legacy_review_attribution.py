from contextlib import closing
import json
from pathlib import Path
import sqlite3
import tempfile
import unittest

from icon_set.scripts.attribute_legacy_reviews import MIGRATION, run
from icon_set.scripts.deploy import init_database
from icon_set.scripts.reviewer_stats import reviewer_stats


class LegacyReviewAttributionTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.path = Path(self.tmp.name) / 'feedback.sqlite3'
        with closing(sqlite3.connect(self.path)) as db, db:
            db.execute('CREATE TABLE reviews(icon,svg_sha256,status,updated_at,updated_by,PRIMARY KEY(icon,svg_sha256))')
            db.execute('CREATE TABLE activity_log(id INTEGER PRIMARY KEY,username,action,icon,details,created_at)')
            db.executemany('INSERT INTO reviews VALUES (?,?,?,?,?)', [
                ('solo/a', 'v1', 'approve', '2026-09-10T01:00:00Z', None),
                ('solo/a', 'v2', 'pending', '2026-09-10T02:00:00Z', ''),
                ('solo/b', 'v1', 'rejected', '2026-09-11T01:00:00Z', '  '),
                ('solo/c', 'v1', 'approve', '2026-09-11T01:00:00Z', 'jakes'),
                ('solo/d', 'v1', 'ready', '2026-09-11T01:00:00Z', None),
            ])

    def test_backup_preserve_names_dates_and_idempotence(self):
        self.assertFalse(run(self.path)['applied'])
        result = run(self.path, apply=True)
        self.assertEqual((result['records'], result['icons']), (3, 2))
        with closing(sqlite3.connect(result['backup'])) as db:
            self.assertIsNone(db.execute("SELECT updated_by FROM reviews WHERE icon='solo/a' AND svg_sha256='v1'").fetchone()[0])
        with closing(sqlite3.connect(self.path)) as db:
            self.assertEqual(db.execute("SELECT updated_by,updated_at FROM reviews WHERE icon='solo/a' AND svg_sha256='v1'").fetchone(), ('hina', '2026-09-10T01:00:00Z'))
            self.assertEqual(db.execute("SELECT updated_by FROM reviews WHERE icon='solo/c'").fetchone()[0], 'jakes')
            self.assertIsNone(db.execute("SELECT updated_by FROM reviews WHERE icon='solo/d'").fetchone()[0])
            self.assertTrue(json.loads(db.execute('SELECT details FROM activity_log LIMIT 1').fetchone()[0])['legacy_snapshot'])
            stats = reviewer_stats(db, {'start': ['2026-09-10'], 'end': ['2026-09-11']}, ['hina'])
            self.assertEqual(stats['totals'], {'total': 2, 'approved': 0, 'disapproved': 1, 'rejected': 1})
        self.assertEqual(run(self.path, apply=True)['records'], 0)
        with closing(sqlite3.connect(self.path)) as db:
            self.assertEqual(db.execute('SELECT COUNT(*) FROM activity_log').fetchone()[0], 3)

    def test_invalid_date_rolls_back_all_changes(self):
        with closing(sqlite3.connect(self.path)) as db, db:
            db.execute("UPDATE reviews SET updated_at='unknown' WHERE icon='solo/b'")
        with self.assertRaises(ValueError):
            run(self.path, apply=True)
        with closing(sqlite3.connect(self.path)) as db:
            self.assertEqual(db.execute('SELECT COUNT(*) FROM activity_log').fetchone()[0], 0)
            self.assertEqual(db.execute("SELECT COUNT(*) FROM reviews WHERE updated_by='hina'").fetchone()[0], 0)

    def test_normal_startup_migrates_actual_configured_database_once(self):
        # Simulate a production database created by the previous server version,
        # stored somewhere other than the default local data directory.
        production = Path(self.tmp.name) / 'persistent' / 'production.sqlite3'
        init_database(production)
        with closing(sqlite3.connect(self.path)) as source, closing(sqlite3.connect(production)) as db, db:
            db.execute('DROP TABLE review_data_migrations')
            db.executemany('INSERT INTO reviews(icon,svg_sha256,status,updated_at,updated_by) VALUES (?,?,?,?,?)',
                           source.execute('SELECT * FROM reviews').fetchall())
            db.execute("INSERT INTO reviews VALUES ('solo/later','v1','approve','2026-09-17T00:00:00Z',NULL)")
        init_database(production)
        with closing(sqlite3.connect(production)) as db, db:
            self.assertEqual(db.execute("SELECT count(*) FROM reviews WHERE updated_by='hina'").fetchone()[0], 3)
            self.assertIsNone(db.execute("SELECT updated_by FROM reviews WHERE icon='solo/later'").fetchone()[0])
            ledger = json.loads(db.execute('SELECT details FROM review_data_migrations WHERE id=?', (MIGRATION,)).fetchone()[0])
            self.assertTrue(Path(ledger['backup']).is_file())
            db.execute("INSERT INTO reviews VALUES ('solo/not-covered','v1','pending','2026-09-10T00:00:00Z',NULL)")
        init_database(production)
        with closing(sqlite3.connect(production)) as db:
            self.assertEqual(db.execute('SELECT count(*) FROM activity_log').fetchone()[0], 3)
            self.assertIsNone(db.execute("SELECT updated_by FROM reviews WHERE icon='solo/not-covered'").fetchone()[0])
        # Starting production never copied or modified the separate local DB.
        with closing(sqlite3.connect(self.path)) as db:
            self.assertEqual(db.execute("SELECT count(*) FROM reviews WHERE updated_by='hina'").fetchone()[0], 0)

    def test_previous_manual_attribution_does_not_duplicate_history(self):
        run(self.path, apply=True)
        with closing(sqlite3.connect(self.path)) as db, db:
            # The first standalone script did not have a migration ledger.
            db.execute('DROP TABLE review_data_migrations')
        result = run(self.path, apply=True)
        self.assertEqual(result['records'], 0)
        self.assertNotIn('backup', result)
        with closing(sqlite3.connect(self.path)) as db:
            self.assertEqual(db.execute('SELECT count(*) FROM activity_log').fetchone()[0], 3)
            self.assertEqual(db.execute('SELECT count(*) FROM review_data_migrations').fetchone()[0], 1)
