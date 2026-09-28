"""And 1 (_uncategorized_03), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '113ea344-bc63-41ae-8230-7dfe245254c0'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_03/and 1_113ea344-bc63-41ae-8230-7dfe245254c0.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class And1(Solo48):
    icon_id = 'and-1'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('and', '_uncategorized_03')

    def build(self):
        self.add_line('e0', (4, 16), (14, 16))
        self.add_line('e1', (4, 31), (14, 31))
        self.add_line('e2', (44, 24), (34, 24))
        self.add_line('e3', (14, 16), (14, 31))
        self.add_line('e4', (14, 16), (14, 8))
        self.add_line('e5', (14, 8), (21, 8))
        self.add_line('e6', (14, 31), (14, 40))
        self.add_line('e7', (14, 40), (21, 40))
        self.add_arc('e8', (21, 8), (34, 24), radius_x=15)
        self.add_arc('e9', (21, 40), (34, 24), radius_x=15, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4', 'e5', 'e8')
        self.add_contour('c5', 'e6', 'e7', 'e9')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c1', 'c5')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c4', 'c5')
