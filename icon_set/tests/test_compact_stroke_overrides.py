"""Explicit compact exceptions preserve frames, readable inner strokes and default exports."""
import unittest
import xml.etree.ElementTree as ET
from icon_set.model.icons.sub._base import Sub32
from icon_set.renderers.svg import render_svg
from icon_set.renderers.png import render_png
import io
from PIL import Image

class Example(Sub32):
    icon_id='test-compact-strokes'
    STROKE_WIDTH=2
    PATH_STROKE_WIDTHS={'frame':4}
    def build(self):
        self.add_arc('a',(2,16),(30,16),radius_x=14)
        self.add_arc('b',(30,16),(2,16),radius_x=14)
        self.add_contour('frame','a','b',closed=True)
        self.add_line('inner',(16,10),(16,22))

class CompactStrokeTests(unittest.TestCase):
    def test_native_svg_and_png_keep_mixed_widths(self):
        m=Example();root=ET.fromstring(render_svg(m));paths={p.get('id'):p for p in root if p.get('id')}
        self.assertEqual(root.get('viewBox'),'0 0 32 32')
        self.assertEqual(root.get('stroke-width'),'2')
        self.assertEqual(paths['frame'].get('stroke-width'),'4')
        self.assertIsNone(paths['inner'].get('stroke-width'))
        png=Image.open(io.BytesIO(render_png(m))).convert('RGBA')
        self.assertEqual(png.size,(32,32))
        # A 4px circular boundary reaches the canvas edge; the thin inner stroke stays 2px.
        self.assertGreater(png.getpixel((0,16))[3],0)
        self.assertEqual(png.getpixel((14,16))[3],0)
        self.assertGreater(png.getpixel((15,16))[3],0)
    def test_default_export_has_no_path_override(self):
        m=Example();m.PATH_STROKE_WIDTHS={};root=ET.fromstring(render_svg(m))
        self.assertTrue(all(p.get('stroke-width') is None for p in root))
    def test_unknown_and_invalid_widths_fail(self):
        for overrides in ({'missing':2},{'frame':0},{'frame':float('nan')}):
            m=Example();m.PATH_STROKE_WIDTHS=overrides
            with self.assertRaises(ValueError):render_svg(m)
