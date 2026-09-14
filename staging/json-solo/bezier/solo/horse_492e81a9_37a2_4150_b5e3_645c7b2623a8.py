"""Horse (sports), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
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
        self.add_bezier('e6', (11, 26), ((11.741, 20.409), (13.844, 15.255), (17.314, 11.109)), ((18.611, 9.555), (19.636, 8.473), (21, 7)))
        self.add_bezier('e7', (25, 7), ((25.505, 8.645), (25.451, 10.109), (27, 11)))
        self.add_bezier('e8', (40, 19), ((40, 19.427), (40, 19.409), (40, 19.836)), ((40, 23.255), (37.549, 25.936), (34.594, 26.655)), ((33.592, 26.891), (33.002, 27.309), (32, 27)))
        self.add_bezier('e9', (26, 25), ((26.008, 31.791), (27.345, 38.373), (31, 44)))
        self.add_contour('c0', 'e0', 'e1', 'e6', 'e2', 'e3', 'e7', 'e4', 'e8', 'e5', 'e9')
