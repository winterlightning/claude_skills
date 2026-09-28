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
from icon_set.scripts.side_combination_approval import approved_pairs

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

    def test_class_stroke_styles_are_inlined_for_the_combiner(self):
        document = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48">'
                    '<defs><style>.line{fill:none;stroke:#000;stroke-width:4px}</style></defs>'
                    '<path class="line" d="M4 4L40 40"/></svg>')
        from icon_set.scripts.build_combination_previews import _inline_class_styles
        normalized = _inline_class_styles(document)
        self.assertIn('stroke="#000"', normalized)
        self.assertNotIn('<style>', normalized)
        from icon_set.scripts.combination_experiment import custom_item
        self.assertEqual(custom_item({'document': normalized}, 'main')['bounds'], [4.0, 4.0, 40.0, 40.0])

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

    def test_only_approved_main_and_sub_are_planned(self):
        rows = [row('a', 'alpha'), row('b', 'beta')]
        rows[0]['mains'].insert(0, {'icon': 'unapproved', 'family': 'solo'})
        catalog = {f'{item["family"]}/{item["icon"]}': {
            'svg_sha256': item['icon'], 'validation': {'status': 'valid'}}
            for pair in rows for group in ('mains', 'subs') for item in pair[group]}
        reviews = {'solo/main-a': 'approve', 'sub/sub-a': 'approve',
                   'solo/main-b': 'approve', 'sub/sub-b': 'pending'}
        self.assertEqual(approved_pairs(rows, catalog, reviews), {
            'a': {'main': {'icon': 'main-a', 'key': 'solo/main-a', 'svg_sha256': 'main-a'},
                  'sub': {'icon': 'sub-a', 'key': 'sub/sub-a', 'svg_sha256': 'sub-a'}}})

    def test_approved_plan_replaces_old_unapproved_preview(self):
        data = self.root / 'icon_set/data'
        data.mkdir(parents=True)
        pairs = data / 'combination-pairs.json'
        rows = [row('a', 'alpha'), row('b', 'beta')]
        for pair in rows:
            for group in ('mains', 'subs'):
                pair[group][0]['sha256'] = pair[group][0]['icon']
        pairs.write_text(json.dumps({'rows': rows}))
        self.write('experiment-combination.json', {'rows': rows})
        self.write('experiments.json', {'combination': 0})
        plan = {'a': {'main': {'icon': 'main-a', 'key': 'solo/main-a', 'svg_sha256': 'main-a'},
                      'sub': {'icon': 'sub-a', 'key': 'sub/sub-a', 'svg_sha256': 'sub-a'}}}
        render = lambda query, row: {'svg': SVG.format(len(row['id'])), 'placements': []}
        with patch.object(build_combination_previews, 'ROOT', self.root / 'icon_set'), \
             patch.object(build_combination_previews, 'DATA', pairs), \
             patch.object(build_combination_previews, 'render', render), \
             patch.object(build_combination_previews, '_engine', lambda: 'engine'), \
             patch.object(build_combination_previews, 'build_dist', lambda _: self.root / 'dist'), \
             patch.object(build_combination_previews.combination_layouts, 'load', lambda: {}):
            build_combination_previews.build()
            build_combination_previews.build(approved_plan=plan)
        self.assertEqual(sorted(p.name for p in (self.gallery / 'combination-previews').glob('*.svg')), ['a.svg'])
        self.assertEqual(json.loads((self.gallery / 'side-combination64.json').read_text())['count'], 1)

    def test_unmeasurable_approved_artwork_does_not_abort_other_pairs(self):
        data = self.root / 'icon_set/data'
        data.mkdir(parents=True)
        pairs = data / 'combination-pairs.json'
        rows = [row('a', 'alpha'), row('b', 'beta')]
        for pair in rows:
            for group in ('mains', 'subs'):
                pair[group][0]['sha256'] = pair[group][0]['icon']
        pairs.write_text(json.dumps({'rows': rows}))
        self.write('experiment-combination.json', {'rows': rows})
        self.write('experiments.json', {'combination': 0})
        plan = {pair['id']: {
            role: {'icon': pair[group][0]['icon'], 'key': pair[group][0]['family'] + '/' + pair[group][0]['icon'],
                   'svg_sha256': pair[group][0]['icon'], **({'document': '<svg/>'} if pair['id'] == 'b' else {})}
            for role, group in (('main', 'mains'), ('sub', 'subs'))} for pair in rows}
        with patch.object(build_combination_previews, 'ROOT', self.root / 'icon_set'), \
             patch.object(build_combination_previews, 'DATA', pairs), \
             patch.object(build_combination_previews, 'render', lambda query, row: {'svg': SVG.format(1), 'placements': []}), \
             patch.object(build_combination_previews, '_engine', lambda: 'engine'), \
             patch.object(build_combination_previews, 'build_dist', lambda _: self.root / 'dist'), \
             patch.object(build_combination_previews.combination_layouts, 'load', lambda: {}), \
             patch('icon_set.scripts.combination_experiment.custom_item', side_effect=ValueError('No supported stroke geometry.')):
            build_combination_previews.build(approved_plan=plan)
        self.assertEqual(json.loads((self.gallery / 'side-combination64.json').read_text())['count'], 1)
        failures = json.loads((data / 'combination-failures.json').read_text())
        self.assertIn('No supported stroke geometry', failures['b']['error'])

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
