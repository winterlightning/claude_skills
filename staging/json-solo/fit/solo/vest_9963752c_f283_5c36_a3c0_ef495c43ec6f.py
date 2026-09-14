"""Vest (clothes), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9963752c-f283-5c36-a3c0-ef495c43ec6f'
SOURCE_PATH = 'icons-json/clothes/vest_9963752c-f283-5c36-a3c0-ef495c43ec6f.json'
AUTHOR = 'json_to_solo'

class Vest9963752c(Solo48):
    icon_id = 'vest-9963752c'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'clothes'
    aliases = ()
    keywords = ('vest', 'clothes')

    def build(self):
        self.add_line('e0', (17, 4), (12, 5))
        self.add_line('e1', (8, 19), (8, 40))
        self.add_line('e2', (8, 40), (20, 44))
        self.add_line('e3', (20, 44), (24, 39))
        self.add_line('e4', (24, 17), (26, 13))
        self.add_line('e5', (31, 4), (36, 5))
        self.add_line('e6', (36, 5), (36, 9))
        self.add_line('e7', (40, 19), (40, 40))
        self.add_line('e8', (40, 40), (28, 44))
        self.add_line('e9', (28, 44), (24, 39))
        self.add_line('e10', (24, 17), (24, 39))
        self.add_arc('e11', (24, 17), (17, 4), radius_x=57)
        self.add_arc('e12', (12, 5), (8, 19), radius_x=13)
        self.add_arc('e13', (26, 13), (31, 4), radius_x=38, sweep=False)
        self.add_arc('e14', (36, 9), (40, 19), radius_x=10, sweep=False)
        self.add_contour('c0', 'e11', 'e0', 'e12', 'e1', 'e2', 'e3')
        self.add_contour('c1', 'e4', 'e13', 'e5', 'e6', 'e14', 'e7', 'e8', 'e9')
        self.add_contour('c2', 'e10')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
