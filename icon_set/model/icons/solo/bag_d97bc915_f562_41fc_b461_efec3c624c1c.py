"""Bag (shopping), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd97bc915-f562-41fc-b461-efec3c624c1c'
SOURCE_PATH = 'icons-json/shopping/bag_d97bc915-f562-41fc-b461-efec3c624c1c.json'
AUTHOR = 'json_to_solo'

class BagD97bc915(Solo48):
    icon_id = 'bag-d97bc915'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shopping'
    aliases = ()
    keywords = ('bag', 'shopping')

    def build(self):
        self.add_line('e0', (17, 21), (17, 9))
        self.add_line('e1', (32, 11), (32, 21))
        self.add_line('e2', (40, 44), (36, 44))
        self.add_line('e3', (36, 44), (10, 44))
        self.add_line('e4', (8, 44), (11, 16))
        self.add_line('e5', (11, 16), (37, 16))
        self.add_line('e6', (37, 16), (40, 44))
        self.add_arc('e7-1', (17, 9), (20, 5), radius_x=9)
        self.add_line('e7-2', (20, 5), (24, 4))
        self.add_arc('e7-3', (24, 4), (29, 6), radius_x=8)
        self.add_line('e7-4', (29, 6), (32, 11))
        self.add_line('e8-1', (10, 44), (9, 44))
        self.add_arc('e8-2', (9, 44), (8, 44), radius_x=23, sweep=False)
        self.add_contour('c0', 'e0', 'e7-1', 'e7-2', 'e7-3', 'e7-4', 'e1')
        self.add_contour('c1', 'e2', 'e3', 'e8-1', 'e8-2', 'e4', 'e5', 'e6', closed=True)
