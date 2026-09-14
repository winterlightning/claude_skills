"""Boxing glove (sports), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dbf91214-8ada-5b30-9a04-1c64d7b7b10a'
SOURCE_PATH = 'icons-json/sports/boxing glove_dbf91214-8ada-5b30-9a04-1c64d7b7b10a.json'
AUTHOR = 'json_to_solo'

class BoxingGlove(Solo48):
    icon_id = 'boxing-glove'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'sports'
    aliases = ()
    keywords = ('boxing', 'glove', 'sports')

    def build(self):
        self.add_line('e0', (34, 20), (39, 25))
        self.add_line('e1', (15, 44), (32, 44))
        self.add_line('e2', (35, 41), (35, 35))
        self.add_line('e3', (13, 35), (35, 35))
        self.add_line('e4', (13, 35), (10, 31))
        self.add_line('e5', (8, 27), (8, 12))
        self.add_line('e6', (18, 4), (29, 4))
        self.add_line('e7', (40, 11), (40, 26))
        self.add_arc('e8', (28, 27), (34, 20), radius_x=5)
        self.add_line('e9-1', (39, 25), (40, 26))
        self.add_line('e9-2', (40, 26), (39, 31))
        self.add_arc('e9-3', (39, 31), (35, 35), radius_x=11)
        self.add_arc('e10', (13, 35), (15, 44), radius_x=5, sweep=False)
        self.add_arc('e11', (32, 44), (35, 41), radius_x=3, sweep=False)
        self.add_arc('e12', (10, 31), (8, 27), radius_x=12)
        self.add_arc('e13-1', (8, 12), (9, 9), radius_x=6)
        self.add_arc('e13-2', (9, 9), (18, 4), radius_x=11)
        self.add_arc('e14-1', (29, 4), (38, 8), radius_x=13)
        self.add_line('e14-2', (38, 8), (40, 11))
        self.add_contour('c0', 'e8', 'e0', 'e9-1', 'e9-2', 'e9-3')
        self.add_contour('c1', 'e10', 'e1', 'e11', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('c3', 'e4', 'e12', 'e5', 'e13-1', 'e13-2', 'e6', 'e14-1', 'e14-2', 'e7')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c3', 'c0')
