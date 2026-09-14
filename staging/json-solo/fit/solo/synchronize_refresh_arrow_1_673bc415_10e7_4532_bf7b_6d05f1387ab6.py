"""Synchronize refresh arrow 1 (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '673bc415-10e7-4532-bf7b-6d05f1387ab6'
SOURCE_PATH = 'icons-json/interface-essential/synchronize refresh arrow 1_673bc415-10e7-4532-bf7b-6d05f1387ab6.json'
AUTHOR = 'json_to_solo'

class SynchronizeRefreshArrow1673bc415(Solo48):
    icon_id = 'synchronize-refresh-arrow-1-673bc415'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('synchronize', 'refresh', 'arrow', 'interface-essential')

    def build(self):
        self.add_line('e0', (4, 21), (9, 26))
        self.add_line('e1', (14, 21), (10, 24))
        self.add_line('e2', (10, 24), (9, 26))
        self.add_line('e3-1', (25, 40), (32, 39))
        self.add_arc('e3-2', (32, 39), (39, 35), radius_x=18, sweep=False)
        self.add_arc('e3-3', (39, 35), (44, 24), radius_x=15, sweep=False)
        self.add_line('e3-4', (44, 24), (43, 18))
        self.add_line('e3-5', (43, 18), (40, 14))
        self.add_arc('e3-6', (40, 14), (35, 10), radius_x=19, sweep=False)
        self.add_line('e3-7', (35, 10), (26, 8))
        self.add_line('e3-8', (26, 8), (20, 9))
        self.add_arc('e3-9', (20, 9), (11, 16), radius_x=17, sweep=False)
        self.add_arc('e3-10', (11, 16), (9, 26), radius_x=17, sweep=False)
        self.add_contour('c0', 'e3-1', 'e3-2', 'e3-3', 'e3-4', 'e3-5', 'e3-6', 'e3-7', 'e3-8', 'e3-9', 'e3-10')
        self.add_contour('c1', 'e0')
        self.add_contour('c2', 'e1', 'e2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
