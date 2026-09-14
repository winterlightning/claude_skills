"""Cart (shopping), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e7cacb27-40ca-4398-ba88-df122b223505'
SOURCE_PATH = 'icons-json/shopping/cart_e7cacb27-40ca-4398-ba88-df122b223505.json'
AUTHOR = 'json_to_solo'

class CartE7cacb27(Solo48):
    icon_id = 'cart-e7cacb27'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shopping'
    aliases = ()
    keywords = ('cart', 'shopping')

    def build(self):
        self.add_line('e0', (4, 8), (10, 8))
        self.add_line('e1', (10, 8), (17, 30))
        self.add_line('e2', (18, 31), (38, 31))
        self.add_line('e3', (39, 30), (44, 14))
        self.add_line('e4', (43, 12), (12, 12))
        self.add_line('e5', (17, 30), (18, 31))
        self.add_line('e6', (38, 31), (39, 30))
        self.add_line('e7', (44, 14), (43, 12))
        self.add_dot('e8', (20, 40))
        self.add_dot('e9', (36, 40))
        self.add_contour('c0', 'e0', 'e1', 'e5', 'e2', 'e6', 'e3', 'e7', 'e4')
