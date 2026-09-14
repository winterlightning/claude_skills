"""Synchronize refresh arrow (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '291489e2-79f7-5f3b-9d47-fde1ae00f80e'
SOURCE_PATH = 'icons-json/interface-essential/synchronize refresh arrow_291489e2-79f7-5f3b-9d47-fde1ae00f80e.json'
AUTHOR = 'json_to_solo'

class SynchronizeRefreshArrow291489e2(Solo48):
    icon_id = 'synchronize-refresh-arrow-291489e2'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('synchronize', 'refresh', 'arrow', 'interface-essential')

    def build(self):
        self.add_line('e0', (9, 26), (4, 21))
        self.add_line('e1', (9, 26), (14, 21))
        self.add_line('e2-1', (25, 40), (35, 38))
        self.add_arc('e2-2', (35, 38), (44, 24), radius_x=16, sweep=False)
        self.add_arc('e2-3', (44, 24), (39, 13), radius_x=15, sweep=False)
        self.add_arc('e2-4', (39, 13), (33, 9), radius_x=19, sweep=False)
        self.add_line('e2-5', (33, 9), (26, 8))
        self.add_arc('e2-6', (26, 8), (11, 16), radius_x=19, sweep=False)
        self.add_arc('e2-7', (11, 16), (9, 26), radius_x=18, sweep=False)
        self.add_contour('c0', 'e2-1', 'e2-2', 'e2-3', 'e2-4', 'e2-5', 'e2-6', 'e2-7', 'e0')
        self.add_contour('c1', 'e1')
