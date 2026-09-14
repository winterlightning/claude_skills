"""Actions authentication squares (programing), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4cf555e8-6422-547f-97cc-9abb1d898f4e'
SOURCE_PATH = 'icons-json/programing/actions authentication squares_4cf555e8-6422-547f-97cc-9abb1d898f4e.json'
AUTHOR = 'json_to_solo'

class ActionsAuthenticationSquaresPrograming(Solo48):
    icon_id = 'actions-authentication-squares-programing'
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
        self.add_bezier('e11', (17, 37), ((15.159, 36.386), (13.887, 35.528), (12.971, 33.72)), ((10.852, 29.547), (14.092, 25.456), (18.355, 24.949)), ((18.575, 24.925), (18.795, 25), (19, 25)))
        self.add_bezier('e12', (29, 25), ((29.434, 25), (30.873, 24.303), (31.315, 24.098)), ((33.425, 23.125), (35.119, 21.202), (35.176, 18.772)), ((35.242, 15.859), (32.812, 13.585), (30.185, 12.84)), ((29.809, 12.734), (29.393, 13), (29, 13)))
        self.add_contour('c0', 'e0', 'e11', 'e1', 'e12', 'e2')
        self.add_contour('c1', 'e3', 'e4', 'e5', 'e6', closed=True)
        self.add_contour('c2', 'e7', 'e8', 'e9', 'e10', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
