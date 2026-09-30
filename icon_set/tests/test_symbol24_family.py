"""SYMBOL24: a 24x24 family with the library's uniform 4-unit stroke."""
import unittest
import xml.etree.ElementTree as ET

from icon_set.model.icons.symbol24._base import Symbol24
from icon_set.model.icons.sub._base import Sub32
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.scripts.symbol24 import convert_from32, strict_check_icon


class Frame(Symbol24):
    icon_id = 'test-symbol24-frame'

    def build(self):
        self.add_polyline('frame', (2, 2), (22, 2), (22, 22), (2, 22), closed=True)


class Plus32(Sub32):
    icon_id = 'test-symbol24-plus32'

    def build(self):
        self.add_line('h', (2, 16), (30, 16))
        self.add_line('v', (16, 2), (16, 30))
        self.relate('connect', 'h', 'v')


class Symbol24Tests(unittest.TestCase):
    def test_profile_and_keyshapes(self):
        self.assertEqual(Profile.for_family('symbol24'), Profile.SYMBOL24)
        spec = Profile.SYMBOL24.spec
        self.assertEqual((spec.canvas_size, spec.mic, spec.equal_stroke_centerline_min), (24, 2, 6))
        self.assertEqual(spec.center, (12, 12))
        self.assertEqual(Keyshape.SQUARE.bounds_for(Profile.SYMBOL24), (0, 0, 24, 24))
        self.assertEqual(Keyshape.CIRCLE.centerline_radius_for(Profile.SYMBOL24), 10)
        self.assertEqual(Keyshape.HRECT_L.bounds_for(Profile.SYMBOL24), (0, 3, 24, 21))
        self.assertEqual(Keyshape.VRECT_M.bounds_for(Profile.SYMBOL24), (4, 0, 20, 24))

    def test_full_square_validates_with_4_stroke(self):
        icon = Frame()
        self.assertEqual(icon.validate_icon().status, 'valid')
        root = ET.fromstring(icon.to_svg())
        self.assertEqual((root.get('width'), root.get('viewBox')), ('24', '0 0 24 24'))
        self.assertTrue(strict_check_icon(icon)['strict_24'] == 'pass')

    def test_parallel_minimum_is_6(self):
        icon = Frame()
        icon.add_line('bar', (8, 8), (16, 8))  # 6 from the top edge: allowed
        self.assertNotIn('mic', ' '.join(icon.validate_icon().errors))
        icon = Frame()
        icon.add_line('bar', (8, 6), (16, 6))  # 4 from the top edge: too close
        self.assertEqual(icon.validate_icon().status, 'invalid')

    def test_convert_from32_scales_three_quarters_onto_the_grid(self):
        text = convert_from32(Plus32(), icon_id='plus-symbol24', class_name='PlusSymbol24',
                              author='test-model', source_path=None)
        self.assertIn("self.add_line('h', (2, 12), (22, 12))", text)
        self.assertIn("self.add_line('v', (12, 2), (12, 22))", text)
        self.assertIn("self.relate('connect', 'h', 'v')", text)
        self.assertIn("DERIVED_FROM_32 = 'test-symbol24-plus32'", text)
        namespace = {}
        exec(compile(text.replace('from ...keyshapes', 'from icon_set.model.keyshapes')
                     .replace('from ._base', 'from icon_set.model.icons.symbol24._base'),
                     'draft', 'exec'), namespace)
        self.assertEqual(namespace['PlusSymbol24']().validate_icon().status, 'valid')


if __name__ == '__main__':
    unittest.main()
