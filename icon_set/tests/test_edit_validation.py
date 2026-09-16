"""The editor runs the real release checks without importing authored icon modules."""
from copy import deepcopy
import tempfile
import unittest
from pathlib import Path

from icon_set.model.icons.base import Icon
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.scripts.stroke_edits import StrokeEditStore, EditConflict, effective_validation_status


def portrait():
    icon = Icon('editor-experiment', Profile.SOLO48, semantic_role='MAIN', keyshape=Keyshape.VRECT_L)
    icon.family = 'solo'
    icon.semantic_kind = 'noun'
    icon.add_polyline('outline', (8, 4), (40, 4), (40, 44), (8, 44), closed=True)
    return icon.to_record() | {'key': 'solo/editor-experiment', 'svg_sha256': 'fixture'}


class EditValidationTests(unittest.TestCase):
    def test_human_override_is_attributed_and_bound_to_exact_geometry(self):
        with tempfile.TemporaryDirectory() as folder:
            store, icon = StrokeEditStore(folder), portrait()
            data = {'svg_sha256': 'fixture', 'revision': 0, 'offsets': {}, 'keyshape': 'VRECT_M'}
            for invalid in ({}, {'reason': '  '}, {'reason': 'x'*2001}, True):
                with self.assertRaises(ValueError):
                    store.save(icon, data | {'validation_override': invalid}, 'jakes')
            saved = store.save(icon, data | {'validation_override': {
                'reason': ' Intentional proportions, visually reviewed. ', 'reviewed_by': 'spoof'}}, 'jakes')
            self.assertEqual(saved['validation']['status'], 'fail')
            self.assertTrue(saved['validation']['errors'])
            self.assertEqual(saved['effective_validation_status'], 'pass')
            self.assertEqual(effective_validation_status(saved), 'pass')
            self.assertEqual(saved['validation_override']['reviewed_by'], 'jakes')
            self.assertEqual(saved['validation_override']['reason'], 'Intentional proportions, visually reviewed.')
            self.assertEqual(store.get(icon['key'], 'fixture'), saved)
            changed = deepcopy(saved)
            changed['edited_graph']['primitives'][0]['start'][0] += 1
            self.assertEqual(effective_validation_status(changed), 'not-run')
            changed = deepcopy(saved)
            changed['source_svg_sha256'] = 'new-source'
            self.assertEqual(effective_validation_status(changed), 'fail')
            # Legacy clients preserve the decision only on identical geometry.
            same = store.save(icon, data | {'revision': 1}, 'other')
            self.assertEqual(same['validation_override'], saved['validation_override'])
            removed = store.save(icon, data | {'revision': 2, 'validation_override': None, 'validate': True}, 'jakes')
            self.assertIsNone(removed['validation_override'])
            self.assertEqual(removed['effective_validation_status'], 'fail')
            store.save(icon, data | {'revision': 3, 'validation_override': {'reason': 'Reviewed'}}, 'jakes')
            moved = store.save(icon, data | {'revision': 4, 'offsets': {'contour:outline': [1, 0]}}, 'jakes')
            self.assertIsNone(moved['validation_override'])
            self.assertEqual(moved['effective_validation_status'], 'not-run')

    def test_guitar_circle_size_uses_path_units_and_keeps_spacing_separate(self):
        from icon_set.model.icons.solo.acoustic_guitar_2e3b9013_429e_4cb3_8093_1e76dd0f5307 import AcousticGuitar
        icon = AcousticGuitar().to_record() | {'key': 'solo/acoustic-guitar', 'svg_sha256': 'fixture'}
        with tempfile.TemporaryDirectory() as folder:
            store = StrokeEditStore(folder)
            for path_diameter, hole_status in ((2, 'fail'), (4, 'pass'), (6, 'pass')):
                scale = path_diameter / 6
                data = {'svg_sha256': 'fixture', 'keyshape': 'VRECT_M',
                        'offsets': {'contour:sound-hole': [0, 6*(1-scale)]},
                        'scales': {'contour:body': [.875, 1], 'primitive:neck': [.875, 1],
                                   'primitive:peg': [.875, 1], 'contour:sound-hole': [scale, scale]}}
                report = store.validate(icon, data)
                circle = next(c for c in report['circles'] if c['element_id'] == 'sound-hole')
                self.assertEqual(circle['path_diameter'], path_diameter)
                self.assertEqual(circle['visible_diameter'], path_diameter + 4)
                self.assertEqual(circle['approved_visible_diameters'], [8, 10])
                self.assertEqual(circle['exception_applied'], path_diameter in (4, 6))
                self.assertEqual(report['checks']['negative_space'], hole_status)
                if path_diameter in (4, 6):
                    self.assertTrue(any(e.startswith('mic ') for e in report['errors']))
                    self.assertFalse(any(e.startswith('holes/pinches:') for e in report['errors']))

    def test_change_keyshape_fail_then_resize_pass_and_persist(self):
        with tempfile.TemporaryDirectory() as folder:
            store = StrokeEditStore(Path(folder) / 'edits')
            icon = portrait()
            original = deepcopy(icon)
            data = {'svg_sha256': 'fixture', 'revision': 0, 'offsets': {}}
            self.assertEqual(store.validate(icon, data)['status'], 'pass')
            data['keyshape'] = 'VRECT_M'
            failed = store.validate(icon, data)
            self.assertEqual(failed['status'], 'fail')
            self.assertTrue(any('VRECT_M envelope' in e for e in failed['errors']))
            self.assertFalse(store.root.exists(), 'Checking must not save edits')
            data['scales'] = {'contour:outline': [.875, 1]}
            passed = store.validate(icon, data)
            self.assertEqual(passed['status'], 'pass', passed)
            self.assertEqual(passed['keyshape_bounds'], [8, 2, 40, 46])
            self.assertIn('symmetry', passed['checks_run'])
            self.assertEqual(passed['checks']['negative_space'], 'pass')
            saved = store.save(icon, data | {'validate': True}, 'jakes')
            self.assertEqual(saved['keyshape'], 'VRECT_M')
            self.assertEqual(saved['validation']['graph_sha256'], passed['graph_sha256'])
            self.assertEqual(saved['validation']['status'], 'pass')
            self.assertEqual(saved['original_graph']['keyshape'], 'VRECT_L')
            self.assertEqual(saved['edited_graph']['keyshape'], 'VRECT_M')
            self.assertEqual(store.get(icon['key'], 'fixture'), saved)
            self.assertEqual(icon, original)
            # Older clients must not erase a stored keyshape experiment.
            legacy = store.save(icon, {'svg_sha256': 'fixture', 'revision': 1, 'offsets': {}}, 'jakes')
            self.assertEqual(legacy['keyshape'], 'VRECT_M')
            self.assertEqual(legacy['validation']['status'], 'not-run')

    def test_fractional_grid_and_invalid_or_stale_requests(self):
        with tempfile.TemporaryDirectory() as folder:
            store, icon = StrokeEditStore(folder), portrait()
            data = {'svg_sha256': 'fixture', 'offsets': {'contour:outline': [.5, 0]}}
            result = store.validate(icon, data)
            self.assertEqual(result['status'], 'fail')
            self.assertTrue(any('integer on grid' in e for e in result['errors']))
            for name in ('VRECT_XS', 'FREE', 'not-a-shape', 123):
                with self.subTest(name=name), self.assertRaises(ValueError):
                    store.validate(icon, data | {'keyshape': name})
            with self.assertRaises(EditConflict):
                store.validate(icon, data | {'svg_sha256': 'old'})
