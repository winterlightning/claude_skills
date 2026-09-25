"""Each Combine all side pairs run replaces the previous set and feeds the Side combination 64 review family."""
import json
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

from icon_set.scripts import build_combination_previews
from icon_set.scripts.deploy import GalleryHandler, init_database
from icon_set.scripts.experiment_gallery import stage_side_combination64

SVG = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><path d="M2 2h{0}"/></svg>'


def row(pair_id, concept):
    return {'id': pair_id, 'concept': concept, 'position': 'br',
            'mains': [{'icon': 'main-' + pair_id, 'family': 'solo'}],
            'subs': [{'icon': 'sub-' + pair_id, 'family': 'sub'}]}


class SideCombination64Tests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name)
        self.gallery = self.root / 'dist/gallery'
        self.gallery.mkdir(parents=True)

    def write(self, name, data):
        (self.gallery / name).write_text(json.dumps(data))

    def test_manifest_lists_only_combined_icons_and_keeps_unchanged_dates(self):
        self.write('experiment-combination.json', {'rows': [row('a', 'alpha'), row('b', 'beta'), row('c', 'gamma')]})
        self.write('experiment-combination-results.json', {'results': {
            'a': {'url': 'combination-previews/a.svg', 'result': {'svg': SVG.format(1)}},
            'b': {'error': 'Does not fit', 'concept': 'beta'}}})
        self.assertEqual(stage_side_combination64(self.gallery), 1)
        first = json.loads((self.gallery / 'side-combination64.json').read_text())
        icon = first['icons'][0]
        self.assertEqual((first['count'], icon['key'], icon['family']), (1, 'side_combination64/a', 'side_combination64'))
        self.assertTrue(icon['preview_url'].startswith('combination-previews/a.svg?v='))
        stage_side_combination64(self.gallery)
        again = json.loads((self.gallery / 'side-combination64.json').read_text())['icons'][0]
        self.assertEqual(again['created_at'], icon['created_at'])
        self.assertEqual(again['svg_sha256'], icon['svg_sha256'])

    def test_build_replaces_previous_run_and_counts_combined_icons(self):
        data = self.root / 'icon_set/data'
        data.mkdir(parents=True)
        pairs = data / 'combination-pairs.json'
        self.write('experiments.json', {'combination': 99})
        self.write('experiment-combination.json', {'rows': []})
        render = lambda query, row: {'svg': SVG.format(len(row['id'])), 'placements': []}
        with patch.object(build_combination_previews, 'ROOT', self.root / 'icon_set'), \
             patch.object(build_combination_previews, 'DATA', pairs), \
             patch.object(build_combination_previews, 'render', render), \
             patch.object(build_combination_previews, '_engine', lambda: 'engine'), \
             patch.object(build_combination_previews, 'build_dist', lambda _: self.root / 'dist'), \
             patch.object(build_combination_previews.combination_layouts, 'load', lambda: {}):
            for rows in ([row('a', 'alpha'), row('bb', 'beta')], [row('a', 'alpha')]):
                pairs.write_text(json.dumps({'rows': rows}))
                self.write('experiment-combination.json', {'rows': rows})
                build_combination_previews.build()
        self.assertEqual(sorted(p.name for p in (self.gallery / 'combination-previews').glob('*.svg')), ['a.svg'])
        self.assertEqual(json.loads((self.gallery / 'experiments.json').read_text())['combination'], 1)
        self.assertEqual(json.loads((self.gallery / 'side-combination64.json').read_text())['count'], 1)

    def test_review_catalog_includes_side_combinations(self):
        self.write('icons.json', {'icons': [{'key': 'solo/x', 'svg_sha256': 's'}], 'failed_icons': []})
        self.write('side-combination64.json', {'count': 1, 'icons': [{'key': 'side_combination64/a', 'svg_sha256': 'c'}]})
        init_database(self.root / 'db.sqlite3')
        handler = GalleryHandler.__new__(GalleryHandler)
        handler.root, handler.database, handler.server = self.root / 'dist', self.root / 'db.sqlite3', SimpleNamespace()
        keys = [icon['key'] for icon in handler.catalog_data()['icons']]
        self.assertEqual(keys, ['solo/x', 'side_combination64/a'])


if __name__ == '__main__':
    unittest.main()
