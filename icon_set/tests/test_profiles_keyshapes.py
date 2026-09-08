"""Profile constants and the 30 standard keyshape resolutions."""

from __future__ import annotations

import unittest

from icon_set.model import contracts
from icon_set.model.keyshapes import (
    Keyshape,
    KeyshapeSize,
    ReservedKeyshapeError,
    resolve_token,
)
from icon_set.model.profiles import Profile

STANDARD = tuple(shape for shape in Keyshape if shape is not Keyshape.FREE)


class ProfileSpecTests(unittest.TestCase):
    def test_locked_constants(self) -> None:
        expected = {
            Profile.SUB32: (32, 4, 2, 6),
            Profile.SOLO48: (48, 6, 2, 6),
            Profile.CONTAINER64: (64, 8, 2, 6),
        }
        for profile, (canvas, inset, mic, spacing) in expected.items():
            spec = profile.spec
            self.assertEqual(spec.canvas_size, canvas)
            self.assertEqual(spec.interior_guide_inset, inset)
            self.assertEqual(spec.mic, mic)
            self.assertEqual(spec.equal_stroke_centerline_min, spacing)

    def test_minimum_spacing_is_mic_plus_stroke(self) -> None:
        for profile in Profile:
            spec = profile.spec
            self.assertEqual(spec.equal_stroke_centerline_min, spec.mic + 4)

    def test_interior_guide_bounds(self) -> None:
        self.assertEqual(Profile.SUB32.spec.interior_guide_bounds, (4, 4, 28, 28))
        self.assertEqual(Profile.SOLO48.spec.interior_guide_bounds, (6, 6, 42, 42))
        self.assertEqual(Profile.CONTAINER64.spec.interior_guide_bounds, (8, 8, 56, 56))

    def test_profiles_are_named_for_their_family_and_canvas(self) -> None:
        for profile in Profile:
            with self.subTest(profile=profile.name):
                self.assertEqual(profile.name, f"{profile.family.upper()}{profile.spec.canvas_size}")

    def test_family_binding_is_one_to_one(self) -> None:
        families = contracts.families()
        self.assertEqual(set(families), {"sub", "solo", "container"})
        self.assertEqual({Profile.for_family(f) for f in families}, set(Profile))
        for family in families:
            self.assertEqual(Profile.for_family(family).family, family)
        with self.assertRaises(ValueError):
            Profile.for_family("primitive")

    def test_centers(self) -> None:
        self.assertEqual(Profile.SUB32.spec.center, (16, 16))
        self.assertEqual(Profile.SOLO48.spec.center, (24, 24))
        self.assertEqual(Profile.CONTAINER64.spec.center, (32, 32))


class KeyshapeResolutionTests(unittest.TestCase):
    def test_ten_base_definitions(self) -> None:
        self.assertEqual(len(STANDARD), 10)

    def test_thirty_resolutions_match_the_contract(self) -> None:
        table = contracts.keyshapes()["resolved"]
        count = 0
        for profile in Profile:
            for shape in STANDARD:
                row = table[profile.name][shape.name]
                size = shape.size_for(profile)
                self.assertEqual([size.width, size.height], [row["width"], row["height"]])
                self.assertEqual(list(shape.bounds_for(profile)), row["visible_bounds"])
                count += 1
        self.assertEqual(count, 30)

    def test_solo48_is_exactly_one_and_a_half_times_sub32(self) -> None:
        for shape in STANDARD:
            base = shape.size_for(Profile.SUB32)
            main = shape.size_for(Profile.SOLO48)
            self.assertEqual(main.width * 2, base.width * 3)
            self.assertEqual(main.height * 2, base.height * 3)

    def test_container64_is_exactly_twice_sub32(self) -> None:
        for shape in STANDARD:
            base = shape.size_for(Profile.SUB32)
            composite = shape.size_for(Profile.CONTAINER64)
            self.assertEqual(composite.width, base.width * 2)
            self.assertEqual(composite.height, base.height * 2)

    def test_horizontal_and_vertical_are_transposes(self) -> None:
        pairs = (
            (Keyshape.HRECT_XL, Keyshape.VRECT_XL),
            (Keyshape.HRECT_L, Keyshape.VRECT_L),
            (Keyshape.HRECT_M, Keyshape.VRECT_M),
            (Keyshape.HRECT_S, Keyshape.VRECT_S),
        )
        for horizontal, vertical in pairs:
            for profile in Profile:
                across = horizontal.size_for(profile)
                down = vertical.size_for(profile)
                self.assertEqual(KeyshapeSize(down.height, down.width), across)

    def test_xl_l_m_s_descend(self) -> None:
        order = (Keyshape.HRECT_XL, Keyshape.HRECT_L, Keyshape.HRECT_M, Keyshape.HRECT_S)
        heights = [shape.size_for(Profile.SUB32).height for shape in order]
        self.assertEqual(heights, sorted(heights, reverse=True))

    def test_bounds_are_centered_integers(self) -> None:
        for profile in Profile:
            canvas = profile.spec.canvas_size
            for shape in STANDARD:
                left, top, right, bottom = shape.bounds_for(profile)
                self.assertEqual(left, canvas - right)
                self.assertEqual(top, canvas - bottom)
                for value in (left, top, right, bottom):
                    self.assertIsInstance(value, int)

    def test_reserved_xs_tokens_fail(self) -> None:
        for token in ("HRECT_XS", "VRECT_XS", "hrect-xs", "vrect-xs"):
            with self.assertRaises(ReservedKeyshapeError):
                resolve_token(token)

    def test_free_requires_explicit_dimensions(self) -> None:
        with self.assertRaises(ValueError):
            Keyshape.FREE.size_for(Profile.SUB32)

    def test_circle_radius(self) -> None:
        self.assertEqual(Keyshape.CIRCLE.visible_radius_for(Profile.SUB32), 16.0)
        self.assertEqual(Keyshape.CIRCLE.centerline_radius_for(Profile.SUB32), 14.0)
        self.assertEqual(Keyshape.CIRCLE.visible_radius_for(Profile.CONTAINER64), 32.0)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
