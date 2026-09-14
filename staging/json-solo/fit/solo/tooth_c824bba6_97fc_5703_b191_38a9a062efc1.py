"""Tooth (health), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c824bba6-97fc-5703-b191-38a9a062efc1'
SOURCE_PATH = 'icons-json/health/tooth_c824bba6-97fc-5703-b191-38a9a062efc1.json'
AUTHOR = 'json_to_solo'

class Tooth(Solo48):
    icon_id = 'tooth'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    aliases = ()
    keywords = ('tooth', 'health')

    def build(self):
        self.add_line('e0', (37, 29), (37, 27))
        self.add_line('e1', (21, 5), (16, 4))
        self.add_line('e2', (11, 27), (11, 30))
        self.add_line('e3', (19, 39), (20, 35))
        self.add_line('e4-1', (37, 27), (40, 13))
        self.add_line('e4-2', (40, 13), (39, 8))
        self.add_arc('e4-3', (39, 8), (36, 5), radius_x=9, sweep=False)
        self.add_line('e4-4', (36, 5), (32, 4))
        self.add_arc('e4-5', (32, 4), (21, 5), radius_x=16)
        self.add_line('e5-1', (16, 4), (12, 5))
        self.add_line('e5-2', (12, 5), (9, 8))
        self.add_line('e5-3', (9, 8), (8, 13))
        self.add_line('e5-4', (8, 13), (11, 27))
        self.add_arc('e6-1', (11, 30), (16, 44), radius_x=22, sweep=False)
        self.add_arc('e6-2', (16, 44), (19, 39), radius_x=4, sweep=False)
        self.add_arc('e7-1', (20, 35), (25, 29), radius_x=5)
        self.add_arc('e7-2', (25, 29), (28, 33), radius_x=5)
        self.add_arc('e7-3', (28, 33), (31, 44), radius_x=20, sweep=False)
        self.add_arc('e7-4', (31, 44), (35, 39), radius_x=5, sweep=False)
        self.add_arc('e7-5', (35, 39), (37, 29), radius_x=39)
        self.add_contour('c0', 'e0', 'e4-1', 'e4-2', 'e4-3', 'e4-4', 'e4-5', 'e1', 'e5-1', 'e5-2', 'e5-3', 'e5-4', 'e2', 'e6-1', 'e6-2', 'e3', 'e7-1', 'e7-2', 'e7-3', 'e7-4', 'e7-5', closed=True)
