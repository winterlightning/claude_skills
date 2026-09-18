"""Complete reference redraw on SUB32; earlier incomplete variant preserved.
Source parts: frame, glyph-0-0.
Construction: native 32px layout, 4px strokes, integer nodes; complete source comparison.
Typeface reuse: digit-0
"""
from icon_set.model.icons.sub._base import Sub32
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = 'e3714f65-499d-4ba7-9ecb-87ecc26acfff'
SOURCE_PATH = 'pictographic-primitives/state/0 text in circle_e3714f65-499d-4ba7-9ecb-87ecc26acfff.svg'
AUTHOR = 'gpt-6'
class CompleteReferenceRedraw(Sub32):
    icon_id = 'zero-v2'
    variant_of = 'zero'
    variant_label = 'Complete reference redraw'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    def build(self):
        self.add_arc('frame-0-0', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=True, sweep=True)
        self.add_arc('frame-0-1', (30, 16), (2, 16), radius_x=14, radius_y=14, large_arc=True, sweep=True)
        self.add_contour('frame-0', 'frame-0-0', 'frame-0-1', closed=True)
        self.add_arc('glyph-0-0-0-0', (11, 13), (21, 13), radius_x=5, radius_y=4, large_arc=False, sweep=True)
        self.add_line('glyph-0-0-0-1', (21, 13), (21, 19))
        self.add_arc('glyph-0-0-0-2', (21, 19), (11, 19), radius_x=5, radius_y=4, large_arc=False, sweep=True)
        self.add_line('glyph-0-0-0-3', (11, 19), (11, 13))
        self.add_contour('glyph-0-0-0', 'glyph-0-0-0-0', 'glyph-0-0-0-1', 'glyph-0-0-0-2', 'glyph-0-0-0-3', closed=True)
