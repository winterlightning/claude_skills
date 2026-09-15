"""Arrow turn right (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b1a0e52e-87b0-4102-b77d-5268b50a437a'
SOURCE_PATH = 'pictographic-primitives/symbol/arrow turn right_b1a0e52e-87b0-4102-b77d-5268b50a437a.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class ArrowTurnRightSymbol(Solo48):
    icon_id = 'arrow-turn-right-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('arrow', 'turn', 'right', 'symbol')

    def build(self):
        self.add_line('e0', (34, 6), (42, 13))
        self.add_line('e1', (6, 42), (6, 22))
        self.add_line('e2', (15, 13), (42, 13))
        self.add_line('e3', (35, 21), (42, 13))
        self.add_arc('e4', (6, 22), (15, 13), radius_x=11)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e4', 'e2')
        self.add_contour('c2', 'e3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
