"""Batch-01/umbrella (accessories), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '82042441-8abf-5e1b-9607-fac33bc3b256'
SOURCE_PATH = 'icons-json/accessories/batch-01/umbrella_82042441-8abf-5e1b-9607-fac33bc3b256.json'
AUTHOR = 'json_to_solo'

class Batch01Umbrella(Solo48):
    icon_id = 'batch-01-umbrella'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    aliases = ()
    keywords = ('batch', 'umbrella', 'accessories')

    def build(self):
        self.add_line('e0', (24, 39), (24, 19))
        self.add_line('e1', (24, 4), (21, 5))
        self.add_line('e2', (21, 7), (24, 4))
        self.add_line('e3', (24, 4), (27, 5))
        self.add_line('e4', (40, 19), (40, 21))
        self.add_line('e5', (40, 21), (38, 20))
        self.add_line('e6', (31, 22), (31, 20))
        self.add_line('e7', (27, 7), (24, 4))
        self.add_arc('e8-1', (30, 39), (27, 44), radius_x=4)
        self.add_arc('e8-2', (27, 44), (24, 39), radius_x=4)
        self.add_arc('e9-1', (21, 5), (8, 22), radius_x=18, sweep=False)
        self.add_arc('e9-2', (8, 22), (18, 22), radius_x=7)
        self.add_arc('e9-3', (18, 22), (21, 7), radius_x=32)
        self.add_arc('e10', (30, 22), (18, 22), radius_x=8, sweep=False)
        self.add_arc('e11', (27, 5), (40, 19), radius_x=18)
        self.add_arc('e12', (38, 20), (31, 22), radius_x=6, sweep=False)
        self.add_arc('e13', (31, 20), (27, 7), radius_x=26, sweep=False)
        self.add_contour('c0', 'e8-1', 'e8-2', 'e0')
        self.add_contour('c1', 'e1', 'e9-1', 'e9-2', 'e9-3', 'e2')
        self.add_contour('c2', 'e10')
        self.add_contour('c3', 'e3', 'e11', 'e4', 'e5', 'e12', 'e6', 'e13', 'e7', closed=True)
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c2', 'c1')
