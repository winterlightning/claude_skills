import json
import unittest
import xml.etree.ElementTree as ET
from icon_set.model.icons.sub._base import Sub32
from icon_set.model.icons.sub._text_base import TextSub32, canvas_dimensions
from icon_set.model.keyshapes import Keyshape
from icon_set.scripts.migrate_sub_profiles import primitive_calls
from icon_set.scripts.profile_links import annotate, validate

class WideText(TextSub32):
    icon_id='test-wide-text'
    keyshape=Keyshape.SQUARE
    text_canvas_width=56
    text_ink_bounds=(0,0,56,32)
    def build(self):
        self.add_line('a',(2,2),(2,30))
        self.add_line('b',(54,2),(54,30))

class SubProfileMigrationTests(unittest.TestCase):
    def test_text_natural_width_is_rendered_and_validated(self):
        icon=WideText()
        root=ET.fromstring(icon.to_svg())
        self.assertEqual(root.get('viewBox'),'0 0 56 32')
        self.assertEqual(canvas_dimensions(icon),(56,32))
        self.assertEqual(icon.to_record()['sizing_mode'],'text-height32')
        self.assertTrue(icon.validate_icon().ok,icon.validate_icon().describe())

    def test_text_overflow_and_wrong_height_still_fail(self):
        icon=WideText();icon.add_line('overflow',(58,2),(58,30))
        self.assertTrue(any('leaves' in e for e in icon.validate_icon().errors))
        icon=WideText();icon.text_ink_bounds=(0,0,56,30)
        self.assertTrue(any('height 32' in e for e in icon.validate_icon().errors))

    def test_square_sub_does_not_inherit_text_exception(self):
        class Square(Sub32):
            icon_id='test-square-sub'
            def build(self):self.add_line('wide',(2,2),(54,30))
        icon=Square();icon.text_canvas_width=56
        self.assertEqual(canvas_dimensions(icon),(32,32))
        self.assertFalse(icon.validate_icon().ok)

    def test_rotated_arc_preserves_ellipse_axes(self):
        svg='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 40 32" stroke-width="4"><path d="M2 16 A14 10 90 0 1 22 16"/></svg>'
        calls=primitive_calls(svg,text=True)
        self.assertTrue(any('radius_x=10, radius_y=14' in s for s in calls))
        with self.assertRaises(ValueError):primitive_calls(svg)

    def test_link_validation_keeps_variant_ancestry_separate(self):
        from types import SimpleNamespace
        registry={'a':SimpleNamespace(family='solo'),'b':SimpleNamespace(family='sub')}
        links=[{'source':'solo/a','target':'sub/b'}]
        validate(links,registry)
        with self.assertRaises(ValueError):validate(links+links,registry)
        with self.assertRaises(ValueError):validate([{'source':'solo/missing','target':'sub/b'}],registry)

    def test_text_graph_round_trip_preserves_width_and_validation(self):
        from icon_set.scripts.edit_validation import icon_from_graph
        original=WideText()
        restored=icon_from_graph(original.to_record())
        self.assertEqual(restored.to_svg(),original.to_svg())
        self.assertTrue(restored.validate_icon().ok)

    def test_open_returning_path_does_not_acquire_close_command(self):
        svg='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" stroke-width="4"><path d="M15 9 A1 1 0 0 1 17 9 A1 1 0 0 1 15 9"/></svg>'
        calls=primitive_calls(svg)
        self.assertIn('closed=False',calls[-1])

    def test_original_integer_arc_radii_are_not_autoscaled_in_source(self):
        svg='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" stroke-width="4"><path d="M28 4 A2 2 0 0 1 25 7"/></svg>'
        self.assertIn('radius_x=2, radius_y=2',primitive_calls(svg)[0])

    def test_rectangular_hole_measurement_uses_design_units_without_squeezing(self):
        from icon_set.validation.library_qa import measure_negative_space
        base='<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="32" viewBox="0 0 {w} 32" fill="none" stroke="black" stroke-width="4"><path d="M4 4H28V28H4Z"/></svg>'
        square=measure_negative_space(base.format(w=32),32)
        wide=measure_negative_space(base.format(w=96),(96,32))
        self.assertEqual(square['status'],wide['status'])
        self.assertEqual(square['holes'],wide['holes'])

    def test_point_only_text_scales_caps_and_spacing_to_height32(self):
        from icon_set.model.icons.sub.container_content_text_51708702_sub32 import Drawing
        from icon_set.scripts.edit_validation import icon_from_graph
        from icon_set.validation.envelope import visible_bounds
        icon=Drawing()
        self.assertEqual(visible_bounds(icon.draw().primitives, icon.STROKE_WIDTH/2),(0,0,256,32))
        self.assertEqual(icon_from_graph(icon.to_record()).to_svg(),icon.to_svg())
        self.assertTrue(icon.validate_icon().ok,icon.validate_icon().describe())
        source='<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32" stroke-width="4"><path d="M2 16L2 16"/><path d="M16 16L16 16"/><path d="M30 16L30 16"/></svg>'
        self.assertIn('(240, 16)',primitive_calls(source,text=True)[-2])
        icon.add_line('non-dot',(16,16),(20,16))
        self.assertTrue(any('stroke width' in e for e in icon.validate_icon().errors))
