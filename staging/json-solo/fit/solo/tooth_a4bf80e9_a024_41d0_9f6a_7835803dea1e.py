"""Tooth (health), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a4bf80e9-a024-41d0-9f6a-7835803dea1e'
SOURCE_PATH = 'icons-json/health/tooth_a4bf80e9-a024-41d0-9f6a-7835803dea1e.json'
AUTHOR = 'json_to_solo'

class ToothA4bf80e9(Solo48):
    icon_id = 'tooth-a4bf80e9'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    aliases = ()
    keywords = ('tooth', 'health')

    def build(self):
        self.add_line('e0', (37, 21), (37, 35))
        self.add_line('e1', (12, 37), (13, 32))
        self.add_line('e2', (17, 10), (13, 8))
        self.add_line('e3', (8, 26), (7, 32))
        self.add_arc('e4', (31, 16), (37, 21), radius_x=6)
        self.add_arc('e5-1', (37, 35), (39, 39), radius_x=4, sweep=False)
        self.add_arc('e5-2', (39, 39), (44, 37), radius_x=4, sweep=False)
        self.add_arc('e6-1', (13, 32), (20, 29), radius_x=5)
        self.add_line('e6-2', (20, 29), (25, 40))
        self.add_arc('e6-3', (25, 40), (28, 34), radius_x=9, sweep=False)
        self.add_line('e6-4', (28, 34), (28, 25))
        self.add_arc('e6-5', (28, 25), (31, 14), radius_x=14, sweep=False)
        self.add_arc('e6-6', (31, 14), (24, 8), radius_x=8, sweep=False)
        self.add_arc('e6-7', (24, 8), (17, 10), radius_x=9)
        self.add_line('e7-1', (13, 8), (9, 8))
        self.add_arc('e7-2', (9, 8), (6, 10), radius_x=7, sweep=False)
        self.add_line('e7-3', (6, 10), (4, 16))
        self.add_line('e7-4', (4, 16), (8, 26))
        self.add_arc('e8-1', (7, 32), (10, 40), radius_x=8, sweep=False)
        self.add_arc('e8-2', (10, 40), (12, 37), radius_x=7, sweep=False)
        self.add_contour('c0', 'e4', 'e0', 'e5-1', 'e5-2')
        self.add_contour('c1', 'e1', 'e6-1', 'e6-2', 'e6-3', 'e6-4', 'e6-5', 'e6-6', 'e6-7', 'e2', 'e7-1', 'e7-2', 'e7-3', 'e7-4', 'e3', 'e8-1', 'e8-2', closed=True)
        self.relate('connect', 'c0', 'c1')
