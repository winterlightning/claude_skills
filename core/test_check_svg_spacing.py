"""Regressions for independent SVG stroke-component clearance checks.

Distances are measured along the actual segments, including separate M
subpaths in one element. Paint touching must not hide a centerline gap.
"""

import json
import math
import os
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

import icon_profiles
import check_svg_spacing as gate


SCRIPT = Path(__file__).with_name("check_svg_spacing.py")


def drawing(body=None, *, canvas=48, stroke=4):
    if body is None:
        body = '<path d="M6 10H42 M6 18H42"/>'
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{canvas}" height="{canvas}" '
        f'viewBox="0 0 {canvas} {canvas}" fill="none" stroke="currentColor" '
        f'stroke-width="{stroke}" stroke-linecap="round" stroke-linejoin="round">'
        f'{body}</svg>'
    )


def parallel_lines(distance):
    return drawing(f'<line x1="6" y1="10" x2="42" y2="10"/>'
                   f'<line x1="6" y1="{10 + distance}" x2="42" y2="{10 + distance}"/>')


class StrokeSpacingTests(unittest.TestCase):
    def check(self, body=None, **kwargs):
        return gate.check_drawing(drawing(body), **kwargs)

    def assertPass(self, result):
        self.assertTrue(result["ok"], result)
        self.assertEqual(result["status"], "pass")
        self.assertEqual(result["errors"], [])

    def assertNotPass(self, result):
        self.assertFalse(result["ok"], result)
        self.assertNotEqual(result["status"], "pass")
        self.assertTrue(result["errors"], result)

    def onePair(self, result):
        self.assertEqual(len(result["pairs"]), 1, result)
        return result["pairs"][0]

    def assertDistance(self, pair, expected, *, delta=1e-6):
        self.assertAlmostEqual(pair["centerlineDistance"], expected, delta=delta)
        self.assertAlmostEqual(pair["inkClearance"], max(0, expected - 4), delta=delta)
        self.assertAlmostEqual(pair["signedInkClearance"], expected - 4, delta=delta)
        self.assertLessEqual(pair["lowerBound"], expected + delta)
        self.assertGreaterEqual(pair["upperBound"], expected - delta)

    def test_exact_eight_centerline_four_ink_passes(self):
        result = gate.check_drawing(parallel_lines(8))
        self.assertPass(result)
        self.assertEqual(result["requiredCenterline"], 8)
        self.assertEqual(result["requiredInkClearance"], 4)
        self.assertEqual(len(result["contours"]), 2)
        self.assertEqual(len(result["components"]), 2)
        pair = self.onePair(result)
        self.assertEqual(pair["status"], "pass")
        self.assertEqual(pair["requiredCenterline"], 8)
        self.assertDistance(pair, 8)

    def test_distance_below_eight_fails_without_rounding_up(self):
        for distance in (7.99, 7.5, 4, 2, .01):
            with self.subTest(distance=distance):
                result = gate.check_drawing(parallel_lines(distance))
                self.assertNotPass(result)
                self.assertEqual(len(result["components"]), 2)
                self.assertDistance(self.onePair(result), distance)

    def test_distance_above_eight_passes(self):
        for distance in (8.01, 12, 24):
            with self.subTest(distance=distance):
                result = gate.check_drawing(parallel_lines(distance))
                self.assertPass(result)
                self.assertDistance(self.onePair(result), distance)

    def test_nearest_point_can_be_inside_a_segment_not_an_endpoint(self):
        result = self.check('<path d="M6 10H42"/><path d="M24 18V36"/>')
        self.assertPass(result)
        pair = self.onePair(result)
        self.assertDistance(pair, 8)
        points = pair["nearestPoints"]
        self.assertEqual(len(points), 2)
        self.assertEqual({tuple(round(value, 6) for value in point) for point in points},
                         {(24, 10), (24, 18)})
        self.assertEqual(len(pair["closestContours"]), 2)

    def test_nearest_interior_point_violation_is_not_missed(self):
        result = self.check('<path d="M6 10H42"/><path d="M24 17V36"/>')
        self.assertNotPass(result)
        self.assertDistance(self.onePair(result), 7)

    def test_diagonal_endpoint_caps_use_euclidean_distance(self):
        result = self.check('<path d="M6 6L18 18 M24 24L36 36"/>')
        self.assertPass(result)
        self.assertDistance(self.onePair(result), math.sqrt(72))
        result = self.check('<path d="M6 6L18 18 M23 23L36 36"/>')
        self.assertNotPass(result)
        self.assertDistance(self.onePair(result), math.sqrt(50))

    def test_tiny_positive_gap_does_not_underflow_or_hang_distance_refinement(self):
        # Squaring 1e-200 as a float becomes zero. Keep this in a bounded child
        # process so a regression in exact-distance root refinement cannot hang
        # the entire suite or silently turn separate centerlines into a join.
        source = drawing('<line x1="0" y1="0" x2="0" y2="0"/>'
                         '<line x1="1e-200" y1="0" x2="1e-200" y2="0"/>')
        code = ("import json, sys; import check_svg_spacing as gate; "
                "print(json.dumps(gate.check_drawing(sys.argv[1]), allow_nan=False))")
        process = subprocess.run([sys.executable, "-B", "-c", code, source],
                                 cwd=SCRIPT.parent, text=True, capture_output=True, timeout=5)
        self.assertEqual(process.returncode, 0, process.stdout + process.stderr)
        result = json.loads(process.stdout)
        self.assertNotPass(result)
        self.assertEqual(len(result["components"]), 2)
        distance = self.onePair(result)["centerlineDistance"]
        self.assertTrue(math.isfinite(distance))
        self.assertGreater(distance, 0)
        self.assertAlmostEqual(distance / 1e-200, 1, delta=1e-12)

    def test_separate_move_subpaths_are_detected_inside_one_path(self):
        for body in ('<path d="M6 10H42 M6 18H42"/>',
                     '<path d="m6 10h36 m-36 8h36"/>'):
            with self.subTest(body=body):
                result = self.check(body)
                self.assertPass(result)
                self.assertEqual(len(result["contours"]), 2)
                self.assertEqual(len(result["components"]), 2)
                self.assertDistance(self.onePair(result), 8)

    def test_all_independent_component_pairs_are_checked(self):
        result = self.check('<path d="M6 8H42 M6 16H42 M6 24H42"/>')
        self.assertPass(result)
        self.assertEqual(len(result["contours"]), 3)
        self.assertEqual(len(result["components"]), 3)
        self.assertEqual(len(result["pairs"]), 3)
        self.assertEqual(sorted(pair["centerlineDistance"] for pair in result["pairs"]), [8, 8, 16])

    def test_shared_endpoints_form_one_component(self):
        for body in ('<path d="M8 8H24"/><path d="M24 8V24"/>',
                     '<path d="M8 8H24 M24 8V24"/>'):
            with self.subTest(body=body):
                result = self.check(body)
                self.assertPass(result)
                self.assertEqual(len(result["contours"]), 2)
                self.assertEqual(len(result["components"]), 1)
                self.assertEqual(result["pairs"], [])

    def test_true_centerline_crossings_form_one_component(self):
        result = self.check('<path d="M8 24H40"/><path d="M24 8V40"/>')
        self.assertPass(result)
        self.assertEqual(len(result["components"]), 1)
        self.assertEqual(result["pairs"], [])

    def test_collinear_overlapping_centerlines_form_one_component(self):
        result = self.check('<path d="M8 24H28"/><path d="M20 24H40"/>')
        self.assertPass(result)
        self.assertEqual(len(result["contours"]), 2)
        self.assertEqual(len(result["components"]), 1)
        self.assertEqual(result["pairs"], [])

    def test_transitive_centerline_connections_form_one_component(self):
        result = self.check('<path d="M8 8H24"/><path d="M24 8V24"/>'
                            '<path d="M24 24H40"/>')
        self.assertPass(result)
        self.assertEqual(len(result["contours"]), 3)
        self.assertEqual(len(result["components"]), 1)
        self.assertEqual(result["pairs"], [])

    def test_component_distance_uses_its_closest_member_contour(self):
        result = self.check('<path d="M8 8H24"/><path d="M24 8V24"/>'
                            '<path d="M32 20V36"/>')
        self.assertPass(result)
        self.assertEqual(len(result["contours"]), 3)
        self.assertEqual(len(result["components"]), 2)
        self.assertDistance(self.onePair(result), 8)

    def test_continuous_outlines_are_not_compared_against_themselves(self):
        for body in ('<rect x="6" y="6" width="36" height="36"/>',
                     '<path d="M6 6H42V42H6Z"/>',
                     '<polygon points="6 6 42 6 24 42"/>',
                     '<polyline points="8 8 24 8 24 24"/>'):
            with self.subTest(body=body):
                result = self.check(body)
                self.assertPass(result)
                self.assertEqual(len(result["components"]), 1)
                self.assertEqual(result["pairs"], [])

    def test_disconnected_detail_inside_outline_is_checked(self):
        result = self.check('<rect x="6" y="6" width="36" height="36"/>'
                            '<line x1="18" y1="24" x2="30" y2="24"/>')
        self.assertPass(result)
        self.assertDistance(self.onePair(result), 12)
        result = self.check('<rect x="6" y="6" width="36" height="36"/>'
                            '<line x1="12" y1="24" x2="30" y2="24"/>')
        self.assertNotPass(result)
        self.assertDistance(self.onePair(result), 6)

    def test_ink_contact_or_overlap_does_not_merge_separated_centerlines(self):
        for distance in (4, 3):
            with self.subTest(distance=distance):
                result = gate.check_drawing(parallel_lines(distance))
                self.assertNotPass(result)
                self.assertEqual(len(result["components"]), 2)
                self.assertDistance(self.onePair(result), distance)

    def test_explicit_zero_length_round_capped_strokes_are_dots(self):
        result = self.check('<line x1="12" y1="12" x2="12" y2="12"/>'
                            '<path d="M20 12L20 12"/>')
        self.assertPass(result)
        self.assertEqual(len(result["components"]), 2)
        self.assertDistance(self.onePair(result), 8)

    def test_dot_on_another_centerline_is_a_connected_component(self):
        result = self.check('<line x1="24" y1="12" x2="24" y2="12"/>'
                            '<path d="M8 12H40"/>')
        self.assertPass(result)
        self.assertEqual(len(result["components"]), 1)
        self.assertEqual(result["pairs"], [])

    def test_quadratic_interior_minimum_is_measured(self):
        curve = '<path d="M8 22Q24 6 40 22"/>'
        result = self.check(curve + '<path d="M6 4H42"/>')
        self.assertPass(result)
        self.assertDistance(self.onePair(result), 10, delta=.01)
        result = self.check(curve + '<path d="M6 8H42"/>')
        self.assertNotPass(result)
        self.assertDistance(self.onePair(result), 6, delta=.01)

    def test_cubic_interior_minimum_is_measured(self):
        curve = '<path d="M8 24C8 8 40 8 40 24"/>'
        result = self.check(curve + '<path d="M6 3H42"/>')
        self.assertPass(result)
        self.assertDistance(self.onePair(result), 9, delta=.01)
        result = self.check(curve + '<path d="M6 6H42"/>')
        self.assertNotPass(result)
        self.assertDistance(self.onePair(result), 6, delta=.01)

    def test_relative_and_smooth_curve_commands_are_supported(self):
        result = self.check('<path d="m8 20q4 -4 8 0t8 0c2 0 2 4 4 4s2 -4 4 -4"/>')
        self.assertPass(result)
        self.assertEqual(len(result["components"]), 1)

    def test_native_circle_ellipse_and_two_arc_circle_are_measured(self):
        first_shapes = (
            '<circle cx="12" cy="24" r="6"/>',
            '<ellipse cx="12" cy="24" rx="6" ry="4"/>',
            '<path d="M18 24A6 6 0 1 0 6 24A6 6 0 1 0 18 24Z"/>',
        )
        for first in first_shapes:
            with self.subTest(first=first):
                result = self.check(first + '<circle cx="36" cy="24" r="6"/>')
                self.assertPass(result)
                self.assertEqual(len(result["components"]), 2)
                self.assertDistance(self.onePair(result), 12, delta=.01)
                result = self.check(first + '<circle cx="30" cy="24" r="6"/>')
                self.assertNotPass(result)
                self.assertDistance(self.onePair(result), 6, delta=.01)

    def test_ambiguous_curve_contact_cannot_silently_grant_pass(self):
        # The Q reaches y=16 at its interior midpoint, tangent to the line.
        # It must not be silently joined based only on approximate polylines.
        result = self.check('<path d="M8 24Q24 8 40 24"/><path d="M6 16H42"/>')
        self.assertNotPass(result)

    def test_sub_and_container_keep_their_own_profile_thresholds(self):
        for icon_type, canvas, required in (("sub", 32, 3), ("container", 64, 4)):
            with self.subTest(icon_type=icon_type):
                source = drawing(f'<path d="M6 6H26 M6 {6 + required}H26"/>', canvas=canvas)
                result = gate.check_drawing(source, icon_type=icon_type)
                self.assertPass(result)
                self.assertEqual(result["requiredCenterline"], required)
                self.assertEqual(result["requiredInkClearance"], max(0, required - 4))

    def test_profile_json_threshold_changes_the_verdict(self):
        source = icon_profiles.source_document()
        source["profiles"]["normal"].setdefault("validation", {})["minimumDistinctCenterlineDistance"] = 10
        with patch.object(icon_profiles, "_PROFILES", icon_profiles.resolve_profiles(source)):
            result = gate.check_drawing(parallel_lines(9))
            self.assertNotPass(result)
            self.assertEqual(result["requiredCenterline"], 10)
            self.assertEqual(result["requiredInkClearance"], 6)

    def test_native_canvas_and_configured_stroke_are_required(self):
        source = drawing()
        changes = (
            ('width="48"', 'width="24"'),
            ('height="48"', 'height="24"'),
            ('width="48" ', ''),
            ('height="48" ', ''),
            ('viewBox="0 0 48 48"', 'viewBox="1 0 48 48"'),
            ('viewBox="0 0 48 48"', 'viewBox="0 0 32 32"'),
            ('viewBox="0 0 48 48" ', ''),
            ('stroke-width="4"', 'stroke-width="2"'),
            ('stroke-width="4"', 'stroke-width="nan"'),
        )
        for before, after in changes:
            with self.subTest(after=after):
                self.assertNotPass(gate.check_drawing(source.replace(before, after, 1)))
        self.assertNotPass(gate.check_drawing(source, icon_type="unknown"))

    def test_native_px_units_and_single_quotes_are_supported(self):
        source = drawing().replace('width="48"', 'width="48px"').replace('height="48"', 'height="48px"')
        self.assertPass(gate.check_drawing(source.replace('"', "'")))

    def test_unsupported_paint_hidden_transforms_and_external_nodes_fail(self):
        bodies = (
            '<g><path d="M6 10H42 M6 18H42"/></g>',
            '<path d="M6 10H42" transform="translate(0 0)"/>',
            '<path d="M6 10H42" style="stroke-width:4"/>',
            '<path d="M6 10H42" display="none"/>',
            '<path d="M6 10H42" opacity="0"/>',
            '<path d="M6 10H42" stroke-width="2"/>',
            '<path d="M6 10H42" fill="black"/>',
            '<defs><path id="a" d="M6 10H42"/></defs><use href="#a"/>',
            '<image href="https://example.invalid/icon.svg"/>',
            '<script>alert(1)</script><path d="M6 10H42"/>',
        )
        for body in bodies:
            with self.subTest(body=body):
                self.assertNotPass(self.check(body))
        for before, after in (('fill="none"', 'fill="black"'),
                              ('stroke="currentColor"', 'stroke="black"'),
                              ('stroke-linecap="round"', 'stroke-linecap="butt"'),
                              ('stroke-linejoin="round"', 'stroke-linejoin="miter"')):
            with self.subTest(after=after):
                self.assertNotPass(gate.check_drawing(drawing().replace(before, after)))

    def test_empty_malformed_nonfinite_or_entity_svg_fails_closed(self):
        sources = (
            drawing(""), drawing()[:-6],
            drawing('<path d="M6 10H42 M"/>'),
            drawing('<path d="M6 10H42 garbage"/>'),
            drawing('<path d="M6 10Lnan 24"/>'),
            drawing('<path d="M6 10A2 2 0 2 1 8 12"/>'),
            '<!DOCTYPE svg [<!ENTITY line "M6 10H42">]>' + drawing('<path d="&line;"/>'),
        )
        for source in sources:
            with self.subTest(source=source):
                self.assertNotPass(gate.check_drawing(source))

    def test_check_file_preserves_source_and_is_read_only_without_reports(self):
        with TemporaryDirectory() as folder:
            root = Path(folder)
            svg = root / "sym-001-spacing-design.svg"
            original = drawing().encode()
            svg.write_bytes(original)
            result = gate.check_file(svg)
            self.assertPass(result)
            self.assertEqual(result["file"], svg.name)
            self.assertEqual(Path(result["source"]).resolve(), svg.resolve())
            self.assertEqual(svg.read_bytes(), original)
            self.assertEqual(list(root.iterdir()), [svg])

    def test_missing_unreadable_and_invalid_utf8_files_return_failure(self):
        with TemporaryDirectory() as folder:
            root = Path(folder)
            self.assertNotPass(gate.check_file(root / "missing.svg"))
            self.assertNotPass(gate.check_file(root))
            svg = root / "invalid.svg"
            svg.write_bytes(b"\xff\xfe\x00")
            self.assertNotPass(gate.check_file(svg))

    def test_missing_geometry_engine_never_grants_pass(self):
        with patch.dict(sys.modules, {"stroke_distance": None}):
            self.assertNotPass(self.check())

    def test_fresh_reports_and_colored_overlays_preserve_source(self):
        with TemporaryDirectory() as folder:
            root = Path(folder)
            svg = root / "spacing.svg"
            output = root / "qa"
            original = drawing().encode()
            svg.write_bytes(original)
            first = gate.check_file(svg, output_dir=output)
            self.assertPass(first)
            self.assertEqual(svg.read_bytes(), original)
            old_report = Path(first["reportPath"])
            old_data = old_report.read_bytes()
            self.assertEqual(json.loads(old_data), first)
            overlay = Path(first["overlayPath"])
            self.assertTrue(overlay.is_file())
            self.assertIn('<svg ', overlay.read_text())
            self.assertIn('width="48"', overlay.read_text())
            self.assertIn('height="48"', overlay.read_text())
            failing_source = parallel_lines(7).encode()
            svg.write_bytes(failing_source)
            second = gate.check_file(svg, output_dir=output)
            self.assertNotPass(second)
            self.assertNotEqual(first["reportPath"], second["reportPath"])
            self.assertEqual(old_report.read_bytes(), old_data)
            self.assertEqual(json.loads(Path(second["reportPath"]).read_text()), second)
            self.assertEqual(svg.read_bytes(), failing_source)

    def test_source_changed_during_measurement_cannot_pass(self):
        import stroke_distance

        with TemporaryDirectory() as folder:
            source = Path(folder) / "spacing.svg"
            source.write_text(drawing())
            analyze = stroke_distance.analyze_paths

            def changed(*args, **kwargs):
                result = analyze(*args, **kwargs)
                source.write_text(parallel_lines(7))
                return result

            with patch.object(stroke_distance, "analyze_paths", side_effect=changed):
                result = gate.check_file(source)
            self.assertNotPass(result)
            self.assertIn("changed", " ".join(result["errors"]))

    def test_too_many_contours_stop_with_review_instead_of_unbounded_pair_work(self):
        import stroke_distance

        body = "".join(f'<path d="M6 {8 + index / 100}H42"/>'
                       for index in range(stroke_distance.MAX_CONTOURS + 1))
        result = self.check(body)
        self.assertNotPass(result)
        self.assertEqual(result["status"], "review")
        self.assertIn("limit", " ".join(result["errors"]).lower())
        self.assertEqual(result["stats"]["distanceTests"], 0)

    def test_exhausted_numerical_work_limits_never_grant_pass(self):
        import stroke_distance

        cases = (
            ("MAX_DISTANCE_TESTS", '<path d="M6 10H42 M6 18H42"/>'),
            ("MAX_CONNECTION_TESTS", '<path d="M8 24H40"/><path d="M24 8V40"/>'),
            ("MAX_ADAPTIVE_NODES", '<path d="M8 22Q24 6 40 22"/>'),
            ("MAX_SEGMENTS", '<path d="M6 10H42"/>'),
        )
        for name, body in cases:
            with self.subTest(limit=name), patch.object(stroke_distance, name, 0):
                result = self.check(body)
                self.assertNotPass(result)
                self.assertEqual(result["status"], "review")
                self.assertIn("limit", " ".join(result["errors"]).lower())


class StrokeSpacingCliTests(unittest.TestCase):
    def run_gate(self, *args):
        return subprocess.run([sys.executable, "-B", str(SCRIPT), *map(str, args)],
                              text=True, capture_output=True)

    def fixture(self, root, name="spacing.svg", *, distance=8):
        svg = root / name
        svg.write_text(parallel_lines(distance))
        return svg

    def test_cli_json_and_quiet_modes_preserve_input(self):
        with TemporaryDirectory() as folder:
            root = Path(folder)
            svg = self.fixture(root)
            before = svg.read_bytes()
            process = self.run_gate(svg, "--json")
            self.assertEqual(process.returncode, 0, process.stdout + process.stderr)
            summary = json.loads(process.stdout)
            self.assertTrue(summary["ok"])
            self.assertEqual(summary["checked"], 1)
            self.assertEqual(summary["failed"], 0)
            self.assertEqual(len(summary["rows"]), 1)
            process = self.run_gate(svg, "--quiet")
            self.assertEqual(process.returncode, 0, process.stdout + process.stderr)
            self.assertEqual(process.stdout, "")
            self.assertEqual(svg.read_bytes(), before)
            self.assertEqual(list(root.iterdir()), [svg])

    def test_cli_violation_is_nonzero_even_when_quiet(self):
        with TemporaryDirectory() as folder:
            svg = self.fixture(Path(folder), distance=7)
            process = self.run_gate(svg, "--quiet")
            self.assertEqual(process.returncode, 1, process.stdout + process.stderr)
            self.assertEqual(process.stdout, "")

    def test_folder_checks_all_svg_files_and_does_not_skip_failures(self):
        with TemporaryDirectory() as folder:
            root = Path(folder)
            self.fixture(root, "spacing.svg")
            self.fixture(root, "spacing-design.svg", distance=7)
            (root / "notes.txt").write_text("Not an SVG")
            process = self.run_gate(root, "--json")
            self.assertEqual(process.returncode, 1, process.stdout + process.stderr)
            summary = json.loads(process.stdout)
            self.assertFalse(summary["ok"])
            self.assertEqual(summary["checked"], 2)
            self.assertEqual(summary["failed"], 1)

    def test_mixed_valid_and_missing_inputs_never_silently_pass(self):
        with TemporaryDirectory() as folder:
            root = Path(folder)
            svg = self.fixture(root)
            process = self.run_gate(svg, root / "missing.svg", "--json")
            self.assertEqual(process.returncode, 1, process.stdout + process.stderr)
            summary = json.loads(process.stdout)
            self.assertFalse(summary["ok"])
            self.assertGreaterEqual(summary["checked"], 2)
            self.assertGreaterEqual(summary["failed"], 1)

    def test_missing_or_empty_input_fails_without_traceback(self):
        self.assertEqual(self.run_gate().returncode, 2)
        with TemporaryDirectory() as folder:
            root = Path(folder)
            for source in (root, root / "missing.svg"):
                with self.subTest(source=source):
                    process = self.run_gate(source, "--json")
                    self.assertEqual(process.returncode, 1, process.stdout + process.stderr)
                    self.assertNotIn("Traceback", process.stderr)
                    self.assertFalse(json.loads(process.stdout)["ok"])

    def test_cli_cannot_override_required_threshold(self):
        with TemporaryDirectory() as folder:
            svg = self.fixture(Path(folder), distance=7)
            process = self.run_gate(svg, "--minimum-distance", "1")
            self.assertEqual(process.returncode, 2, process.stdout + process.stderr)

    def test_cli_writes_matching_aggregate_and_native_review_report(self):
        with TemporaryDirectory() as folder:
            root = Path(folder)
            svg = self.fixture(root)
            before = svg.read_bytes()
            output = root / "qa"
            process = self.run_gate(svg, "--output-dir", output, "--json")
            self.assertEqual(process.returncode, 0, process.stdout + process.stderr)
            summary = json.loads(process.stdout)
            self.assertEqual(json.loads((output / "spacing-results.json").read_text()), summary)
            self.assertTrue((output / "spacing-report.html").is_file())
            row = summary["rows"][0]
            self.assertEqual(json.loads(Path(row["reportPath"]).read_text()), row)
            self.assertTrue(Path(row["overlayPath"]).is_file())
            self.assertEqual(svg.read_bytes(), before)

    def test_report_targets_cannot_overwrite_inputs_through_hardlinks(self):
        for report_name in ("spacing-results.json", "spacing-report.html"):
            with self.subTest(report_name=report_name), TemporaryDirectory() as folder:
                root = Path(folder)
                svg = self.fixture(root)
                before = svg.read_bytes()
                os.link(svg, root / report_name)
                process = self.run_gate(svg, "--output-dir", root, "--json")
                self.assertEqual(process.returncode, 1, process.stdout + process.stderr)
                self.assertFalse(json.loads(process.stdout)["ok"])
                self.assertEqual(svg.read_bytes(), before)
                self.assertEqual((root / report_name).read_bytes(), before)

    def test_symlink_report_directory_is_rejected_without_touching_target(self):
        with TemporaryDirectory() as folder:
            root = Path(folder)
            svg = self.fixture(root)
            target = root / "target"
            target.mkdir()
            output = root / "qa"
            output.symlink_to(target, target_is_directory=True)
            process = self.run_gate(svg, "--output-dir", output, "--json")
            self.assertEqual(process.returncode, 1, process.stdout + process.stderr)
            self.assertFalse(json.loads(process.stdout)["ok"])
            self.assertEqual(list(target.iterdir()), [])


if __name__ == "__main__":
    unittest.main()
