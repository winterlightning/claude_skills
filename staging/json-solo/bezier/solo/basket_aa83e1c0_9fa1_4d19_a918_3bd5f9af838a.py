"""Basket (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'aa83e1c0-9fa1-4d19-a918-3bd5f9af838a'
SOURCE_PATH = 'icons-json/symbol/basket_aa83e1c0-9fa1-4d19-a918-3bd5f9af838a.json'
AUTHOR = 'json_to_solo'

class BasketSymbol(Solo48):
    icon_id = 'basket-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('basket', 'symbol')

    def build(self):
        self.add_line('e0', (31, 8), (39, 20))
        self.add_line('e1', (17, 8), (9, 20))
        self.add_line('e2', (44, 20), (4, 20))
        self.add_line('e3', (4, 20), (10, 40))
        self.add_line('e4', (10, 40), (39, 40))
        self.add_line('e5', (39, 40), (44, 20))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e3', 'e4', 'e5', closed=True)
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
