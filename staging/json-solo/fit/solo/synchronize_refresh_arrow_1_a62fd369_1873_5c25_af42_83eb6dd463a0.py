"""Synchronize refresh arrow 1 (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a62fd369-1873-5c25-af42-83eb6dd463a0'
SOURCE_PATH = 'icons-json/interface-essential/synchronize refresh arrow 1_a62fd369-1873-5c25-af42-83eb6dd463a0.json'
AUTHOR = 'json_to_solo'

class SynchronizeRefreshArrow1A62fd369(Solo48):
    icon_id = 'synchronize-refresh-arrow-1-a62fd369'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('synchronize', 'refresh', 'arrow', 'interface-essential')

    def build(self):
        self.add_line('e0', (9, 26), (4, 22))
        self.add_line('e1', (14, 21), (9, 26))
        self.add_arc('e2-1', (10, 32), (25, 40), radius_x=19, sweep=False)
        self.add_line('e2-2', (25, 40), (35, 38))
        self.add_line('e2-3', (35, 38), (40, 34))
        self.add_arc('e2-4', (40, 34), (44, 24), radius_x=15, sweep=False)
        self.add_arc('e2-5', (44, 24), (40, 14), radius_x=15, sweep=False)
        self.add_arc('e2-6', (40, 14), (35, 10), radius_x=19, sweep=False)
        self.add_line('e2-7', (35, 10), (26, 8))
        self.add_line('e2-8', (26, 8), (17, 10))
        self.add_arc('e2-9', (17, 10), (12, 14), radius_x=18, sweep=False)
        self.add_arc('e2-10', (12, 14), (9, 26), radius_x=14, sweep=False)
        self.add_contour('c0', 'e2-1', 'e2-2', 'e2-3', 'e2-4', 'e2-5', 'e2-6', 'e2-7', 'e2-8', 'e2-9', 'e2-10', 'e0')
        self.add_contour('c1', 'e1')
