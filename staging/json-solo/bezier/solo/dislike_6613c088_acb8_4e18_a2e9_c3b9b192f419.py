"""Dislike (rating), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6613c088-acb8-4e18-a2e9-c3b9b192f419'
SOURCE_PATH = 'icons-json/rating/dislike_6613c088-acb8-4e18-a2e9-c3b9b192f419.json'
AUTHOR = 'json_to_solo'

class DislikeRating(Solo48):
    icon_id = 'dislike-rating'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'rating'
    aliases = ()
    keywords = ('dislike', 'rating')

    def build(self):
        self.add_line('e0', (12, 8), (17, 7))
        self.add_line('e1', (19, 6), (30, 6))
        self.add_line('e2', (39, 13), (41, 20))
        self.add_line('e3', (38, 26), (26, 27))
        self.add_line('e4', (26, 27), (29, 33))
        self.add_line('e5', (24, 40), (17, 30))
        self.add_line('e6', (6, 26), (6, 7))
        self.add_bezier('e7', (6, 8), ((7.595, 8.123), (10.323, 8.556), (12, 8)))
        self.add_bezier('e8', (17, 7), ((17.745, 6.755), (18.206, 6), (19, 6)))
        self.add_bezier('e9', (30, 6), ((30.655, 6), (31.028, 6.008), (31.683, 6.008)), ((35.651, 6.008), (37.879, 9.637), (39, 13)))
        self.add_bezier('e10', (41, 20), ((41.245, 20.728), (41.992, 21.93), (41.992, 22.691)), ((42, 22.747), (42, 22.812), (42, 22.868)), ((42, 22.869), (42, 22.87), (42, 22.871)), ((42, 22.994), (41.992, 23.116), (41.992, 23.239)), ((41.992, 25.53), (39.915, 25.861), (38, 26)))
        self.add_bezier('e11', (29, 33), ((29.622, 34.44), (29.94, 36.395), (29.785, 37.975)), ((29.719, 38.637), (29.457, 39.308), (29.204, 39.914)), ((28.934, 40.56), (27.845, 41.992), (27.134, 41.992)), ((27.069, 41.992), (27.013, 42), (26.956, 42)), ((26.955, 42), (26.955, 42), (26.954, 42)), ((26.888, 42), (26.831, 41.992), (26.774, 41.992)), ((25.465, 41.992), (24.605, 40.916), (24, 40)))
        self.add_bezier('e12', (17, 30), ((13.776, 25.156), (11.49, 25.057), (6, 25)))
        self.add_contour('c0', 'e7', 'e0', 'e8', 'e1', 'e9', 'e2', 'e10', 'e3', 'e4', 'e11', 'e5', 'e12')
        self.add_contour('c1', 'e6')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
