"""Dentistry tooth chipped (health), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3be1d7f3-7a5d-5505-b530-fef1f4917455'
SOURCE_PATH = 'icons-json/health/dentistry tooth chipped_3be1d7f3-7a5d-5505-b530-fef1f4917455.json'
AUTHOR = 'json_to_solo'

class DentistryToothChippedHealth(Solo48):
    icon_id = 'dentistry-tooth-chipped-health'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    aliases = ()
    keywords = ('dentistry', 'tooth', 'chipped', 'health')

    def build(self):
        self.add_line('e0', (19, 40), (20, 33))
        self.add_line('e1', (28, 33), (29, 41))
        self.add_line('e2', (35, 36), (37, 24))
        self.add_line('e3', (37, 24), (34, 20))
        self.add_arc('e4-1', (34, 20), (39, 18), radius_x=14, sweep=False)
        self.add_arc('e4-2', (39, 18), (40, 12), radius_x=24, sweep=False)
        self.add_line('e4-3', (40, 12), (38, 6))
        self.add_arc('e4-4', (38, 6), (37, 5), radius_x=7)
        self.add_line('e4-5', (37, 5), (32, 4))
        self.add_arc('e4-6', (32, 4), (15, 4), radius_x=22)
        self.add_arc('e4-7', (15, 4), (8, 11), radius_x=7, sweep=False)
        self.add_arc('e4-8', (8, 11), (11, 23), radius_x=26, sweep=False)
        self.add_line('e4-9', (11, 23), (13, 37))
        self.add_arc('e4-10', (13, 37), (18, 44), radius_x=9, sweep=False)
        self.add_line('e4-11', (18, 44), (19, 40))
        self.add_arc('e5-1', (20, 33), (26, 28), radius_x=5)
        self.add_arc('e5-2', (26, 28), (28, 33), radius_x=8)
        self.add_line('e6-1', (29, 41), (30, 44))
        self.add_arc('e6-2', (30, 44), (35, 36), radius_x=11, sweep=False)
        self.add_contour('c0', 'e4-1', 'e4-2', 'e4-3', 'e4-4', 'e4-5', 'e4-6', 'e4-7', 'e4-8', 'e4-9', 'e4-10', 'e4-11', 'e0', 'e5-1', 'e5-2', 'e1', 'e6-1', 'e6-2', 'e2', 'e3', closed=True)
