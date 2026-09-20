"""Tall side exceptions retain ordinary SUB32 geometry and isolation rules."""
import sys
import unittest
from unittest.mock import patch
from icon_set.model.icons.sub._base import Sub32
from icon_set.model.icons.sub._tall_base import TallSideSub32
from icon_set.model.icons.sub._text_base import canvas_dimensions
from icon_set.model.keyshapes import Keyshape

SOURCE_ICON_ID = '8d317b81-2d88-4d5c-9090-0c063df565b3'


class Tall(TallSideSub32):
    icon_id = 'test-tall-side'
    keyshape = Keyshape.SQUARE

    def build(self):
        self.add_polyline('frame', (2, 2), (30, 2), (30, 46), (2, 46), (2, 2))


class Square(Sub32):
    icon_id = 'test-square-sub'

    def build(self):
        self.add_polyline('frame', (2, 2), (30, 2), (30, 30), (2, 30), (2, 2))


class TallSideTests(unittest.TestCase):
    def test_approved_tall_export_retains_four_pixel_stroke(self):
        icon = Tall()
        self.assertEqual(canvas_dimensions(icon), (32, 48))
        self.assertEqual(icon.validate_icon().status, 'valid')
        self.assertIn('viewBox="0 0 32 48"', icon.to_svg())
        self.assertIn('stroke-width="4"', icon.to_svg())
        self.assertEqual(icon.to_record()['canvas_height'], 48)
        self.assertEqual(icon.anchors['center'].as_tuple(), (16, 24))

    def test_unapproved_source_cannot_expand(self):
        with patch.object(sys.modules[__name__], 'SOURCE_ICON_ID', 'unapproved'):
            with self.assertRaisesRegex(ValueError, 'approved source'):
                Tall()

    def test_square_profile_is_unchanged(self):
        self.assertEqual(canvas_dimensions(Square()), (32, 32))
        self.assertEqual(Square().validate_icon().status, 'valid')

    def test_tall_overflow_is_still_rejected(self):
        icon = Tall()
        icon.add_line('outside', (16, 46), (16, 48))
        self.assertEqual(icon.validate_icon().status, 'invalid')

    def test_tall_does_not_fit_square_container_slot(self):
        from icon_set.model.icons.combined import CombinedIcon
        from icon_set.model.icons.registry import create
        from icon_set.model.position import Position
        combined = CombinedIcon('test-placement', 'CONTAINER_COMBINE', Keyshape.CIRCLE,
                                icons=[create('container-circle'), Tall()],
                                positions=[Position(0, 0), Position(16, 16)])
        report = combined.validate_icon()
        self.assertTrue(any('square container-content' in str(e) for e in report.errors))

    def test_side_auto_placement_preserves_tall_size(self):
        from icon_set.scripts.combination_experiment import placement
        item = dict(bounds=[2,2,30,46], canvas=32, canvas_width=32,
                    canvas_height=48, sizing_mode='side-32x48')
        for anchor in ((0,0),(1,1),(1,.5)):
            p = placement(item,32,anchor,(0,0),size_lock='auto')
            self.assertEqual((p['painted_box']['w'],p['painted_box']['h']), (32,48))
            self.assertEqual(p['size_lock'],'none')
        with self.assertRaisesRegex(ValueError,'original 32×48'):
            placement(item,32,(1,1),(0,0),size_lock='height',bound_size=32)

class FlexibleSideTests(unittest.TestCase):
    def test_wide_exception_exports_and_places_without_scaling(self):
        from icon_set.model.icons.sub._tall_base import SideSub32Exception
        from icon_set.scripts.combination_experiment import placement
        class Wide(SideSub32Exception):
            icon_id = 'test-wide-side'
            keyshape = Keyshape.SQUARE
            canvas_width, canvas_height = 48, 32
            def build(self):
                self.add_polyline('frame', (2,2),(46,2),(46,30),(2,30),(2,2))
        icon=Wide()
        self.assertEqual(icon.validate_icon().status,'valid')
        self.assertEqual(canvas_dimensions(icon),(48,32))
        self.assertIn('viewBox="0 0 48 32"',icon.to_svg())
        self.assertIn('stroke-width="4"',icon.to_svg())
        p=placement(dict(bounds=[2,2,46,30],canvas=32,canvas_width=48,canvas_height=32,
                         sizing_mode='side-one-axis32'),32,(1,1),(0,0),size_lock='auto')
        self.assertEqual((p['painted_box']['w'],p['painted_box']['h']),(48,32))
        class Invalid(Wide):
            canvas_height=48
        with self.assertRaises(ValueError):Invalid()

class SourceFaithfulSizeTests(unittest.TestCase):
    def test_both_axes_may_grow_without_changing_stroke(self):
        from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
        from icon_set.scripts.combination_experiment import placement
        class Full(SourceFaithfulSideSub):
            icon_id='test-complete-source'
            keyshape=Keyshape.SQUARE
            canvas_width=48
            canvas_height=56
            def build(self):
                self.add_polyline('frame',(2,2),(46,2),(46,54),(2,54),(2,2))
        m=Full()
        self.assertEqual(m.validate_icon().status,'valid')
        self.assertEqual(canvas_dimensions(m),(48,56))
        self.assertIn('stroke-width="4"',m.to_svg())
        p=placement(dict(bounds=[2,2,46,54],canvas_width=48,canvas_height=56,
                         sizing_mode='side-source-fit'),32,(1,1),(0,0))
        self.assertEqual((p['painted_box']['w'],p['painted_box']['h']),(48,56))
        with self.assertRaisesRegex(ValueError,'larger combination canvas'):
            placement(dict(bounds=[2,2,62,62],canvas_width=64,canvas_height=64,
                           sizing_mode='side-source-fit'),32,(1,1),(0,0))
