"""Tall rounded card containing a left-facing crescent moon."""
from ._tall_base import SourceFaithfulSideSub
from ...keyshapes import Keyshape
from ._compact_reference_helpers import rounded_rect
SOURCE_ICON_ID = '23e48a73-6f3a-4649-8e2c-1ae7c754ab02'
SOURCE_PATH = 'pictographic-primitives/other/card moon_23e48a73-6f3a-4649-8e2c-1ae7c754ab02.svg'
AUTHOR = 'gpt-6'
SOURCE_PARTS = ('open-bottom card with rounded top', 'left-facing crescent')

class DrawingVariant2(SourceFaithfulSideSub):
    canvas_width = 52
    canvas_height = 60
    icon_id = 'crescent-moon-card-v2'
    variant_of = 'crescent-moon-card'
    variant_label = 'Complete source on a proportionate canvas'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/symbol'
    aliases = ('moon-card',)
    keywords = ('crescent', 'moon', 'card', 'night')

    def build(self):
        self.add_line('card-left', (2, 58), (2, 10))
        self.add_arc('card-upper-left', (2, 10), (10, 2), radius_x=8)
        self.add_line('card-top', (10, 2), (42, 2))
        self.add_arc('card-upper-right', (42, 2), (50, 10), radius_x=8)
        self.add_line('card-right', (50, 10), (50, 58))
        self.add_contour('card', 'card-left', 'card-upper-left', 'card-top', 'card-upper-right', 'card-right', closed=False)
        self.add_bezier('moon', (30, 16), ((12, 16), (12, 44), (30, 44)), ((20, 36), (20, 24), (30, 16)))
        self.add_contour('crescent', 'moon', closed=True)
