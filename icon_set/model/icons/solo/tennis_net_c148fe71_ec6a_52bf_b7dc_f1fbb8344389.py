"""Tennis net (sports), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c148fe71-ec6a-52bf-b7dc-f1fbb8344389'
SOURCE_PATH = 'icons-json/sports/tennis net_c148fe71-ec6a-52bf-b7dc-f1fbb8344389.json'
AUTHOR = 'json_to_solo'

class TennisNet(Solo48):
    icon_id = 'tennis-net'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'sports'
    aliases = ()
    keywords = ('tennis', 'net', 'sports')

    def build(self):
        self.add_line('e0', (44, 17), (4, 17))
        self.add_line('e1', (44, 40), (44, 8))
        self.add_line('e2', (44, 8), (4, 8))
        self.add_line('e3', (4, 8), (4, 40))
        self.add_line('e4', (44, 31), (4, 31))
        self.add_line('e5', (34, 31), (34, 17))
        self.add_line('e6', (24, 31), (24, 17))
        self.add_line('e7', (14, 31), (14, 17))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2', 'e3')
        self.add_contour('c2', 'e4')
        self.add_contour('c3', 'e5')
        self.add_contour('c4', 'e6')
        self.add_contour('c5', 'e7')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c2', 'c1')
        self.relate('connect', 'c2', 'c1')
        self.relate('connect', 'c3', 'c2')
        self.relate('connect', 'c3', 'c0')
        self.relate('connect', 'c4', 'c2')
        self.relate('connect', 'c4', 'c0')
        self.relate('connect', 'c5', 'c2')
        self.relate('connect', 'c5', 'c0')
