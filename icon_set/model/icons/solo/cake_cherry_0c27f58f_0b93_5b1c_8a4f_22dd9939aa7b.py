"""Cake cherry (food), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0c27f58f-0b93-5b1c-8a4f-22dd9939aa7b'
SOURCE_PATH = 'icons-json/food/cake cherry_0c27f58f-0b93-5b1c-8a4f-22dd9939aa7b.json'
AUTHOR = 'json_to_solo'

class CakeCherry(Solo48):
    icon_id = 'cake-cherry'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('cake', 'cherry', 'food')

    def build(self):
        self.add_line('e0', (7, 26), (6, 31))
        self.add_line('e1', (6, 31), (6, 42))
        self.add_line('e2', (6, 42), (42, 42))
        self.add_line('e3', (42, 42), (42, 31))
        self.add_line('e4', (42, 31), (6, 31))
        self.add_line('e5', (30, 20), (42, 31))
        self.add_arc('e6-top', (19, 17), (31, 17), radius_x=6)
        self.add_arc('e6-bottom', (31, 17), (19, 17), radius_x=6)
        self.add_arc('e7-1', (26, 11), (34, 6), radius_x=9)
        self.add_arc('e7-2', (34, 6), (37, 7), radius_x=7)
        self.add_arc('e8', (19, 16), (7, 26), radius_x=15, sweep=False)
        self.add_contour('c0', 'e7-1', 'e7-2')
        self.add_contour('c1', 'e8', 'e0', 'e1', 'e2', 'e3', 'e4')
        self.add_contour('c2', 'e5')
        self.add_contour('e6', 'e6-top', 'e6-bottom', closed=True)
        self.relate('connect', 'c0', 'e6')
        self.relate('connect', 'c1', 'e6')
        self.relate('connect', 'c2', 'e6')
