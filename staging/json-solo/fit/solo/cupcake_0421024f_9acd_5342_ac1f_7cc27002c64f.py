"""Cupcake (food), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0421024f-9acd-5342-ac1f-7cc27002c64f'
SOURCE_PATH = 'icons-json/food/cupcake_0421024f-9acd-5342-ac1f-7cc27002c64f.json'
AUTHOR = 'json_to_solo'

class CupcakeFood(Solo48):
    icon_id = 'cupcake-food'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('cupcake', 'food')

    def build(self):
        self.add_line('e0', (24, 44), (24, 32))
        self.add_line('e1', (36, 31), (34, 41))
        self.add_line('e2', (30, 44), (17, 44))
        self.add_line('e3', (14, 41), (12, 31))
        self.add_arc('e4-top', (18, 15), (30, 15), radius_x=6, radius_y=5)
        self.add_arc('e4-bottom', (30, 15), (18, 15), radius_x=6, radius_y=5)
        self.add_arc('e5', (29, 4), (24, 9), radius_x=5, sweep=False)
        self.add_arc('e6-1', (29, 18), (40, 26), radius_x=13)
        self.add_arc('e6-2', (40, 26), (36, 31), radius_x=6)
        self.add_arc('e7-1', (36, 31), (29, 30), radius_x=6)
        self.add_arc('e7-2', (29, 30), (28, 31), radius_x=14, sweep=False)
        self.add_arc('e7-3', (28, 31), (19, 30), radius_x=7)
        self.add_arc('e7-4', (19, 30), (12, 31), radius_x=6)
        self.add_arc('e8-1', (34, 41), (32, 44), radius_x=3)
        self.add_arc('e8-2', (32, 44), (30, 44), radius_x=15, sweep=False)
        self.add_arc('e9', (17, 44), (14, 41), radius_x=3)
        self.add_arc('e10-1', (12, 31), (8, 26), radius_x=6)
        self.add_arc('e10-2', (8, 26), (18, 16), radius_x=11)
        self.add_contour('c0', 'e5')
        self.add_contour('c1', 'e6-1', 'e6-2')
        self.add_contour('c2', 'e0')
        self.add_contour('c3', 'e7-1', 'e7-2', 'e7-3', 'e7-4')
        self.add_contour('c4', 'e1', 'e8-1', 'e8-2', 'e2', 'e9', 'e3')
        self.add_contour('c5', 'e10-1', 'e10-2')
        self.add_contour('e4', 'e4-top', 'e4-bottom', closed=True)
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c0', 'e4')
        self.relate('connect', 'c1', 'e4')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c5', 'e4')
