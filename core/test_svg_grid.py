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

    def test_fractional_axis_line_fails(self):
        result = inspect(self.write('<path d="M 2 10.8 L 46 10.8"/>'), "design")
        self.assertEqual(result["status"], "fail")
        self.assertEqual(result["fractionalAxisOr45Segments"], 1)

    def test_off_angle_fails(self):
        result = inspect(self.write('<path d="M 2 2 L 19 9"/>'), "design")
        self.assertEqual(result["status"], "fail")
        self.assertEqual(result["offAngleSegments"], 1)

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


if __name__ == "__main__":
    unittest.main()
