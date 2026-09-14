"""Synchronize refresh arrow (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a0553293-203d-4c9b-9583-f6ead215b9d7'
SOURCE_PATH = 'icons-json/interface-essential/synchronize refresh arrow_a0553293-203d-4c9b-9583-f6ead215b9d7.json'
AUTHOR = 'json_to_solo'

class SynchronizeRefreshArrow(Solo48):
    icon_id = 'synchronize-refresh-arrow'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('synchronize', 'refresh', 'arrow', 'interface-essential')

    def build(self):
        self.add_line('e0', (39, 20), (40, 25))
        self.add_line('e1', (34, 21), (40, 25))
        self.add_line('e2', (44, 19), (40, 25))
        self.add_arc('e3-1', (24, 40), (21, 40), radius_x=44, sweep=False)
        self.add_arc('e3-2', (21, 40), (5, 29), radius_x=18)
        self.add_arc('e3-3', (5, 29), (4, 24), radius_x=13)
        self.add_arc('e3-4', (4, 24), (10, 12), radius_x=15)
        self.add_arc('e3-5', (10, 12), (22, 8), radius_x=20)
        self.add_arc('e3-6', (22, 8), (39, 20), radius_x=19)
        self.add_contour('c0', 'e3-1', 'e3-2', 'e3-3', 'e3-4', 'e3-5', 'e3-6', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
