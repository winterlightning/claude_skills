"""Cart (shopping), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b9e134df-638b-471e-a6c6-fbdef9c3658e'
SOURCE_PATH = 'icons-json/shopping/cart_b9e134df-638b-471e-a6c6-fbdef9c3658e.json'
AUTHOR = 'json_to_solo'

class CartB9e134df(Solo48):
    icon_id = 'cart-b9e134df'
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
