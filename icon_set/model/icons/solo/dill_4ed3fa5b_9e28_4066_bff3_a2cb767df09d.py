"""Dill (food), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4ed3fa5b-9e28-4066-bff3-a2cb767df09d'
SOURCE_PATH = 'icons-json/food/dill_4ed3fa5b-9e28-4066-bff3-a2cb767df09d.json'
AUTHOR = 'json_to_solo'

class Dill(Solo48):
    icon_id = 'dill'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('dill', 'food')

    def build(self):
        self.add_line('e0', (31, 34), (29, 35))
        self.add_line('e1', (29, 35), (23, 36))
        self.add_arc('e2', (31, 4), (24, 44), radius_x=50, sweep=False)
        self.add_arc('e3', (19, 9), (25, 15), radius_x=10, sweep=False)
        self.add_arc('e4', (8, 17), (23, 30), radius_x=18, sweep=False)
        self.add_arc('e5', (12, 35), (23, 41), radius_x=10, sweep=False)
        self.add_arc('e6', (40, 26), (31, 34), radius_x=14)
        self.add_arc('e7', (36, 9), (28, 10), radius_x=15)
        self.add_contour('c0', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4')
        self.add_contour('c3', 'e5')
        self.add_contour('c4', 'e6', 'e0', 'e1')
        self.add_contour('c5', 'e7')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c2', 'c0')
        self.relate('connect', 'c3', 'c0')
        self.relate('connect', 'c4', 'c0')
        self.relate('connect', 'c5', 'c0')
