"""Expand vertical left right (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '48373455-7c35-4928-8419-3623bf606696'
SOURCE_PATH = 'pictographic-primitives/interface-essential/expand vertical left right_48373455-7c35-4928-8419-3623bf606696.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class ExpandVerticalLeftRight(Solo48):
    icon_id = 'expand-vertical-left-right'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('expand', 'vertical', 'left', 'right', 'interface-essential')

    def build(self):
        self.add_line('e0', (17, 9), (24, 4))
        self.add_line('e1', (8, 20), (24, 20))
        self.add_line('e2', (8, 28), (24, 28))
        self.add_line('e3', (17, 39), (24, 44))
        self.add_line('e4', (31, 39), (24, 44))
        self.add_line('e5', (40, 28), (24, 28))
        self.add_line('e6', (40, 20), (24, 20))
        self.add_line('e7', (31, 9), (24, 4))
        self.add_line('e8', (24, 4), (24, 20))
        self.add_line('e9', (24, 44), (24, 28))
        self.add_line('e10', (24, 20), (24, 28))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.add_contour('c5', 'e5')
        self.add_contour('c6', 'e6')
        self.add_contour('c7', 'e7')
        self.add_contour('c8', 'e8')
        self.add_contour('c9', 'e9')
        self.add_contour('c10', 'e10')
        self.relate('connect', 'c0', 'c7')
        self.relate('connect', 'c0', 'c8')
        self.relate('connect', 'c7', 'c8')
        self.relate('connect', 'c1', 'c10')
        self.relate('connect', 'c1', 'c6')
        self.relate('connect', 'c1', 'c8')
        self.relate('connect', 'c10', 'c6')
        self.relate('connect', 'c10', 'c8')
        self.relate('connect', 'c6', 'c8')
        self.relate('connect', 'c10', 'c2')
        self.relate('connect', 'c10', 'c5')
        self.relate('connect', 'c10', 'c9')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c2', 'c9')
        self.relate('connect', 'c5', 'c9')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c9')
        self.relate('connect', 'c4', 'c9')
