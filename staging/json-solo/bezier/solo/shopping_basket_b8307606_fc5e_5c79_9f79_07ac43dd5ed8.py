"""Shopping basket (shopping), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
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
        self.add_bezier('e7', (39, 37), ((38.664, 38.187), (37.727, 40), (36, 40)))
        self.add_bezier('e8', (14, 40), ((13.845, 40), (13.691, 39.992), (13.545, 39.992)), ((10.709, 39.992), (9.582, 38.358), (9, 36)))
        self.add_bezier('e9', (34, 16), ((34.3, 16.278), (34.7, 15.722), (35, 16)))
        self.add_contour('c0', 'e0', 'e1', 'e7', 'e2', 'e8', 'e3', 'e4')
        self.add_contour('c1', 'e5')
        self.add_contour('c2', 'e9')
        self.add_contour('c3', 'e6')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c2', 'c1')
        self.relate('connect', 'c2', 'c1')
        self.relate('connect', 'c3', 'c0')
