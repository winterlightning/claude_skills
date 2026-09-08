"""Acceptance fixtures for the ordered validator chain (plan section 5)."""

from __future__ import annotations

import unittest

from icon_set.model.icons.base import Icon
from icon_set.model.keyshapes import FreeKeyshapeSpec, Keyshape
from icon_set.model.profiles import NUMERIC_EPSILON, Profile
from icon_set.validation.validator import IconValidator


def make(
    icon_id: str = "fixture",
    keyshape: Keyshape = Keyshape.SQUARE,
    *,
    profile: Profile = Profile.SUB32,
    role: str | None = "SUB",
    kind: str = "modifier",
    free: FreeKeyshapeSpec | None = None,
) -> Icon:
    icon = Icon(
        icon_id, profile, semantic_role=role, keyshape=keyshape, free_keyshape=free
    )
    icon.semantic_kind = kind
    return icon


def errors_for(icon: Icon, check: str) -> list[str]:
    return [line for line in icon.validate_icon().errors if line.startswith(check)]


class CanvasAndKeyshapeTests(unittest.TestCase):
    def test_sub32_circle_radius_14_paints_exactly_to_the_canvas(self) -> None:
        icon = make("circle", Keyshape.CIRCLE, role="MAIN", kind="noun")
        icon.add_arc("top", (2, 16), (30, 16), radius_x=14)
        icon.add_arc("bottom", (30, 16), (2, 16), radius_x=14)
        icon.add_contour("ring", "top", "bottom", closed=True)
        self.assertEqual(icon.validate_icon().status, "valid")

    def test_sub32_circle_radius_15_overflows_and_fails(self) -> None:
        icon = make("circle", Keyshape.CIRCLE, role="MAIN", kind="noun")
        icon.add_arc("top", (1, 16), (31, 16), radius_x=15)
        icon.add_arc("bottom", (31, 16), (1, 16), radius_x=15)
        icon.add_contour("ring", "top", "bottom", closed=True)
        failures = errors_for(icon, "canvas/keyshape bounds")
        self.assertTrue(failures)
        self.assertIn("(-1, -1, 33, 33)", failures[0])

    def test_centerline_box_is_visible_box_inset_by_two(self) -> None:
        """Square and all eight rectangles, measured from vector geometry."""
        shapes = (
            Keyshape.SQUARE,
            Keyshape.HRECT_XL, Keyshape.HRECT_L, Keyshape.HRECT_M, Keyshape.HRECT_S,
            Keyshape.VRECT_XL, Keyshape.VRECT_L, Keyshape.VRECT_M, Keyshape.VRECT_S,
        )
        for shape in shapes:
            with self.subTest(shape=shape.name):
                left, top, right, bottom = shape.bounds_for(Profile.SUB32)
                icon = make("box", shape, role="MAIN", kind="noun")
                icon.add_polyline(
                    "outline",
                    (left + 2, top + 2), (right - 2, top + 2),
                    (right - 2, bottom - 2), (left + 2, bottom - 2),
                    closed=True,
                )
                self.assertEqual(icon.validate_icon().status, "valid")

    def test_full_canvas_rectangle_edges_touch_without_exceeding(self) -> None:
        icon = make("wide", Keyshape.HRECT_XL, role="MAIN", kind="noun")
        icon.add_polyline("outline", (2, 4), (30, 4), (30, 28), (2, 28), closed=True)
        self.assertEqual(icon.validate_icon().status, "valid")

    def test_interior_guide_does_not_cause_a_false_edge_failure(self) -> None:
        """SUB32's 4-unit guide must not be read as outer ink padding."""
        icon = make("bar", Keyshape.HRECT_S)
        icon.add_line("top", (2, 10), (30, 10))
        icon.add_line("bottom", (2, 22), (30, 22))
        self.assertEqual(icon.validate_icon().status, "valid")

    def test_undersized_artwork_fails_to_reach_its_keyshape(self) -> None:
        icon = make("small", Keyshape.SQUARE, role="MAIN", kind="noun")
        icon.add_polyline("outline", (8, 8), (24, 8), (24, 24), (8, 24), closed=True)
        self.assertTrue(errors_for(icon, "canvas/keyshape bounds"))

    def test_radial_subject_must_touch_the_circle(self) -> None:
        icon = make("small-circle", Keyshape.CIRCLE, role="MAIN", kind="noun")
        icon.add_arc("top", (6, 16), (26, 16), radius_x=10)
        icon.add_arc("bottom", (26, 16), (6, 16), radius_x=10)
        icon.add_contour("ring", "top", "bottom", closed=True)
        failures = errors_for(icon, "canvas/keyshape bounds")
        self.assertTrue(failures)
        self.assertIn("touches its envelope", failures[0])


class NumericEpsilonTests(unittest.TestCase):
    """The epsilon absorbs float construction error, never a design allowance."""

    def _circle(self, radius: int) -> Icon:
        icon = make("circle", Keyshape.CIRCLE, role="MAIN", kind="noun")
        left, right = 16 - radius, 16 + radius
        icon.add_arc("top", (left, 16), (right, 16), radius_x=radius)
        icon.add_arc("bottom", (right, 16), (left, 16), radius_x=radius)
        icon.add_contour("ring", "top", "bottom", closed=True)
        return icon

    def test_arc_derived_bounds_survive_square_root_error(self) -> None:
        """A sparkle's arc centres come out ~1e-15 off; that must not fail."""
        icon = make("sparkle", Keyshape.CIRCLE, role="MAIN", kind="noun")
        icon.add_arc("edge-ne", (16, 2), (30, 16), radius_x=14, sweep=False)
        icon.add_arc("edge-se", (30, 16), (16, 30), radius_x=14, sweep=False)
        icon.add_arc("edge-sw", (16, 30), (2, 16), radius_x=14, sweep=False)
        icon.add_arc("edge-nw", (2, 16), (16, 2), radius_x=14, sweep=False)
        icon.add_contour("outline", "edge-ne", "edge-se", "edge-sw", "edge-nw", closed=True)
        self.assertEqual(icon.validate_icon().status, "valid")

    def test_epsilon_is_far_below_any_real_deviation(self) -> None:
        """A thousandth of a unit is nine orders above the guard and must fail."""
        self.assertLess(NUMERIC_EPSILON, 0.001 / 1000)

    def test_a_real_deviation_still_fails_the_rect_fit(self) -> None:
        """Independent bars, so the nudge reaches the bounds check itself."""
        icon = make("bars", Keyshape.HRECT_S)
        icon.add_line("bar-top", (2, 10), (30, 10))
        icon.add_line("bar-bottom", (2, 22), (30, 22))
        self.assertEqual(icon.validate_icon().status, "valid")
        for point in (icon.primitives[1].start, icon.primitives[1].end):
            object.__setattr__(point, "y", 22.001)
        self.assertTrue(errors_for(icon, "canvas/keyshape bounds"))

    def test_a_real_overflow_still_fails_the_canvas(self) -> None:
        self.assertTrue(errors_for(self._circle(15), "canvas/keyshape bounds"))


class SpacingTests(unittest.TestCase):
    def _shafts(self, gap: int, profile: Profile) -> Icon:
        """Two parallel shafts exactly ``gap`` units apart on centerlines."""
        canvas = profile.spec.canvas_size
        top = (canvas - gap) // 2
        icon = make("bars", Keyshape.HRECT_S, profile=profile)
        icon.add_line("bar-top", (2, top), (canvas - 2, top))
        icon.add_line("bar-bottom", (2, top + gap), (canvas - 2, top + gap))
        return icon

    def _caps(self, gap: int, profile: Profile) -> Icon:
        """Two collinear shafts whose round endcaps face each other."""
        canvas = profile.spec.canvas_size
        centre = canvas // 2
        icon = make("caps", Keyshape.HRECT_S, profile=profile)
        icon.add_line("left", (2, centre), (centre - gap, centre))
        icon.add_line("right", (centre, centre), (canvas - 2, centre))
        return icon

    def test_locked_minimum_spacing_passes(self) -> None:
        """Each profile's own centerline minimum, read from the contract.

        Written against the contract rather than against three literals: the
        numbers have moved once (CONTAINER64 went from 10 to 8 when the
        protected slot was withdrawn) and a hardcoded copy just goes stale.
        """
        for profile in Profile:
            gap = profile.spec.equal_stroke_centerline_min
            for name, build in (("shafts", self._shafts), ("endcaps", self._caps)):
                with self.subTest(profile=profile.name, geometry=name):
                    self.assertEqual(errors_for(build(gap, profile), "mic"), [])

    def test_one_unit_below_the_minimum_fails(self) -> None:
        """One unit under each profile's own minimum must fail."""
        for profile in Profile:
            gap = profile.spec.equal_stroke_centerline_min - 1
            for name, build in (("shafts", self._shafts), ("endcaps", self._caps)):
                with self.subTest(profile=profile.name, geometry=name):
                    self.assertTrue(errors_for(build(gap, profile), "mic"))

    def test_undeclared_contact_fails(self) -> None:
        icon = make("cross", Keyshape.SQUARE)
        icon.add_line("bar-horizontal", (4, 16), (28, 16))
        icon.add_line("near", (16, 4), (16, 13))
        self.assertTrue(errors_for(icon, "mic"))

    def test_declared_connect_passes_the_same_contact(self) -> None:
        icon = make("cross", Keyshape.SQUARE)
        icon.add_line("bar-horizontal", (4, 16), (28, 16))
        icon.add_line("near", (16, 4), (16, 13))
        icon.relate("connect", "bar-horizontal", "near")
        self.assertEqual(errors_for(icon, "mic"), [])

    def test_a_declaration_is_scoped_to_its_own_pair(self) -> None:
        """Declaring one contact must not excuse an unrelated close pair."""
        icon = make("bars", Keyshape.SQUARE)
        icon.add_line("a", (4, 4), (28, 4))
        icon.add_line("b", (4, 9), (28, 9))
        icon.add_line("c", (4, 28), (28, 28))
        icon.relate("connect", "a", "c")
        self.assertTrue(errors_for(icon, "mic"))


class StyleGridTests(unittest.TestCase):
    def test_non_integer_coordinates_fail(self) -> None:
        icon = make("half", Keyshape.SQUARE)
        icon.add_line("bar", (4, 16), (28, 16))
        object.__setattr__(icon.primitives[0].end, "x", 27.5)
        self.assertTrue(errors_for(icon, "style/grid"))

    def test_wrong_stroke_width_fails(self) -> None:
        for width in (3, 6):
            with self.subTest(width=width):
                icon = make("bar", Keyshape.SQUARE)
                icon.STROKE_WIDTH = width
                icon.add_line("bar", (4, 4), (28, 28))
                self.assertTrue(errors_for(icon, "style/grid"))

    def test_butt_caps_and_miter_joins_fail(self) -> None:
        icon = make("bar", Keyshape.SQUARE)
        icon.LINE_CAP = "butt"
        icon.LINE_JOIN = "miter"
        icon.add_line("bar", (4, 4), (28, 28))
        failures = errors_for(icon, "style/grid")
        self.assertEqual(len(failures), 2)


class KeyshapeAndCompositionTests(unittest.TestCase):
    def _square(self, **kwargs) -> Icon:
        icon = make("box", Keyshape.SQUARE, **kwargs)
        icon.add_polyline("outline", (4, 4), (28, 4), (28, 28), (4, 28), closed=True)
        return icon

    def test_main_with_a_modifier_fails(self) -> None:
        self.assertTrue(errors_for(self._square(role="MAIN", kind="modifier"), "composition"))

    def test_sub_with_a_noun_fails(self) -> None:
        self.assertTrue(errors_for(self._square(role="SUB", kind="noun"), "composition"))

    def test_main_noun_passes(self) -> None:
        self.assertEqual(errors_for(self._square(role="MAIN", kind="noun"), "composition"), [])

    def test_sub_state_passes(self) -> None:
        self.assertEqual(errors_for(self._square(role="SUB", kind="state"), "composition"), [])

    def test_solo_requires_a_role(self) -> None:
        self.assertTrue(errors_for(self._square(role=None), "composition"))

    def test_unfrozen_composition_class_is_rejected(self) -> None:
        icon = self._square(role="MAIN", kind="noun")
        icon.composition_class = "SIDE_COMBINE"
        self.assertTrue(errors_for(icon, "composition"))


class FreeKeyshapeTests(unittest.TestCase):
    def _minus(self, free: FreeKeyshapeSpec) -> Icon:
        icon = make("minus", Keyshape.FREE, free=free, kind="verb")
        icon.add_line("bar", (2, 16), (30, 16))
        return icon

    def test_approved_free_record_passes(self) -> None:
        spec = FreeKeyshapeSpec(0, 14, 32, 18, "1-D bar glyph.", "FREE-2026-09-07-001")
        icon = self._minus(spec)
        self.assertEqual(errors_for(icon, "schema/profile"), [])

    def test_unapproved_free_use_fails(self) -> None:
        spec = FreeKeyshapeSpec(0, 14, 32, 18, "no approval recorded")
        self.assertTrue(errors_for(self._minus(spec), "schema/profile"))

    def test_free_bounds_must_match_the_approved_record(self) -> None:
        spec = FreeKeyshapeSpec(0, 12, 32, 20, "wrong bounds", "FREE-2026-09-07-001")
        failures = errors_for(self._minus(spec), "schema/profile")
        self.assertTrue(any("approved bounds" in line for line in failures))

    def test_free_requires_a_spec_at_construction(self) -> None:
        with self.assertRaises(ValueError):
            Icon("x", Profile.SUB32, semantic_role="SUB", keyshape=Keyshape.FREE)

    def test_a_spec_without_free_is_rejected(self) -> None:
        spec = FreeKeyshapeSpec(0, 14, 32, 18, "why", "id")
        with self.assertRaises(ValueError):
            Icon(
                "x", Profile.SUB32, semantic_role="SUB",
                keyshape=Keyshape.SQUARE, free_keyshape=spec,
            )

    def test_a_proposed_record_is_draft_only(self) -> None:
        """An agent may author against a proposed record; release still refuses."""
        from unittest.mock import patch

        from icon_set.model import contracts

        proposed = dict(contracts.approved_free_keyshapes())
        record = dict(proposed[("minus", "SUB32")])
        record["status"] = "proposed"
        proposed[("minus", "SUB32")] = record
        spec = FreeKeyshapeSpec(0, 14, 32, 18, "1-D bar glyph.", "FREE-2026-09-07-001")
        icon = self._minus(spec)
        with patch.object(contracts, "approved_free_keyshapes", lambda: proposed):
            release = [
                line for line in IconValidator().validate(icon).errors
                if line.startswith("schema/profile")
            ]
            draft = IconValidator(require_free_approval=False).validate(icon)
        self.assertTrue(any("'proposed'" in line for line in release))
        self.assertEqual(
            [line for line in draft.errors if line.startswith("schema/profile")], []
        )

    def test_free_bounds_outside_the_canvas_fail(self) -> None:
        spec = FreeKeyshapeSpec(-2, 14, 34, 18, "overflowing", "id")
        with self.assertRaises(ValueError):
            spec.bounds_for(Profile.SUB32)


class ValidatorSurfaceTests(unittest.TestCase):
    def test_every_check_runs_in_the_locked_order(self) -> None:
        icon = make("box", Keyshape.SQUARE, role="MAIN", kind="noun")
        icon.add_polyline("outline", (4, 4), (28, 4), (28, 28), (4, 28), closed=True)
        report = IconValidator().validate(icon)
        self.assertEqual(
            list(report.checks_run),
            [
                "schema/profile", "style/grid", "canvas/keyshape bounds", "mic",
                "keyshape", "composition", "svg round-trip", "reproducibility",
            ],
        )

    def test_an_empty_icon_fails(self) -> None:
        icon = make("empty", Keyshape.SQUARE)
        self.assertEqual(icon.validate_icon().status, "invalid")


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
