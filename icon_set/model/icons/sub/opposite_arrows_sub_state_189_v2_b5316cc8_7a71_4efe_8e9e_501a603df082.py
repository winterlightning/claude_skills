"""Complete reference redraw on SUB32; earlier incomplete variant preserved.
Source parts: frame, left, right.
Construction: native 32px layout, 4px strokes, integer nodes; complete source comparison.

"""
from icon_set.model.icons.sub._base import Sub32
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = 'b5316cc8-7a71-4efe-8e9e-501a603df082'
SOURCE_PATH = 'pictographic-primitives/state/opposite arrows 1_b5316cc8-7a71-4efe-8e9e-501a603df082.svg'
AUTHOR = 'gpt-6'
class CompleteReferenceRedraw(Sub32):
    icon_id = 'opposite-arrows-sub-state-189-v2'
    variant_of = 'opposite-arrows-sub-state-189'
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
        self.add_line('left-0-0', (21, 12), (11, 12))
        self.add_line('left-0-1', (11, 12), (14, 9))
        self.add_contour('left-0', 'left-0-0', 'left-0-1', closed=False)
        self.add_line('left-1-0', (11, 12), (14, 14))
        self.add_line('right-0-0', (11, 21), (21, 21))
        self.add_line('right-0-1', (21, 21), (18, 19))
        self.add_contour('right-0', 'right-0-0', 'right-0-1', closed=False)
        self.add_line('right-1-0', (21, 21), (18, 23))
        self.relate('connect', 'left-0', 'left-1-0')
        self.relate('connect', 'right-0', 'right-1-0')
