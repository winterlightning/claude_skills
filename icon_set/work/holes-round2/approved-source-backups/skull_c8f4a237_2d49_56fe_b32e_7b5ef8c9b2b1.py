"""Skull (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c8f4a237-2d49-56fe-b32e-7b5ef8c9b2b1'
SOURCE_PATH = 'icons-json/interface-essential/skull_c8f4a237-2d49-56fe-b32e-7b5ef8c9b2b1.json'
AUTHOR = 'json_to_solo'

class SkullC8f4a237(Solo48):
    icon_id = 'skull-c8f4a237'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('skull', 'interface-essential')

    def build(self):
        self.add_arc('sym-e0', (28, 23), (35, 23), radius_x=3, radius_y=4)
        self.add_arc('sym-e1', (35, 23), (28, 23), radius_x=3, radius_y=4)
        self.add_arc('sym-e2', (20, 23), (13, 23), radius_x=3, radius_y=4, sweep=False)
        self.add_arc('sym-e3', (13, 23), (20, 23), radius_x=3, radius_y=4, sweep=False)
        self.add_line('sym-e4', (27, 37), (27, 44))
        self.add_line('sym-e5', (27, 44), (29, 44))
        self.add_arc('sym-e6', (29, 44), (30, 44), radius_x=31)
        self.add_line('sym-e7', (30, 44), (31, 44))
        self.add_arc('sym-e8', (31, 44), (34, 39), radius_x=5, sweep=False)
        self.add_line('sym-e9', (34, 39), (34, 36))
        self.add_arc('sym-e10', (34, 36), (38, 30), radius_x=7)
        self.add_arc('sym-e11', (38, 30), (40, 24), radius_x=10, sweep=False)
        self.add_line('sym-e13', (40, 24), (40, 23))
        self.add_line('sym-e14', (40, 23), (38, 12))
        self.add_arc('sym-e15-1', (38, 12), (32, 6), radius_x=15, sweep=False)
        self.add_arc('sym-e15-2', (32, 6), (24, 4), radius_x=17, sweep=False)
        self.add_arc('sym-e18-1', (24, 4), (16, 6), radius_x=17, sweep=False)
        self.add_arc('sym-e18-2', (16, 6), (10, 12), radius_x=15, sweep=False)
        self.add_line('sym-e19', (10, 12), (8, 23))
        self.add_line('sym-e20', (8, 23), (8, 24))
        self.add_arc('sym-e22', (8, 24), (10, 30), radius_x=10, sweep=False)
        self.add_arc('sym-e23', (10, 30), (14, 36), radius_x=7)
        self.add_line('sym-e24', (14, 36), (14, 39))
        self.add_arc('sym-e25', (14, 39), (17, 44), radius_x=5, sweep=False)
        self.add_line('sym-e26', (17, 44), (18, 44))
        self.add_arc('sym-e27', (18, 44), (19, 44), radius_x=25)
        self.add_line('sym-e28', (19, 44), (21, 44))
        self.add_line('sym-e29', (21, 44), (21, 37))
        self.add_line('sym-e30', (27, 44), (24, 44))
        self.add_line('sym-e31', (24, 44), (21, 44))
        self.add_arc('sym-e32', (26, 31), (24, 28), radius_x=5, sweep=False)
        self.add_line('sym-e33', (24, 28), (24, 27))
        self.add_arc('sym-e34', (24, 27), (24, 28), radius_x=9, sweep=False)
        self.add_arc('sym-e35', (24, 28), (22, 31), radius_x=5, sweep=False)
        self.add_line('sym-e36', (22, 31), (24, 32))
        self.add_line('sym-e37', (24, 32), (26, 31))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', closed=True)
        self.add_contour('sym-c2', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e13', 'sym-e14', 'sym-e15-1', 'sym-e15-2', 'sym-e18-1', 'sym-e18-2', 'sym-e19', 'sym-e20', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e27', 'sym-e28', 'sym-e29')
        self.add_contour('sym-c3', 'sym-e30', 'sym-e31')
        self.add_contour('sym-c4', 'sym-e32', 'sym-e33', 'sym-e34', 'sym-e35', 'sym-e36', 'sym-e37', closed=True)
        self.relate('connect', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c2', 'sym-c3')
