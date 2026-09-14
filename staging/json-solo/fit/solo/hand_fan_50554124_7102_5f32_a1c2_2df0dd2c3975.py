"""Batch-06/hand fan (accessories), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '50554124-7102-5f32-a1c2-2df0dd2c3975'
SOURCE_PATH = 'icons-json/accessories/batch-06/hand fan_50554124-7102-5f32-a1c2-2df0dd2c3975.json'
AUTHOR = 'json_to_solo'

class Batch06HandFan(Solo48):
    icon_id = 'batch-06-hand-fan'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    aliases = ()
    keywords = ('batch', 'hand', 'fan', 'accessories')

    def build(self):
        self.add_line('e0', (24, 32), (21, 33))
        self.add_line('e1', (27, 34), (24, 32))
        self.add_line('e2', (25, 32), (27, 32))
        self.add_line('e3', (25, 32), (26, 30))
        self.add_line('e4', (26, 30), (34, 10))
        self.add_line('e5', (24, 32), (22, 30))
        self.add_line('e6', (22, 30), (12, 11))
        self.add_line('e7', (24, 8), (24, 32))
        self.add_arc('e8-1', (21, 33), (24, 40), radius_x=5, sweep=False)
        self.add_arc('e8-2', (24, 40), (27, 34), radius_x=4, sweep=False)
        self.add_line('e9-1', (27, 32), (44, 18))
        self.add_arc('e9-2', (44, 18), (34, 10), radius_x=33, sweep=False)
        self.add_line('e10-1', (21, 33), (4, 18))
        self.add_arc('e10-2', (4, 18), (12, 11), radius_x=22)
        self.add_line('e11-1', (34, 10), (32, 9))
        self.add_line('e11-2', (32, 9), (24, 8))
        self.add_line('e11-3', (24, 8), (12, 11))
        self.add_contour('c0', 'e0', 'e8-1', 'e8-2', 'e1')
        self.add_contour('c1', 'e2', 'e9-1', 'e9-2')
        self.add_contour('c2', 'e3', 'e4')
        self.add_contour('c3', 'e5', 'e6')
        self.add_contour('c4', 'e10-1', 'e10-2')
        self.add_contour('c5', 'e7')
        self.add_contour('c6', 'e11-1', 'e11-2', 'e11-3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c6')
        self.relate('connect', 'c2', 'c6')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c6')
        self.relate('connect', 'c4', 'c6')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c2', 'c0')
        self.relate('connect', 'c3', 'c0')
        self.relate('connect', 'c4', 'c0')
        self.relate('connect', 'c5', 'c6')
