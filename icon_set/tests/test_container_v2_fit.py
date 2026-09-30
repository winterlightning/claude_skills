"""The v2 container lattice keeps structure while it resizes."""

from __future__ import annotations

import unittest

from icon_set.scripts.container_v2_fit import AxisMap, _ring, allocate


class LatticeTests(unittest.TestCase):
    def test_outer_values_hit_the_target(self) -> None:
        table = allocate([2, 6, 10, 32, 54, 58, 62], 6, 58)
        self.assertEqual(table[2], 6)
        self.assertEqual(table[62], 58)

    def test_mirrored_values_stay_mirrored(self) -> None:
        table = allocate([2, 10, 20, 44, 54, 62], 6, 58)
        for value, mapped in table.items():
            self.assertEqual(64 - mapped, table[64 - value])

    def test_small_gaps_keep_their_size(self) -> None:
        # Gaps of 8 or less (stroke detail) survive; the long spans shrink.
        table = allocate([2, 6, 14, 50, 58, 62], 6, 58)
        self.assertEqual(table[6] - table[2], 4)
        self.assertEqual(table[14] - table[6], 8)
        self.assertEqual(table[62] - table[58], 4)

    def test_order_is_preserved(self) -> None:
        values = [2, 3, 9, 16, 30, 31, 33, 40, 61, 62]
        table = allocate(values, 6, 58)
        mapped = [table[v] for v in sorted(table)]
        self.assertEqual(mapped, sorted(set(mapped)))

    def test_shared_coordinates_move_together(self) -> None:
        axis = AxisMap(allocate([2, 22, 42, 62], 6, 58))
        self.assertEqual(axis.snap(22), axis.snap(22))
        self.assertAlmostEqual(axis(12), (axis.snap(2) + axis.snap(22)) / 2)

    def test_ring_points_are_exact(self) -> None:
        for x, y in _ring(20):
            self.assertEqual(x * x + y * y, 400)
        self.assertIn((12, 16), _ring(20))


if __name__ == "__main__":
    unittest.main()
