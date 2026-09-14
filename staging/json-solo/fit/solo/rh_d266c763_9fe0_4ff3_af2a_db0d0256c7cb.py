"""Rh (state), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd266c763-9fe0-4ff3-af2a-db0d0256c7cb'
SOURCE_PATH = 'icons-json/state/Rh_d266c763-9fe0-4ff3-af2a-db0d0256c7cb.json'
AUTHOR = 'json_to_solo'

class RhState(Solo48):
    icon_id = 'rh-state'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('rh', 'state')

    def build(self):
        self.add_line('e0', (4, 25), (14, 25))
        self.add_line('e1', (15, 8), (5, 8))
        self.add_line('e2', (4, 9), (4, 40))
        self.add_line('e3', (21, 40), (14, 25))
        self.add_line('e4', (31, 8), (31, 40))
        self.add_line('e5', (44, 29), (44, 40))
        self.add_arc('e6', (14, 25), (15, 8), radius_x=9, sweep=False)
        self.add_arc('e7', (5, 8), (4, 9), radius_x=1, sweep=False)
        self.add_arc('e8-1', (31, 24), (38, 19), radius_x=7)
        self.add_arc('e8-2', (38, 19), (42, 21), radius_x=6)
        self.add_line('e8-3', (42, 21), (44, 28))
        self.add_arc('e8-4', (44, 28), (44, 29), radius_x=32, sweep=False)
        self.add_contour('c0', 'e0', 'e6', 'e1', 'e7', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4')
        self.add_contour('c3', 'e8-1', 'e8-2', 'e8-3', 'e8-4', 'e5')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c3', 'c2')
