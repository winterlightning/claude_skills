"""Explicit resize envelopes retain ordinary symbol validation and exports."""
import unittest
from icon_set.model.icons.symbol._resize_base import ResizeSymbol
from icon_set.model.icons.symbol._base import Symbol32
from icon_set.model.icons.sub._text_base import canvas_dimensions
from icon_set.model.keyshapes import Keyshape

class Wide(ResizeSymbol):
    icon_id = 'test-container-resize'
    canvas_width, canvas_height = 40, 32
    def build(self):
        self.add_polyline('frame', (2,2), (38,2), (38,30), (2,30), (2,2))

class ContainerResizeTests(unittest.TestCase):
    def test_native_placement_and_rectangular_art_reader(self):
        from icon_set.scripts.combination_experiment import placement
        from icon_set.scripts.container_placement import Artwork
        m=Wide()
        art=Artwork.read(m.to_svg(),(40,32))
        item=dict(bounds=art.bounds,canvas=32,canvas_width=40,canvas_height=32,
                  sizing_mode=m.sizing_mode)
        for lock in ('none','auto'):
            result=placement(item,32,(.5,.5),(0,0),size_lock=lock)
            self.assertEqual(result['painted_box'],dict(x=12,y=16,w=40,h=32))
        with self.assertRaises(ValueError):
            placement(item,32,(.5,.5),(0,0),size_lock='width',bound_size=24)
        with self.assertRaises(ValueError):Artwork.read(m.to_svg(),32)
    def test_native_dimensions_and_stroke(self):
        m=Wide()
        self.assertEqual(canvas_dimensions(m),(40,32))
        self.assertEqual(m.validate_icon().status,'valid')
        self.assertIn('viewBox="0 0 40 32"',m.to_svg())
        self.assertIn('stroke-width="4"',m.to_svg())
        self.assertEqual(m.to_record()['canvas_width'],40)
    def test_exact_envelope_and_grid_still_required(self):
        m=Wide();m.primitives.pop()
        m.contours.clear()
        m.add_line('off-grid',(5.5,10),(10,10))
        self.assertEqual(m.validate_icon().status,'invalid')
        m=Wide();m.canvas_width=42
        self.assertEqual(m.validate_icon().status,'invalid')
        m=Wide();m.canvas_width=38
        self.assertEqual(m.validate_icon().status,'invalid')
    def test_reduced_stroke_and_radial_escape_rejected(self):
        m=Wide();m.STROKE_WIDTH=2
        self.assertEqual(m.validate_icon().status,'invalid')
        m=Wide();m.keyshape=Keyshape.CIRCLE
        self.assertEqual(m.validate_icon().status,'invalid')
    def test_internal_clearance_still_required(self):
        m=Wide();m.add_line('crowded',(6,10),(6,22))
        self.assertEqual(m.validate_icon().status,'invalid')
    def test_invalid_dimensions_rejected_and_default_unchanged(self):
        for w in (3,61,39.6):
            m=Wide();m.canvas_width=w
            with self.assertRaises(ValueError):canvas_dimensions(m)
        class Ordinary(Symbol32):
            icon_id='test-ordinary-symbol'
            def build(self):
                self.add_polyline('frame',(2,2),(30,2),(30,30),(2,30),(2,2))
        m=Ordinary();self.assertEqual(canvas_dimensions(m),(32,32))
        self.assertEqual(m.validate_icon().status,'valid')
