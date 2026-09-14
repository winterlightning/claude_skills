"""Shop sign (shopping), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ef0b754b-7f5c-4dca-81ee-ac4219b79501'
SOURCE_PATH = 'icons-json/shopping/shop sign_ef0b754b-7f5c-4dca-81ee-ac4219b79501.json'
AUTHOR = 'json_to_solo'

class ShopSignShopping(Solo48):
    icon_id = 'shop-sign-shopping'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shopping'
    aliases = ()
    keywords = ('shop', 'sign', 'shopping')

    def build(self):
        self.add_line('sym-e0', (8, 42), (24, 42))
        self.add_line('sym-e1', (24, 42), (40, 42))
        self.add_bezier('sym-e2', (40, 42), ((41.473, 41.37), (41.46, 41.555), (42, 40)))
        self.add_line('sym-e3', (42, 40), (42, 20))
        self.add_bezier('sym-e4', (42, 20), ((41.992, 19.967), (42, 20.033), (42, 20)))
        self.add_bezier('sym-e5', (42, 20), ((42, 19.787), (42, 19.188), (42, 19)))
        self.add_bezier('sym-e6', (42, 19), ((41.566, 17.928), (41.064, 17.286), (40, 17)))
        self.add_line('sym-e7', (40, 17), (32, 17))
        self.add_line('sym-e8', (32, 17), (24, 17))
        self.add_line('sym-e9', (24, 17), (16, 17))
        self.add_line('sym-e10', (16, 17), (8, 17))
        self.add_bezier('sym-e11', (8, 17), ((6.936, 17.286), (6.434, 17.928), (6, 19)))
        self.add_bezier('sym-e12', (6, 19), ((6, 19.188), (6, 19.787), (6, 20)))
        self.add_bezier('sym-e13', (6, 20), ((6, 20.033), (6.008, 19.967), (6, 20)))
        self.add_line('sym-e14', (6, 20), (6, 40))
        self.add_bezier('sym-e15', (6, 40), ((6.54, 41.555), (6.527, 41.37), (8, 42)))
        self.add_line('sym-e16', (16, 17), (22, 7))
        self.add_bezier('sym-e17', (22, 7), ((22.45, 6.607), (23.345, 6), (24, 6)))
        self.add_bezier('sym-e18', (24, 6), ((24.039, 6), (23.954, 6.001), (24, 6)))
        self.add_bezier('sym-e19', (24, 6), ((24.046, 6.001), (23.961, 6), (24, 6)))
        self.add_bezier('sym-e20', (24, 6), ((24.655, 6), (25.55, 6.607), (26, 7)))
        self.add_line('sym-e21', (26, 7), (32, 17))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', closed=True)
        self.add_contour('sym-c1', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
