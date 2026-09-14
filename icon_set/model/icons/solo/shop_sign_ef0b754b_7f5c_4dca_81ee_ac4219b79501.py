"""Shop sign (shopping), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ef0b754b-7f5c-4dca-81ee-ac4219b79501'
SOURCE_PATH = 'icons-json/shopping/shop sign_ef0b754b-7f5c-4dca-81ee-ac4219b79501.json'
AUTHOR = 'json_to_solo'

class ShopSign(Solo48):
    icon_id = 'shop-sign'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shopping'
    aliases = ()
    keywords = ('shop', 'sign', 'shopping')

    def build(self):
        self.add_line('sym-e0', (8, 42), (24, 42))
        self.add_line('sym-e1', (24, 42), (40, 42))
        self.add_line('sym-e2', (40, 42), (42, 40))
        self.add_line('sym-e3', (42, 40), (42, 20))
        self.add_line('sym-e5', (42, 20), (42, 19))
        self.add_arc('sym-e6', (42, 19), (40, 17), radius_x=2)
        self.add_line('sym-e7', (40, 17), (32, 17))
        self.add_line('sym-e8', (32, 17), (24, 17))
        self.add_line('sym-e9', (24, 17), (16, 17))
        self.add_line('sym-e10', (16, 17), (8, 17))
        self.add_arc('sym-e11', (8, 17), (6, 19), radius_x=2)
        self.add_line('sym-e12', (6, 19), (6, 20))
        self.add_line('sym-e14', (6, 20), (6, 40))
        self.add_arc('sym-e15', (6, 40), (8, 42), radius_x=4, sweep=False)
        self.add_line('sym-e16', (16, 17), (22, 7))
        self.add_line('sym-e17', (22, 7), (24, 6))
        self.add_line('sym-e20', (24, 6), (26, 7))
        self.add_line('sym-e21', (26, 7), (32, 17))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e14', 'sym-e15', closed=True)
        self.add_contour('sym-c1', 'sym-e16', 'sym-e17', 'sym-e20', 'sym-e21')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
