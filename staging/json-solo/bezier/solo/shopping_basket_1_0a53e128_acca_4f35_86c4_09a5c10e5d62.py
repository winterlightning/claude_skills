"""Shopping basket 1 (shopping), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0a53e128-acca-4f35-86c4-09a5c10e5d62'
SOURCE_PATH = 'icons-json/shopping/shopping basket 1_0a53e128-acca-4f35-86c4-09a5c10e5d62.json'
AUTHOR = 'json_to_solo'

class ShoppingBasket1Shopping(Solo48):
    icon_id = 'shopping-basket-1-shopping'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shopping'
    aliases = ()
    keywords = ('shopping', 'basket')

    def build(self):
        self.add_line('e0', (6, 12), (42, 12))
        self.add_line('e1', (40, 12), (36, 37))
        self.add_line('e2', (29, 42), (14, 42))
        self.add_line('e3', (11, 36), (8, 12))
        self.add_line('e4', (34, 12), (32, 8))
        self.add_line('e5', (30, 6), (19, 6))
        self.add_line('e6', (17, 8), (14, 12))
        self.add_bezier('e7', (36, 37), ((35.812, 38.456), (35.684, 39.905), (34.825, 41.108)), ((34.759, 41.206), (34.62, 41.485), (34.505, 41.542)), ((33.777, 41.885), (32.869, 41.984), (32.075, 41.984)), ((31.683, 41.984), (31.29, 42), (30.897, 42)), ((30.235, 42), (29.663, 42), (29, 42)))
        self.add_bezier('e8', (14, 42), ((13.419, 41.795), (12.979, 41.656), (12.521, 41.174)), ((11.302, 39.873), (11.172, 37.685), (11, 36)))
        self.add_bezier('e9', (32, 8), ((31.665, 7.157), (30.884, 6), (30, 6)))
        self.add_bezier('e10', (19, 6), ((18.926, 6), (18.952, 6), (18.886, 6)), ((17.847, 6), (17.475, 7.206), (17, 8)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e7', 'e2', 'e8', 'e3')
        self.add_contour('c2', 'e4', 'e9', 'e5', 'e10', 'e6')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c2', 'c0')
        self.relate('connect', 'c2', 'c0')
