"""Basketball ball (sports), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ddfe4674-487d-5d76-931c-e1fabe65e8d7'
SOURCE_PATH = 'icons-json/sports/basketball ball_ddfe4674-487d-5d76-931c-e1fabe65e8d7.json'
AUTHOR = 'json_to_solo'

class BasketballBall(Solo48):
    icon_id = 'basketball-ball'
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
        self.add_bezier('sym-e10', (19, 24), ((19.004, 23.865), (19, 24.137), (19, 24)))
        self.add_bezier('sym-e11', (19, 24), ((19, 23.863), (19.004, 23.135), (19, 23)))
        self.add_bezier('sym-e12', (19, 23), ((18.91, 19.662), (17.217, 16.479), (15, 14)))
        self.add_bezier('sym-e13', (15, 14), ((13.936, 12.805), (13.235, 11.998), (12, 11)))
        self.add_line('sym-e14', (24, 24), (28, 24))
        self.add_line('sym-e15', (28, 24), (29, 24))
        self.add_bezier('sym-e16', (29, 24), ((28.996, 23.865), (29, 24.137), (29, 24)))
        self.add_bezier('sym-e17', (29, 24), ((29, 23.863), (28.996, 23.135), (29, 23)))
        self.add_bezier('sym-e18', (29, 23), ((29.09, 19.662), (30.783, 16.479), (33, 14)))
        self.add_bezier('sym-e19', (33, 14), ((34.064, 12.805), (34.765, 11.998), (36, 11)))
        self.add_bezier('sym-e20', (12, 37), ((13.235, 36.002), (13.936, 35.195), (15, 34)))
        self.add_bezier('sym-e21', (15, 34), ((17.217, 31.521), (18.91, 28.338), (19, 25)))
        self.add_bezier('sym-e22', (19, 25), ((19.004, 24.865), (19, 24.137), (19, 24)))
        self.add_bezier('sym-e23', (19, 24), ((19, 23.863), (19.004, 24.135), (19, 24)))
        self.add_bezier('sym-e24', (36, 37), ((34.765, 36.002), (34.064, 35.195), (33, 34)))
        self.add_bezier('sym-e25', (33, 34), ((30.783, 31.521), (29.09, 28.338), (29, 25)))
        self.add_bezier('sym-e26', (29, 25), ((28.996, 24.865), (29, 24.137), (29, 24)))
        self.add_bezier('sym-e27', (29, 24), ((29, 23.863), (28.996, 24.135), (29, 24)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5')
        self.add_contour('sym-c1', 'sym-e6')
        self.add_contour('sym-c2', 'sym-e7')
        self.add_contour('sym-c3', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13')
        self.add_contour('sym-c4', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19')
        self.add_contour('sym-c5', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23')
        self.add_contour('sym-c6', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e27')
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
