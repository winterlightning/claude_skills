"""Crane hook (shipping), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '40e56b92-93e6-4122-b70a-f6f602cc3011'
SOURCE_PATH = 'icons-json/shipping/crane hook_40e56b92-93e6-4122-b70a-f6f602cc3011.json'
AUTHOR = 'json_to_solo'

class CraneHook(Solo48):
    icon_id = 'crane-hook'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shipping'
    aliases = ()
    keywords = ('crane', 'hook', 'shipping')

    def build(self):
        self.add_line('e0', (24, 30), (24, 27))
        self.add_line('e1', (40, 6), (40, 16))
        self.add_line('e2', (40, 17), (32, 26))
        self.add_line('e3', (29, 27), (24, 27))
        self.add_line('e4', (24, 27), (19, 27))
        self.add_line('e5', (16, 26), (12, 21))
        self.add_line('e6', (37, 4), (11, 4))
        self.add_line('e7', (8, 6), (8, 16))
        self.add_line('e8', (8, 17), (12, 21))
        self.add_line('e9', (12, 21), (37, 4))
        self.add_arc('e10-1', (33, 38), (31, 42), radius_x=4)
        self.add_line('e10-2', (31, 42), (24, 44))
        self.add_line('e10-3', (24, 44), (17, 42))
        self.add_arc('e10-4', (17, 42), (15, 37), radius_x=5)
        self.add_arc('e10-5', (15, 37), (17, 34), radius_x=6)
        self.add_arc('e10-6', (17, 34), (22, 32), radius_x=11)
        self.add_arc('e10-7', (22, 32), (24, 30), radius_x=2, sweep=False)
        self.add_arc('e11', (37, 4), (40, 6), radius_x=4)
        self.add_arc('e12', (40, 16), (40, 17), radius_x=23, sweep=False)
        self.add_arc('e13', (32, 26), (29, 27), radius_x=10, sweep=False)
        self.add_arc('e14', (19, 27), (16, 26), radius_x=9, sweep=False)
        self.add_arc('e15', (11, 4), (8, 6), radius_x=4, sweep=False)
        self.add_line('e16', (8, 16), (8, 17))
        self.add_contour('c0', 'e10-1', 'e10-2', 'e10-3', 'e10-4', 'e10-5', 'e10-6', 'e10-7', 'e0')
        self.add_contour('c1', 'e11', 'e1', 'e12', 'e2', 'e13', 'e3')
        self.add_contour('c2', 'e4', 'e14', 'e5')
        self.add_contour('c3', 'e6', 'e15', 'e7', 'e16', 'e8', 'e9', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c2', 'c3')
