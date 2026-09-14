"""Shopping basket (shopping), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b8307606-fc5e-5c79-9f79-07ac43dd5ed8'
SOURCE_PATH = 'icons-json/shopping/shopping basket_b8307606-fc5e-5c79-9f79-07ac43dd5ed8.json'
AUTHOR = 'json_to_solo'

class ShoppingBasketB8307606(Solo48):
    icon_id = 'shopping-basket-b8307606'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shopping'
    aliases = ()
    keywords = ('shopping', 'basket')

    def build(self):
        self.add_line('e0', (11, 17), (44, 17))
        self.add_line('e1', (44, 17), (39, 37))
        self.add_line('e2', (36, 40), (14, 40))
        self.add_line('e3', (9, 36), (4, 17))
        self.add_line('e4', (4, 17), (15, 17))
        self.add_line('e5', (28, 8), (36, 17))
        self.add_line('e6', (19, 8), (12, 17))
        self.add_line('e7', (39, 37), (36, 40))
        self.add_line('e8-1', (14, 40), (10, 39))
        self.add_line('e8-2', (10, 39), (9, 36))
        self.add_arc('e9', (34, 16), (35, 16), radius_x=61, sweep=False)
        self.add_contour('c0', 'e0', 'e1', 'e7', 'e2', 'e8-1', 'e8-2', 'e3', 'e4')
        self.add_contour('c1', 'e5')
        self.add_contour('c2', 'e9')
        self.add_contour('c3', 'e6')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c2', 'c1')
        self.relate('connect', 'c2', 'c1')
        self.relate('connect', 'c3', 'c0')
