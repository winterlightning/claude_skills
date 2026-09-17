"""Combination mains retain solo geometry but save and publish independently."""
import copy
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import types
import unittest
from unittest.mock import patch

from icon_set.model import contracts, metadata
from icon_set.model.icons import registry
from icon_set.model.icons.combination_main._base import CombinationMain48
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.scripts import build


class Probe(CombinationMain48):
    icon_id = 'combination-main-probe'

    def build(self):
        self.add_polyline('outline', (6, 6), (42, 6), (42, 42), (6, 42), closed=True)


class CombinationMainTests(unittest.TestCase):
    def test_geometry_contract_matches_solo(self):
        profiles = contracts.icon_profile()['profiles']
        expected = copy.deepcopy(profiles['SOLO48'])
        expected['family'] = 'combination_main'
        self.assertEqual(profiles['COMBINATION_MAIN48'], expected)
        for shape in Keyshape:
            if shape is not Keyshape.FREE:
                self.assertEqual(shape.bounds_for(Profile.COMBINATION_MAIN48),
                                 shape.bounds_for(Profile.SOLO48))
        report = Probe().validate_icon()
        self.assertEqual(report.status, 'valid', report.describe())
        self.assertFalse(report.warnings)

    def test_solo_module_cannot_be_saved_in_new_family(self):
        module = types.ModuleType('icon_set.model.icons.combination_main.stray')
        class Stray(Solo48):
            icon_id = 'stray'
        Stray.__module__ = module.__name__
        module.Stray = Stray
        with self.assertRaises(TypeError):
            registry._collect(module, 'combination_main', CombinationMain48,
                              registry.families(), {})

    def test_real_export_uses_separate_family_folder_and_metadata(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            icon = Probe()
            with patch.object(build, 'icons_in', return_value=[icon]), \
                 patch.object(build, 'factories', return_value={icon.icon_id: Probe}), \
                 patch.object(metadata, 'ROOT', root / 'metadata'):
                count, failed = build._stage_family(
                    'combination_main', root / 'dist', None, write_png=False,
                    published_dist=root / 'published', qa_rows=[], qa_dir=None,
                    debug=False, artwork_dir=root / 'artwork')
                self.assertEqual((count, failed), (1, 0))
                destination = root / 'dist/combination_main48'
                self.assertTrue((destination / f'{icon.icon_id}.svg').is_file())
                record = json.loads((destination / 'manifest.json').read_text())['icons'][0]
                self.assertEqual(record['family'], 'combination_main')
                self.assertEqual(record['profile'], 'COMBINATION_MAIN48')
                self.assertEqual(record['canvas_size'], 48)
                self.assertTrue(metadata.metadata_path(icon).is_file())
                self.assertFalse((root / 'dist/solo48').exists())
