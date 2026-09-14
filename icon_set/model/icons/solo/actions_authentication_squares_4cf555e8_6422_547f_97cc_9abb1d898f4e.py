"""Actions authentication squares (programing), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4cf555e8-6422-547f-97cc-9abb1d898f4e'
SOURCE_PATH = 'icons-json/programing/actions authentication squares_4cf555e8-6422-547f-97cc-9abb1d898f4e.json'
AUTHOR = 'json_to_solo'

class ActionsAuthenticationSquares(Solo48):
    icon_id = 'actions-authentication-squares'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'programing'
    aliases = ()
    keywords = ('actions', 'authentication', 'squares', 'programing')

    def build(self):
        self.add_line('e0', (30, 37), (17, 37))
        self.add_line('e1', (19, 25), (29, 25))
        self.add_line('e2', (29, 13), (17, 13))
        self.add_line('e3', (42, 31), (30, 31))
        self.add_line('e4', (30, 31), (30, 42))
        self.add_line('e5', (30, 42), (42, 42))
        self.add_line('e6', (42, 42), (42, 31))
        self.add_line('e7', (17, 6), (6, 6))
        self.add_line('e8', (6, 6), (6, 17))
        self.add_line('e9', (6, 17), (17, 17))
        self.add_line('e10', (17, 17), (17, 6))
        self.add_arc('e11-1', (17, 37), (14, 27), radius_x=6)
        self.add_arc('e11-2', (14, 27), (19, 25), radius_x=8)
        self.add_arc('e12', (29, 25), (29, 13), radius_x=6, sweep=False)
        self.add_contour('c0', 'e0', 'e11-1', 'e11-2', 'e1', 'e12', 'e2')
        self.add_contour('c1', 'e3', 'e4', 'e5', 'e6', closed=True)
        self.add_contour('c2', 'e7', 'e8', 'e9', 'e10', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
