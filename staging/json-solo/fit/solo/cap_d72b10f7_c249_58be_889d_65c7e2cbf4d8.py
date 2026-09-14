"""Batch-01/cap (accessories), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd72b10f7-c249-58be-889d-65c7e2cbf4d8'
SOURCE_PATH = 'icons-json/accessories/batch-01/cap_d72b10f7-c249-58be-889d-65c7e2cbf4d8.json'
AUTHOR = 'json_to_solo'

class Batch01Cap(Solo48):
    icon_id = 'batch-01-cap'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    aliases = ()
    keywords = ('batch', 'cap', 'accessories')

    def build(self):
        self.add_line('e0', (30, 30), (26, 29))
        self.add_line('e1', (13, 27), (4, 34))
        self.add_line('e2', (37, 22), (36, 32))
        self.add_line('e3', (38, 32), (35, 35))
        self.add_arc('e4-1', (9, 33), (4, 35), radius_x=3)
        self.add_line('e4-2', (4, 35), (4, 34))
        self.add_line('e5-1', (35, 11), (25, 10))
        self.add_arc('e5-2', (25, 10), (16, 16), radius_x=11, sweep=False)
        self.add_arc('e5-3', (16, 16), (13, 27), radius_x=25, sweep=False)
        self.add_arc('e6-1', (27, 10), (29, 8), radius_x=3)
        self.add_line('e6-2', (29, 8), (35, 11))
        self.add_arc('e6-3', (35, 11), (41, 16), radius_x=15)
        self.add_arc('e6-4', (41, 16), (43, 20), radius_x=16)
        self.add_line('e6-5', (43, 20), (44, 26))
        self.add_line('e6-6', (44, 26), (44, 30))
        self.add_arc('e6-7', (44, 30), (41, 32), radius_x=3)
        self.add_arc('e6-8', (41, 32), (30, 30), radius_x=14)
        self.add_arc('e7', (26, 29), (13, 27), radius_x=20, sweep=False)
        self.add_arc('e8', (32, 11), (37, 22), radius_x=15)
        self.add_arc('e9-1', (35, 35), (26, 40), radius_x=12)
        self.add_line('e9-2', (26, 40), (13, 34))
        self.add_arc('e9-3', (13, 34), (9, 33), radius_x=15)
        self.add_line('e10', (9, 33), (4, 34))
        self.add_contour('c0', 'e4-1', 'e4-2')
        self.add_contour('c1', 'e5-1', 'e5-2', 'e5-3')
        self.add_contour('c2', 'e6-1', 'e6-2', 'e6-3', 'e6-4', 'e6-5', 'e6-6', 'e6-7', 'e6-8', 'e0', 'e7')
        self.add_contour('c3', 'e1')
        self.add_contour('c4', 'e8', 'e2')
        self.add_contour('c5', 'e3', 'e9-1', 'e9-2', 'e9-3')
        self.add_contour('c6', 'e10')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c2', 'c1')
        self.relate('connect', 'c4', 'c1')
        self.relate('connect', 'c4', 'c2')
        self.relate('connect', 'c5', 'c2')
