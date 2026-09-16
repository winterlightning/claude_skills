"""Migration fitting preserves originals and exposes failures instead of hiding them."""
import unittest

from icon_set.model.icons.base import Icon
from icon_set.model.keyshapes import Keyshape
from icon_set.model.primitives import Arc, Point
from icon_set.model.profiles import Profile
from icon_set.validation.envelope import visible_bounds, visible_radial_extent


def draft():
    icon = Icon("test-shape", Profile.SOLO48, semantic_role="MAIN", keyshape=Keyshape.SQUARE)
    icon.family = "solo"
    icon.semantic_kind = "noun"
    return icon


class FittingTests(unittest.TestCase):
    def test_square_fits_without_mutating_source(self):
        icon = draft().add_polyline("outline", (2, 2), (46, 2), (46, 46), (2, 46), closed=True)
        icon.add_anchor("center", (24, 24))
        icon.add_anchor("corner", (2, 2))
        before = icon.to_record()
        result = icon.fit_to_keyshape(Keyshape.SQUARE)
        self.assertEqual(visible_bounds(result.icon.primitives), (4, 4, 44, 44))
        self.assertEqual(result.icon.STROKE_WIDTH, 4)
        self.assertEqual(result.icon.anchors["corner"], Point(6, 6))
        self.assertEqual(result.icon.anchors["center"], Point(24, 24))
        self.assertEqual(result.icon.contours, icon.contours)
        self.assertEqual(result.icon.variant_of, icon.icon_id)
        result.icon.add_line("new", (6, 6), (42, 42))
        self.assertEqual(icon.to_record(), before)
        self.assertTrue(result.report["requires_visual_review"])

    def test_aspect_mismatch_is_reported(self):
        icon = draft().add_polyline("outline", (2, 2), (46, 2), (46, 46), (2, 46), closed=True)
        result = icon.fit_to_keyshape(Keyshape.HRECT_L)
        bounds = visible_bounds(result.icon.primitives)
        self.assertEqual(bounds[2] - bounds[0], bounds[3] - bounds[1])
        self.assertEqual(result.report["validation"]["status"], "fail")
        self.assertTrue(any("does not match" in e for e in result.report["validation"]["errors"]))

    def test_circle_keeps_shared_points_and_circular_radii(self):
        icon = draft()
        icon.add_arc("a", (2, 24), (46, 24), radius_x=22)
        icon.add_arc("b", (46, 24), (2, 24), radius_x=22)
        icon.add_contour("ring", "a", "b", closed=True)
        result = icon.fit_to_keyshape(Keyshape.CIRCLE)
        a, b = result.icon.primitives
        self.assertIsInstance(a, Arc)
        self.assertEqual((a.radius_x, a.radius_y), (20, 20))
        self.assertEqual(a.end, b.start)
        self.assertEqual(a.start, b.end)
        self.assertAlmostEqual(visible_radial_extent(result.icon.primitives, (24, 24)), 22)
        self.assertEqual(result.report["validation"]["status"], "pass")
        self.assertEqual(result.report, icon.fit_to_keyshape(Keyshape.CIRCLE).report)

    def test_rejects_unsupported_inputs(self):
        for icon, target in [(draft(), Keyshape.SQUARE),
                             (draft().add_dot("point", (24, 24)), Keyshape.SQUARE),
                             (draft(), Keyshape.FREE), (draft(), "square")]:
            with self.subTest(target=target), self.assertRaises(ValueError):
                icon.fit_to_keyshape(target)
        icon = draft().add_line("line", (2, 2), (46, 46))
        icon.family = "sub"
        with self.assertRaisesRegex(ValueError, "SOLO48"):
            icon.fit_to_keyshape(Keyshape.SQUARE)

    def test_flat_drawing_reports_unfilled_axis(self):
        result = draft().add_line("bar", (2, 24), (46, 24)).fit_to_keyshape(Keyshape.HRECT_L)
        self.assertEqual(visible_bounds(result.icon.primitives), (2, 22, 46, 26))
        self.assertEqual(result.report["validation"]["status"], "fail")

    def test_force_stretch_fills_both_axes_and_keeps_original(self):
        icon = draft().add_polyline("outline", (2, 2), (46, 2), (46, 46), (2, 46), closed=True)
        before = icon.to_record()
        result = icon.fit_to_keyshape(Keyshape.HRECT_L, force_stretch=True)
        self.assertEqual(visible_bounds(result.icon.primitives), (2, 6, 46, 42))
        self.assertNotEqual(result.report['scale_x'], result.report['scale_y'])
        self.assertEqual(result.report['mode'], 'stretch')
        self.assertEqual(result.icon.STROKE_WIDTH, 4)
        self.assertEqual(result.report['validation']['status'], 'pass')
        self.assertEqual(icon.to_record(), before)

    def test_force_stretch_scales_arc_radii_per_axis(self):
        icon = draft()
        icon.add_arc('a', (2, 24), (46, 24), radius_x=22)
        icon.add_arc('b', (46, 24), (2, 24), radius_x=22)
        icon.add_contour('ring', 'a', 'b', closed=True)
        result = icon.fit_to_keyshape(Keyshape.HRECT_L, force_stretch=True)
        a, b = result.icon.primitives
        self.assertEqual((a.radius_x, a.radius_y), (20, 16))
        self.assertEqual(a.end, b.start)
        self.assertEqual(visible_bounds(result.icon.primitives), (2, 6, 46, 42))
        self.assertEqual(result.report['validation']['status'], 'pass')
        circle = icon.fit_to_keyshape(Keyshape.CIRCLE, force_stretch=True)
        self.assertEqual(circle.report['mode'], 'uniform')
        self.assertAlmostEqual(visible_radial_extent(circle.icon.primitives, (24, 24)), 22)

    def test_slim_rectangles_fit_and_reject_the_larger_envelope(self):
        for shape, points, expected in (
            (Keyshape.HRECT_M, ((4, 8), (44, 8), (44, 40), (4, 40)), (2, 8, 46, 40)),
            (Keyshape.VRECT_M, ((8, 4), (40, 4), (40, 44), (8, 44)), (8, 2, 40, 46)),
        ):
            with self.subTest(shape=shape.name):
                icon = draft().add_polyline("outline", *points, closed=True)
                icon.keyshape = shape
                self.assertTrue(any(
                    "does not match" in error
                    for error in icon.validate_icon().errors
                ))
                result = icon.fit_to_keyshape(shape, force_stretch=True)
                self.assertEqual(visible_bounds(result.icon.primitives), expected)
                self.assertEqual(result.report['validation']['status'], 'pass')

    def test_force_stretch_rejects_zero_width_or_height(self):
        for start, end in [((2, 24), (46, 24)), ((24, 2), (24, 46))]:
            with self.subTest(start=start), self.assertRaisesRegex(ValueError, 'non-zero width and height'):
                draft().add_line('bar', start, end).fit_to_keyshape(Keyshape.HRECT_L, force_stretch=True)


if __name__ == "__main__":
    unittest.main()
