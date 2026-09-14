"""Recycling (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a343142c-bd20-4f34-9bb1-46e62075b0e3'
SOURCE_PATH = 'icons-json/symbol/recycling_a343142c-bd20-4f34-9bb1-46e62075b0e3.json'
AUTHOR = 'json_to_solo'

class RecyclingA343142c(Solo48):
    icon_id = 'recycling-a343142c'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('recycling', 'symbol')

    def build(self):
        self.add_line('e0', (40, 17), (42, 13))
        self.add_line('e1', (36, 16), (40, 17))
        self.add_line('e2', (11, 33), (8, 33))
        self.add_line('e3', (7, 36), (8, 33))
        self.add_arc('e4-1', (41, 26), (24, 42), radius_x=18)
        self.add_arc('e4-2', (24, 42), (8, 33), radius_x=19)
        self.add_arc('e5-1', (6, 25), (6, 20), radius_x=19, sweep=False)
        self.add_line('e5-2', (6, 20), (9, 14))
        self.add_arc('e5-3', (9, 14), (14, 9), radius_x=17)
        self.add_arc('e5-4', (14, 9), (22, 6), radius_x=18)
        self.add_line('e5-5', (22, 6), (24, 6))
        self.add_arc('e5-6', (24, 6), (40, 17), radius_x=18)
        self.add_contour('c0', 'e4-1', 'e4-2')
        self.add_contour('c1', 'e5-1', 'e5-2', 'e5-3', 'e5-4', 'e5-5', 'e5-6', 'e0')
        self.add_contour('c2', 'e1')
        self.add_contour('c3', 'e2')
        self.add_contour('c4', 'e3')
        self.relate('connect', 'c0', 'c4')
