"""Navigation left (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6136ac07-dc00-55f8-a4db-5b81bfb23a45'
SOURCE_PATH = 'icons-json/interface-essential/navigation left_6136ac07-dc00-55f8-a4db-5b81bfb23a45.json'
AUTHOR = 'json_to_solo'

class NavigationLeft(Solo48):
    icon_id = 'navigation-left'
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
        self.add_bezier('e3', (7, 27), ((10.655, 28.787), (14.482, 29.613), (18, 32)))
        self.add_bezier('e4', (9, 23), ((11.673, 21.427), (13.7, 19), (16.464, 17.76)), ((25, 13.92), (37.418, 14.387), (42.273, 27.307)), ((43.027, 29.333), (43.982, 32.56), (43.982, 34.893)), ((43.991, 35), (43.991, 35.107), (44, 35.213)), ((44, 36.8), (44, 38.4), (44, 40)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e3')
        self.add_contour('c2', 'e2', 'e4')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
