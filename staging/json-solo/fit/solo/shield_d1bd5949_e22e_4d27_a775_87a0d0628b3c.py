"""Shield (protection), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd1bd5949-e22e-4d27-a775-87a0d0628b3c'
SOURCE_PATH = 'icons-json/protection/shield_d1bd5949-e22e-4d27-a775-87a0d0628b3c.json'
AUTHOR = 'json_to_solo'

class Shield(Solo48):
    icon_id = 'shield'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'protection'
    aliases = ()
    keywords = ('shield', 'protection')

    def build(self):
        self.add_line('e0', (32, 23), (30, 25))
        self.add_line('e1', (38, 7), (32, 5))
        self.add_line('e2', (16, 6), (10, 8))
        self.add_line('e3', (8, 9), (8, 25))
        self.add_line('e4', (40, 26), (40, 8))
        self.add_arc('e5-1', (30, 25), (28, 25), radius_x=2)
        self.add_line('e5-2', (28, 25), (28, 17))
        self.add_arc('e5-3', (28, 17), (25, 13), radius_x=8, sweep=False)
        self.add_arc('e5-4', (25, 13), (24, 12), radius_x=13)
        self.add_line('e5-5', (24, 12), (23, 17))
        self.add_arc('e5-6', (23, 17), (17, 24), radius_x=12, sweep=False)
        self.add_arc('e5-7', (17, 24), (18, 31), radius_x=8, sweep=False)
        self.add_arc('e5-8', (18, 31), (28, 33), radius_x=7, sweep=False)
        self.add_arc('e5-9', (28, 33), (32, 23), radius_x=10, sweep=False)
        self.add_arc('e6', (40, 8), (38, 7), radius_x=4, sweep=False)
        self.add_line('e7-1', (32, 5), (25, 4))
        self.add_line('e7-2', (25, 4), (16, 6))
        self.add_arc('e8', (10, 8), (8, 9), radius_x=2, sweep=False)
        self.add_arc('e9-1', (8, 25), (24, 44), radius_x=23, sweep=False)
        self.add_arc('e9-2', (24, 44), (40, 26), radius_x=22, sweep=False)
        self.add_contour('c0', 'e0', 'e5-1', 'e5-2', 'e5-3', 'e5-4', 'e5-5', 'e5-6', 'e5-7', 'e5-8', 'e5-9', closed=True)
        self.add_contour('c1', 'e6', 'e1', 'e7-1', 'e7-2', 'e2', 'e8', 'e3', 'e9-1', 'e9-2', 'e4', closed=True)
