"""Button syncing (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '18f9d573-e7b3-5500-9011-0bd7ffb6dcc0'
SOURCE_PATH = 'icons-json/interface-essential/button syncing_18f9d573-e7b3-5500-9011-0bd7ffb6dcc0.json'
AUTHOR = 'json_to_solo'

class ButtonSyncingInterfaceEssential(Solo48):
    icon_id = 'button-syncing-interface-essential'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('button', 'syncing', 'interface-essential')

    def build(self):
        self.add_line('e0', (31, 4), (35, 10))
        self.add_line('e1', (35, 10), (29, 11))
        self.add_line('e2', (17, 40), (13, 38))
        self.add_line('e3', (19, 37), (13, 38))
        self.add_line('e4', (13, 38), (17, 44))
        self.add_arc('e5-1', (10, 31), (8, 24), radius_x=19)
        self.add_arc('e5-2', (8, 24), (17, 8), radius_x=19)
        self.add_arc('e5-3', (17, 8), (35, 10), radius_x=17)
        self.add_arc('e6-1', (38, 17), (40, 24), radius_x=18)
        self.add_line('e6-2', (40, 24), (39, 30))
        self.add_arc('e6-3', (39, 30), (35, 37), radius_x=18)
        self.add_arc('e6-4', (35, 37), (17, 40), radius_x=15)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e5-1', 'e5-2', 'e5-3', 'e1')
        self.add_contour('c2', 'e6-1', 'e6-2', 'e6-3', 'e6-4', 'e2')
        self.add_contour('c3', 'e3', 'e4')
        self.relate('connect', 'c2', 'c3')
