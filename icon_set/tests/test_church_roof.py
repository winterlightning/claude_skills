"""Prevent rounded strokes from hiding a kink in the church roof centerlines."""
import unittest
from icon_set.model.icons.registry import create


class ChurchRoofTests(unittest.TestCase):
    def test_each_roof_side_is_straight_through_its_wall_attachment(self):
        drawing = create('a-frame-church-sub32-v3').draw().by_id()
        for first, second in [('p1-r1-1', 'p1-r1-2'), ('p1-r1-3', 'p1-r1-4')]:
            a, b = drawing[first], drawing[second]
            self.assertEqual(a.end, b.start)
            ux, uy = a.end.x-a.start.x, a.end.y-a.start.y
            vx, vy = b.end.x-b.start.x, b.end.y-b.start.y
            self.assertEqual(ux*vy-uy*vx, 0, 'Roof centerline changes direction at the wall')
            self.assertGreater(ux*vx+uy*vy, 0, 'Roof folds back at the wall')
