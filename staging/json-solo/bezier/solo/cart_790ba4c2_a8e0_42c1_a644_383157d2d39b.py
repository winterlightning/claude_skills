"""Cart (spas), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '790ba4c2-a8e0-42c1-a644-383157d2d39b'
SOURCE_PATH = 'icons-json/spas/cart_790ba4c2-a8e0-42c1-a644-383157d2d39b.json'
AUTHOR = 'json_to_solo'

class Cart790ba4c2(Solo48):
    icon_id = 'cart-790ba4c2'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'spas'
    aliases = ()
    keywords = ('cart', 'spas')

    def build(self):
        self.add_line('e0', (19, 8), (11, 21))
        self.add_line('e1', (29, 8), (37, 21))
        self.add_line('e2', (44, 21), (4, 21))
        self.add_line('e3', (4, 21), (9, 40))
        self.add_line('e4', (9, 40), (39, 40))
        self.add_line('e5', (39, 40), (44, 21))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e3', 'e4', 'e5', closed=True)
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
