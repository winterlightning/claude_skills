"""Synchronize refresh arrow (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f65dbb66-bdc9-586b-93bf-1c0b16f11a19'
SOURCE_PATH = 'icons-json/interface-essential/synchronize refresh arrow_f65dbb66-bdc9-586b-93bf-1c0b16f11a19.json'
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
        self.add_line('e0', (4, 20), (9, 26))
        self.add_line('e1', (9, 26), (15, 20))
        self.add_arc('e2-1', (11, 32), (18, 38), radius_x=17, sweep=False)
        self.add_line('e2-2', (18, 38), (27, 40))
        self.add_arc('e2-3', (27, 40), (41, 33), radius_x=18, sweep=False)
        self.add_line('e2-4', (41, 33), (43, 30))
        self.add_line('e2-5', (43, 30), (44, 24))
        self.add_line('e2-6', (44, 24), (43, 18))
        self.add_line('e2-7', (43, 18), (41, 15))
        self.add_arc('e2-8', (41, 15), (27, 8), radius_x=18, sweep=False)
        self.add_line('e2-9', (27, 8), (21, 9))
        self.add_arc('e2-10', (21, 9), (15, 12), radius_x=19, sweep=False)
        self.add_arc('e2-11', (15, 12), (9, 26), radius_x=16, sweep=False)
        self.add_contour('c0', 'e2-1', 'e2-2', 'e2-3', 'e2-4', 'e2-5', 'e2-6', 'e2-7', 'e2-8', 'e2-9', 'e2-10', 'e2-11')
        self.add_contour('c1', 'e0', 'e1')
