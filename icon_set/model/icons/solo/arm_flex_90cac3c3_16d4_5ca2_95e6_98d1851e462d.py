"""Arm flex (health), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '90cac3c3-16d4-5ca2-95e6-98d1851e462d'
SOURCE_PATH = 'icons-json/health/arm flex_90cac3c3-16d4-5ca2-95e6-98d1851e462d.json'
AUTHOR = 'json_to_solo'

class ArmFlex(Solo48):
    icon_id = 'arm-flex'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    aliases = ()
    keywords = ('arm', 'flex', 'health')

    def build(self):
        self.add_line('e0', (21, 30), (19, 33))
        self.add_line('e1', (19, 33), (18, 19))
        self.add_line('e2', (18, 19), (21, 17))
        self.add_line('e3', (23, 5), (15, 10))
        self.add_line('e4', (11, 15), (9, 34))
        self.add_line('e5', (13, 44), (40, 44))
        self.add_arc('e6-1', (35, 32), (30, 28), radius_x=9, sweep=False)
        self.add_arc('e6-2', (30, 28), (21, 30), radius_x=9, sweep=False)
        self.add_arc('e7-1', (21, 17), (30, 12), radius_x=6, sweep=False)
        self.add_arc('e7-2', (30, 12), (25, 4), radius_x=11, sweep=False)
        self.add_arc('e7-3', (25, 4), (23, 5), radius_x=3, sweep=False)
        self.add_arc('e8', (15, 10), (11, 15), radius_x=7, sweep=False)
        self.add_arc('e9-1', (9, 34), (8, 40), radius_x=37, sweep=False)
        self.add_arc('e9-2', (8, 40), (11, 44), radius_x=5, sweep=False)
        self.add_arc('e9-3', (11, 44), (13, 44), radius_x=8)
        self.add_arc('e10', (21, 17), (22, 13), radius_x=5, sweep=False)
        self.add_arc('e11', (40, 28), (35, 32), radius_x=7, sweep=False)
        self.add_contour('c0', 'e6-1', 'e6-2', 'e0', 'e1', 'e2')
        self.add_contour('c1', 'e7-1', 'e7-2', 'e7-3', 'e3', 'e8', 'e4', 'e9-1', 'e9-2', 'e9-3', 'e5')
        self.add_contour('c2', 'e10')
        self.add_contour('c3', 'e11')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
