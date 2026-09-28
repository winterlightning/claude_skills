"""Complete reference redraw on SUB32; earlier incomplete variant preserved.
Source parts: frame, plus, minus.
Construction: native 32px layout, 4px strokes, integer nodes; complete source comparison.

"""
from icon_set.model.icons.sub._base import Sub32
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = '3f98c7ee-fee3-4e59-a8f0-396c97cdef92'
SOURCE_PATH = 'pictographic-primitives/state/circle math_3f98c7ee-fee3-4e59-a8f0-396c97cdef92.svg'
AUTHOR = 'gpt-6'
class CompleteReferenceRedraw(Sub32):
    icon_id = 'plus-minus-sign-state-64-v2'
    variant_of = 'plus-minus-sign-state-64'
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
        self.add_line('plus-0-0', (10, 12), (22, 12))
        self.add_line('plus-1-0', (16, 9), (16, 16))
        self.add_line('minus-0-0', (12, 22), (20, 22))
        self.relate('connect', 'plus-0-0', 'plus-1-0')
