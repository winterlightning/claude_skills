"""Flame (products), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '40563a28-79a3-40b5-8561-0142a3687b2c'
SOURCE_PATH = 'icons-json/products/flame_40563a28-79a3-40b5-8561-0142a3687b2c.json'
AUTHOR = 'json_to_solo'

class Flame40563a28(Solo48):
    icon_id = 'flame-40563a28'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'products'
    aliases = ()
    keywords = ('flame', 'products')

    def build(self):
        self.add_line('e0', (23, 4), (23, 7))
        self.add_line('e1', (29, 9), (23, 4))
        self.add_arc('e2-1', (23, 7), (20, 14), radius_x=14)
        self.add_line('e2-2', (20, 14), (9, 26))
        self.add_line('e2-3', (9, 26), (8, 31))
        self.add_arc('e2-4', (8, 31), (16, 42), radius_x=13, sweep=False)
        self.add_line('e2-5', (16, 42), (25, 44))
        self.add_arc('e2-6', (25, 44), (40, 29), radius_x=16, sweep=False)
        self.add_arc('e2-7', (40, 29), (29, 9), radius_x=28, sweep=False)
        self.add_contour('c0', 'e0', 'e2-1', 'e2-2', 'e2-3', 'e2-4', 'e2-5', 'e2-6', 'e2-7', 'e1', closed=True)
