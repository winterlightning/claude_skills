"""Complete reference redraw on SUB32; earlier incomplete variant preserved.
Source parts: frame, horizontal, vertical.
Construction: native 32px layout, 4px strokes, integer nodes; complete source comparison.

"""
from icon_set.model.icons.sub._base import Sub32
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = 'c9ddd792-c9fb-45cb-91b0-6af0af0c8e17'
SOURCE_PATH = 'pictographic-primitives/state/square medical cross_c9ddd792-c9fb-45cb-91b0-6af0af0c8e17.svg'
AUTHOR = 'gpt-6'
class CompleteReferenceRedraw(Sub32):
    icon_id = 'plus-sign-state-266-v2'
    variant_of = 'plus-sign-state-266'
    variant_label = 'Complete reference redraw'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    def build(self):
        self.add_line('frame-0-0', (5, 2), (27, 2))
        self.add_arc('frame-0-1', (27, 2), (30, 5), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('frame-0-2', (30, 5), (30, 27))
        self.add_arc('frame-0-3', (30, 27), (27, 30), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('frame-0-4', (27, 30), (5, 30))
        self.add_arc('frame-0-5', (5, 30), (2, 27), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('frame-0-6', (2, 27), (2, 5))
        self.add_arc('frame-0-7', (2, 5), (5, 2), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('frame-0', 'frame-0-0', 'frame-0-1', 'frame-0-2', 'frame-0-3', 'frame-0-4', 'frame-0-5', 'frame-0-6', 'frame-0-7', closed=True)
        self.add_line('horizontal-0-0', (10, 16), (22, 16))
        self.add_line('vertical-0-0', (16, 10), (16, 22))
        self.relate('connect', 'horizontal-0-0', 'vertical-0-0')
