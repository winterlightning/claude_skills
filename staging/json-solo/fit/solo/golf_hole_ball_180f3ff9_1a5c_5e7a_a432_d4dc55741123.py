"""Golf hole ball (sports), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '180f3ff9-1a5c-5e7a-a432-d4dc55741123'
SOURCE_PATH = 'icons-json/sports/golf hole ball_180f3ff9-1a5c-5e7a-a432-d4dc55741123.json'
AUTHOR = 'json_to_solo'

class GolfHoleBallSports(Solo48):
    icon_id = 'golf-hole-ball-sports'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'sports'
    aliases = ()
    keywords = ('golf', 'hole', 'ball', 'sports')

    def build(self):
        self.add_arc('e0-top', (22, 13), (36, 13), radius_x=7)
        self.add_arc('e0-bottom', (36, 13), (22, 13), radius_x=7)
        self.add_arc('e1-1', (40, 39), (34, 41), radius_x=28)
        self.add_line('e1-2', (34, 41), (24, 42))
        self.add_line('e1-3', (24, 42), (11, 40))
        self.add_arc('e1-4', (11, 40), (6, 35), radius_x=7)
        self.add_arc('e1-5', (6, 35), (11, 30), radius_x=7)
        self.add_arc('e1-6', (11, 30), (25, 28), radius_x=38)
        self.add_arc('e1-7', (25, 28), (37, 30), radius_x=35)
        self.add_arc('e1-8', (37, 30), (42, 35), radius_x=6)
        self.add_line('e1-9', (42, 35), (40, 39))
        self.add_contour('c0', 'e1-1', 'e1-2', 'e1-3', 'e1-4', 'e1-5', 'e1-6', 'e1-7', 'e1-8', 'e1-9', closed=True)
        self.add_contour('e0', 'e0-top', 'e0-bottom', closed=True)
