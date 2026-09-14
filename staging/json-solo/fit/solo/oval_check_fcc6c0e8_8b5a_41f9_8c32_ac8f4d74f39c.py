"""Oval check (state), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fcc6c0e8-8b5a-41f9-8c32-ac8f4d74f39c'
SOURCE_PATH = 'icons-json/state/oval check_fcc6c0e8-8b5a-41f9-8c32-ac8f4d74f39c.json'
AUTHOR = 'json_to_solo'

class OvalCheckState(Solo48):
    icon_id = 'oval-check-state'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('oval', 'check', 'state')

    def build(self):
        self.add_line('e0', (33, 17), (21, 31))
        self.add_line('e1', (21, 31), (15, 23))
        self.add_line('e2', (33, 8), (15, 8))
        self.add_line('e3', (15, 40), (33, 40))
        self.add_arc('e4-1', (15, 8), (6, 15), radius_x=13, sweep=False)
        self.add_line('e4-2', (6, 15), (4, 24))
        self.add_arc('e4-3', (4, 24), (9, 37), radius_x=20, sweep=False)
        self.add_arc('e4-4', (9, 37), (15, 40), radius_x=9, sweep=False)
        self.add_arc('e5-1', (33, 40), (39, 37), radius_x=10, sweep=False)
        self.add_arc('e5-2', (39, 37), (43, 30), radius_x=17, sweep=False)
        self.add_arc('e5-3', (43, 30), (44, 24), radius_x=19, sweep=False)
        self.add_line('e5-4', (44, 24), (42, 15))
        self.add_arc('e5-5', (42, 15), (33, 8), radius_x=12, sweep=False)
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2', 'e4-1', 'e4-2', 'e4-3', 'e4-4', 'e3', 'e5-1', 'e5-2', 'e5-3', 'e5-4', 'e5-5', closed=True)
