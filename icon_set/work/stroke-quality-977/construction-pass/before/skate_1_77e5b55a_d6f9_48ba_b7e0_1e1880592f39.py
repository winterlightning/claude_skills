"""Skate 1 (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '77e5b55a-d6f9-48ba-b7e0-1e1880592f39'
SOURCE_PATH = 'pictographic-primitives/symbol/skate 1_77e5b55a-d6f9-48ba-b7e0-1e1880592f39.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class Skate1(Solo48):
    icon_id = 'skate-1'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('skate', 'symbol')

    def build(self):
        self.add_line('e0', (35, 23), (29, 21))
        self.add_line('e1', (25, 15), (25, 6))
        self.add_line('e2', (25, 6), (8, 6))
        self.add_line('e3', (8, 6), (8, 19))
        self.add_line('e4', (9, 32), (42, 32))
        self.add_line('e5-1', (42, 32), (41, 27))
        self.add_arc('e5-2', (41, 27), (35, 23), radius_x=11, sweep=False)
        self.add_arc('e6', (29, 21), (25, 15), radius_x=6)
        self.add_arc('e7-1', (8, 19), (6, 26), radius_x=27, sweep=False)
        self.add_arc('e7-2', (6, 26), (7, 30), radius_x=9, sweep=False)
        self.add_arc('e7-3', (7, 30), (9, 32), radius_x=2, sweep=False)
        self.add_dot('e8', (25, 42))
        self.add_dot('e9', (10, 42))
        self.add_dot('e10', (40, 42))
        self.add_contour('c0', 'e5-1', 'e5-2', 'e0', 'e6', 'e1', 'e2', 'e3', 'e7-1', 'e7-2', 'e7-3', 'e4', closed=True)
