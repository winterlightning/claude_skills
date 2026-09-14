"""Soccer ball (sports), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3551c0d1-57e5-4543-b765-7f45c9f453c8'
SOURCE_PATH = 'icons-json/sports/soccer ball_3551c0d1-57e5-4543-b765-7f45c9f453c8.json'
AUTHOR = 'json_to_solo'

class SoccerBallSports(Solo48):
    icon_id = 'soccer-ball-sports'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'sports'
    aliases = ()
    keywords = ('soccer', 'ball', 'sports')

    def build(self):
        self.add_line('e0', (24, 4), (24, 14))
        self.add_line('e1', (19, 32), (29, 32))
        self.add_line('e2', (19, 32), (15, 21))
        self.add_line('e3', (19, 32), (13, 40))
        self.add_line('e4', (29, 32), (35, 40))
        self.add_line('e5', (29, 32), (33, 21))
        self.add_line('e6', (43, 19), (33, 21))
        self.add_line('e7', (33, 21), (24, 14))
        self.add_line('e8', (5, 19), (15, 21))
        self.add_line('e9', (15, 21), (24, 14))
        self.add_arc('e10-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e10-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.add_contour('c5', 'e5')
        self.add_contour('c6', 'e6')
        self.add_contour('c7', 'e7')
        self.add_contour('c8', 'e8')
        self.add_contour('c9', 'e9')
        self.add_contour('e10', 'e10-top', 'e10-bottom', closed=True)
        self.relate('connect', 'c0', 'c7')
        self.relate('connect', 'c0', 'c9')
        self.relate('connect', 'c7', 'c9')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c1', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c2', 'c8')
        self.relate('connect', 'c2', 'c9')
        self.relate('connect', 'c8', 'c9')
        self.relate('connect', 'c5', 'c6')
        self.relate('connect', 'c5', 'c7')
        self.relate('connect', 'c6', 'c7')
        self.relate('connect', 'c0', 'e10')
        self.relate('connect', 'c3', 'e10')
        self.relate('connect', 'c4', 'e10')
        self.relate('connect', 'c6', 'e10')
        self.relate('connect', 'c8', 'e10')
