"""Cart (shopping), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd135db2c-7817-40f2-a866-11f751605109'
SOURCE_PATH = 'icons-json/shopping/cart_d135db2c-7817-40f2-a866-11f751605109.json'
AUTHOR = 'json_to_solo'

class CartD135db2c(Solo48):
    icon_id = 'cart-d135db2c'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shopping'
    aliases = ()
    keywords = ('cart', 'shopping')

    def build(self):
        self.add_line('e0', (42, 6), (39, 13))
        self.add_line('e1', (39, 13), (6, 13))
        self.add_line('e2', (6, 13), (13, 32))
        self.add_line('e3', (13, 32), (31, 32))
        self.add_line('e4', (31, 32), (39, 13))
        self.add_dot('e5', (16, 42))
        self.add_dot('e6', (29, 42))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2', 'e3', 'e4', closed=True)
        self.relate('connect', 'c0', 'c1')
