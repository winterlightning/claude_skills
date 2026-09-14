"""Poop (state), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '253c812e-496e-430b-a314-0567c9af7421'
SOURCE_PATH = 'icons-json/state/poop_253c812e-496e-430b-a314-0567c9af7421.json'
AUTHOR = 'json_to_solo'

class PoopState(Solo48):
    icon_id = 'poop-state'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('poop', 'state')

    def build(self):
        self.add_line('e0', (16, 42), (37, 42))
        self.add_line('e1', (27, 8), (25, 6))
        self.add_line('e2', (25, 6), (24, 10))
        self.add_line('e3', (18, 16), (14, 17))
        self.add_arc('e4-1', (13, 26), (6, 35), radius_x=10, sweep=False)
        self.add_arc('e4-2', (6, 35), (10, 41), radius_x=7, sweep=False)
        self.add_line('e4-3', (10, 41), (15, 42))
        self.add_arc('e4-4', (15, 42), (16, 42), radius_x=23)
        self.add_arc('e5-1', (37, 42), (42, 37), radius_x=5, sweep=False)
        self.add_arc('e5-2', (42, 37), (37, 33), radius_x=5, sweep=False)
        self.add_arc('e5-3', (37, 33), (37, 26), radius_x=6, sweep=False)
        self.add_arc('e5-4', (37, 26), (32, 23), radius_x=9, sweep=False)
        self.add_arc('e5-5', (32, 23), (32, 15), radius_x=9, sweep=False)
        self.add_arc('e5-6', (32, 15), (27, 8), radius_x=15, sweep=False)
        self.add_arc('e6', (24, 10), (18, 16), radius_x=9)
        self.add_arc('e7', (14, 17), (13, 26), radius_x=5, sweep=False)
        self.add_contour('c0', 'e4-1', 'e4-2', 'e4-3', 'e4-4', 'e0', 'e5-1', 'e5-2', 'e5-3', 'e5-4', 'e5-5', 'e5-6', 'e1', 'e2', 'e6', 'e3', 'e7')
