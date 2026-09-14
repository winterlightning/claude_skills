"""Exotic shorthair (pets), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd474f15d-d178-4b58-a27b-c0ae5030abcd'
SOURCE_PATH = 'icons-json/pets/exotic shorthair_d474f15d-d178-4b58-a27b-c0ae5030abcd.json'
AUTHOR = 'json_to_solo'

class ExoticShorthair(Solo48):
    icon_id = 'exotic-shorthair'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'pets'
    aliases = ()
    keywords = ('exotic', 'shorthair', 'pets')

    def build(self):
        self.add_line('e0', (4, 40), (4, 28))
        self.add_line('e1', (19, 14), (19, 10))
        self.add_line('e2', (29, 14), (29, 10))
        self.add_line('e3', (44, 40), (44, 28))
        self.add_line('e4', (12, 10), (16, 11))
        self.add_arc('e5', (12, 26), (4, 28), radius_x=13)
        self.add_arc('e6', (35, 26), (44, 28), radius_x=15, sweep=False)
        self.add_line('e7-1', (4, 28), (4, 22))
        self.add_arc('e7-2', (4, 22), (6, 17), radius_x=11)
        self.add_line('e7-3', (6, 17), (7, 16))
        self.add_arc('e7-4', (7, 16), (6, 8), radius_x=10)
        self.add_line('e7-5', (6, 8), (12, 10))
        self.add_arc('e8', (16, 11), (19, 10), radius_x=15)
        self.add_line('e9-1', (44, 28), (43, 19))
        self.add_arc('e9-2', (43, 19), (41, 16), radius_x=8, sweep=False)
        self.add_arc('e9-3', (41, 16), (41, 8), radius_x=6, sweep=False)
        self.add_arc('e9-4', (41, 8), (33, 11), radius_x=16, sweep=False)
        self.add_arc('e9-5', (33, 11), (29, 10), radius_x=12)
        self.add_arc('e10', (19, 10), (29, 10), radius_x=32)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e5')
        self.add_contour('c2', 'e1')
        self.add_contour('c3', 'e2')
        self.add_contour('c4', 'e6')
        self.add_contour('c5', 'e3')
        self.add_contour('c6', 'e7-1', 'e7-2', 'e7-3', 'e7-4', 'e7-5', 'e4', 'e8')
        self.add_contour('c7', 'e9-1', 'e9-2', 'e9-3', 'e9-4', 'e9-5')
        self.add_contour('c8', 'e10')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c6')
        self.relate('connect', 'c1', 'c6')
        self.relate('connect', 'c2', 'c6')
        self.relate('connect', 'c2', 'c8')
        self.relate('connect', 'c6', 'c8')
        self.relate('connect', 'c3', 'c7')
        self.relate('connect', 'c3', 'c8')
        self.relate('connect', 'c7', 'c8')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c4', 'c7')
        self.relate('connect', 'c5', 'c7')
