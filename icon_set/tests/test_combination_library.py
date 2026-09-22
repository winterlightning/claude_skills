import copy
import json
from pathlib import Path
import sqlite3
from tempfile import TemporaryDirectory
import unittest

from icon_set.scripts.combination_library import (
    connect, export_definitions, get_pair, save_pair, seed, summary,
)


class CombinationLibraryTest(unittest.TestCase):
    def setUp(self):
        self.folder = TemporaryDirectory()
        self.addCleanup(self.folder.cleanup)
        self.path = Path(self.folder.name) / 'state/combinations.sqlite3'
        self.definitions = {
            'container': [dict(id='same-id', concept='Host star', main_id='host', sub_id=None,
                               review_note='Keep editorial notes', placement={'dx': 2})],
            'side': [dict(id='same-id', concept='Host plus', main_id='host', sub_id='plus', position='br')],
        }
        self.catalog = dict(rows=[dict(r, kind=k) for k, rows in self.definitions.items() for r in rows],
                            references={'host': {'concept': 'Host', 'generated': [{'key': 'container/host'}]},
                                        'star': {'concept': 'Star'}, 'plus': {'concept': 'Plus'}})
        self.catalog['rows'][0].update(sub_id='star', remappings=[dict(role='sub', reference_id='star')])

    def test_lossless_import_and_idempotence_across_reopen(self):
        with connect(self.path) as db:
            self.assertEqual(seed(db, self.definitions, self.catalog)['inserted'], 2)
            self.assertEqual(export_definitions(db), self.definitions)
            rows = db.execute('SELECT * FROM pairs ORDER BY kind').fetchall()
            self.assertNotEqual(rows[0]['pair_id'], rows[1]['pair_id'])
            self.assertEqual(rows[0]['sub_id'], 'star')
            ids = [r['pair_id'] for r in rows]
        with connect(self.path) as db:
            self.assertEqual(seed(db, self.definitions, self.catalog), dict(inserted=0, unchanged=2, conflicts=[]))
            self.assertEqual(summary(db)['history_entries'], 2)
            self.assertEqual([r[0] for r in db.execute('SELECT pair_id FROM pairs ORDER BY kind')], ids)
            self.assertEqual(db.execute('PRAGMA foreign_key_check').fetchall(), [])

    def test_edit_archive_conflicts_and_history(self):
        with connect(self.path) as db:
            seed(db, self.definitions, self.catalog)
            pair_id = db.execute("SELECT pair_id FROM pairs WHERE kind='container'").fetchone()[0]
            definition = dict(self.definitions['container'][0], concept='Updated name')
            saved = save_pair(db, 'container', definition, pair_id=pair_id, revision=1, status='archived', actor='reviewer')
            self.assertEqual(saved['revision'], 2)
            self.assertEqual(saved['sub_id'], 'star')
            self.assertEqual(export_definitions(db)['container'], [])
            self.assertEqual(export_definitions(db, True)['container'][0], definition)
            with self.assertRaisesRegex(ValueError, 'Revision conflict'):
                save_pair(db, 'container', definition, pair_id=pair_id, revision=1)
            seed(db, self.definitions, self.catalog)
            self.assertEqual(get_pair(db, pair_id)['status'], 'archived')
            changed_source = copy.deepcopy(self.definitions)
            changed_source['container'][0]['concept'] = 'Upstream edit'
            self.assertEqual(len(seed(db, changed_source, self.catalog)['conflicts']), 1)
            self.assertEqual(get_pair(db, pair_id)['definition']['concept'], 'Updated name')
            log = db.execute('SELECT actor,snapshot_json FROM pair_history WHERE pair_id=? ORDER BY revision', (pair_id,)).fetchall()
            self.assertEqual(log[1]['actor'], 'reviewer')
            self.assertEqual(json.loads(log[0]['snapshot_json'])['definition'], self.definitions['container'][0])

    def test_create_and_change_component_invalidates_resolution(self):
        with connect(self.path) as db:
            seed(db, self.definitions, self.catalog)
            original = db.execute("SELECT pair_id FROM pairs WHERE kind='side'").fetchone()[0]
            changed = dict(self.definitions['side'][0], sub_id='different')
            saved = save_pair(db, 'side', changed, pair_id=original, revision=1)
            self.assertEqual(saved['resolution'], {})
            self.assertEqual(saved['sub_id'], 'different')
            created = save_pair(db, 'side', dict(changed, id='new-id', position='tl'))
            self.assertEqual(created['definition']['position'], 'tl')
            self.assertIsNone(created['imported'])
            with self.assertRaises(sqlite3.IntegrityError):
                save_pair(db, 'side', dict(changed, id='new-id'))

    def test_stale_catalog_rolls_back_whole_import(self):
        self.catalog['rows'][1]['concept'] = 'Stale'
        with self.assertRaisesRegex(ValueError, 'stale'):
            with connect(self.path) as db:
                seed(db, self.definitions, self.catalog)
        with connect(self.path) as db:
            self.assertEqual(summary(db)['history_entries'], 0)
            self.assertEqual(db.execute('SELECT COUNT(*) FROM pairs').fetchone()[0], 0)

    def test_validation_and_explicit_selection(self):
        with connect(self.path) as db:
            for definition in (dict(id='x', concept='', main_id=None, sub_id=None, position='br'),
                               dict(id='x', concept='Pair', position='unknown'),
                               dict(id='x', concept='Pair', position='br', main_id='container/x',
                                    sub_id='symbol/y', main_key='container/wrong', component_selection='explicit')):
                with self.assertRaises(ValueError):
                    save_pair(db, 'side', definition)
            definition = dict(id='exact', concept='Exact', main_id='container/x', sub_id='symbol/y',
                              main_key='container/x', sub_key='symbol/y', component_selection='explicit')
            result = save_pair(db, 'container', definition)
            self.assertEqual(result['definition'], definition)


if __name__ == '__main__':
    unittest.main()
