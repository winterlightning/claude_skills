"""Complete reference redraw on SUB32; earlier incomplete variant preserved.
Source parts: frame, left, right.
Construction: native 32px layout, 4px strokes, integer nodes; complete source comparison.

"""
from icon_set.model.icons.sub._base import Sub32
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = 'f587e9fa-2c98-4afb-8edc-fcfcb1437a91'
SOURCE_PATH = 'pictographic-primitives/state/circle double next_f587e9fa-2c98-4afb-8edc-fcfcb1437a91.svg'
AUTHOR = 'gpt-6'
class CompleteReferenceRedraw(Sub32):
    icon_id = 'double-chevron-right-v2'
    variant_of = 'double-chevron-right'
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
        self.add_line('left-0-0', (10, 12), (13, 16))
        self.add_line('left-0-1', (13, 16), (10, 20))
        self.add_contour('left-0', 'left-0-0', 'left-0-1', closed=False)
        self.add_line('right-0-0', (20, 12), (23, 16))
        self.add_line('right-0-1', (23, 16), (20, 20))
        self.add_contour('right-0', 'right-0-0', 'right-0-1', closed=False)
