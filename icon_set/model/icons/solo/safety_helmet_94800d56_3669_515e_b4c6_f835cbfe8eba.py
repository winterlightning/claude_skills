"""Safety helmet (construction), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '94800d56-3669-515e-b4c6-f835cbfe8eba'
SOURCE_PATH = 'icons-json/construction/safety helmet_94800d56-3669-515e-b4c6-f835cbfe8eba.json'
AUTHOR = 'json_to_solo'

class SafetyHelmet(Solo48):
    icon_id = 'safety-helmet'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'construction'
    aliases = ()
    keywords = ('safety', 'helmet', 'construction')

    def build(self):
        self.add_line('e0', (29, 11), (28, 29))
        self.add_line('e1', (28, 29), (21, 29))
        self.add_line('e2', (21, 29), (19, 11))
        self.add_line('e3', (27, 8), (21, 8))
        self.add_bezier('e4', (29, 11), ((30.127, 11.49), (31.755, 11.95), (32.818, 12.59)), ((36.345, 14.71), (39.227, 18.33), (40.536, 22.53)), ((41.109, 24.37), (41.436, 26.41), (41.473, 28.34)), ((41.482, 28.57), (41.482, 30.51), (41.545, 30.57)), ((41.673, 30.7), (41.882, 30.69), (42.045, 30.76)), ((42.755, 31.05), (43.309, 31.35), (43.682, 32.09)), ((43.782, 32.3), (43.982, 32.65), (43.982, 32.89)), ((43.991, 33.02), (43.991, 33.15), (44, 33.28)), ((44, 33.281), (44, 33.282), (44, 33.283)), ((44, 33.352), (43.991, 33.431), (43.991, 33.51)), ((43.991, 35.26), (42.291, 36.45), (40.955, 36.97)), ((36.309, 38.78), (31.345, 39.98), (26.382, 39.98)), ((25.791, 39.98), (25.2, 40), (24.609, 40)), ((24.6, 40), (24.59, 40), (24.581, 40)), ((23.981, 40), (23.391, 39.98), (22.8, 39.98)), ((17.673, 39.98), (12.364, 39.13), (7.555, 37.17)), ((6.145, 36.59), (4.018, 35.39), (4.018, 33.44)), ((4.009, 33.361), (4, 33.292), (4, 33.214)), ((4, 33.212), (4, 33.211), (4, 33.21)), ((4, 31.55), (5.527, 31.13), (6.564, 30.57)), ((6.6, 30.55), (6.682, 28.88), (6.709, 28.3)), ((6.791, 26.17), (7.018, 24.04), (7.782, 22.06)), ((10.009, 16.27), (13.809, 13.33), (19, 11)))
        self.add_bezier('e5', (29, 11), ((28.727, 9.71), (28.645, 8.02), (27.136, 8.02)), ((27.073, 8.01), (27.009, 8.01), (26.936, 8)), ((26.864, 8), (27.073, 8), (27, 8)))
        self.add_bezier('e6', (21, 8), ((19.409, 8), (19.418, 9.58), (19, 11)))
        self.add_contour('c0', 'e4')
        self.add_contour('c1', 'e0', 'e1', 'e2')
        self.add_contour('c2', 'e5', 'e3', 'e6')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
