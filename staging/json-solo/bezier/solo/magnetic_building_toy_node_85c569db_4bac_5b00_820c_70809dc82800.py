"""Magnetic building toy node (internet), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '85c569db-4bac-5b00-820c-70809dc82800'
SOURCE_PATH = 'icons-json/internet/magnetic building toy node_85c569db-4bac-5b00-820c-70809dc82800.json'
AUTHOR = 'json_to_solo'

class MagneticBuildingToyNodeInternet(Solo48):
    icon_id = 'magnetic-building-toy-node-internet'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'internet'
    aliases = ()
    keywords = ('magnetic', 'building', 'toy', 'node', 'internet')

    def build(self):
        self.add_line('e0', (35, 35), (31, 29))
        self.add_line('e1', (29, 17), (35, 13))
        self.add_line('e2', (17, 19), (13, 13))
        self.add_line('e3', (19, 31), (13, 35))
        self.add_arc('e4-top', (34, 38), (42, 38), radius_x=4)
        self.add_arc('e4-bottom', (42, 38), (34, 38), radius_x=4)
        self.add_arc('e5-top', (16, 24), (32, 24), radius_x=8)
        self.add_arc('e5-bottom', (32, 24), (16, 24), radius_x=8)
        self.add_bezier('e6', (35, 13), ((34.632, 12.206), (33.843, 10.934), (33.818, 10.034)), ((33.753, 7.915), (35.757, 6.016), (37.852, 6.016)), ((37.958, 6.008), (38.065, 6), (38.171, 6)), ((40.118, 6), (41.992, 7.882), (41.992, 9.829)), ((41.992, 9.877), (42, 9.926), (42, 9.974)), ((42, 9.975), (42, 9.976), (42, 9.976)), ((42, 10.025), (41.992, 10.075), (41.992, 10.124)), ((41.992, 11.073), (41.542, 11.989), (40.953, 12.693)), ((39.742, 14.174), (37.827, 14.779), (35.995, 14.116)), ((35.52, 13.945), (35.434, 13.254), (35, 13)))
        self.add_bezier('e7', (13, 13), ((13.311, 12.255), (14.108, 11.776), (14.157, 10.95)), ((14.247, 9.412), (13.519, 7.923), (12.341, 6.974)), ((11.76, 6.499), (10.991, 6), (10.214, 6)), ((10.213, 6), (10.212, 6), (10.211, 6)), ((10.163, 6), (10.123, 6), (10.083, 6)), ((9.976, 6.008), (9.87, 6.008), (9.764, 6.016)), ((7.841, 6.016), (6.016, 7.906), (6.016, 9.829)), ((6.008, 9.878), (6.008, 9.927), (6, 9.976)), ((6, 12.586), (8.275, 14.542), (10.827, 14.395)), ((11.703, 14.345), (12.272, 13.393), (13, 13)))
        self.add_bezier('e8', (13, 35), ((13.221, 35.695), (13.977, 36.944), (14.035, 37.68)), ((14.182, 39.758), (12.545, 41.992), (10.336, 41.992)), ((10.256, 42), (10.183, 42), (10.103, 42)), ((10.102, 42), (10.1, 42), (10.099, 42)), ((9.96, 42), (9.813, 41.992), (9.674, 41.992)), ((7.71, 41.992), (6.008, 39.922), (6.008, 38.048)), ((6, 37.984), (6, 37.911), (6, 37.847)), ((6, 37.846), (6, 37.845), (6, 37.844)), ((6, 37.721), (6.008, 37.59), (6.016, 37.467)), ((6.016, 35.332), (8.577, 33.434), (10.598, 33.565)), ((11.588, 33.63), (12.157, 34.566), (13, 35)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e6')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e7', closed=True)
        self.add_contour('c4', 'e3', 'e8')
        self.add_contour('e4', 'e4-top', 'e4-bottom', closed=True)
        self.add_contour('e5', 'e5-top', 'e5-bottom', closed=True)
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c0', 'e4')
        self.relate('connect', 'c0', 'e5')
        self.relate('connect', 'c1', 'e5')
        self.relate('connect', 'c2', 'e5')
        self.relate('connect', 'c4', 'e5')
