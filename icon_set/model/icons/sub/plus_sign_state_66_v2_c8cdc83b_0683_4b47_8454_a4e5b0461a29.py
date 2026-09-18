"""Complete reference redraw on SUB32; earlier incomplete variant preserved.
Source parts: frame, horizontal, vertical.
Construction: native 32px layout, 4px strokes, integer nodes; complete source comparison.

"""
from icon_set.model.icons.sub._base import Sub32
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = 'c8cdc83b-0683-4b47-8454-a4e5b0461a29'
SOURCE_PATH = 'pictographic-primitives/state/circle medical cross_c8cdc83b-0683-4b47-8454-a4e5b0461a29.svg'
AUTHOR = 'gpt-6'
class CompleteReferenceRedraw(Sub32):
    icon_id = 'plus-sign-state-66-v2'
    variant_of = 'plus-sign-state-66'
    variant_label = 'Complete reference redraw'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    def build(self):
        self.add_arc('frame-0-0', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=True, sweep=True)
        self.add_arc('frame-0-1', (30, 16), (2, 16), radius_x=14, radius_y=14, large_arc=True, sweep=True)
        self.add_contour('frame-0', 'frame-0-0', 'frame-0-1', closed=True)
        self.add_line('horizontal-0-0', (10, 16), (22, 16))
        self.add_line('vertical-0-0', (16, 10), (16, 22))
        self.relate('connect', 'horizontal-0-0', 'vertical-0-0')
