"""Paper ball (ecology), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1f506f94-c8e2-5f66-872b-f0986ae9024e'
SOURCE_PATH = 'pictographic-primitives/ecology/paper ball_1f506f94-c8e2-5f66-872b-f0986ae9024e.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class PaperBall(Solo48):
    icon_id = 'paper-ball'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'ecology'
    categories = ('primitives', 'ecology')
    aliases = ()
    keywords = ('paper', 'ball', 'ecology')

    def build(self):
        # Plan: absorb microscopic detours into neighboring cubics; retain the true extremes.
        # Reference: original stroke graph and contour extremes.
        self.add_line('e0', (29, 30), (31, 30))
        self.add_line('e1', (31, 30), (40, 33))
        self.add_line('e2', (40, 33), (42, 23))
        self.add_line('e3', (41, 20), (35, 14))
        self.add_line('e4', (32, 8), (26, 7))
        self.add_line('e5', (18, 40), (16, 40))
        self.add_line('e6', (12, 36), (7, 28))
        self.add_line('e7', (18, 25), (20, 29))
        self.add_bezier('e8', (26, 22), ((27.538, 20.552), (28.925, 19.737), (30.259, 18.076)), ((30.889, 17.307), (31.331, 16.35), (31.789, 15.475)), ((32.46, 14.223), (33.313, 13.244), (34, 12)))
        self.add_bezier('e9', (42, 23), ((42, 22.795), (41.984, 22.765), (41.984, 22.56)), ((41.984, 22.413), (42, 22.274), (42, 22.135)), ((42, 21.987), (42, 21.832), (42, 21.685)), ((42, 21.169), (41.36, 20.36), (41, 20)))
        self.add_bezier('e10', (35, 14), ((34.305, 13.305), (34.121, 12.652), (33.818, 11.727)), ((33.483, 10.705), (33.342, 8.385), (32, 8)))
        self.add_bezier('e11', (26, 7), ((25.198, 6.771), (24.163, 6.0), (23.345, 6)), ((23.231, 6), (23.125, 6.008), (23.018, 6.008)), ((21.75, 6.008), (19.156, 8.626), (18.052, 9.477)), ((16.841, 10.41), (15.548, 11.155), (14.108, 11.703)), ((12.652, 12.259), (10.713, 12.734), (9.87, 14.198)), ((9.355, 15.082), (9.131, 16.035), (9, 17)))
        self.add_bezier('e12', (40, 33), ((38.486, 34.424), (37.336, 35.839), (35.815, 37.238)), ((35.086, 37.909), (34.334, 38.809), (33.466, 39.325)), ((32.321, 40.004), (31.028, 40.47), (29.785, 40.936)), ((28.68, 41.345), (27.125999999999998, 42.0), (25.915, 42)), ((25.203, 42.0), (24.442, 41.624), (23.795, 41.362)), ((22.936, 41.018), (22.061, 40.732), (21.21, 40.388)), ((20.212, 39.987), (19.105, 40), (18, 40)))
        self.add_bezier('e13', (16, 40), ((15.697, 40), (15.262, 39.603), (14.951, 39.513)), ((13.895, 39.21), (12.717, 38.024), (12.128, 37.124)), ((11.956, 36.854), (12.164, 36.27), (12, 36)))
        self.add_bezier('e14', (7, 28), ((6.656, 27.419), (5.999999999999999, 26.594), (5.999999999999999, 25.882)), ((5.999999999999999, 24.925), (7.915, 21.881), (8.389, 20.744)), ((8.708, 19.975), (8.888, 19.148), (9.076, 18.338)), ((9.125, 18.125), (9.175, 17.905), (9.224, 17.684)), ((9.24, 17.61), (9.256, 17.528), (9.273, 17.455)), ((9.518, 17.455), (11.801, 18.805), (12.235, 19.034)), ((13.061, 19.475), (16.35, 20.965), (16.939, 21.709)), ((17.602, 22.552), (17.607, 24.018), (18, 25)))
        self.add_contour('c0', 'e8', closed=False)
        self.add_contour('c1', 'e0', 'e1', 'e2', 'e9', 'e3', 'e10', 'e4', 'e11', closed=False)
        self.add_contour('c2', 'e12', 'e5', 'e13', 'e6', 'e14', 'e7', closed=False)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c1', 'c2')
