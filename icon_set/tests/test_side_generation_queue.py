"""Side-component generation queue and its positional CLI."""
import contextlib
import io
import json
import sqlite3
import tempfile
import unittest
from pathlib import Path

from icon_set.scripts import side_generation_queue
from icon_set.scripts.side_component_queue import generation_queue


class SideComponentQueueTests(unittest.TestCase):
    def fixture(self):
        references = {
            'pair-a': {'generated': []}, 'pair-b': {'generated': []},
            'main-alias': {'canonical_id': 'main', 'concept': 'Monitor', 'reference_url': 'main.svg', 'generated': []},
            'main': {'concept': 'Monitor', 'reference_url': 'main.svg', 'generated': []},
            'sub': {'concept': 'ABC label', 'reference_url': 'sub.svg', 'generated': []},
            'done': {'concept': 'Check', 'reference_url': 'done.svg', 'generated': [{'icon_id': 'check'}]},
        }
        rows = [
            {'id': 'pair-a', 'kind': 'side', 'concept': 'Monitor label', 'main_id': 'main-alias', 'sub_id': 'sub'},
            {'id': 'pair-b', 'kind': 'side', 'concept': 'Monitor check', 'main_id': 'main', 'sub_id': 'done'},
        ]
        combinations = {'references': references, 'rows': rows}
        primitives = {'root_label': 'pictographic-primitives', 'rows': [
            {'uuid': 'main', 'concept': 'Monitor', 'path': 'computers/monitor.svg', 'category': 'computers'},
            {'uuid': 'sub', 'concept': 'ABC label', 'path': 'text/abc.svg', 'category': 'text'},
        ]}
        return combinations, primitives

    def test_deduplicates_aliases_excludes_generated_and_marked_text(self):
        combinations, primitives = self.fixture()
        result = generation_queue(combinations, primitives, {'sub': {'reason': 'text_number'}},
                                  role='all', limit=10, offset=0)
        self.assertEqual(result['total'], 1)
        self.assertEqual(result['marked_text_requirements'], 1)
        self.assertEqual(result['missing_by_role'], {'main': 1, 'sub': 0})
        self.assertEqual(result['marked_text_by_role'], {'main': 0, 'sub': 1})
        self.assertEqual(result['briefs'][0]['uuid'], 'main')
        self.assertEqual(result['briefs'][0]['role'], 'main')
        self.assertEqual(result['briefs'][0]['combination_count'], 2)
        self.assertIn('icon-solo-distilled', result['briefs'][0]['brief'])

    def test_role_and_pagination(self):
        combinations, primitives = self.fixture()
        result = generation_queue(combinations, primitives, {}, role='sub', limit=1, offset=0)
        self.assertEqual((result['total'], result['next_offset']), (1, None))
        self.assertEqual(result['briefs'][0]['skill'], 'icon-sub')

    def test_cli_accepts_limit_then_offset(self):
        combinations, primitives = self.fixture()
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / 'gallery').mkdir()
            (root / 'gallery/combinations.json').write_text(json.dumps(combinations))
            (root / 'gallery/primitives.json').write_text(json.dumps(primitives))
            database = root / 'review.sqlite3'
            with sqlite3.connect(database) as connection:
                connection.execute('CREATE TABLE primitive_status (uuid TEXT PRIMARY KEY, status TEXT, reason TEXT, note TEXT, updated_by TEXT, updated_at TEXT, main_brief TEXT, sub_brief TEXT, sub_position TEXT)')
            with contextlib.redirect_stdout(io.StringIO()) as output:
                self.assertEqual(side_generation_queue.main(
                    ['1', '1', '--dist', str(root), '--database', str(database)]), 0)
            result = json.loads(output.getvalue())
            self.assertEqual((result['limit'], result['offset']), (1, 1))
            self.assertEqual(len(result['briefs']), 1)


if __name__ == '__main__':
    unittest.main()
