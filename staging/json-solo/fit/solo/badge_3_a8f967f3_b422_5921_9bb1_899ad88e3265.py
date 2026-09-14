"""Badge 3 (protection), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a8f967f3-b422-5921-9bb1-899ad88e3265'
SOURCE_PATH = 'icons-json/protection/badge 3_a8f967f3-b422-5921-9bb1-899ad88e3265.json'
AUTHOR = 'json_to_solo'

class Badge3Protection(Solo48):
    icon_id = 'badge-3-protection'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'protection'
    aliases = ()
    keywords = ('badge', 'protection')

    def build(self):
        self.add_line('e0', (15, 18), (15, 13))
        self.add_line('e1', (33, 13), (33, 20))
        self.add_line('e2', (33, 19), (44, 19))
        self.add_line('e3', (38, 28), (32, 28))
        self.add_line('e4', (15, 19), (4, 19))
        self.add_line('e5', (11, 28), (16, 28))
        self.add_arc('e6', (16, 29), (15, 18), radius_x=32)
        self.add_arc('e7-1', (15, 13), (24, 8), radius_x=19)
        self.add_arc('e7-2', (24, 8), (33, 13), radius_x=26)
        self.add_arc('e8-1', (33, 20), (24, 40), radius_x=24)
        self.add_arc('e8-2', (24, 40), (16, 29), radius_x=23)
        self.add_arc('e9', (44, 19), (38, 28), radius_x=11)
        self.add_arc('e10-1', (4, 19), (7, 26), radius_x=15, sweep=False)
        self.add_line('e10-2', (7, 26), (11, 28))
        self.add_contour('c0', 'e6', 'e0', 'e7-1', 'e7-2', 'e1', 'e8-1', 'e8-2')
        self.add_contour('c1', 'e2', 'e9', 'e3')
        self.add_contour('c2', 'e4', 'e10-1', 'e10-2', 'e5')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c2', 'c0')
        self.relate('connect', 'c2', 'c0')
