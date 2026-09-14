"""Minibus (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '23e6b09f-d221-4470-a691-1c757b5c826a'
SOURCE_PATH = 'icons-json/symbol/minibus_23e6b09f-d221-4470-a691-1c757b5c826a.json'
AUTHOR = 'json_to_solo'

class Minibus23e6b09f(Solo48):
    icon_id = 'minibus-23e6b09f'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('minibus', 'symbol')

    def build(self):
        self.add_line('e0', (4, 20), (44, 20))
        self.add_line('e1', (31, 35), (18, 35))
        self.add_line('e2', (40, 35), (42, 35))
        self.add_line('e3', (44, 32), (44, 11))
        self.add_line('e4', (41, 8), (10, 8))
        self.add_line('e5', (9, 10), (4, 19))
        self.add_line('e6', (4, 21), (4, 32))
        self.add_line('e7', (6, 35), (9, 35))
        self.add_arc('e8-top', (31, 35), (41, 35), radius_x=5)
        self.add_arc('e8-bottom', (41, 35), (31, 35), radius_x=5)
        self.add_arc('e9-top', (8, 35), (18, 35), radius_x=5)
        self.add_arc('e9-bottom', (18, 35), (8, 35), radius_x=5)
        self.add_arc('e10', (42, 35), (44, 32), radius_x=4, sweep=False)
        self.add_arc('e11', (44, 11), (41, 8), radius_x=3, sweep=False)
        self.add_line('e12', (10, 8), (9, 10))
        self.add_arc('e13', (4, 19), (4, 21), radius_x=52)
        self.add_arc('e14', (4, 32), (6, 35), radius_x=4, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e10', 'e3', 'e11', 'e4', 'e12', 'e5', 'e13', 'e6', 'e14', 'e7')
        self.add_contour('e8', 'e8-top', 'e8-bottom', closed=True)
        self.add_contour('e9', 'e9-top', 'e9-bottom', closed=True)
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'e8')
        self.relate('connect', 'c1', 'e9')
        self.relate('connect', 'c2', 'e8')
        self.relate('connect', 'c2', 'e9')
