"""Shopping basket 1 (shopping), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0a53e128-acca-4f35-86c4-09a5c10e5d62'
SOURCE_PATH = 'icons-json/shopping/shopping basket 1_0a53e128-acca-4f35-86c4-09a5c10e5d62.json'
AUTHOR = 'json_to_solo'

class ShoppingBasket1(Solo48):
    icon_id = 'shopping-basket-1'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shopping'
    aliases = ()
    keywords = ('shopping', 'basket')

    def build(self):
        self.add_line('e0', (6, 12), (42, 12))
        self.add_line('e1', (40, 12), (36, 37))
        self.add_line('e2', (29, 42), (14, 42))
        self.add_line('e3', (11, 36), (8, 12))
        self.add_line('e4', (34, 12), (32, 8))
        self.add_line('e5', (30, 6), (19, 6))
        self.add_line('e6', (17, 8), (14, 12))
        self.add_arc('e7-1', (36, 37), (34, 42), radius_x=5)
        self.add_line('e7-2', (34, 42), (30, 42))
        self.add_arc('e7-3', (30, 42), (29, 42), radius_x=31, sweep=False)
        self.add_arc('e8', (14, 42), (11, 36), radius_x=5)
        self.add_arc('e9', (32, 8), (30, 6), radius_x=3, sweep=False)
        self.add_arc('e10', (19, 6), (17, 8), radius_x=2, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e7-1', 'e7-2', 'e7-3', 'e2', 'e8', 'e3')
        self.add_contour('c2', 'e4', 'e9', 'e5', 'e10', 'e6')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c2', 'c0')
        self.relate('connect', 'c2', 'c0')
