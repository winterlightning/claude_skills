"""Exact human head spacing must pass without accepting narrower gaps."""
import unittest

from icon_set.model.icons.solo.user_reference import UserReference
from icon_set.validation.path_commands import Command
from icon_set.validation.stroke_distance import analyze_paths


def circle_and_line(y):
    return [
        {"id": "head", "commands": [Command("M", [(15, 13)]),
            Command("A", [(33, 13)], (9, 9, 0, 0, 1)),
            Command("A", [(15, 13)], (9, 9, 0, 0, 1)), Command("Z", [])]},
        {"id": "body", "commands": [Command("M", [(8, y)]), Command("L", [(40, y)])]},
    ]


class HumanSpacingTests(unittest.TestCase):
    def test_exact_four_unit_ink_gap_passes(self):
        result = analyze_paths(circle_and_line(30))
        self.assertEqual(result["status"], "pass")
        self.assertEqual(result["pairs"][0]["lowerBound"], 8)
        self.assertEqual(result["minimumInkClearance"], 4)

    def test_subminimum_gap_never_passes(self):
        for y in (29, 29.999, 29.999999):
            with self.subTest(y=y):
                self.assertNotEqual(analyze_paths(circle_and_line(y))["status"], "pass")

    def test_bezier_control_hull_protrusion_is_not_ignored(self):
        paths = circle_and_line(30)
        paths[1]["commands"] = [Command("M", [(8, 30)]),
            Command("C", [(20, 20), (28, 20), (40, 30)])]
        self.assertNotEqual(analyze_paths(paths)["status"], "pass")

    def test_major_arc_bulging_toward_head_fails(self):
        paths = circle_and_line(30)
        paths[1]["commands"] = [Command("M", [(8, 42)]),
            Command("A", [(20, 30)], (12, 12, 0, 1, 1))]
        self.assertNotEqual(analyze_paths(paths)["status"], "pass")

    def test_reference_user_full_validation(self):
        report = UserReference().validate_icon()
        self.assertEqual(report.status, "valid", report.describe())
        self.assertFalse(report.warnings)


if __name__ == "__main__":
    unittest.main()
