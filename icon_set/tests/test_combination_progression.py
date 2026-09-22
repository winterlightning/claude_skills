from contextlib import closing
import json
from pathlib import Path
import sqlite3
from tempfile import TemporaryDirectory
import unittest

from icon_set.scripts.combination_library import connect, save_pair, summary
from icon_set.scripts.combination_progression import index_references, migrate_legacy
from icon_set.scripts.primitive_status import set_status

UID = '11111111-2222-3333-4444-555555555555'


class CombinationProgressionTest(unittest.TestCase):
    def setUp(self):
        self.folder = TemporaryDirectory()
        self.addCleanup(self.folder.cleanup)
        self.database = Path(self.folder.name) / 'feedback.sqlite3'

    def mark(self, db, reason='container', status='skip', **kwargs):
        set_status(db, [UID], status, reason, user='reviewer', record=lambda *a, **kw: None, **kwargs)

    def test_live_flags_briefs_positions_and_reclassification(self):
        with connect(self.database) as db:
            index_references(db, {'rows': [dict(uuid=UID, concept='Clipboard strategy', path='office/clipboard.svg')]})
        # Simulate the already-running gallery: an ordinary independent connection,
        # no combination-library initialization or synchronization call on writes.
        with closing(sqlite3.connect(self.database)) as writer, writer:
            self.mark(writer, main_brief=dict(family='container', name='Clipboard', description='Empty frame'))
        with connect(self.database) as db:
            rows = db.execute('SELECT * FROM combination_entries').fetchall()
            self.assertEqual(len(rows), 1)
            row = dict(rows[0])
            self.assertEqual(row['concept'], 'Clipboard strategy')
            self.assertEqual(row['kind'], 'container')
            self.assertEqual(row['origin'], 'progression')
            self.assertIsNone(row['main_id'])
            self.assertEqual((row['main_status'], row['sub_status']), ('brief_ready', 'needed'))
            self.assertEqual(json.loads(row['main_brief'])['name'], 'Clipboard')
        with closing(sqlite3.connect(self.database)) as writer, writer:
            self.mark(writer, 'combination', sub_position='top-left')
        with connect(self.database) as db:
            row = db.execute('SELECT * FROM combination_entries').fetchone()
            self.assertEqual((row['kind'], row['position']), ('side', 'top-left'))
        with closing(sqlite3.connect(self.database)) as writer, writer:
            self.mark(writer, status='todo')
        with connect(self.database) as db:
            self.assertEqual(db.execute('SELECT COUNT(*) FROM combination_entries').fetchone()[0], 0)

    def test_existing_pairs_link_without_duplicate_or_overwriting_selection(self):
        with connect(self.database) as db:
            pair = save_pair(db, 'container', dict(id='separate-pair-id', source_id=UID, concept='Editorial name',
                main_id='container/host', sub_id='symbol/star', component_selection='explicit'))
            self.mark(db)
            rows = db.execute('SELECT * FROM combination_entries').fetchall()
            self.assertEqual(len(rows), 1)
            self.assertEqual(rows[0]['origin'], 'catalog+progression')
            self.assertEqual(rows[0]['main_id'], 'container/host')
            self.assertEqual(rows[0]['pair_id'], pair['pair_id'])
            self.mark(db, 'combination', sub_position='bottom-right')
            rows = db.execute('SELECT * FROM combination_entries ORDER BY kind').fetchall()
            self.assertEqual(len(rows), 2)
            self.assertEqual(rows[0]['kind'], 'container')
            self.assertEqual(rows[0]['progression_kind'], 'side')
            self.assertEqual(rows[1]['origin'], 'progression')
            self.mark(db, status='todo')
            self.assertEqual(db.execute('SELECT COUNT(*) FROM combination_entries').fetchone()[0], 1)

    def test_migration_retains_reviews_edits_archives_history_and_is_repeatable(self):
        legacy = Path(self.folder.name) / 'legacy.sqlite3'
        with connect(legacy) as db:
            pair = save_pair(db, 'side', dict(id='pair', concept='Example', position='br'), status='archived')
            save_pair(db, 'side', dict(pair['definition'], concept='Edited'), pair_id=pair['pair_id'], revision=1, status='archived')
        with connect(self.database) as db:
            db.execute('CREATE TABLE reviews (note TEXT)')
            db.execute("INSERT INTO reviews VALUES ('Keep my review')")
            first = migrate_legacy(db, legacy, self.database)
            self.assertEqual(first['copied']['pairs'], 1)
            self.assertEqual(first['copied']['pair_history'], 2)
            self.assertEqual(migrate_legacy(db, legacy, self.database)['copied']['pairs'], 0)
            self.assertEqual(db.execute('SELECT note FROM reviews').fetchone()[0], 'Keep my review')
            self.assertEqual(db.execute('SELECT status FROM pairs').fetchone()[0], 'archived')
            self.assertEqual(summary(db)['history_entries'], 2)
        self.assertTrue(legacy.exists())

    def test_conflicting_migration_does_not_replace_shared_data(self):
        legacy = Path(self.folder.name) / 'legacy.sqlite3'
        with connect(legacy) as db:
            pair = save_pair(db, 'container', dict(id='x', concept='Original'))
        with connect(self.database) as db:
            migrate_legacy(db, legacy, self.database)
            save_pair(db, 'container', dict(pair['definition'], concept='Shared edit'), pair_id=pair['pair_id'], revision=1)
        with self.assertRaisesRegex(ValueError, 'conflict'):
            with connect(self.database) as db:
                migrate_legacy(db, legacy, self.database)
        with connect(self.database) as db:
            self.assertEqual(db.execute('SELECT concept FROM pairs').fetchone()[0], 'Shared edit')


if __name__ == '__main__':
    unittest.main()
