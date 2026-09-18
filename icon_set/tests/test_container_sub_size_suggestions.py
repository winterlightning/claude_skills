import unittest
import xml.etree.ElementTree as ET
from shapely.geometry import box
from icon_set.scripts.suggest_container_sub_size import transform,measure,preview
from icon_set.scripts.container_placement import Artwork
from icon_set.scripts.container_vector_geometry import VectorInk


def artwork(path,canvas):
    return Artwork.read(f'<svg viewBox="0 0 {canvas} {canvas}" fill="none" stroke="black" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"><path d="{path}"/></svg>',canvas)

class SubSizeSuggestionsTests(unittest.TestCase):
    def setUp(self):
        self.sub=artwork('M16 2V30M2 16H30',32)

    def test_reduced_ink_footprint_is_24_with_four_unit_stroke(self):
        ink=VectorInk.from_art(self.sub,transform(24,[32,32]))
        x0,y0,x1,y1=ink.lines.bounds
        self.assertAlmostEqual(x1-x0+4,24)
        self.assertAlmostEqual(y1-y0+4,24)
        self.assertEqual(transform(32,[32,32]),(1,16,16))

    def test_recommends_24_only_when_it_passes(self):
        host=VectorInk.from_art(artwork('M15 15H49V49H15Z',64))
        r=measure(host,self.sub,[32,32],box(19,19,45,45),box(19,19,45,45))
        self.assertEqual(r['recommendation'],'suggest-24')
        self.assertEqual(r['trials']['32']['status'],'fail')
        self.assertEqual(r['trials']['24']['status'],'pass')

    def test_keeps_32_when_both_fit(self):
        host=VectorInk.from_art(artwork('M2 2H62V62H2Z',64))
        r=measure(host,self.sub,[32,32],box(6,6,58,58),box(6,6,58,58))
        self.assertEqual(r['recommendation'],'keep-32')

    def test_missing_interior_does_not_receive_size_approval(self):
        host=VectorInk.from_art(artwork('M2 2H62V62H2Z',64))
        self.assertEqual(measure(host,self.sub,[32,32],None,None)['recommendation'],'review')

    def test_small_container_is_not_falsely_approved(self):
        host=VectorInk.from_art(artwork('M22 22H42V42H22Z',64))
        self.assertEqual(measure(host,self.sub,[32,32],box(26,26,38,38),box(26,26,38,38))['recommendation'],'no-fit-at-center')

    def test_preview_retains_effective_stroke_and_measured_position(self):
        h=artwork('M2 2H62V62H2Z',64)
        svg=ET.fromstring(preview(h,self.sub,[32,35],24))
        group=list(svg)[1]
        self.assertAlmostEqual(float(group.get('stroke-width'))*transform(24,[32,35])[0],4)
        self.assertIn('scale(0.7142857143)',group.get('transform'))

if __name__=='__main__':unittest.main()
