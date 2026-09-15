"""Arrow merge (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '63a673eb-33db-4fa8-8da0-38a8feb57c5c'
SOURCE_PATH = 'pictographic-primitives/symbol/arrow merge_63a673eb-33db-4fa8-8da0-38a8feb57c5c.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class ArrowMerge(Solo48):
    icon_id = 'arrow-merge'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('arrow', 'merge', 'symbol')

    def build(self):
        self.add_line('e0', (16, 6), (6, 6))
        self.add_line('e1', (6, 17), (6, 6))
        self.add_line('e2', (24, 42), (24, 35))
        self.add_line('e3', (42, 17), (42, 6))
        self.add_line('e4', (32, 6), (42, 6))
        self.add_line('e5', (6, 6), (11, 10))
        self.add_line('e6', (22, 28), (24, 35))
        self.add_line('e7', (24, 35), (26, 28))
        self.add_line('e8', (36, 11), (42, 6))
        self.add_arc('e9', (11, 10), (22, 28), radius_x=46)
        self.add_arc('e10', (26, 28), (36, 11), radius_x=48)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.add_contour('c5', 'e5', 'e9', 'e6')
        self.add_contour('c6', 'e7', 'e10', 'e8')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c5')
        self.relate('connect', 'c1', 'c5')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c2', 'c6')
        self.relate('connect', 'c5', 'c6')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c6')
        self.relate('connect', 'c4', 'c6')
