"""Complete reference redraw on SUB32; earlier incomplete variant preserved.
Source parts: frame, glyph-0-0.
Construction: native 32px layout, 4px strokes, integer nodes; complete source comparison.
Typeface reuse: letter-l-uppercase
"""
from icon_set.model.icons.sub._base import Sub32
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = 'a05df7de-5aec-4ad6-b118-d2d02268088c'
SOURCE_PATH = 'pictographic-primitives/state/circle L_a05df7de-5aec-4ad6-b118-d2d02268088c.svg'
AUTHOR = 'gpt-6'
class CompleteReferenceRedraw(Sub32):
    icon_id = 'letter-l-sub-v2'
    variant_of = 'letter-l-sub'
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
        self.add_line('glyph-0-0-0-0', (12, 10), (12, 22))
        self.add_line('glyph-0-0-0-1', (12, 22), (20, 22))
        self.add_contour('glyph-0-0-0', 'glyph-0-0-0-0', 'glyph-0-0-0-1', closed=False)
