import unittest
from shapely.geometry import Polygon
from icon_set.scripts.audit_container_centers import choose_center

class CenterAuditTests(unittest.TestCase):
    def test_rectangle_center_not_arbitrary_medial_axis_point(self):
        chosen,centroid,pole=choose_center(Polygon([(6,8),(58,8),(58,40),(6,40)]))
        self.assertEqual((chosen.x,chosen.y),(32,24))
        self.assertLess(pole.distance(centroid),.001)

    def test_triangle_uses_balance_point_not_bounds_midpoint(self):
        chosen,centroid,pole=choose_center(Polygon([(0,0),(12,0),(0,12)]))
        self.assertEqual((chosen.x,chosen.y),(4,4))

    def test_concave_zone_centroid_outside_uses_contained_fallback(self):
        poly=Polygon([(0,0),(10,0),(10,2),(2,2),(2,8),(10,8),(10,10),(0,10)])
        chosen,centroid,pole=choose_center(poly)
        self.assertFalse(poly.covers(centroid))
        self.assertTrue(poly.covers(chosen))

if __name__=='__main__':unittest.main()
