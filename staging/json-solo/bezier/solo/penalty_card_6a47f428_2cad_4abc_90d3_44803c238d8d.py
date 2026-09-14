"""Penalty card (sports), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6a47f428-2cad-4abc-90d3-44803c238d8d'
SOURCE_PATH = 'icons-json/sports/penalty card_6a47f428-2cad-4abc-90d3-44803c238d8d.json'
AUTHOR = 'json_to_solo'

class PenaltyCardSports(Solo48):
    icon_id = 'penalty-card-sports'
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
        self.add_bezier('e7', (34, 42), ((31.079, 40.724), (27.98, 38.504), (26, 36)))
        self.add_bezier('e8', (42, 34), ((42, 33.313), (41.73, 32.231), (41.476, 31.585)), ((39.668, 26.815), (35.287, 25.029), (31, 23)))
        self.add_bezier('e9', (9, 36), ((7.855, 36), (6.785, 35.594), (6.237, 34.579)), ((6.098, 34.325), (6.098, 34.262), (6, 34)))
        self.add_bezier('e10', (6, 9), ((6.556, 7.151), (7.126, 6.54), (9, 6)))
        self.add_bezier('e11', (29, 6), ((29.237, 6.082), (29.375, 6.065), (29.605, 6.188)), ((30.611, 6.728), (31, 7.846), (31, 9)))
        self.add_bezier('e12', (26, 36), ((25.1, 34.83), (23.255, 32.288), (24.9, 30.783)), ((25.358, 30.365), (25.988, 30.202), (26.594, 30.275)), ((28.426, 30.48), (29.601, 31.928), (31, 33)))
        self.add_contour('c0', 'e7')
        self.add_contour('c1', 'e0')
        self.add_contour('c2', 'e1', 'e8')
        self.add_contour('c3', 'e2', 'e9', 'e3', 'e10', 'e4', 'e11', 'e5')
        self.add_contour('c4', 'e12')
        self.add_contour('c5', 'e6')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c3', 'c5')
