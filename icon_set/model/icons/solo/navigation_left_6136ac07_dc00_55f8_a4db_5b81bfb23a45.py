"""Navigation left (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6136ac07-dc00-55f8-a4db-5b81bfb23a45'
SOURCE_PATH = 'icons-json/interface-essential/navigation left_6136ac07-dc00-55f8-a4db-5b81bfb23a45.json'
AUTHOR = 'json_to_solo'

class NavigationLeft6136ac07(Solo48):
    icon_id = 'navigation-left-6136ac07'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('navigation', 'left', 'interface-essential')

    def build(self):
        self.add_line('e0', (4, 25), (15, 8))
        self.add_line('e1', (4, 25), (7, 27))
        self.add_line('e2', (4, 25), (9, 23))
        self.add_arc('e3', (7, 27), (18, 32), radius_x=64)
        self.add_arc('e4-1', (9, 23), (30, 16), radius_x=25)
        self.add_arc('e4-2', (30, 16), (40, 23), radius_x=15)
        self.add_arc('e4-3', (40, 23), (43, 30), radius_x=24)
        self.add_line('e4-4', (43, 30), (44, 37))
        self.add_line('e4-5', (44, 37), (44, 40))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e3')
        self.add_contour('c2', 'e2', 'e4-1', 'e4-2', 'e4-3', 'e4-4', 'e4-5')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
