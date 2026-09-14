"""Shopping bag side (shopping), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8de2d82c-4baa-5ded-96de-26a834bd33ff'
SOURCE_PATH = 'icons-json/shopping/shopping bag side_8de2d82c-4baa-5ded-96de-26a834bd33ff.json'
AUTHOR = 'json_to_solo'

class ShoppingBagSideShopping(Solo48):
    icon_id = 'shopping-bag-side-shopping'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shopping'
    aliases = ()
    keywords = ('shopping', 'bag', 'side')

    def build(self):
        self.add_line('e0', (31, 23), (29, 44))
        self.add_line('e1', (37, 44), (11, 44))
        self.add_line('e2', (8, 40), (12, 14))
        self.add_line('e3', (12, 14), (37, 14))
        self.add_line('e4', (37, 14), (40, 39))
        self.add_line('e5-1', (17, 14), (18, 8))
        self.add_arc('e5-2', (18, 8), (21, 5), radius_x=7)
        self.add_line('e5-3', (21, 5), (25, 4))
        self.add_line('e5-4', (25, 4), (29, 6))
        self.add_arc('e5-5', (29, 6), (31, 23), radius_x=23)
        self.add_line('e6-1', (40, 39), (40, 41))
        self.add_arc('e6-2', (40, 41), (37, 44), radius_x=4)
        self.add_arc('e7-1', (11, 44), (8, 41), radius_x=3)
        self.add_line('e7-2', (8, 41), (8, 40))
        self.add_contour('c0', 'e5-1', 'e5-2', 'e5-3', 'e5-4', 'e5-5', 'e0')
        self.add_contour('c1', 'e6-1', 'e6-2', 'e1', 'e7-1', 'e7-2', 'e2', 'e3', 'e4', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
