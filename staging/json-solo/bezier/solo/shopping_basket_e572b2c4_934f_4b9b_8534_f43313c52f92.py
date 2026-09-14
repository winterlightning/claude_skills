"""Shopping basket (shopping), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e572b2c4-934f-4b9b-8534-f43313c52f92'
SOURCE_PATH = 'icons-json/shopping/shopping basket_e572b2c4-934f-4b9b-8534-f43313c52f92.json'
AUTHOR = 'json_to_solo'

class ShoppingBasket(Solo48):
    icon_id = 'shopping-basket'
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
        self.add_bezier('e7', (38, 35), ((37.9, 35.893), (37.2, 36.741), (36.773, 37.541)), ((36.473, 38.088), (36.118, 38.737), (35.655, 39.175)), ((34.964, 39.815), (31.555, 39.992), (30.691, 39.992)), ((30.427, 39.992), (30.164, 40), (29.891, 40)), ((29.745, 40), (29.145, 40), (29, 40)))
        self.add_bezier('e8', (13, 40), ((10.036, 39.183), (9.409, 37.552), (9, 35)))
        self.add_bezier('e9', (36, 11), ((35.282, 9.223), (33.9, 8.632), (32, 8)))
        self.add_bezier('e10', (16, 8), ((15.918, 8), (15.645, 8), (15.564, 8)), ((13.936, 8), (12.5, 9.619), (12, 11)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e7', 'e2', 'e8', 'e3')
        self.add_contour('c2', 'e4', 'e9', 'e5', 'e10', 'e6')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c2', 'c0')
        self.relate('connect', 'c2', 'c0')
