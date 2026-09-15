"""Expand horizontal left right (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b91fb7b2-d90b-4056-b643-9bad1a855649'
SOURCE_PATH = 'pictographic-primitives/interface-essential/expand horizontal left right_b91fb7b2-d90b-4056-b643-9bad1a855649.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class ExpandHorizontalLeftRight(Solo48):
    icon_id = 'expand-horizontal-left-right'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('expand', 'horizontal', 'left', 'right', 'interface-essential')

    def build(self):
        self.add_line('e0', (20, 23), (20, 8))
        self.add_line('e1', (9, 19), (4, 24))
        self.add_line('e2', (9, 29), (4, 24))
        self.add_line('e3', (20, 24), (20, 40))
        self.add_line('e4', (20, 24), (4, 24))
        self.add_line('e5', (29, 8), (29, 24))
        self.add_line('e6', (29, 40), (29, 24))
        self.add_line('e7', (39, 29), (44, 24))
        self.add_line('e8', (39, 19), (44, 24))
        self.add_line('e9', (29, 24), (44, 24))
        self.add_arc('e10', (20, 23), (20, 24), radius_x=24)
        self.add_arc('e11', (20, 23), (20, 24), radius_x=24)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e10')
        self.add_contour('c2', 'e11')
        self.add_contour('c3', 'e1')
        self.add_contour('c4', 'e2')
        self.add_contour('c5', 'e3')
        self.add_contour('c6', 'e4')
        self.add_contour('c7', 'e5')
        self.add_contour('c8', 'e6')
        self.add_contour('c9', 'e7')
        self.add_contour('c10', 'e8')
        self.add_contour('c11', 'e9')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c5')
        self.relate('connect', 'c1', 'c6')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c2', 'c6')
        self.relate('connect', 'c5', 'c6')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c6')
        self.relate('connect', 'c4', 'c6')
        self.relate('connect', 'c11', 'c7')
        self.relate('connect', 'c11', 'c8')
        self.relate('connect', 'c7', 'c8')
        self.relate('connect', 'c10', 'c11')
        self.relate('connect', 'c10', 'c9')
        self.relate('connect', 'c11', 'c9')
