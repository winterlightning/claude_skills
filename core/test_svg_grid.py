#!/usr/bin/env python3
import tempfile
import unittest
import hashlib
from pathlib import Path

from check_svg_grid import apply_exceptions, inspect


class SvgGridTests(unittest.TestCase):
    def write(self, body: str, canvas: int = 48, stroke: int = 4) -> Path:
        folder = Path(tempfile.mkdtemp())
        path = folder / "icon.svg"
        path.write_text(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {canvas} {canvas}" fill="none" stroke="currentColor" stroke-width="{stroke}">{body}</svg>')
        return path

    def test_whole_grid_axis_lines_pass(self):
        result = inspect(self.write('<path d="M 2 2 L 46 2 L 46 46"/>'), "design")
        self.assertEqual(result["status"], "pass")

    def test_cubic_and_smooth_curves_are_supported(self):
        for data in ("M 6 24 C 6 6 42 6 42 24", "M6 24 c0 -18 18 -18 18 0 s18 18 18 0"):
            with self.subTest(data=data):
                result=inspect(self.write(f'<path d="{data}"/>'),"design")
                self.assertEqual(result["status"],"pass")
                self.assertNotIn("cubic",[issue["code"] for issue in result["issues"]])

    def test_fractional_cubic_control_points_require_review_not_rejection(self):
        result=inspect(self.write('<path d="M6 24 C6.5 6 41.5 6 42 24"/>'),"design")
        self.assertEqual(result["status"],"review")
        self.assertEqual(result["fractionalDesignValues"],2)

    def test_malformed_cubic_is_a_parse_failure(self):
        result=inspect(self.write('<path d="M6 24 C6 6 42 6"/>'),"design")
        self.assertEqual(result["status"],"fail")
        self.assertEqual([issue["code"] for issue in result["issues"]],["parse-error"])

    def test_small_lucide_corner_radius_is_supported(self):
        result=inspect(self.write('<path d="M6 8 A2 2 0 0 1 8 6 L40 6 A2 2 0 0 1 42 8"/>'),"design")
        self.assertEqual(result["status"],"pass")

    def test_fractional_axis_line_fails(self):
        result = inspect(self.write('<path d="M 2 10.8 L 46 10.8"/>'), "design")
        self.assertEqual(result["status"], "fail")
        self.assertEqual(result["fractionalAxisOr45Segments"], 1)

    def test_arbitrary_angles_pass_for_open_and_closed_paths(self):
        for data in ("M 2 2 L 19 9", "M 2 2 L 19 9 L 24 30 Z"):
            with self.subTest(data=data):
                result = inspect(self.write(f'<path d="{data}"/>'), "design")
                self.assertEqual(result["status"], "pass")
                self.assertEqual(result["issues"], [])
                self.assertNotIn("offAngleSegments", result)

    def test_arbitrary_fractional_slope_is_not_treated_as_an_axis_line(self):
        result = inspect(self.write('<path d="M 2.5 2 L 26.5 4"/>'), "design")
        self.assertEqual(result["status"], "review")
        self.assertEqual(result["fractionalAxisOr45Segments"], 0)
        self.assertEqual(result["issues"], [])

    def test_fractional_axis_and_45_degree_lines_fail_in_both_directions(self):
        for end in ("26.5 2.5", "2.5 26.5", "26.5 26.5", "26.5 -21.5"):
            for start, finish in (("2.5 2.5", end), (end, "2.5 2.5")):
                with self.subTest(start=start, finish=finish):
                    result = inspect(self.write(f'<path d="M {start} L {finish}"/>'), "design")
                    self.assertEqual(result["status"], "fail")
                    self.assertEqual(result["fractionalAxisOr45Segments"], 1)
                    self.assertEqual([issue["code"] for issue in result["issues"]], ["fractional-grid-lines"])

    def test_ship_coordinates_normalize_to_design_grid(self):
        result = inspect(self.write('<path d="M 1 1 L 23 1"/>', 24, 2), "ship")
        self.assertEqual(result["status"], "pass")

    def test_sub_ship_coordinates_normalize_to_32u_profile(self):
        result = inspect(self.write('<path d="M 1 1 L 15 1"/>', 16, 2), "ship", "sub")
        self.assertEqual(result["status"], "pass")
        self.assertEqual(result["designCanvas"], 32)

    def test_sub_canvas_is_not_accepted_as_normal(self):
        result = inspect(self.write('<path d="M 1 1 L 15 1"/>', 16, 2), "ship")
        self.assertEqual(result["status"], "fail")
        self.assertIn("wrong-canvas", [issue["code"] for issue in result["issues"]])

    def test_container_ship_coordinates_normalize_to_64u_profile(self):
        result = inspect(
            self.write('<path d="M 1 1 L 31 1"/>', 32, 2),
            "ship",
            "container",
        )
        self.assertEqual(result["status"], "pass")
        self.assertEqual(result["designCanvas"], 64)

    def test_container_canvas_is_not_accepted_as_normal(self):
        result = inspect(self.write('<path d="M 1 1 L 31 1"/>', 32, 2), "ship")
        self.assertEqual(result["status"], "fail")
        self.assertIn("wrong-canvas", [issue["code"] for issue in result["issues"]])

    def test_hash_locked_exception_passes_documented_fraction(self):
        path = self.write('<path d="M 2 10.8 L 46 10.8"/>')
        result = inspect(path, "design")
        entries = {"icon.svg": {
            "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
            "allow": ["fractional-grid-lines"],
            "reason": "exact junction with a rotated atom",
        }}
        result = apply_exceptions(result, path, entries)
        self.assertEqual(result["status"], "pass")
        self.assertEqual(result["documentedExceptions"][0]["reason"], "exact junction with a rotated atom")

    def test_stale_exception_fails(self):
        path = self.write('<path d="M 2 10.8 L 46 10.8"/>')
        result = apply_exceptions(inspect(path, "design"), path, {
            "icon.svg": {"sha256": "0" * 64, "allow": ["fractional-grid-lines"]}
        })
        self.assertEqual(result["status"], "fail")
        self.assertIn("stale-exception", [issue["code"] for issue in result["issues"]])

    def test_retired_angle_only_exception_preserves_current_result(self):
        for data, status in (
            ("M 2 2 L 19 9", "pass"),
            ("M 2.5 2 L 26.5 4", "review"),
            ("M 2 10.8 L 46 10.8", "fail"),
        ):
            with self.subTest(status=status):
                path = self.write(f'<path d="{data}"/>')
                result = apply_exceptions(inspect(path, "design"), path, {
                    "icon.svg": {"sha256": "0" * 64, "allow": ["off-angle"]}
                })
                self.assertEqual(result["status"], status)
                self.assertNotIn("stale-exception", [issue["code"] for issue in result["issues"]])
                self.assertEqual(result["documentedExceptions"], [])

    def test_mixed_exception_still_requires_matching_hash(self):
        path = self.write('<path d="M 2 10.8 L 46 10.8"/>')
        result = apply_exceptions(inspect(path, "design"), path, {
            "icon.svg": {"sha256": "0" * 64, "allow": ["off-angle", "fractional-grid-lines"]}
        })
        self.assertEqual(result["status"], "fail")
        self.assertIn("stale-exception", [issue["code"] for issue in result["issues"]])


if __name__ == "__main__":
    unittest.main()
