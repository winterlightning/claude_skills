"""Shopping cart empty (shopping), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '265d771c-37ea-4a56-8f73-ffaf2094e77b'
SOURCE_PATH = 'icons-json/shopping/shopping cart empty_265d771c-37ea-4a56-8f73-ffaf2094e77b.json'
AUTHOR = 'json_to_solo'

class ShoppingCartEmpty(Solo48):
    icon_id = 'shopping-cart-empty'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shopping'
    aliases = ()
    keywords = ('shopping', 'cart', 'empty')

    def build(self):
        self.add_line('e0', (4, 31), (35, 31))
        self.add_line('e1', (37, 30), (40, 10))
        self.add_line('e2', (41, 8), (44, 8))
        self.add_arc('e3-top', (7, 37), (15, 37), radius_x=4, radius_y=3)
        self.add_arc('e3-bottom', (15, 37), (7, 37), radius_x=4, radius_y=3)
        self.add_arc('e4-top', (27, 37), (35, 37), radius_x=4, radius_y=3)
        self.add_arc('e4-bottom', (35, 37), (27, 37), radius_x=4, radius_y=3)
        self.add_arc('e5', (35, 31), (37, 30), radius_x=3)
        self.add_line('e6', (40, 10), (41, 8))
        self.add_contour('c0', 'e0', 'e5', 'e1', 'e6', 'e2')
        self.add_contour('e3', 'e3-top', 'e3-bottom', closed=True)
        self.add_contour('e4', 'e4-top', 'e4-bottom', closed=True)
