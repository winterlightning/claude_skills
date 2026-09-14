"""Br (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'eda91265-1b5e-483f-8919-b0ad768010ea'
SOURCE_PATH = 'icons-json/symbol/Br_eda91265-1b5e-483f-8919-b0ad768010ea.json'
AUTHOR = 'json_to_solo'

class Br(Solo48):
    icon_id = 'br'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('br', 'symbol')

    def build(self):
        self.add_line('e0', (4, 8), (4, 40))
        self.add_line('e1', (4, 40), (11, 40))
        self.add_line('e2', (13, 8), (4, 8))
        self.add_line('e3', (14, 24), (4, 24))
        self.add_line('e4', (34, 20), (34, 40))
        self.add_line('e5-1', (11, 40), (18, 39))
        self.add_arc('e5-2', (18, 39), (22, 33), radius_x=8, sweep=False)
        self.add_arc('e5-3', (22, 33), (14, 24), radius_x=8, sweep=False)
        self.add_arc('e5-4', (14, 24), (20, 12), radius_x=9, sweep=False)
        self.add_arc('e5-5', (20, 12), (17, 9), radius_x=6, sweep=False)
        self.add_arc('e5-6', (17, 9), (13, 8), radius_x=9, sweep=False)
        self.add_arc('e6', (44, 21), (34, 26), radius_x=6, sweep=False)
        self.add_contour('c0', 'e0', 'e1', 'e5-1', 'e5-2', 'e5-3', 'e5-4', 'e5-5', 'e5-6', 'e2', closed=True)
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4')
        self.add_contour('c3', 'e6')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c3', 'c2')
