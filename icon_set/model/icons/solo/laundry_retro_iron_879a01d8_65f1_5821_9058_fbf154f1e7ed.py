"""Laundry retro iron (wayfinding), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '879a01d8-65f1-5821-9058-fbf154f1e7ed'
SOURCE_PATH = 'pictographic-primitives/wayfinding/laundry retro iron_879a01d8-65f1-5821-9058-fbf154f1e7ed.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class LaundryRetroIron(Solo48):
    icon_id = 'laundry-retro-iron'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases = ()
    keywords = ('laundry', 'retro', 'iron', 'wayfinding')

    def build(self):
        self.add_line('e0', (19, 8), (34, 8))
        self.add_line('e1', (39, 13), (44, 40))
        self.add_line('e2', (44, 40), (4, 40))
        self.add_line('e3', (20, 21), (40, 21))
        self.add_arc('e4', (34, 8), (39, 13), radius_x=5)
        self.add_arc('e5-1', (4, 40), (8, 28), radius_x=23)
        self.add_arc('e5-2', (8, 28), (20, 21), radius_x=16)
        self.add_contour('c0', 'e0', 'e4', 'e1', 'e2', 'e5-1', 'e5-2', 'e3')
