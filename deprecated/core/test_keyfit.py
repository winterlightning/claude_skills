#!/usr/bin/env python3
"""Regression tests for the four canonical centered keyshapes."""

import unittest

from keyfit import assign, candidate_tokens, canonical_tokens, circle_overflow, contains, nearest, token_box


class KeyfitTests(unittest.TestCase):
    def test_exact_token_family(self):
        names = [token["name"] for token in canonical_tokens()]
        self.assertEqual(names, [
            "circle-44", "square-40", "portrait-36x44", "landscape-44x36",
        ])

    def test_centered_bounds(self):
        self.assertEqual(token_box(44, 44), (2, 2, 46, 46))
        self.assertEqual(token_box(40, 40), (4, 4, 44, 44))
        self.assertEqual(token_box(36, 44), (6, 2, 42, 46))
        self.assertEqual(token_box(44, 36), (2, 6, 46, 42))

    def test_smallest_oriented_token_is_selected_first(self):
        landscape = candidate_tokens((2, 6, 46, 42))
        self.assertEqual(landscape[0]["name"], "landscape-44x36")
        self.assertTrue(contains(token_box(landscape[0]["width"], landscape[0]["height"]), (2, 6, 46, 42)))

    def test_off_center_paint_fails_centered_token(self):
        self.assertFalse(contains(token_box(44, 36), (2, 5, 46, 41)))

    def test_target_must_be_reached_not_only_contained(self):
        self.assertIsNone(assign((6, 6, 42, 42), tolerance=0.01))
        target = nearest((6, 6, 42, 42))
        self.assertEqual(target["name"], "square-40")
        self.assertEqual(target["edgeDeltaToTarget"], {
            "left": 2, "top": 2, "right": 2, "bottom": 2,
        })

    def test_exact_horizontal_target_passes(self):
        assigned = assign((2, 6, 46, 42), tolerance=0.01)
        self.assertEqual(assigned["name"], "landscape-44x36")

    def test_nearest_target_preserves_orientation(self):
        target = nearest((4, 7, 44, 41))
        self.assertEqual(target["name"], "landscape-44x36")

    def test_circle_requires_radial_containment(self):
        self.assertLessEqual(circle_overflow([(24, 4), (44, 24)], stroke_width=4), 0)
        self.assertGreater(circle_overflow([(40, 8)], stroke_width=4), 0)


if __name__ == "__main__":
    unittest.main()
