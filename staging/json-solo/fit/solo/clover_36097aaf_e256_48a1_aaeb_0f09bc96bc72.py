"""Clover (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '36097aaf-e256-48a1-aaeb-0f09bc96bc72'
SOURCE_PATH = 'icons-json/symbol/clover_36097aaf-e256-48a1-aaeb-0f09bc96bc72.json'
AUTHOR = 'json_to_solo'

class Clover36097aaf(Solo48):
    icon_id = 'clover-36097aaf'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('clover', 'symbol')

    def build(self):
        self.add_line('e0', (31, 31), (17, 17))
        self.add_line('e1', (17, 17), (15, 13))
        self.add_line('e2', (32, 17), (26, 24))
        self.add_line('e3', (24, 32), (24, 25))
        self.add_arc('e4-1', (15, 13), (19, 6), radius_x=5)
        self.add_arc('e4-2', (19, 6), (25, 10), radius_x=7)
        self.add_arc('e4-3', (25, 10), (30, 6), radius_x=6)
        self.add_arc('e4-4', (30, 6), (34, 8), radius_x=5)
        self.add_line('e4-5', (34, 8), (35, 11))
        self.add_line('e4-6', (35, 11), (32, 17))
        self.add_line('e4-7', (32, 17), (33, 17))
        self.add_arc('e4-8', (33, 17), (42, 20), radius_x=5)
        self.add_arc('e4-9', (42, 20), (38, 25), radius_x=6)
        self.add_arc('e4-10', (38, 25), (42, 30), radius_x=6)
        self.add_arc('e4-11', (42, 30), (31, 31), radius_x=6)
        self.add_line('e5-1', (26, 24), (14, 34))
        self.add_arc('e5-2', (14, 34), (6, 30), radius_x=5)
        self.add_arc('e5-3', (6, 30), (10, 25), radius_x=7)
        self.add_arc('e5-4', (10, 25), (6, 20), radius_x=6)
        self.add_line('e5-5', (6, 20), (7, 17))
        self.add_arc('e5-6', (7, 17), (10, 15), radius_x=4)
        self.add_line('e5-7', (10, 15), (17, 17))
        self.add_arc('e6', (21, 42), (24, 32), radius_x=12, sweep=False)
        self.add_contour('c0', 'e0', 'e1', 'e4-1', 'e4-2', 'e4-3', 'e4-4', 'e4-5', 'e4-6', 'e4-7', 'e4-8', 'e4-9', 'e4-10', 'e4-11', closed=True)
        self.add_contour('c1', 'e2', 'e5-1', 'e5-2', 'e5-3', 'e5-4', 'e5-5', 'e5-6', 'e5-7')
        self.add_contour('c2', 'e6', 'e3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c2', 'c0')
        self.relate('connect', 'c2', 'c1')
