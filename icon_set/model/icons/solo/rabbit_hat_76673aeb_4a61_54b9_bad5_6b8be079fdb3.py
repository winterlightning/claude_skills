"""Rabbit hat (products), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '76673aeb-4a61-54b9-bad5-6b8be079fdb3'
SOURCE_PATH = 'icons-json/products/rabbit hat_76673aeb-4a61-54b9-bad5-6b8be079fdb3.json'
AUTHOR = 'json_to_solo'

class RabbitHat(Solo48):
    icon_id = 'rabbit-hat'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'products'
    aliases = ()
    keywords = ('rabbit', 'hat', 'products')

    def build(self):
        self.add_line('e0', (23, 18), (23, 8))
        self.add_line('e1', (16, 7), (16, 28))
        self.add_line('e2', (16, 28), (40, 28))
        self.add_line('e3', (31, 22), (31, 28))
        self.add_line('e4', (31, 28), (33, 41))
        self.add_line('e5', (31, 44), (15, 44))
        self.add_line('e6', (13, 41), (15, 28))
        self.add_line('e7', (15, 28), (8, 28))
        self.add_line('e8', (23, 28), (23, 18))
        self.add_arc('e9-1', (23, 14), (33, 16), radius_x=11)
        self.add_arc('e9-2', (33, 16), (35, 21), radius_x=6)
        self.add_arc('e9-3', (35, 21), (31, 22), radius_x=3)
        self.add_arc('e10', (31, 22), (23, 18), radius_x=14)
        self.add_arc('e11-1', (23, 8), (20, 4), radius_x=4, sweep=False)
        self.add_line('e11-2', (20, 4), (17, 5))
        self.add_arc('e11-3', (17, 5), (16, 7), radius_x=6, sweep=False)
        self.add_arc('e12', (33, 41), (31, 44), radius_x=3)
        self.add_arc('e13', (15, 44), (13, 41), radius_x=3)
        self.add_contour('c0', 'e9-1', 'e9-2', 'e9-3')
        self.add_contour('c1', 'e10', 'e0', 'e11-1', 'e11-2', 'e11-3', 'e1', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('c3', 'e4', 'e12', 'e5', 'e13', 'e6', 'e7')
        self.add_contour('c4', 'e8')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c2', 'c1')
        self.relate('connect', 'c3', 'c1')
        self.relate('connect', 'c4', 'c1')
