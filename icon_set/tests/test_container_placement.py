import unittest
from icon_set.scripts.container_placement import Artwork, validate_padding, validate_area, place


def art(path, canvas=64):
    return Artwork.read(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {canvas} {canvas}"><path d="{path}" fill="none" stroke="black" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/></svg>',canvas)


class PlacementTests(unittest.TestCase):
    def test_exact_ink_gap(self):
        host=art('M60 4V60')
        self.assertEqual(validate_padding(host,art('M54 10V50'),(1,0,0),2)['status'],'pass')
        self.assertEqual(validate_padding(host,art('M54.5 10V50'),(1,0,0),2)['status'],'fail')

    def test_crossing_is_never_exempt(self):
        self.assertEqual(validate_padding(art('M4 32H60'),art('M32 4V60'),(1,0,0),2)['status'],'fail')

    def test_saved_area_identity(self):
        area={'source_sha256':'old','polygon':[[4,4],[60,4],[60,60],[4,60]],'center':[32,32],'status':'reviewed'}
        with self.assertRaisesRegex(ValueError,'stale'):validate_area(area,'new')
        area['source_sha256']='new';area['polygon']=[[4,4],[60,60],[4,60],[60,4]]
        with self.assertRaises(ValueError):validate_area(area,'new')

    def test_automatic_area_needs_review(self):
        result=place(art('M4 4H60V60H4Z'),art('M12 24H36 M24 12V36',48))
        self.assertEqual(result['status'],'review-area')
        self.assertEqual(result['placement']['stroke'],4)
        self.assertEqual(result['validation']['status'],'pass')

    def test_center_only_preserves_requested_center_without_safe_zone(self):
        host=art('M4 4H60V60H4Z M32 4V60')
        area={'source_sha256':host.sha256,'kind':'center-only','center':[32,32],
              'status':'reviewed','composition_mode':'overlay'}
        result=place(host,art('M12 24H36 M24 12V36',48),area=area)
        self.assertEqual(result['placement']['center'],[32,32])
        self.assertEqual(result['status'],'review-overlay')
        self.assertFalse(result['validation']['safe_zone_claimed'])
        self.assertEqual(result['validation']['status'],'fail')

    def test_css_source_uses_current_geometry(self):
        a=Artwork.read('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48"><style>.ink{stroke:black;stroke-width:4;fill:none;stroke-linecap:round;stroke-linejoin:round}</style><path class="ink" d="M10 12L30 36"/></svg>',48)
        self.assertEqual(a.bounds,(10,12,30,36))

if __name__=='__main__':unittest.main()
