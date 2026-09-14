"""Actions authentication square circle (programing), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '43c5cb15-1b1e-5958-b961-97113e130958'
SOURCE_PATH = 'icons-json/programing/actions authentication square circle_43c5cb15-1b1e-5958-b961-97113e130958.json'
AUTHOR = 'json_to_solo'

class ActionsAuthenticationSquareCircle(Solo48):
    icon_id = 'actions-authentication-square-circle'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'programing'
    aliases = ()
    keywords = ('actions', 'authentication', 'square', 'circle', 'programing')

    def build(self):
        self.add_line('e0', (20, 13), (29, 13))
        self.add_line('e1', (30, 25), (19, 25))
        self.add_line('e2', (20, 37), (31, 37))
        self.add_line('e3', (42, 31), (31, 31))
        self.add_line('e4', (31, 31), (31, 42))
        self.add_line('e5', (31, 42), (42, 42))
        self.add_line('e6', (42, 42), (42, 31))
        self.add_arc('e7-top', (6, 13), (20, 13), radius_x=7)
        self.add_arc('e7-bottom', (20, 13), (6, 13), radius_x=7)
        self.add_arc('e8', (19, 13), (20, 13), radius_x=22)
        self.add_arc('e9-1', (29, 13), (35, 16), radius_x=6)
        self.add_arc('e9-2', (35, 16), (30, 25), radius_x=7)
        self.add_arc('e10-1', (19, 25), (14, 33), radius_x=6, sweep=False)
        self.add_arc('e10-2', (14, 33), (20, 37), radius_x=6, sweep=False)
        self.add_contour('c0', 'e8', 'e0', 'e9-1', 'e9-2', 'e1', 'e10-1', 'e10-2', 'e2')
        self.add_contour('c1', 'e3', 'e4', 'e5', 'e6', closed=True)
        self.add_contour('e7', 'e7-top', 'e7-bottom', closed=True)
        self.relate('connect', 'c0', 'e7')
        self.relate('connect', 'c0', 'c1')
