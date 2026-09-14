"""Vest (clothes), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c9403137-cb21-5da2-b4de-4d67a662fe18'
SOURCE_PATH = 'icons-json/clothes/vest_c9403137-cb21-5da2-b4de-4d67a662fe18.json'
AUTHOR = 'json_to_solo'

class VestC9403137(Solo48):
    icon_id = 'vest-c9403137'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'clothes'
    aliases = ()
    keywords = ('vest', 'clothes')

    def build(self):
        self.add_line('e0', (17, 4), (12, 5))
        self.add_line('e1', (12, 5), (12, 9))
        self.add_line('e2', (8, 20), (8, 38))
        self.add_line('e3', (18, 44), (26, 44))
        self.add_line('e4', (28, 44), (35, 43))
        self.add_line('e5', (40, 39), (40, 20))
        self.add_line('e6', (36, 13), (36, 5))
        self.add_line('e7', (36, 5), (31, 4))
        self.add_line('e8', (24, 12), (24, 44))
        self.add_arc('e9', (12, 9), (8, 20), radius_x=12)
        self.add_line('e10-1', (8, 38), (9, 42))
        self.add_arc('e10-2', (9, 42), (11, 43), radius_x=4, sweep=False)
        self.add_line('e10-3', (11, 43), (18, 44))
        self.add_line('e11-1', (26, 44), (27, 44))
        self.add_arc('e11-2', (27, 44), (28, 44), radius_x=31)
        self.add_arc('e12-1', (35, 43), (39, 42), radius_x=8, sweep=False)
        self.add_line('e12-2', (39, 42), (40, 39))
        self.add_arc('e13', (40, 20), (36, 13), radius_x=7)
        self.add_arc('e14-1', (31, 4), (25, 12), radius_x=8)
        self.add_arc('e14-2', (25, 12), (17, 4), radius_x=8)
        self.add_contour('c0', 'e0', 'e1', 'e9', 'e2', 'e10-1', 'e10-2', 'e10-3', 'e3', 'e11-1', 'e11-2', 'e4', 'e12-1', 'e12-2', 'e5', 'e13', 'e6', 'e7', 'e14-1', 'e14-2', closed=True)
        self.add_contour('c1', 'e8')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c0')
