"""Spa lotus (spas), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e8702a12-17ed-5a47-8c95-0f49c17db245'
SOURCE_PATH = 'icons-json/spas/spa lotus_e8702a12-17ed-5a47-8c95-0f49c17db245.json'
AUTHOR = 'json_to_solo'

class SpaLotusSpas(Solo48):
    icon_id = 'spa-lotus-spas'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'spas'
    aliases = ()
    keywords = ('spa', 'lotus', 'spas')

    def build(self):
        self.add_line('e0', (23, 37), (19, 36))
        self.add_line('e1', (19, 39), (23, 37))
        self.add_arc('e2-1', (37, 28), (44, 28), radius_x=12)
        self.add_arc('e2-2', (44, 28), (31, 40), radius_x=15)
        self.add_arc('e2-3', (31, 40), (24, 37), radius_x=11)
        self.add_arc('e3-1', (19, 36), (10, 23), radius_x=15)
        self.add_arc('e3-2', (10, 23), (10, 15), radius_x=42)
        self.add_arc('e3-3', (10, 15), (18, 19), radius_x=13)
        self.add_line('e4-1', (11, 28), (4, 28))
        self.add_arc('e4-2', (4, 28), (16, 40), radius_x=16, sweep=False)
        self.add_line('e4-3', (16, 40), (19, 39))
        self.add_arc('e5-1', (24, 8), (28, 31), radius_x=18)
        self.add_line('e5-2', (28, 31), (24, 37))
        self.add_arc('e5-3', (24, 37), (18, 19), radius_x=22)
        self.add_arc('e6-1', (24, 37), (35, 31), radius_x=14, sweep=False)
        self.add_arc('e6-2', (35, 31), (38, 15), radius_x=23, sweep=False)
        self.add_arc('e7', (38, 15), (30, 19), radius_x=12, sweep=False)
        self.add_arc('e8', (18, 19), (24, 8), radius_x=24)
        self.add_contour('c0', 'e2-1', 'e2-2', 'e2-3')
        self.add_contour('c1', 'e0', 'e3-1', 'e3-2', 'e3-3')
        self.add_contour('c2', 'e4-1', 'e4-2', 'e4-3', 'e1')
        self.add_contour('c3', 'e5-1', 'e5-2', 'e5-3')
        self.add_contour('c4', 'e6-1', 'e6-2')
        self.add_contour('c5', 'e7')
        self.add_contour('c6', 'e8')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c2', 'c1')
        self.relate('connect', 'c5', 'c3')
