"""Watchtower (video-games), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b5ab23b2-5464-476e-b461-f81265e40aca'
SOURCE_PATH = 'icons-json/video-games/watchtower_b5ab23b2-5464-476e-b461-f81265e40aca.json'
AUTHOR = 'json_to_solo'

class WatchtowerVideoGames(Solo48):
    icon_id = 'watchtower-video-games'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    aliases = ()
    keywords = ('watchtower', 'video-games')

    def build(self):
        self.add_line('e0', (17, 10), (17, 4))
        self.add_line('e1', (31, 10), (31, 4))
        self.add_line('e2', (17, 4), (8, 4))
        self.add_line('e3', (8, 4), (8, 14))
        self.add_line('e4', (8, 14), (11, 17))
        self.add_line('e5', (11, 18), (11, 29))
        self.add_line('e6', (8, 34), (8, 44))
        self.add_line('e7', (8, 44), (20, 44))
        self.add_line('e8', (20, 44), (20, 36))
        self.add_line('e9', (28, 36), (28, 44))
        self.add_line('e10', (28, 44), (40, 44))
        self.add_line('e11', (40, 44), (40, 33))
        self.add_line('e12', (40, 32), (37, 30))
        self.add_line('e13', (37, 30), (37, 18))
        self.add_line('e14', (40, 14), (40, 4))
        self.add_line('e15', (40, 4), (31, 4))
        self.add_line('e16', (17, 4), (31, 4))
        self.add_bezier('e17', (11, 17), ((11.286, 17.309), (10.731, 17.664), (11, 18)))
        self.add_bezier('e18', (11, 29), ((10.806, 29.364), (11.099, 30.145), (10.821, 30.482)), ((10.265, 31.136), (8.008, 32.927), (8.008, 33.773)), ((8.008, 33.845), (8, 33.927), (8, 34)))
        self.add_bezier('e19', (20, 36), ((20.446, 34.273), (21.112, 32.673), (22.779, 32.091)), ((25.027, 31.309), (28, 33.2), (28, 36)))
        self.add_bezier('e20', (40, 33), ((40, 32.7), (40, 32.3), (40, 32)))
        self.add_bezier('e21', (37, 18), ((37.126, 17.782), (36.775, 17.182), (36.943, 16.964)), ((37.676, 16.009), (39.284, 15.427), (39.865, 14.473)), ((39.949, 14.336), (39.907, 14.136), (40, 14)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e3', 'e4', 'e17', 'e5', 'e18', 'e6', 'e7', 'e8', 'e19', 'e9', 'e10', 'e11', 'e20', 'e12', 'e13', 'e21', 'e14', 'e15')
        self.add_contour('c3', 'e16')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
