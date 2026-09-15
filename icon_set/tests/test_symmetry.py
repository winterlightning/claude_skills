"""Regressions for ink hiding asymmetric centerlines."""
from dataclasses import replace
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

from icon_set.model.icons.base import Icon
from icon_set.model.icons.solo.airmail_055d9bbb_508e_4991_84fd_c6c91f3a1a47 import Airmail
from icon_set.model.profiles import Profile
from icon_set.model.keyshapes import Keyshape
from icon_set.validation.symmetry import analyze


def fixture():
    return Icon('symmetry-fixture', Profile.SOLO48, semantic_role='MAIN', keyshape=Keyshape.SQUARE)


class SymmetryTests(unittest.TestCase):
    def test_airmail_ink_hides_nonmirrored_arcs(self):
        result = analyze(Airmail())
        vertical = result['axes'][0]
        self.assertGreater(vertical['ink_iou'], 0.999)
        self.assertEqual(result['status'], 'fail')
        self.assertEqual({m['element_id'] for m in vertical['mismatches']},
                         {'sym-e3', 'sym-e12-1', 'sym-e12-2'})
        self.assertGreater(vertical['max_sampled_distance'], 0.003)

    def test_airmail_with_matching_straight_edges_passes(self):
        from icon_set.model.primitives import Line
        icon = Airmail()
        drawing = icon.draw()
        repaired = replace(drawing, primitives=tuple(
            Line(p.element_id, p.start, p.end) if p.element_id.startswith('sym-e12-') else p
            for p in drawing.primitives))
        # Same fixture only: do not modify the real icon's source.
        icon.primitives = list(repaired.primitives)
        self.assertEqual(analyze(icon)['status'], 'pass')

    def test_split_reversed_lines_and_off_canvas_axis(self):
        icon = fixture()
        icon.add_line('left', (-4, 10), (-4, 30))
        icon.add_line('right-a', (12, 20), (12, 10))
        icon.add_line('right-b', (12, 30), (12, 20))
        result = analyze(icon)
        self.assertEqual(result['status'], 'pass')
        self.assertEqual(result['axes'][0]['coordinate'], 4)

    def test_circle_split_into_different_arc_lengths(self):
        icon = fixture()
        icon.add_arc('left', (24, 18), (24, 30), radius_x=6, sweep=False)
        icon.add_arc('right-top', (24, 18), (30, 24), radius_x=6)
        icon.add_arc('right-bottom', (30, 24), (24, 30), radius_x=6)
        self.assertEqual(analyze(icon)['status'], 'pass')

    def test_mirrored_cubic_curves(self):
        icon = fixture()
        icon.add_bezier('left', (20, 16), ((14, 18), (14, 28), (20, 30)))
        icon.add_bezier('right', (28, 16), ((34, 18), (34, 28), (28, 30)))
        self.assertEqual(analyze(icon)['status'], 'pass')

    def test_ellipse(self):
        icon = fixture()
        icon.add_arc('top', (18, 24), (30, 24), radius_x=6, radius_y=3)
        icon.add_arc('bottom', (30, 24), (18, 24), radius_x=6, radius_y=3)
        self.assertEqual(analyze(icon)['status'], 'pass')

    def test_symmetric_ink_does_not_hide_an_extra_centerline(self):
        icon = fixture()
        icon.add_line('upper', (10, 23), (38, 23))
        icon.add_line('lower', (10, 25), (38, 25))
        icon.add_dot('hidden', (15, 24))  # Entirely inside the two strokes' union.
        result = analyze(icon)
        self.assertGreater(result['axes'][0]['ink_iou'], 0.98)
        self.assertEqual(result['status'], 'fail')

    def test_intentionally_asymmetric_shape_is_not_applicable(self):
        icon = fixture()
        icon.add_polyline('shape', (8, 8), (8, 38), (39, 38), (26, 29))
        self.assertEqual(analyze(icon)['status'], 'not_applicable')

    def test_empty_geometry_is_error(self):
        with self.assertRaises(ValueError):
            analyze(fixture(), document='<svg xmlns="http://www.w3.org/2000/svg"/>')

    def test_build_qa_blocks_mismatch_and_records_rules(self):
        from icon_set.validation.library_qa import inspect_icon
        row = inspect_icon(Airmail())
        self.assertEqual(row['symmetry']['status'], 'fail')
        self.assertEqual(row['status'], 'fail')
        self.assertTrue(any(e.startswith('symmetry [sym-e12-1]') for e in row['errors']))
        self.assertIn('rules', row['symmetry'])
        self.assertIn('symmetry_rules_sha256', row)

    def test_missing_checker_never_passes(self):
        from icon_set.validation.library_qa import inspect_icon
        with patch('icon_set.validation.library_qa.analyze_symmetry', side_effect=ImportError('renderer missing')):
            row = inspect_icon(Airmail())
        self.assertEqual(row['status'], 'error')
        self.assertEqual(row['symmetry']['status'], 'error')

    def test_cli_saves_evidence_and_returns_failure(self):
        from icon_set.scripts.check_symmetry import main
        with TemporaryDirectory() as folder:
            self.assertEqual(main(['--icon', 'airmail', '--out', folder]), 1)
            report = json.loads((Path(folder)/'results.json').read_text())
            self.assertEqual(report['summary'], {'fail': 1})
            self.assertIn('sym-e12-1', (Path(folder)/'index.html').read_text())


if __name__ == '__main__':
    unittest.main()
