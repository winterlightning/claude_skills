"""Cough (health), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bc3ea9f7-36ca-4b3a-a099-e36c89039b41'
SOURCE_PATH = 'icons-json/health/cough_bc3ea9f7-36ca-4b3a-a099-e36c89039b41.json'
AUTHOR = 'json_to_solo'

class CoughHealth(Solo48):
    icon_id = 'cough-health'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    aliases = ()
    keywords = ('cough', 'health')

    def build(self):
        self.add_line('e0', (35, 44), (35, 36))
        self.add_line('e1', (11, 14), (8, 27))
        self.add_line('e2', (8, 27), (12, 27))
        self.add_line('e3', (12, 27), (12, 33))
        self.add_line('e4', (16, 37), (19, 38))
        self.add_line('e5', (20, 39), (20, 44))
        self.add_arc('e6-1', (35, 36), (40, 21), radius_x=27, sweep=False)
        self.add_line('e6-2', (40, 21), (39, 14))
        self.add_arc('e6-3', (39, 14), (36, 9), radius_x=16, sweep=False)
        self.add_arc('e6-4', (36, 9), (26, 4), radius_x=13, sweep=False)
        self.add_line('e6-5', (26, 4), (18, 6))
        self.add_arc('e6-6', (18, 6), (11, 14), radius_x=15, sweep=False)
        self.add_arc('e7', (12, 33), (16, 37), radius_x=4, sweep=False)
        self.add_line('e8', (19, 38), (20, 39))
        self.add_contour('c0', 'e0', 'e6-1', 'e6-2', 'e6-3', 'e6-4', 'e6-5', 'e6-6', 'e1', 'e2', 'e3', 'e7', 'e4', 'e8', 'e5')
