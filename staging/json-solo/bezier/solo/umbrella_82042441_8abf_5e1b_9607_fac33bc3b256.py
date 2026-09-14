"""Batch-01/umbrella (accessories), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '82042441-8abf-5e1b-9607-fac33bc3b256'
SOURCE_PATH = 'icons-json/accessories/batch-01/umbrella_82042441-8abf-5e1b-9607-fac33bc3b256.json'
AUTHOR = 'json_to_solo'

class Batch01Umbrella(Solo48):
    icon_id = 'batch-01-umbrella'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    aliases = ()
    keywords = ('batch', 'umbrella', 'accessories')

    def build(self):
        self.add_line('e0', (24, 39), (24, 19))
        self.add_line('e1', (24, 4), (21, 5))
        self.add_line('e2', (21, 7), (24, 4))
        self.add_line('e3', (24, 4), (27, 5))
        self.add_line('e4', (40, 19), (40, 21))
        self.add_line('e5', (40, 21), (38, 20))
        self.add_line('e6', (31, 22), (31, 20))
        self.add_line('e7', (27, 7), (24, 4))
        self.add_bezier('e8', (30, 39), ((30.025, 40.845), (29.962, 42.255), (28.396, 43.436)), ((28.008, 43.727), (27.495, 43.991), (27.006, 43.991)), ((26.94, 44), (26.882, 44), (26.824, 44)), ((26.823, 44), (26.822, 44), (26.821, 44)), ((26.762, 44), (26.695, 43.991), (26.636, 43.991)), ((26.164, 43.991), (25.676, 43.7), (25.322, 43.391)), ((23.899, 42.136), (24, 40.782), (24, 39)))
        self.add_bezier('e9', (21, 5), ((14.92, 6.636), (9.844, 12.027), (8.472, 18.573)), ((8.281, 19.477), (8, 20.662), (8, 21.549)), ((8, 21.563), (8, 21.577), (8, 21.591)), ((8.514, 21.282), (9.036, 20.973), (9.549, 20.664)), ((10.442, 20.127), (11.478, 19.873), (12.488, 19.845)), ((13.794, 19.809), (15.124, 20.136), (16.261, 20.836)), ((16.724, 21.118), (18.08, 22.2), (18.105, 22.182)), ((18.122, 21.582), (18.139, 20.982), (18.156, 20.382)), ((18.181, 19.509), (18.223, 18.636), (18.291, 17.764)), ((18.585, 13.809), (18.945, 10.336), (21, 7)))
        self.add_bezier('e10', (30, 22), ((28.274, 20.745), (26.198, 19.445), (24, 19.455)), ((21.095, 19.473), (20.248, 20.209), (18, 22)))
        self.add_bezier('e11', (27, 5), ((33.425, 6.736), (38.771, 12.036), (40, 19)))
        self.add_bezier('e12', (38, 20), ((34.648, 18.545), (33.72, 19.8), (31, 22)))
        self.add_bezier('e13', (31, 20), ((30.874, 16.427), (30.223, 13.164), (28.935, 9.827)), ((28.682, 9.182), (27.48, 7.382), (27, 7)))
        self.add_contour('c0', 'e8', 'e0')
        self.add_contour('c1', 'e1', 'e9', 'e2')
        self.add_contour('c2', 'e10')
        self.add_contour('c3', 'e3', 'e11', 'e4', 'e5', 'e12', 'e6', 'e13', 'e7', closed=True)
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c2', 'c1')
