"""Complete reference redraw on SUB32; earlier incomplete variant preserved.
Source parts: frame, check.
Construction: native 32px layout, 4px strokes, integer nodes; complete source comparison.

"""
from icon_set.model.icons.sub._base import Sub32
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = '73c8946e-7f3b-466a-a068-7e9d9a1db8c1'
SOURCE_PATH = 'pictographic-primitives/state/message check_73c8946e-7f3b-466a-a068-7e9d9a1db8c1.svg'
AUTHOR = 'gpt-6'
class CompleteReferenceRedraw(Sub32):
    icon_id = 'check-mark-state-165-v2'
    variant_of = 'check-mark-state-165'
    variant_label = 'Complete reference redraw'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    def build(self):
        self.add_line('frame-0-0', (5, 2), (27, 2))
        self.add_arc('frame-0-1', (27, 2), (30, 5), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('frame-0-2', (30, 5), (30, 21))
        self.add_arc('frame-0-3', (30, 21), (27, 24), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('frame-0-4', (27, 24), (23, 24))
        self.add_line('frame-0-5', (23, 24), (23, 30))
        self.add_line('frame-0-6', (23, 30), (16, 24))
        self.add_line('frame-0-7', (16, 24), (5, 24))
        self.add_arc('frame-0-8', (5, 24), (2, 21), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('frame-0-9', (2, 21), (2, 5))
        self.add_arc('frame-0-10', (2, 5), (5, 2), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('frame-0', 'frame-0-0', 'frame-0-1', 'frame-0-2', 'frame-0-3', 'frame-0-4', 'frame-0-5', 'frame-0-6', 'frame-0-7', 'frame-0-8', 'frame-0-9', 'frame-0-10', closed=True)
        self.add_line('check-0-0', (10, 13), (14, 17))
        self.add_line('check-0-1', (14, 17), (22, 9))
        self.add_contour('check-0', 'check-0-0', 'check-0-1', closed=False)
