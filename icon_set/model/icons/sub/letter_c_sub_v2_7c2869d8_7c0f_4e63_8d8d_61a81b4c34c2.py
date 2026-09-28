"""Complete reference redraw on SUB32; earlier incomplete variant preserved.
Source parts: frame, glyph-0-0.
Construction: native 32px layout, 4px strokes, integer nodes; complete source comparison.
Typeface reuse: letter-c-uppercase
"""
from icon_set.model.icons.sub._base import Sub32
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = '7c2869d8-7c0f-4e63-8d8d-61a81b4c34c2'
SOURCE_PATH = 'pictographic-primitives/state/circle c_7c2869d8-7c0f-4e63-8d8d-61a81b4c34c2.svg'
AUTHOR = 'gpt-6'
class CompleteReferenceRedraw(Sub32):
    icon_id = 'letter-c-sub-v2'
    variant_of = 'letter-c-sub'
    variant_label = 'Complete reference redraw'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    def build(self):
        self.add_arc('frame-0-0', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=True, sweep=True)
        self.add_arc('frame-0-1', (30, 16), (2, 16), radius_x=14, radius_y=14, large_arc=True, sweep=True)
        self.add_contour('frame-0', 'frame-0-0', 'frame-0-1', closed=True)
        self.add_arc('glyph-0-0-0-0', (20, 11), (20, 21), radius_x=5, radius_y=7, large_arc=True, sweep=False)
