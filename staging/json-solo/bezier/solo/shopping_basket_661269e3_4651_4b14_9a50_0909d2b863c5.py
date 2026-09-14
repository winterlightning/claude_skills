"""Shopping basket (shopping), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '661269e3-4651-4b14-9a50-0909d2b863c5'
SOURCE_PATH = 'icons-json/shopping/shopping basket_661269e3-4651-4b14-9a50-0909d2b863c5.json'
AUTHOR = 'json_to_solo'

class ShoppingBasket661269e3(Solo48):
    icon_id = 'shopping-basket-661269e3'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shopping'
    aliases = ()
    keywords = ('shopping', 'basket')

    def build(self):
        self.add_line('e0', (16, 8), (9, 21))
        self.add_line('e1', (32, 8), (39, 21))
        self.add_line('e2', (9, 21), (4, 21))
        self.add_line('e3', (4, 21), (9, 34))
        self.add_line('e4', (13, 40), (34, 40))
        self.add_line('e5', (37, 38), (43, 23))
        self.add_line('e6', (44, 21), (39, 21))
        self.add_line('e7', (9, 21), (39, 21))
        self.add_line('e8', (29, 32), (29, 28))
        self.add_line('e9', (19, 29), (19, 32))
        self.add_bezier('e10', (9, 34), ((9.618, 35.541), (10.809, 39.091), (12.455, 39.874)), ((12.709, 39.992), (12.745, 39.907), (13, 40)))
        self.add_bezier('e11', (34, 40), ((34.1, 40), (34.2, 39.992), (34.3, 39.992)), ((35.236, 39.992), (36.673, 38.775), (37, 38)))
        self.add_bezier('e12', (43, 23), ((43.245, 22.419), (43.7, 21.564), (44, 21)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e3', 'e10', 'e4', 'e11', 'e5', 'e12', 'e6')
        self.add_contour('c3', 'e7')
        self.add_contour('c4', 'e8')
        self.add_contour('c5', 'e9')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
