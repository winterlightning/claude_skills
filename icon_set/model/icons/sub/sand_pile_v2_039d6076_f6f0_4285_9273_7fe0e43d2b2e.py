"""Complete reference redraw on SUB32; earlier incomplete variant preserved.
Source parts: pile, top, left, right.
Construction: native 32px layout, 4px strokes, integer nodes; complete source comparison.

"""
from icon_set.model.icons.sub._base import Sub32
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = '039d6076-f6f0-4285-9273-7fe0e43d2b2e'
SOURCE_PATH = 'pictographic-primitives/state/sand_039d6076-f6f0-4285-9273-7fe0e43d2b2e.svg'
AUTHOR = 'gpt-6'
class CompleteReferenceRedraw(Sub32):
    icon_id = 'sand-pile-v2'
    variant_of = 'sand-pile'
    variant_label = 'Complete reference redraw'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    def build(self):
        self.add_line('pile-0-0', (2, 26), (16, 6))
        self.add_line('pile-0-1', (16, 6), (30, 26))
        self.add_contour('pile-0', 'pile-0-0', 'pile-0-1', closed=False)
        self.add_line('top-0-0', (16, 18), (16, 18))
        self.add_line('left-0-0', (11, 25), (11, 25))
        self.add_line('right-0-0', (21, 25), (21, 25))
