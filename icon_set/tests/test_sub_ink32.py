import io,unittest,xml.etree.ElementTree as ET
from svgpathtools import Document
from icon_set.scripts.sub_ink32 import normalize_ink32
from icon_set.scripts.combination_experiment import placement

class Ink32Tests(unittest.TestCase):
    def test_off_center_rectangle_preserves_ratio_and_centers_ink(self):
        doc='<svg xmlns="http://www.w3.org/2000/svg"><path d="M10 20H50V40H10Z"/></svg>'
        output,metrics=normalize_ink32(doc)
        boxes=[p.bbox() for p in Document(io.StringIO(output)).paths()]
        self.assertAlmostEqual(boxes[0][0],2)
        self.assertAlmostEqual(boxes[0][1],30)
        self.assertAlmostEqual(boxes[0][2],9)
        self.assertAlmostEqual(boxes[0][3],23)
        self.assertEqual(metrics['ink_width'],32)
        self.assertEqual(metrics['ink_height'],18)
        root=ET.fromstring(output)
        self.assertEqual(root.get('stroke-width'),'4')
        self.assertFalse(any(e.get('transform') for e in root.iter()))
    def test_curves_and_disconnected_round_dots_survive(self):
        doc='<svg xmlns="http://www.w3.org/2000/svg"><path d="M0 0C20 -30 30 60 40 20"/><path d="M50 10L50 10"/></svg>'
        output,metrics=normalize_ink32(doc)
        paths=Document(io.StringIO(output)).paths()
        self.assertEqual(len(paths),2)
        self.assertEqual(type(paths[0][0]).__name__,'CubicBezier')
        self.assertEqual(paths[1][0].start,paths[1][0].end)
        self.assertAlmostEqual(max(metrics['ink_width'],metrics['ink_height']),32)
        self.assertAlmostEqual(metrics['ink_bounds'][0]+metrics['ink_bounds'][2],32)
        self.assertAlmostEqual(metrics['ink_bounds'][1]+metrics['ink_bounds'][3],32)
    def test_auto_placement_does_not_round_or_shrink_normalized_export(self):
        item=dict(bounds=[2,7.37,30,24.63],canvas=32,family='solo')
        box=placement(item,32,(1,1),(0,0),size_lock='auto')['painted_box']
        self.assertAlmostEqual(box['w'],32)
        self.assertAlmostEqual(box['h'],21.26)
    def test_idempotent_ink_normalization(self):
        doc='<svg xmlns="http://www.w3.org/2000/svg"><circle cx="17" cy="33" r="10"/></svg>'
        first,a=normalize_ink32(doc);second,b=normalize_ink32(first)
        for before,after in zip(a['ink_bounds'],b['ink_bounds']):
            self.assertAlmostEqual(before,after)
        self.assertAlmostEqual(b['geometry_scale'],1)

    def test_all_icon_path_coordinates_snap_to_integer_grid(self):
        doc='<svg xmlns="http://www.w3.org/2000/svg"><path d="M1.2 3.7C12.4 -8.1 20.2 26.8 31.5 27.1"/></svg>'
        output,metrics=normalize_ink32(doc)
        for path in Document(io.StringIO(output)).paths():
            for segment in path:
                for attr in ('start','end','control','control1','control2'):
                    if hasattr(segment,attr):
                        z=getattr(segment,attr)
                        self.assertEqual(z.real,round(z.real))
                        self.assertEqual(z.imag,round(z.imag))
        self.assertEqual(metrics['grid'],1)
        self.assertAlmostEqual(max(metrics['ink_width'],metrics['ink_height']),32)

    def test_text_height_only_preserves_free_width(self):
        output,metrics=normalize_ink32('<svg xmlns="http://www.w3.org/2000/svg"><path d="M0 0H100V20H0Z"/></svg>',text=True)
        self.assertAlmostEqual(metrics['ink_height'],32)
        self.assertEqual(metrics['canvas_width'],144)
        self.assertEqual(metrics['grid'],1)

    def test_text_stem_snaps_in_final_canvas_coordinates(self):
        source='<svg xmlns="http://www.w3.org/2000/svg"><path d="M0 0V28M27.43 0V28H37.2C55.6 28 55.6 0 37.2 0Z"/></svg>'
        output,m=normalize_ink32(source,text=True)
        paths=Document(io.StringIO(output)).paths()
        self.assertEqual(paths[0][1].start.real,round(paths[0][1].start.real))
        self.assertEqual(m['ink_height'],32)
        self.assertGreater(m['canvas_width'],32)
        for p in paths:
            for seg in p:
                for point in (seg.start,seg.end):
                    self.assertEqual(point.real,round(point.real))
                    self.assertEqual(point.imag,round(point.imag))
