"""Complete reference redraw on SUB32; earlier incomplete variant preserved.
Source parts: outer, middle, inner.
Construction: native 32px layout, 4px strokes, integer nodes; complete source comparison.

"""
from icon_set.model.icons.sub._base import Sub32
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = 'a2bdace2-2a1a-4fef-a5e1-bc6b29bda0f7'
SOURCE_PATH = 'pictographic-primitives/state/smart_a2bdace2-2a1a-4fef-a5e1-bc6b29bda0f7.svg'
AUTHOR = 'gpt-6'
class CompleteReferenceRedraw(Sub32):
    icon_id = 'wireless-arcs-v2'
    variant_of = 'wireless-arcs'
    variant_label = 'Complete reference redraw'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    def build(self):
        self.add_bezier('outer-0-0', (2, 10), ((7.0, 7.0), (11.0, 6.0), (16, 6)))
        self.add_bezier('outer-0-1', (16, 6), ((21.0, 6.0), (25.0, 7.0), (30, 10)))
        self.add_contour('outer-0', 'outer-0-0', 'outer-0-1', closed=False)
        self.add_bezier('middle-0-0', (8, 18), ((12.0, 14.0), (20.0, 14.0), (24, 18)))
        self.add_bezier('inner-0-0', (13, 26), ((15.0, 24.0), (17.0, 24.0), (19, 26)))
