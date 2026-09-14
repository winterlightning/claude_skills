"""Vip crown queen (rewards), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9bf9adad-592d-5190-a18f-1b11b32973bf'
SOURCE_PATH = 'icons-json/rewards/vip crown queen_9bf9adad-592d-5190-a18f-1b11b32973bf.json'
AUTHOR = 'json_to_solo'

class VipCrownQueenRewards(Solo48):
    icon_id = 'vip-crown-queen-rewards'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'rewards'
    aliases = ()
    keywords = ('vip', 'crown', 'queen', 'rewards')

    def build(self):
        self.add_bezier('sym-e0', (24, 40), ((23.925, 40), (24.076, 40), (24, 40)))
        self.add_bezier('sym-e1', (24, 40), ((20.382, 40), (16.518, 39.99), (13, 39)))
        self.add_bezier('sym-e2', (13, 39), ((11.245, 38.5), (10.018, 37.81), (9, 36)))
        self.add_bezier('sym-e3', (9, 36), ((8.491, 35.1), (8.273, 35.04), (8, 34)))
        self.add_line('sym-e4', (8, 34), (4, 20))
        self.add_bezier('sym-e5', (4, 20), ((4, 19.48), (4, 18.53), (4, 18)))
        self.add_bezier('sym-e6', (4, 18), ((4, 16.16), (5.727, 16.75), (7, 17)))
        self.add_bezier('sym-e7', (7, 17), ((9.973, 17.59), (12.627, 19.08), (15, 21)))
        self.add_line('sym-e8', (15, 21), (19, 13))
        self.add_bezier('sym-e9', (19, 13), ((19.86, 11.108), (21.906, 8), (24, 8)))
        self.add_bezier('sym-e10', (24, 8), ((26.094, 8), (28.14, 11.108), (29, 13)))
        self.add_line('sym-e11', (29, 13), (33, 21))
        self.add_bezier('sym-e12', (33, 21), ((35.373, 19.08), (38.027, 17.59), (41, 17)))
        self.add_bezier('sym-e13', (41, 17), ((42.273, 16.75), (44, 16.16), (44, 18)))
        self.add_bezier('sym-e14', (44, 18), ((44, 18.53), (44, 19.48), (44, 20)))
        self.add_line('sym-e15', (44, 20), (40, 34))
        self.add_bezier('sym-e16', (40, 34), ((39.727, 35.04), (39.509, 35.1), (39, 36)))
        self.add_bezier('sym-e17', (39, 36), ((37.982, 37.81), (36.755, 38.5), (35, 39)))
        self.add_bezier('sym-e18', (35, 39), ((31.482, 39.99), (27.618, 40), (24, 40)))
        self.add_bezier('sym-e19', (24, 40), ((23.924, 40), (24.075, 40), (24, 40)))
        self.add_bezier('sym-e20', (24, 31), ((20.726, 31), (17.054, 31.357), (14, 32)))
        self.add_bezier('sym-e21', (14, 32), ((12.564, 32.3), (11.209, 33.01), (10, 34)))
        self.add_bezier('sym-e22', (10, 34), ((9.473, 34.45), (8.536, 34.55), (8, 35)))
        self.add_bezier('sym-e23', (8, 35), ((8.064, 35.25), (8.936, 35.75), (9, 36)))
        self.add_bezier('sym-e24', (24, 31), ((27.274, 31), (30.946, 31.357), (34, 32)))
        self.add_bezier('sym-e25', (34, 32), ((35.436, 32.3), (36.791, 33.01), (38, 34)))
        self.add_bezier('sym-e26', (38, 34), ((38.527, 34.45), (39.464, 34.55), (40, 35)))
        self.add_bezier('sym-e27', (40, 35), ((39.936, 35.25), (39.064, 35.75), (39, 36)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', closed=True)
        self.add_contour('sym-c1', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23')
        self.add_contour('sym-c2', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e27')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
