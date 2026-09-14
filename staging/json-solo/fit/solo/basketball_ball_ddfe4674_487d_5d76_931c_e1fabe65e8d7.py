"""Basketball ball (sports), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ddfe4674-487d-5d76-931c-e1fabe65e8d7'
SOURCE_PATH = 'icons-json/sports/basketball ball_ddfe4674-487d-5d76-931c-e1fabe65e8d7.json'
AUTHOR = 'json_to_solo'

class BasketballBallSports(Solo48):
    icon_id = 'basketball-ball-sports'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'sports'
    aliases = ()
    keywords = ('basketball', 'ball', 'sports')

    def build(self):
        self.add_line('sym-e0', (24, 6), (24, 24))
        self.add_line('sym-e1', (24, 24), (24, 42))
        self.add_arc('sym-e2', (24, 42), (42, 24), radius_x=18, sweep=False)
        self.add_arc('sym-e3', (42, 24), (24, 6), radius_x=18, sweep=False)
        self.add_arc('sym-e4', (24, 6), (6, 24), radius_x=18, sweep=False)
        self.add_arc('sym-e5', (6, 24), (24, 42), radius_x=18, sweep=False)
        self.add_line('sym-e6', (19, 24), (6, 24))
        self.add_line('sym-e7', (29, 24), (42, 24))
        self.add_line('sym-e8', (24, 24), (20, 24))
        self.add_line('sym-e9', (20, 24), (19, 24))
        self.add_line('sym-e11', (19, 24), (19, 23))
        self.add_arc('sym-e12', (19, 23), (15, 14), radius_x=14, sweep=False)
        self.add_arc('sym-e13', (15, 14), (12, 11), radius_x=28)
        self.add_line('sym-e14', (24, 24), (28, 24))
        self.add_line('sym-e15', (28, 24), (29, 24))
        self.add_line('sym-e17', (29, 24), (29, 23))
        self.add_arc('sym-e18', (29, 23), (33, 14), radius_x=14)
        self.add_line('sym-e19', (33, 14), (36, 11))
        self.add_arc('sym-e20', (12, 37), (15, 34), radius_x=29)
        self.add_arc('sym-e21', (15, 34), (19, 25), radius_x=14, sweep=False)
        self.add_arc('sym-e22', (19, 25), (19, 24), radius_x=10)
        self.add_line('sym-e24', (36, 37), (33, 34))
        self.add_arc('sym-e25', (33, 34), (29, 25), radius_x=14)
        self.add_arc('sym-e26', (29, 25), (29, 24), radius_x=10)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5')
        self.add_contour('sym-c1', 'sym-e6')
        self.add_contour('sym-c2', 'sym-e7')
        self.add_contour('sym-c3', 'sym-e8', 'sym-e9', 'sym-e11', 'sym-e12', 'sym-e13')
        self.add_contour('sym-c4', 'sym-e14', 'sym-e15', 'sym-e17', 'sym-e18', 'sym-e19')
        self.add_contour('sym-c5', 'sym-e20', 'sym-e21', 'sym-e22')
        self.add_contour('sym-c6', 'sym-e24', 'sym-e25', 'sym-e26')
        self.relate('connect', 'sym-c0', 'sym-c3', 'sym-c4')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c1', 'sym-c3', 'sym-c5')
        self.relate('connect', 'sym-c2', 'sym-c4', 'sym-c6')
        self.relate('connect', 'sym-c0', 'sym-c4')
        self.relate('connect', 'sym-c0', 'sym-c5')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c6')
        self.relate('connect', 'sym-c0', 'sym-c4')
        self.relate('connect', 'sym-c0', 'sym-c5')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c6')
        self.relate('connect', 'sym-c0', 'sym-c4')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c4')
        self.relate('connect', 'sym-c3', 'sym-c5')
        self.relate('connect', 'sym-c4', 'sym-c6')
        self.relate('connect', 'sym-c2', 'sym-c4')
        self.relate('connect', 'sym-c1', 'sym-c5')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c2', 'sym-c6')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
