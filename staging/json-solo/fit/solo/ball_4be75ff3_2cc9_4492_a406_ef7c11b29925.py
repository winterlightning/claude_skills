"""Ball (sports), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4be75ff3-2cc9-4492-a406-ef7c11b29925'
SOURCE_PATH = 'icons-json/sports/ball_4be75ff3-2cc9-4492-a406-ef7c11b29925.json'
AUTHOR = 'json_to_solo'

class BallSports(Solo48):
    icon_id = 'ball-sports'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'sports'
    aliases = ()
    keywords = ('ball', 'sports')

    def build(self):
        self.add_arc('e0-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e0-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_arc('e1-1', (5, 19), (20, 30), radius_x=47)
        self.add_arc('e1-2', (20, 30), (24, 44), radius_x=19)
        self.add_arc('e2', (19, 5), (43, 29), radius_x=31, sweep=False)
        self.add_contour('c0', 'e1-1', 'e1-2')
        self.add_contour('c1', 'e2')
        self.add_contour('e0', 'e0-top', 'e0-bottom', closed=True)
        self.relate('connect', 'c0', 'e0')
        self.relate('connect', 'c0', 'e0')
        self.relate('connect', 'c1', 'e0')
        self.relate('connect', 'c1', 'e0')
