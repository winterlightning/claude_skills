import math
import unittest
from shapely.geometry import box
from icon_set.scripts.container_vector_geometry import VectorInk, read_art, vector_zone, check_pair, pair_groups


def art(path):
    return read_art(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" fill="none" stroke="black" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"><path d="{path}"/></svg>')


def zone(ink, polygon=None):
    return vector_zone(ink, {'kind':'safe-zone', 'method':'selected semantic enclosed face',
                            'polygon':polygon or [[10,10],[54,10],[54,54],[10,54]]})


class VectorGeometryTests(unittest.TestCase):
    def test_rectangle_analytic_area_and_center(self):
        ink = VectorInk.from_art(art('M4 4H60V60H4Z'))
        info, inner, outer = zone(ink)
        self.assertEqual(info['status'], 'vector')
        self.assertLessEqual(inner.area, 48**2)
        self.assertGreaterEqual(outer.area, 48**2)
        self.assertAlmostEqual(info['center_units'][0],32,places=6)
        self.assertAlmostEqual(info['center_units'][1],32,places=6)
        self.assertLess(outer.area-inner.area,.03)

    def test_circle_analytic_area_enclosed_by_bounds(self):
        ink = VectorInk.from_art(art('M2 32A30 30 0 0 1 62 32A30 30 0 0 1 2 32Z'))
        info, inner, outer = zone(ink, [[20,20],[44,20],[44,44],[20,44]])
        exact = math.pi*26**2
        self.assertLessEqual(inner.area,exact)
        self.assertGreaterEqual(outer.area,exact)
        self.assertLess(outer.area-inner.area,1)

    def test_selector_does_not_limit_new_boundary(self):
        ink = VectorInk.from_art(art('M4 4H60V60H4Z'))
        a, _, _ = zone(ink)
        b, _, _ = zone(ink, [[30,30],[34,30],[34,34],[30,34]])
        self.assertEqual(a['bounds_units'],b['bounds_units'])

    def test_spacing_threshold_and_overlap(self):
        host = VectorInk.from_art(art('M4 10H60'))
        for y, expected in [(16.01,'pass'),(15.99,'fail'),(16,'review'),(12,'fail')]:
            sub = VectorInk.from_art(art(f'M10 {y}H50'))
            result = check_pair(host,sub,box(0,0,64,64),box(0,0,64,64))
            self.assertEqual(result['gap_status'],expected)
            exact=max(0,y-14)
            self.assertLessEqual(result['ink_gap_lower_units'],exact)
            self.assertGreaterEqual(result['ink_gap_upper_units'],exact)

    def test_clear_gap_outside_container_is_not_pass(self):
        host = VectorInk.from_art(art('M20 20H44V44H20Z'))
        _, inner, outer = zone(host, [[25,25],[39,25],[39,39],[25,39]])
        sub = VectorInk.from_art(art('M4 4H12'))
        result = check_pair(host,sub,inner,outer)
        self.assertEqual(result['gap_status'],'pass')
        self.assertEqual(result['containment_status'],'fail')
        self.assertEqual(result['status'],'fail')

    def test_open_face_is_not_fabricated(self):
        host=VectorInk.from_art(art('M4 4V60H60V4'))
        info, inner, outer=zone(host)
        self.assertEqual(info['status'],'review')
        self.assertIsNone(inner)

    def test_manual_boundary_remains_review(self):
        host=VectorInk.from_art(art('M4 4H60V60H4Z'))
        info, _, _=vector_zone(host,{'kind':'safe-zone','method':'manually bounded content face'})
        self.assertEqual(info['status'],'review')

    def test_effects_are_rejected(self):
        with self.assertRaises(ValueError):
            read_art('<svg viewBox="0 0 64 64"><path stroke-dasharray="2 2" d="M4 4H60"/></svg>')

    def test_saved_scaled_pair_uses_actual_transform_and_stroke(self):
        document='''<svg viewBox="0 0 64 64" fill="none" stroke="black" stroke-linecap="round" stroke-linejoin="round"><g id="container" transform="translate(0 0) scale(1)" stroke-width="4"><path d="M4 4H60"/></g><g id="content" transform="translate(5 7) scale(0.5)" stroke-width="8"><path d="M10 10H30"/></g></svg>'''
        groups=pair_groups(document)
        sub=VectorInk.from_art(*groups['content'])
        self.assertEqual(sub.lines.bounds,(10,12,20,12))
        with self.assertRaises(ValueError):
            pair_groups(document.replace('stroke-width="8"','stroke-width="4"'))

if __name__=='__main__':unittest.main()
