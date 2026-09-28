"""Minus one increment (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b56d9b8f-7208-47a1-a1b1-7c804dfd614e'
SOURCE_PATH = 'pictographic-primitives/interface-essential/minus one increment_b56d9b8f-7208-47a1-a1b1-7c804dfd614e.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class MinusOneIncrement(Solo48):
    icon_id = 'minus-one-increment'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('minus', 'one', 'increment', 'interface-essential')

    def build(self):
        self.add_line('e0', (38, 8), (38, 40))
        self.add_line('e1', (29, 40), (38, 40))
        self.add_line('e2', (44, 40), (38, 40))
        self.add_line('e3', (4, 25), (22, 25))
        self.add_arc('e4', (31, 15), (38, 8), radius_x=13, sweep=False)
        self.add_contour('c0', 'e4', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
