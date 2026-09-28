"""Complete reference redraw on SUB32; earlier incomplete variant preserved.
Source parts: frame, handle, horizontal, vertical.
Construction: native 32px layout, 4px strokes, integer nodes; complete source comparison.

"""
from icon_set.model.icons.sub._base import Sub32
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = '7b93bc8d-d30f-4c36-872b-5f1688b6b3e8'
SOURCE_PATH = 'pictographic-primitives/state/magnifying glass add_7b93bc8d-d30f-4c36-872b-5f1688b6b3e8.svg'
AUTHOR = 'gpt-6'
class CompleteReferenceRedraw(Sub32):
    icon_id = 'plus-sign-state-153-v2'
    variant_of = 'plus-sign-state-153'
    variant_label = 'Complete reference redraw'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    def build(self):
        self.add_arc('frame-0-0', (2, 14), (26, 14), radius_x=12, radius_y=12, large_arc=True, sweep=True)
        self.add_arc('frame-0-1', (26, 14), (2, 14), radius_x=12, radius_y=12, large_arc=True, sweep=True)
        self.add_contour('frame-0', 'frame-0-0', 'frame-0-1', closed=True)
        self.add_line('handle-0-0', (22, 22), (30, 30))
        self.add_line('horizontal-0-0', (9, 14), (19, 14))
        self.add_line('vertical-0-0', (14, 9), (14, 19))
        self.relate('connect', 'frame-0', 'handle-0-0')
        self.relate('connect', 'horizontal-0-0', 'vertical-0-0')
