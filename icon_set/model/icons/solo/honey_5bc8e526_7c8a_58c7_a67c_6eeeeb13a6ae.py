"""Honey (food), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5bc8e526-7c8a-58c7-a67c-6eeeeb13a6ae'
SOURCE_PATH = 'icons-json/food/honey_5bc8e526-7c8a-58c7-a67c-6eeeeb13a6ae.json'
AUTHOR = 'gpt-6'

class Honey(Solo48):
    icon_id = 'honey'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('honey', 'food')

    def build(self):
        self.add_line('e0', (24, 37), (32, 42))
        self.add_line('e2', (38, 39), (42, 36))
        self.add_line('e3', (42, 36), (42, 26))
        self.add_line('e4', (42, 26), (33, 22))
        self.add_line('e5', (24, 37), (24, 27))
        self.add_line('e6', (24, 37), (15, 42))
        self.add_line('e7', (15, 42), (6, 37))
        self.add_line('e8', (6, 37), (6, 26))
        self.add_line('e9', (6, 26), (15, 22))
        self.add_line('e10', (15, 22), (15, 12))
        self.add_line('e11', (16, 11), (20, 8))
        self.add_line('e12', (20, 8), (24, 6))
        self.add_line('e13', (24, 6), (33, 11))
        self.add_line('e14', (33, 11), (33, 22))
        self.add_line('e15', (33, 22), (24, 27))
        self.add_line('e16', (24, 27), (15, 22))
        self.add_line('e17', (32, 42), (38, 39))
        self.add_arc('e18', (15, 12), (16, 11), radius_x=8, radius_y=8, large_arc=False, sweep=False)
        self.add_contour('c0', 'e0', 'e17', 'e2', 'e3', 'e4', closed=False)
        self.add_contour('c1', 'e5', closed=False)
        self.add_contour('c2', 'e6', 'e7', 'e8', 'e9', closed=False)
        self.add_contour('c3', 'e10', 'e18', 'e11', 'e12', 'e13', 'e14', closed=False)
        self.add_contour('c4', 'e15', 'e16', closed=False)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c1', 'c4')
