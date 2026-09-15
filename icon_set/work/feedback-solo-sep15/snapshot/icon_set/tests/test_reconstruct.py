"""The batch trace/reconstruct loop in ``scripts/reconstruct.py``.

The point of the tool is that it measures the *picture*, so the tests draw
pictures with known features and assert the measurements come back.
"""

from __future__ import annotations

import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from icon_set.model.icons.registry import create
from icon_set.scripts_reconstruct import (
    TOLERANCE,
    _base_slug,
    _fidelity,
    _sources,
    slug_of,
    trace_one,
)

FRAME = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" fill="none"
 stroke="black" stroke-width="4" stroke-linecap="round" stroke-linejoin="round">
<path d="M2 2L62 2L62 62L2 62Z"/><path d="M2 20L62 20"/><path d="M11 11L14 11"/>
</svg>"""


class SlugTests(unittest.TestCase):
    def test_a_uuid_suffix_is_stripped(self) -> None:
        self.assertEqual(
            slug_of(Path("web-browser-window-a434346c-ec35-4a36-89af-8b0682a68ec6.svg")),
            "web-browser-window",
        )

    def test_a_name_without_a_uuid_is_left_alone(self) -> None:
        self.assertEqual(slug_of(Path("clipboard.svg")), "clipboard")

    def test_repeated_concepts_are_kept_apart(self) -> None:
        with TemporaryDirectory() as folder:
            root = Path(folder)
            for name in (
                "desktop-computer-monitor-3b1aecfb-e26b-49bf-9b71-205dbd24b136.svg",
                "desktop-computer-monitor-68edf9b6-f133-45a4-a6a6-b6d0df318a0c.svg",
            ):
                (root / name).write_text(FRAME)
            keys = sorted(_sources(root))
        self.assertEqual(keys, ["desktop-computer-monitor", "desktop-computer-monitor#2"])
        self.assertEqual(_base_slug("desktop-computer-monitor#2"), "desktop-computer-monitor")


class TraceTests(unittest.TestCase):
    """A drawn frame, divider and mark must come back as measurements."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.trace = trace_one(FRAME, 64)

    def test_it_reports_the_painted_bounds(self) -> None:
        left, top, right, bottom = self.trace["bounds"]
        for value, expected in ((left, 0), (top, 0), (right, 64), (bottom, 64)):
            self.assertAlmostEqual(value, expected, delta=1.0)

    def test_a_square_subject_points_at_a_square_keyshape(self) -> None:
        self.assertAlmostEqual(self.trace["aspect"], 1.0, delta=0.05)
        self.assertIn("SQUARE", self.trace["keyshape_hint"])

    def test_the_divider_is_found_at_its_own_height(self) -> None:
        centres = [band["centre"] for band in self.trace["rules_horizontal"]]
        self.assertTrue(any(abs(c - 20) <= 1.0 for c in centres),
                        f"no rule near y 20 in {centres}")

    def test_the_detached_mark_is_found(self) -> None:
        marks = self.trace["marks"]
        self.assertEqual(len(marks), 1)
        x, y = marks[0]["centre"]
        self.assertAlmostEqual(x, 12.5, delta=1.5)
        self.assertAlmostEqual(y, 11, delta=1.5)

    def test_an_empty_source_says_so_instead_of_raising(self) -> None:
        blank = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"></svg>'
        self.assertTrue(trace_one(blank, 64)["empty"])


class FidelityTests(unittest.TestCase):
    def test_an_icon_scores_one_against_itself(self) -> None:
        icon = create("browser-window")
        scores = _fidelity(icon.to_svg(), icon, 64)
        self.assertEqual(scores["fidelity"], 1.0)
        self.assertEqual(scores["iou"], 1.0)

    def test_a_shift_inside_the_tolerance_still_reads_as_the_same_drawing(self) -> None:
        """Raw IoU collapses on line art; fidelity is why the ledger is usable."""
        square = create("container-square")
        shifted = FRAME.replace('viewBox="0 0 64 64"', 'viewBox="-2 -2 64 64"')
        scores = _fidelity(shifted, square, 64)
        self.assertGreater(scores["fidelity"], 0.75)
        self.assertLess(scores["iou"], scores["fidelity"])

    def test_a_different_subject_scores_low(self) -> None:
        scores = _fidelity(FRAME, create("container-circle"), 64)
        self.assertLess(scores["fidelity"], 0.75)

    def test_the_tolerance_is_stated_in_canvas_units(self) -> None:
        self.assertEqual(TOLERANCE, 2.0)


if __name__ == "__main__":
    unittest.main()
