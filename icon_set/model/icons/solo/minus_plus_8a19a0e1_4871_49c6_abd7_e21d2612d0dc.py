"""Minus plus (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8a19a0e1-4871-49c6-abd7-e21d2612d0dc'
SOURCE_PATH = 'pictographic-primitives/symbol/minus plus_8a19a0e1-4871-49c6-abd7-e21d2612d0dc.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class MinusPlus(Solo48):
    icon_id = 'minus-plus'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    categories = ('symbol',)
    aliases = ()
    keywords = ('minus', 'plus', 'symbol')

    def build(self):
        self.add_line('e0', (24, 4), (24, 17))
        self.add_line('e1', (8, 17), (24, 17))
        self.add_line('e2', (24, 29), (24, 17))
        self.add_line('e3', (40, 17), (24, 17))
        self.add_line('e4', (8, 44), (40, 44))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
