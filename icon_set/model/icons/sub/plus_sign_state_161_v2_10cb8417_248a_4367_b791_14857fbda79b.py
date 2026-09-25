"""Complete reference redraw on SUB32; earlier incomplete variant preserved.
Source parts: frame, clip, horizontal, vertical.
Construction: native 32px layout, 4px strokes, integer nodes; complete source comparison.

"""
from icon_set.model.icons.sub._base import Sub32
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = '10cb8417-248a-4367-b791-14857fbda79b'
SOURCE_PATH = 'pictographic-primitives/state/medical note 1_10cb8417-248a-4367-b791-14857fbda79b.svg'
AUTHOR = 'gpt-6'
class CompleteReferenceRedraw(Sub32):
    icon_id = 'plus-sign-state-161-v2'
    variant_of = 'plus-sign-state-161'
    variant_label = 'Complete reference redraw'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    def build(self):
        self.add_line('frame-0-0', (10, 5), (5, 5))
        self.add_arc('frame-0-1', (5, 5), (2, 8), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_line('frame-0-2', (2, 8), (2, 27))
        self.add_arc('frame-0-3', (2, 27), (5, 30), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_line('frame-0-4', (5, 30), (27, 30))
        self.add_arc('frame-0-5', (27, 30), (30, 27), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_line('frame-0-6', (30, 27), (30, 8))
        self.add_arc('frame-0-7', (30, 8), (27, 5), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_line('frame-0-8', (27, 5), (22, 5))
        self.add_contour('frame-0', 'frame-0-0', 'frame-0-1', 'frame-0-2', 'frame-0-3', 'frame-0-4', 'frame-0-5', 'frame-0-6', 'frame-0-7', 'frame-0-8', closed=False)
        self.add_line('clip-0-0', (13, 2), (19, 2))
        self.add_arc('clip-0-1', (19, 2), (22, 5), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('clip-0-2', (22, 5), (22, 7))
        self.add_arc('clip-0-3', (22, 7), (19, 10), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('clip-0-4', (19, 10), (13, 10))
        self.add_arc('clip-0-5', (13, 10), (10, 7), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('clip-0-6', (10, 7), (10, 5))
        self.add_arc('clip-0-7', (10, 5), (13, 2), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('clip-0', 'clip-0-0', 'clip-0-1', 'clip-0-2', 'clip-0-3', 'clip-0-4', 'clip-0-5', 'clip-0-6', 'clip-0-7', closed=True)
        self.add_line('horizontal-0-0', (11, 20), (21, 20))
        self.add_line('vertical-0-0', (16, 16), (16, 23))
        self.relate('connect', 'frame-0', 'clip-0')
        self.relate('connect', 'horizontal-0-0', 'vertical-0-0')
