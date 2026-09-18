import unittest
from shapely.geometry import Point, Polygon, box
from icon_set.scripts.container_square_fit import assess_square,fit_center,square

class SquareFitTests(unittest.TestCase):
    def test_circle_accepts_32_but_not_48(self):
        zone=Point(32,32).buffer(26,quad_segs=128)
        self.assertEqual(assess_square(zone,zone,32)['status'],'fits')
        self.assertEqual(assess_square(zone,zone,48)['status'],'too-small')

    def test_bounds_are_insufficient_for_diamond(self):
        zone=Polygon([(32,6),(58,32),(32,58),(6,32)])
        self.assertEqual(assess_square(zone,zone,32)['status'],'too-small')

    def test_exact_fit_is_borderline(self):
        zone=box(0,0,32,32)
        self.assertEqual(assess_square(zone,zone,32)['status'],'borderline')

    def test_hole_cannot_hide_inside_square(self):
        zone=box(0,0,40,40).difference(box(19,19,21,21))
        self.assertEqual(assess_square(zone,zone,32)['status'],'too-small')

    def test_shifted_placement_found_in_concave_polygon(self):
        zone=box(0,0,34,34).union(box(32,0,64,8))
        result=assess_square(zone,zone,32,[32,16])
        self.assertEqual(result['status'],'fits')
        self.assertFalse(result['fits_at_preferred_center'])
        self.assertTrue(zone.covers(square(result['placement_center_units'],32)))

    def test_outside_not_allowed_even_if_boundary_far_away(self):
        zone=box(0,0,20,20)
        self.assertIsNone(fit_center(zone,32))

if __name__=='__main__':unittest.main()
