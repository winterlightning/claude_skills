"""Link broken (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'db03fa02-7797-54ce-b9f4-d8c10fd4b4a5'
SOURCE_PATH = 'icons-json/interface-essential/link broken_db03fa02-7797-54ce-b9f4-d8c10fd4b4a5.json'
AUTHOR = 'json_to_solo'

class LinkBrokenInterfaceEssential(Solo48):
    icon_id = 'link-broken-interface-essential'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('link', 'broken', 'interface-essential')

    def build(self):
        self.add_line('e0', (20, 4), (20, 9))
        self.add_line('e1', (22, 17), (28, 9))
        self.add_line('e2', (38, 20), (29, 31))
        self.add_line('e3', (11, 9), (15, 11))
        self.add_line('e4', (8, 18), (12, 18))
        self.add_line('e5', (16, 23), (10, 31))
        self.add_line('e6', (21, 41), (26, 36))
        self.add_arc('e7-1', (28, 9), (40, 15), radius_x=8)
        self.add_arc('e7-2', (40, 15), (38, 20), radius_x=9)
        self.add_arc('e8-1', (10, 31), (8, 36), radius_x=9, sweep=False)
        self.add_line('e8-2', (8, 36), (9, 40))
        self.add_arc('e8-3', (9, 40), (15, 44), radius_x=7, sweep=False)
        self.add_line('e8-4', (15, 44), (17, 44))
        self.add_line('e8-5', (17, 44), (21, 41))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e7-1', 'e7-2', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('c3', 'e4')
        self.add_contour('c4', 'e5', 'e8-1', 'e8-2', 'e8-3', 'e8-4', 'e8-5', 'e6')
