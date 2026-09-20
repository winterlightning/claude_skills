import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

from icon_set.scripts.combination_catalog import write_catalog


class CombinationCatalogTest(unittest.TestCase):
    def test_explicit_component_keys_resolve_without_source_id_cross_product(self):
        with TemporaryDirectory() as folder:
            root = Path(folder)
            gallery = root / 'dist/gallery'
            gallery.mkdir(parents=True)
            pair = {'id': 'original', 'concept': 'Phone clock',
                    'main_id': 'container/phone', 'sub_id': 'symbol/hands',
                    'component_selection': 'explicit'}
            (root / 'combination_data.json').write_text(json.dumps({'container': [pair]}))
            host = {'icon_id': 'phone', 'key': 'container/phone', 'family': 'container',
                    'preview_url': '../container64/phone.svg'}
            child = {'icon_id': 'hands', 'key': 'symbol/hands', 'family': 'symbol',
                     'preview_url': '../symbol32/hands.svg'}
            primitives = {'rows': [{'uuid': 'original', 'generated': [child]}]}
            result = write_catalog(gallery, primitives, [host, child], root)
            row = result['rows'][0]
            self.assertEqual(row['main_generated'][0]['key'], host['key'])
            self.assertEqual(row['sub_generated'][0]['key'], child['key'])
            # A generated component from the same original is not a completed pair.
            self.assertEqual(row['generated'], [])
            self.assertEqual(result['references']['original']['generated'], [child])
            missing = write_catalog(gallery, primitives, [host], root)
            self.assertEqual(missing['rows'][0]['sub_generated'], [])
            self.assertEqual(missing['rows'][0]['generated'], [])

    def test_explicit_selection_survives_legacy_sub_aliases(self):
        with TemporaryDirectory() as folder:
            root = Path(folder)
            gallery = root / 'dist/gallery'
            gallery.mkdir(parents=True)
            config = root / 'icon_set/data'
            config.mkdir(parents=True)
            (config / 'combination-sub32.json').write_text('{"legacy": {}}')
            pair = {'id': 'pair', 'concept': 'Pair', 'main_id': 'container/host',
                    'sub_id': 'symbol/exact', 'component_selection': 'explicit'}
            (root / 'combination_data.json').write_text(json.dumps({'container': [pair]}))
            child = {'icon_id': 'exact', 'key': 'symbol/exact', 'preview_url': '../symbol32/exact.svg'}
            def remap(result, *_):
                result['rows'][0]['sub_generated'] = [{'key': 'sub/other'}]
                result['rows'][0]['sub_exports'] = [{'icon': 'other'}]
            with patch('icon_set.scripts.deduplicate_subs.canonical_map', return_value=({}, [])), \
                 patch('icon_set.scripts.deduplicate_subs.update_catalog', side_effect=remap):
                result = write_catalog(gallery, {'rows': []}, [child], root)
            self.assertEqual(result['rows'][0]['sub_generated'], [child])
            self.assertEqual(result['rows'][0]['sub_exports'], [])

    def test_container_main_mapping_is_role_scoped_and_used_for_compositions(self):
        with TemporaryDirectory() as folder:
            root = Path(folder)
            gallery = root / 'dist/gallery'
            gallery.mkdir(parents=True)
            config = root / 'icon_set/data'
            config.mkdir(parents=True)
            (config / 'container-main-icons.json').write_text(json.dumps({
                'mappings': {'main': {'icon_id': 'native-container'}}}))
            source = {'id': 'pair', 'concept': 'Pair', 'main_id': 'main', 'sub_id': 'sub'}
            (root / 'combination_data.json').write_text(json.dumps({
                'container': [source], 'side': [dict(source, id='side-pair')]}))
            solo = {'icon_id': 'old-solo', 'key': 'solo/old-solo', 'preview_url': '../solo48/old-solo.svg'}
            sub = {'icon_id': 'plus', 'key': 'sub/plus', 'preview_url': '../sub32/plus.svg'}
            native = {'icon_id': 'native-container', 'key': 'container/native-container',
                      'family': 'container', 'preview_url': '../container64/native-container.svg'}
            primitives = {'rows': [{'uuid': 'main', 'generated': [solo]}, {'uuid': 'sub', 'generated': [sub]}]}
            compositions = root / 'dist/compositions'
            compositions.mkdir()
            for host in ('old-solo', 'native-container'):
                (compositions / f'{host}.svg').write_text('<svg/>')
                (compositions / f'{host}.json').write_text(json.dumps({
                    'icon_id': host + '-plus', 'composition_class': 'CONTAINER_COMBINE',
                    'children': [{'icon_id': host}, {'icon_id': 'plus'}]}))
            result = write_catalog(gallery, primitives, [native], root)
            container, side = result['rows']
            self.assertEqual([g['key'] for g in container['main_generated']], ['container/native-container'])
            self.assertEqual([g['icon_id'] for g in container['generated']], ['native-container-plus'])
            self.assertNotIn('main_generated', side)
            self.assertEqual(result['references']['main']['generated'], [solo])
            # An unavailable or wrong-family target must never fall back to solo.
            for records in ([], [dict(native, family='solo', key='solo/native-container')]):
                result = write_catalog(gallery, primitives, records, root)
                self.assertEqual(result['rows'][0]['main_generated'], [])
                self.assertEqual(result['rows'][0]['generated'], [])

    def test_unmapped_container_main_filters_solo_artwork(self):
        with TemporaryDirectory() as folder:
            root = Path(folder)
            gallery = root / 'dist/gallery'
            gallery.mkdir(parents=True)
            (root / 'combination_data.json').write_text(json.dumps({'container': [
                {'id': 'pair', 'concept': 'Pair', 'main_id': 'main', 'sub_id': 'sub'}]}))
            solo = {'icon_id': 'solo', 'key': 'solo/solo', 'preview_url': '../solo48/solo.svg'}
            native = {'icon_id': 'native', 'key': 'container/native', 'preview_url': '../container64/native.svg'}
            result = write_catalog(gallery, {'rows': [{'uuid': 'main', 'generated': [solo, native]}]}, [], root)
            self.assertEqual(result['rows'][0]['main_generated'], [native])

    def test_reviewed_remap_preserves_known_ids_and_original_input(self):
        with TemporaryDirectory() as folder:
            root = Path(folder)
            gallery = root / 'dist/gallery'
            gallery.mkdir(parents=True)
            config = root / 'icon_set/data'
            config.mkdir(parents=True)
            uid = 'aaaaaaaa-1111-2222-3333-bbbbbbbbbbbb'
            (config / 'combination-remaps.json').write_text(json.dumps({'rules': [
                {'role': 'sub', 'fragment': uid[19:34], 'reference_id': 'existing', 'reason': 'Reviewed shape'}]}))
            data = {'container': [{'id': uid, 'concept': 'Test', 'main_id': 'main', 'sub_id': None},
                                  {'id': uid, 'concept': 'Known', 'main_id': 'main', 'sub_id': 'known'}]}
            source = root / 'combination_data.json'
            source.write_text(json.dumps(data))
            result = write_catalog(gallery, {'rows': [{'uuid': 'existing', 'concept': 'Existing', 'generated': []}]}, [], root)
            self.assertEqual(result['rows'][0]['sub_id'], 'existing')
            self.assertIsNone(result['rows'][0]['remappings'][0]['original_id'])
            self.assertEqual(result['rows'][1]['sub_id'], 'known')
            self.assertEqual(json.loads(source.read_text()), data)

    def test_exact_identity_missing_sources_and_completed_pair(self):
        with TemporaryDirectory() as folder:
            root = Path(folder)
            gallery = root / 'dist/gallery'
            gallery.mkdir(parents=True)
            sources = root / 'pictographic-combinations'
            sources.mkdir()
            uid = 'aaaaaaaa-1111-2222-3333-bbbbbbbbbbbb'
            (sources / f'reference_{uid}.svg').write_text('<svg/>')
            (root / 'combination_data.json').write_text(json.dumps({'container': [
                {'id': uid, 'concept': 'Example', 'main_id': 'main', 'sub_id': 'sub'},
                {'id': 'missing', 'concept': 'Unknown', 'main_id': None, 'sub_id': 'sub'}]}))
            primitives = {'rows': [
                {'uuid': 'main', 'concept': 'Main', 'generated': [{'icon_id': 'main-icon', 'key': 'container/main-icon', 'preview_url': '../container64/main-icon.svg'}]},
                {'uuid': 'sub', 'concept': 'Sub', 'generated': [{'icon_id': 'sub-icon', 'key': 'sub/sub-icon', 'preview_url': '../sub32/sub-icon.svg'}]}]}
            compositions = root / 'dist/compositions'
            compositions.mkdir()
            (compositions / 'pair.svg').write_text('<svg/>')
            (compositions / 'pair.json').write_text(json.dumps({'icon_id': 'pair', 'composition_class': 'CONTAINER_COMBINE', 'children': [{'icon_id': 'main-icon'}, {'icon_id': 'sub-icon'}]}))
            result = write_catalog(gallery, primitives, [], root)
            self.assertEqual(len(result['rows']), 2)
            self.assertEqual(result['rows'][0]['generated'][0]['icon_id'], 'pair')
            self.assertEqual(result['rows'][1]['generated'], [])
            self.assertIsNone(result['references'][None]['reference_url'])
            self.assertEqual((gallery / result['references'][uid]['reference_url']).read_text(), '<svg/>')
            self.assertEqual(json.loads((gallery / 'combinations.json').read_text())['references']['null']['concept'], 'Unspecified component')


if __name__ == '__main__':
    unittest.main()
