"""Hand down 1 (state), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ce80faa0-dd47-4d1a-9ecb-fb349333dde8'
SOURCE_PATH = 'icons-json/state/hand down 1_ce80faa0-dd47-4d1a-9ecb-fb349333dde8.json'
AUTHOR = 'json_to_solo'

class HandDown1(Solo48):
    icon_id = 'hand-down-1'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('hand', 'down', 'state')

    def build(self):
        self.add_line('e0', (44, 16), (39, 21))
        self.add_line('e1', (39, 21), (27, 38))
        self.add_line('e2', (23, 40), (15, 40))
        self.add_line('e3', (11, 33), (19, 20))
        self.add_line('e4', (19, 20), (9, 23))
        self.add_line('e5', (4, 23), (4, 21))
        self.add_line('e6', (23, 11), (27, 11))
        self.add_line('e7-1', (27, 38), (24, 40))
        self.add_line('e7-2', (24, 40), (23, 40))
        self.add_arc('e8', (15, 40), (11, 33), radius_x=5)
        self.add_arc('e9', (9, 23), (4, 23), radius_x=8)
        self.add_arc('e10-1', (4, 21), (16, 12), radius_x=26)
        self.add_arc('e10-2', (16, 12), (23, 11), radius_x=11)
        self.add_arc('e11', (27, 11), (35, 8), radius_x=14, sweep=False)
        self.add_contour('c0', 'e0', 'e1', 'e7-1', 'e7-2', 'e2', 'e8', 'e3', 'e4', 'e9', 'e5', 'e10-1', 'e10-2', 'e6', 'e11')
