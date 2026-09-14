"""Horse (sports), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '492e81a9-37a2-4150-b5e3-645c7b2623a8'
SOURCE_PATH = 'icons-json/sports/horse_492e81a9-37a2-4150-b5e3-645c7b2623a8.json'
AUTHOR = 'json_to_solo'

class Horse492e81a9(Solo48):
    icon_id = 'horse-492e81a9'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'sports'
    aliases = ()
    keywords = ('horse', 'sports')

    def build(self):
        self.add_line('e0', (8, 44), (9, 39))
        self.add_line('e1', (9, 39), (11, 26))
        self.add_line('e2', (21, 7), (24, 4))
        self.add_line('e3', (24, 4), (25, 7))
        self.add_line('e4', (27, 11), (40, 19))
        self.add_line('e5', (32, 27), (26, 25))
        self.add_arc('e6', (11, 26), (21, 7), radius_x=31)
        self.add_line('e7', (25, 7), (27, 11))
        self.add_arc('e8', (40, 19), (32, 27), radius_x=8)
        self.add_arc('e9', (26, 25), (31, 44), radius_x=34, sweep=False)
        self.add_contour('c0', 'e0', 'e1', 'e6', 'e2', 'e3', 'e7', 'e4', 'e8', 'e5', 'e9')
