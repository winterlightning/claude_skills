"""Distance/hole diagnostics, optional evidence, and release gating."""
from contextlib import redirect_stdout
import io
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

from icon_set.model.icons.registry import create
from icon_set.scripts import build as builder
from icon_set.validation import library_qa as qa


def circle_svg(radius):
    return ('<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32" '
            'fill="none" stroke="currentColor" stroke-width="4">'
            f'<circle cx="16" cy="16" r="{radius}"/></svg>')


def small_hole_icon():
    icon = create('square')
    icon.add_polyline('tiny', (14, 14), (18, 14), (18, 18), (14, 18), closed=True)
    return icon


class NegativeSpaceTests(unittest.TestCase):
    def test_large_hole_passes_and_small_hole_fails_at_native_stroke(self):
        for radius, expected in ((8, 'pass'), (2.5, 'fail')):
            with self.subTest(radius=radius):
                row = qa.measure_negative_space(circle_svg(radius), 32)
                self.assertEqual(row['status'], expected)
                self.assertEqual(row['hole_count'], 1)
                self.assertEqual(row['minimum_authored_diameter'], 2)
                self.assertAlmostEqual(row['holes'][0]['equivalent_diameter_at_authored_stroke_design_u'],
                                       2 * radius - 4, delta=0.4)

    def test_no_enclosed_hole_is_a_real_pass(self):
        row = qa.inspect_icon(create('plus'))
        self.assertEqual(row['negative_space']['status'], 'pass')
        self.assertEqual(row['negative_space']['hole_count'], 0)

    def test_hole_gate_catches_a_defect_the_vector_validator_cannot(self):
        icon = small_hole_icon()
        self.assertTrue(icon.validate_icon().ok)
        row = qa.inspect_icon(icon)
        self.assertEqual(row['status'], 'fail')
        self.assertGreater(row['negative_space']['failed_hole_count'], 0)

    def test_checker_failure_never_becomes_a_no_holes_pass(self):
        with patch.object(qa, 'measure_negative_space', side_effect=ImportError('cv2 unavailable')):
            row = qa.inspect_icon(create('square'))
        self.assertEqual(row['status'], 'error')
        self.assertEqual(row['negative_space']['status'], 'error')
        self.assertIn('cv2 unavailable', row['errors'][-1])

    def test_invalid_metadata_has_a_complete_error_row_without_a_render(self):
        icon = create('square')
        icon.profile = 'SUB32'
        row = qa.inspect_icon(icon)
        self.assertEqual(row['status'], 'fail')
        self.assertEqual(row['negative_space']['status'], 'not_run')
        self.assertNotIn('_svg', row)
        self.assertTrue(qa.artifact_key(icon).startswith('invalid/'))


class EvidenceBuildTests(unittest.TestCase):
    def setUp(self):
        self.temp = TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        self.addCleanup(patch.stopall)
        patch.object(builder, 'icons_in', return_value=[create('square')]).start()
        patch('icon_set.model.icons.registry.all_icons', return_value=[create('square')]).start()
        self.capture = io.StringIO()
        redirect = redirect_stdout(self.capture)
        redirect.__enter__()
        self.addCleanup(redirect.__exit__, None, None, None)

    def build(self, debug, report, folder='dist'):
        return builder.build(self.root / folder, None, write_png=False, only=['sub'], debug=debug, report=report)

    def test_all_four_switch_combinations(self):
        for debug in (False, True):
            for report in (False, True):
                with self.subTest(debug=debug, report=report):
                    folder = f'dist-{debug}-{report}'
                    self.assertEqual(self.build(debug, report, folder), 0)
                    output = self.root / folder / 'qa'
                    self.assertEqual((output / 'index.html').exists(), report)
                    self.assertEqual((output / 'sub/square/holes.png').exists(), debug)
                    self.assertEqual((output / 'sub/square/spacing.png').exists(), debug)
                    self.assertEqual((output / 'results.json').exists(), debug or report)
                    if debug or report:
                        result = json.loads((output / 'results.json').read_text())
                        row = result['icons'][0]
                        svg = (output / row['artifacts']['svg']).read_bytes()
                        self.assertEqual(qa._hash(svg), row['svg_sha256'])

    def test_disabling_debug_or_html_removes_stale_evidence_in_next_snapshot(self):
        self.assertEqual(self.build(True, True), 0)
        self.assertEqual(self.build(False, True), 0)
        self.assertFalse((self.root / 'dist/qa/sub/square/holes.png').exists())
        self.assertEqual(self.build(True, False), 0)
        self.assertFalse((self.root / 'dist/qa/index.html').exists())

    def test_failed_build_saves_current_debug_and_report_but_keeps_release(self):
        self.assertEqual(self.build(False, False), 0)
        before = (self.root / 'dist/sub32/square.svg').read_bytes()
        with patch.object(builder, 'icons_in', return_value=[small_hole_icon()]):
            self.assertEqual(self.build(True, True), 1)
        self.assertEqual((self.root / 'dist/sub32/square.svg').read_bytes(), before)
        result = json.loads((self.root / 'dist/qa/results.json').read_text())
        self.assertEqual(result['icons'][0]['status'], 'fail')
        self.assertTrue((self.root / 'dist/qa/sub/square/holes.png').exists())
        self.assertTrue((self.root / 'dist/qa/index.html').exists())

    def test_hole_validation_is_still_required_with_both_outputs_disabled(self):
        with patch.object(builder, 'icons_in', return_value=[small_hole_icon()]):
            self.assertEqual(self.build(False, False), 1)
        self.assertFalse((self.root / 'dist/sub32/manifest.json').exists())
        self.assertFalse((self.root / 'dist/qa').exists())

    def test_filtered_build_report_includes_other_families(self):
        with patch('icon_set.model.icons.registry.all_icons', return_value=[create('square'), create('smartwatch')]):
            self.assertEqual(self.build(False, True), 0)
        rows = json.loads((self.root / 'dist/qa/results.json').read_text())['icons']
        self.assertEqual(len(rows), 2)
        self.assertFalse(rows[1]['selected_for_build'])
        self.assertFalse((self.root / 'dist/solo48').exists())

    def test_evidence_write_failure_prevents_release(self):
        with patch.object(builder, 'save_evidence', side_effect=OSError('disk full')):
            with self.assertRaisesRegex(OSError, 'disk full'):
                self.build(False, True)
        self.assertFalse((self.root / 'dist/sub32/manifest.json').exists())

    def test_png_export_error_is_reported_and_remaining_icons_are_checked(self):
        with patch.object(builder, 'icons_in', return_value=[create('square'), create('plus')]), \
                patch.object(builder, 'render_png', side_effect=RuntimeError('preview unavailable')):
            code = builder.build(self.root / 'dist', self.root / 'png', write_png=True,
                                 only=['sub'], debug=False, report=True)
        self.assertEqual(code, 1)
        rows = json.loads((self.root / 'dist/qa/results.json').read_text())['icons']
        self.assertEqual(len(rows), 2)
        self.assertTrue(all(row['status'] == 'error' for row in rows))
        self.assertTrue(all('preview unavailable' in row['errors'][-1] for row in rows))
        self.assertFalse((self.root / 'dist/sub32/manifest.json').exists())


class SmallCircleExceptionTests(unittest.TestCase):
    def test_exact_four_and_six_unit_circles_pass_with_recorded_exceptions(self):
        for radius in (2, 3):
            with self.subTest(radius=radius):
                row = qa.measure_negative_space(circle_svg(radius), 32)
                self.assertEqual(row['status'], 'pass')
                self.assertEqual(row['exception_count'], 1)
                hole = row['holes'][0]
                self.assertEqual(hole['measured_status'], 'fail')
                self.assertEqual(hole['exception']['centerline_diameter'], radius * 2)

    def test_five_unit_circle_is_not_exempt(self):
        row = qa.measure_negative_space(circle_svg(2.5), 32)
        self.assertEqual(row['status'], 'fail')
        self.assertEqual(row['exception_count'], 0)

    def test_arc_authored_hierarchy_circles_pass(self):
        row = qa.inspect_icon(create('organizational-hierarchy-cube'))
        self.assertEqual(row['status'], 'pass')
        self.assertEqual(row['negative_space']['exception_count'], 3)

    def test_non_circular_small_holes_still_fail(self):
        row = qa.inspect_icon(small_hole_icon())
        self.assertEqual(row['status'], 'fail')
        self.assertEqual(row['negative_space']['exception_count'], 0)
        ellipse = circle_svg(3).replace('<circle cx="16" cy="16" r="3"/>',
                                        '<ellipse cx="16" cy="16" rx="3" ry="2"/>')
        self.assertEqual(qa.measure_negative_space(ellipse, 32)['status'], 'fail')

    def test_a_stroke_dividing_a_circle_does_not_exempt_its_fragments(self):
        document = circle_svg(3).replace('</svg>', '<path d="M13 16L19 16"/></svg>')
        row = qa.measure_negative_space(document, 32)
        self.assertEqual(row['status'], 'fail')
        self.assertEqual(row['exception_count'], 0)

    def test_exception_does_not_hide_other_holes_in_the_same_icon(self):
        document = circle_svg(3).replace('</svg>',
            '<path d="M3 3L7 3L7 7L3 7Z"/></svg>')
        row = qa.measure_negative_space(document, 32)
        self.assertEqual(row['status'], 'fail')
        self.assertEqual(row['exception_count'], 1)
        self.assertGreater(row['failed_hole_count'], 0)


class RasterConnectivityTests(unittest.TestCase):
    def test_airplane_has_two_holes_across_measurement_resolutions(self):
        icon = create('paper-airplane-message-send')
        rules = qa.negative_space_rules()
        for samples in (16, 32, 64):
            with self.subTest(samples=samples):
                with patch.object(qa, 'negative_space_rules', return_value={**rules, 'samples_per_unit': samples}):
                    row = qa.inspect_icon(icon)
                self.assertEqual(row['status'], 'pass', row['errors'])
                self.assertEqual(row['negative_space']['hole_count'], 2)
                self.assertEqual(row['negative_space']['failed_hole_count'], 0)

    def test_corner_connected_background_is_one_hole(self):
        import numpy as np
        from icon_set.validation.hole_geometry import enclosed_components
        ink = np.ones((7, 7), dtype=bool)
        ink[2:4, 2:4] = False
        ink[4, 4] = False
        labels, holes = enclosed_components(ink)
        self.assertEqual(len(holes), 1)
        self.assertEqual(labels[3, 3], labels[4, 4])

    def test_diagonal_connection_to_outside_is_not_an_enclosed_hole(self):
        import numpy as np
        from icon_set.validation.hole_geometry import enclosed_components
        ink = np.ones((5, 5), dtype=bool)
        ink[0, 0] = ink[1, 1] = ink[2, 2] = False
        self.assertEqual(enclosed_components(ink)[1], [])

    def test_truly_isolated_single_pixel_hole_is_not_discarded(self):
        import numpy as np
        from icon_set.validation.hole_geometry import enclosed_components
        ink = np.ones((5, 5), dtype=bool)
        ink[2, 2] = False
        self.assertEqual(len(enclosed_components(ink)[1]), 1)
