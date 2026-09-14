"""Bread loaf (food), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4bf61584-bb22-543b-a2bd-b7fd43b78d35'
SOURCE_PATH = 'icons-json/food/bread loaf_4bf61584-bb22-543b-a2bd-b7fd43b78d35.json'
AUTHOR = 'json_to_solo'

class BreadLoafFood(Solo48):
    icon_id = 'bread-loaf-food'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('bread', 'loaf', 'food')

    def build(self):
        self.add_line('e0', (29, 40), (28, 22))
        self.add_line('e1', (23, 8), (11, 8))
        self.add_line('e2', (8, 22), (6, 39))
        self.add_line('e3', (12, 40), (40, 40))
        self.add_line('e4', (42, 37), (40, 23))
        self.add_line('e5', (37, 8), (27, 8))
        self.add_arc('e6-1', (28, 22), (26, 8), radius_x=8, sweep=False)
        self.add_line('e6-2', (26, 8), (23, 8))
        self.add_arc('e7-1', (11, 8), (4, 15), radius_x=8, sweep=False)
        self.add_line('e7-2', (4, 15), (5, 19))
        self.add_arc('e7-3', (5, 19), (8, 22), radius_x=8, sweep=False)
        self.add_line('e8-1', (6, 39), (11, 40))
        self.add_arc('e8-2', (11, 40), (12, 40), radius_x=22)
        self.add_line('e9-1', (40, 40), (42, 39))
        self.add_arc('e9-2', (42, 39), (42, 37), radius_x=4, sweep=False)
        self.add_line('e10-1', (40, 23), (44, 16))
        self.add_line('e10-2', (44, 16), (42, 10))
        self.add_line('e10-3', (42, 10), (38, 8))
        self.add_line('e10-4', (38, 8), (37, 8))
        self.add_contour('c0', 'e0', 'e6-1', 'e6-2', 'e1', 'e7-1', 'e7-2', 'e7-3')
        self.add_contour('c1', 'e2', 'e8-1', 'e8-2', 'e3', 'e9-1', 'e9-2', 'e4', 'e10-1', 'e10-2', 'e10-3', 'e10-4', 'e5')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c1', 'c0')
