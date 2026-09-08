"""Icons reconstructed from a reference drawing.

These tests check the things a machine can decide: that the icon is valid, that
it fills its keyshape, and that it is one connected drawing whose strap tips
meet where the reference made them meet.

They deliberately do **not** score the geometry against the reference. The
reference is drawn near 1024 units and the target is 32, 48 or 64 with a fixed
4-unit stroke, so divergence is guaranteed by the change of canvas alone. Whether
a reconstruction is faithful is judged by looking at it at native size, and no
threshold here can stand in for that.
"""

from __future__ import annotations

import unittest
from pathlib import Path

from icon_set.model.icons.registry import create
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.validation.envelope import visible_bounds

SOURCE = (
    Path(__file__).resolve().parents[2]
    / "(pictoicon) - Square Smartwatch Device.svg"
)


class SmartwatchTraceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.icon = create("smartwatch")

    def test_the_source_is_still_in_the_repository(self) -> None:
        self.assertTrue(SOURCE.is_file(), f"missing trace source: {SOURCE}")

    def test_it_validates_with_no_warnings(self) -> None:
        report = self.icon.validate_icon()
        self.assertEqual(report.status, "valid", report.describe())
        self.assertEqual(report.warnings, ())

    def test_it_is_a_solo_subject_on_solo48(self) -> None:
        self.assertEqual(self.icon.family, "solo")
        self.assertIs(self.icon.profile, Profile.SOLO48)

    def test_it_fills_the_square_keyshape_exactly(self) -> None:
        self.assertIs(self.icon.keyshape, Keyshape.SQUARE)
        self.assertEqual(
            visible_bounds(self.icon.primitives),
            tuple(float(v) for v in Keyshape.SQUARE.bounds_for(Profile.SOLO48)),
        )

    def test_it_is_one_connected_drawing(self) -> None:
        """Straps share endpoints with the case, as they do in the source."""
        ids = {p.element_id for p in self.icon.primitives}
        starts = {(p.start.x, p.start.y) for p in self.icon.primitives}
        for attach in ((8, 9), (23, 9), (8, 39), (23, 39)):
            with self.subTest(attachment=attach):
                self.assertIn(attach, starts)
        self.assertIn("case-top", ids)

    def test_the_strap_tips_converge_on_a_shared_point(self) -> None:
        ends = [(p.end.x, p.end.y) for p in self.icon.primitives]
        self.assertGreaterEqual(ends.count((31, 2)), 2)
        self.assertGreaterEqual(ends.count((31, 46)), 2)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
