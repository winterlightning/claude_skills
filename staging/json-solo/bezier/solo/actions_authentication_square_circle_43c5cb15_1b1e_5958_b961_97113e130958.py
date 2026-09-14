"""Actions authentication square circle (programing), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '43c5cb15-1b1e-5958-b961-97113e130958'
SOURCE_PATH = 'icons-json/programing/actions authentication square circle_43c5cb15-1b1e-5958-b961-97113e130958.json'
AUTHOR = 'json_to_solo'

class ActionsAuthenticationSquareCirclePrograming(Solo48):
    icon_id = 'actions-authentication-square-circle-programing'
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
        self.add_bezier('e8', (19, 13), ((19.27, 13), (19.73, 13), (20, 13)))
        self.add_bezier('e9', (29, 13), ((32.109, 13), (34.939, 14.705), (35.52, 17.823)), ((36.134, 21.153), (33.436, 25), (30, 25)))
        self.add_bezier('e10', (19, 25), ((18.632, 25), (18.273, 25.006), (17.929, 25.129)), ((15.295, 26.021), (13.29, 28.819), (13.634, 31.634)), ((13.994, 34.595), (17.014, 37), (20, 37)))
        self.add_contour('c0', 'e8', 'e0', 'e9', 'e1', 'e10', 'e2')
        self.add_contour('c1', 'e3', 'e4', 'e5', 'e6', closed=True)
        self.add_contour('e7', 'e7-top', 'e7-bottom', closed=True)
        self.relate('connect', 'c0', 'e7')
        self.relate('connect', 'c0', 'c1')
