"""Penalty card (sports), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6a47f428-2cad-4abc-90d3-44803c238d8d'
SOURCE_PATH = 'icons-json/sports/penalty card_6a47f428-2cad-4abc-90d3-44803c238d8d.json'
AUTHOR = 'json_to_solo'

class PenaltyCard(Solo48):
    icon_id = 'penalty-card'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'sports'
    aliases = ()
    keywords = ('penalty', 'card', 'sports')

    def build(self):
        self.add_line('e0', (34, 35), (31, 33))
        self.add_line('e1', (42, 42), (42, 34))
        self.add_line('e2', (26, 36), (9, 36))
        self.add_line('e3', (6, 34), (6, 9))
        self.add_line('e4', (9, 6), (29, 6))
        self.add_line('e5', (31, 9), (31, 23))
        self.add_line('e6', (31, 33), (31, 23))
        self.add_arc('e7', (34, 42), (26, 36), radius_x=19)
        self.add_arc('e8', (42, 34), (31, 23), radius_x=14, sweep=False)
        self.add_arc('e9', (9, 36), (6, 34), radius_x=3)
        self.add_arc('e10', (6, 9), (9, 6), radius_x=4)
        self.add_arc('e11', (29, 6), (31, 9), radius_x=3)
        self.add_arc('e12-1', (26, 36), (25, 31), radius_x=4)
        self.add_arc('e12-2', (25, 31), (31, 33), radius_x=5)
        self.add_contour('c0', 'e7')
        self.add_contour('c1', 'e0')
        self.add_contour('c2', 'e1', 'e8')
        self.add_contour('c3', 'e2', 'e9', 'e3', 'e10', 'e4', 'e11', 'e5')
        self.add_contour('c4', 'e12-1', 'e12-2')
        self.add_contour('c5', 'e6')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c3', 'c5')
