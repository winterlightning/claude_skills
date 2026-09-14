"""Shopping basket (shopping), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e572b2c4-934f-4b9b-8534-f43313c52f92'
SOURCE_PATH = 'icons-json/shopping/shopping basket_e572b2c4-934f-4b9b-8534-f43313c52f92.json'
AUTHOR = 'json_to_solo'

class ShoppingBasketE572b2c4(Solo48):
    icon_id = 'shopping-basket-e572b2c4'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shopping'
    aliases = ()
    keywords = ('shopping', 'basket')

    def build(self):
        self.add_line('e0', (4, 18), (44, 18))
        self.add_line('e1', (39, 18), (38, 35))
        self.add_line('e2', (29, 40), (13, 40))
        self.add_line('e3', (9, 35), (7, 18))
        self.add_line('e4', (39, 18), (36, 11))
        self.add_line('e5', (32, 8), (16, 8))
        self.add_line('e6', (12, 11), (9, 18))
        self.add_line('e7-1', (38, 35), (36, 39))
        self.add_line('e7-2', (36, 39), (30, 40))
        self.add_arc('e7-3', (30, 40), (29, 40), radius_x=31, sweep=False)
        self.add_arc('e8', (13, 40), (9, 35), radius_x=5)
        self.add_arc('e9', (36, 11), (32, 8), radius_x=5, sweep=False)
        self.add_line('e10-1', (16, 8), (13, 9))
        self.add_line('e10-2', (13, 9), (12, 11))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e7-1', 'e7-2', 'e7-3', 'e2', 'e8', 'e3')
        self.add_contour('c2', 'e4', 'e9', 'e5', 'e10-1', 'e10-2', 'e6')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c2', 'c0')
        self.relate('connect', 'c2', 'c0')
