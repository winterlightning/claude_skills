"""Dentistry tooth (health), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0efa6d0c-3493-59f8-8621-84558458859e'
SOURCE_PATH = 'icons-json/health/dentistry tooth_0efa6d0c-3493-59f8-8621-84558458859e.json'
AUTHOR = 'json_to_solo'

class DentistryToothHealth(Solo48):
    icon_id = 'dentistry-tooth-health'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    aliases = ()
    keywords = ('dentistry', 'tooth', 'health')

    def build(self):
        self.add_line('e0', (29, 35), (29, 41))
        self.add_line('e1', (31, 4), (26, 6))
        self.add_line('e2', (12, 26), (13, 36))
        self.add_line('e3-1', (29, 41), (30, 44))
        self.add_arc('e3-2', (30, 44), (35, 37), radius_x=11, sweep=False)
        self.add_arc('e3-3', (35, 37), (36, 29), radius_x=52, sweep=False)
        self.add_line('e3-4', (36, 29), (40, 13))
        self.add_line('e3-5', (40, 13), (38, 6))
        self.add_arc('e3-6', (38, 6), (34, 4), radius_x=7, sweep=False)
        self.add_line('e3-7', (34, 4), (31, 4))
        self.add_line('e4-1', (26, 6), (16, 4))
        self.add_arc('e4-2', (16, 4), (8, 12), radius_x=8, sweep=False)
        self.add_arc('e4-3', (8, 12), (9, 18), radius_x=19, sweep=False)
        self.add_arc('e4-4', (9, 18), (12, 26), radius_x=25)
        self.add_arc('e5-1', (13, 36), (18, 44), radius_x=10, sweep=False)
        self.add_line('e5-2', (18, 44), (21, 29))
        self.add_arc('e5-3', (21, 29), (27, 29), radius_x=4)
        self.add_arc('e5-4', (27, 29), (29, 35), radius_x=12)
        self.add_contour('c0', 'e0', 'e3-1', 'e3-2', 'e3-3', 'e3-4', 'e3-5', 'e3-6', 'e3-7', 'e1', 'e4-1', 'e4-2', 'e4-3', 'e4-4', 'e2', 'e5-1', 'e5-2', 'e5-3', 'e5-4', closed=True)
