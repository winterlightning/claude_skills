"""Batch-06/hand fan (accessories), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '50554124-7102-5f32-a1c2-2df0dd2c3975'
SOURCE_PATH = 'icons-json/accessories/batch-06/hand fan_50554124-7102-5f32-a1c2-2df0dd2c3975.json'
AUTHOR = 'json_to_solo'

class Batch06HandFan(Solo48):
    icon_id = 'batch-06-hand-fan'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    aliases = ()
    keywords = ('batch', 'hand', 'fan', 'accessories')

    def build(self):
        self.add_line('e0', (24, 32), (21, 33))
        self.add_line('e1', (27, 34), (24, 32))
        self.add_line('e2', (25, 32), (27, 32))
        self.add_line('e3', (25, 32), (26, 30))
        self.add_line('e4', (26, 30), (34, 10))
        self.add_line('e5', (24, 32), (22, 30))
        self.add_line('e6', (22, 30), (12, 11))
        self.add_line('e7', (24, 8), (24, 32))
        self.add_bezier('e8', (21, 33), ((20.718, 33.168), (20.773, 33.912), (20.636, 34.181)), ((19.573, 36.354), (20.845, 39.983), (23.855, 39.983)), ((23.982, 39.992), (24.109, 39.992), (24.236, 40)), ((24.237, 40), (24.238, 40), (24.239, 40)), ((24.302, 40), (24.365, 39.992), (24.427, 39.992)), ((27.518, 39.992), (29.036, 35.886), (27, 34)))
        self.add_bezier('e9', (27, 32), ((29.355, 30.139), (31.518, 27.966), (33.882, 26.114)), ((35.9, 24.539), (37.845, 22.888), (39.818, 21.263)), ((40.891, 20.387), (41.955, 19.503), (43.027, 18.627)), ((43.355, 18.358), (43.673, 18.097), (44, 17.827)), ((44, 17.825), (44, 17.822), (44, 17.818)), ((44, 17.602), (42.204, 15.81), (41.909, 15.512)), ((39.591, 13.187), (36.927, 11.608), (34, 10)))
        self.add_bezier('e10', (21, 33), ((18.736, 31.08), (17.2, 29.095), (15.055, 27.074)), ((13, 25.128), (10.7, 23.377), (8.509, 21.566)), ((7.382, 20.64), (6.255, 19.714), (5.118, 18.787)), ((4.877, 18.58), (4, 17.949), (4, 17.881)), ((4, 17.88), (4, 17.879), (4, 17.878)), ((4, 17.777), (5.364, 16.269), (5.618, 16)), ((7.482, 13.987), (9.473, 12.229), (12, 11)))
        self.add_bezier('e11', (34, 10), ((31.318, 8.888), (28.682, 8.017), (25.736, 8.017)), ((25.3, 8.017), (24.873, 8), (24.436, 8)), ((24.291, 8), (24.145, 8), (24, 8)), ((19.7, 8), (15.755, 9.215), (12, 11)))
        self.add_contour('c0', 'e0', 'e8', 'e1')
        self.add_contour('c1', 'e2', 'e9')
        self.add_contour('c2', 'e3', 'e4')
        self.add_contour('c3', 'e5', 'e6')
        self.add_contour('c4', 'e10')
        self.add_contour('c5', 'e7')
        self.add_contour('c6', 'e11')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c6')
        self.relate('connect', 'c2', 'c6')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c6')
        self.relate('connect', 'c4', 'c6')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c2', 'c0')
        self.relate('connect', 'c3', 'c0')
        self.relate('connect', 'c4', 'c0')
        self.relate('connect', 'c5', 'c6')
