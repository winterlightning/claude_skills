"""Warp rise (design), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b44d5b08-5e93-4ae1-8f5d-adcaa261cb2b'
SOURCE_PATH = 'icons-json/design/warp rise_b44d5b08-5e93-4ae1-8f5d-adcaa261cb2b.json'
AUTHOR = 'json_to_solo'

class WarpRiseDesign(Solo48):
    icon_id = 'warp-rise-design'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('warp', 'rise', 'design')

    def build(self):
        self.add_line('e0', (22, 28), (28, 22))
        self.add_line('e1', (6, 33), (6, 42))
        self.add_line('e2', (24, 36), (31, 30))
        self.add_line('e3', (42, 25), (42, 17))
        self.add_line('e4', (6, 33), (6, 22))
        self.add_line('e5', (21, 17), (26, 12))
        self.add_line('e6', (42, 6), (42, 17))
        self.add_bezier('e7', (6, 33), ((12.095, 33.376), (17.435, 32.565), (22, 28)))
        self.add_bezier('e8', (28, 22), ((31.927, 18.073), (36.674, 17.033), (42, 17)))
        self.add_bezier('e9', (6, 42), ((8.242, 42), (10.484, 41.984), (12.725, 41.984)), ((13.208, 41.984), (13.765, 41.82), (14.239, 41.705)), ((17.888, 40.83), (21.333, 38.667), (24, 36)))
        self.add_bezier('e10', (31, 30), ((33.34, 27.66), (36.142, 25.555), (39.431, 25.039)), ((40.29, 24.9), (41.141, 25.09), (42, 25)))
        self.add_bezier('e11', (6, 22), ((11.506, 22.745), (16.901, 21.099), (21, 17)))
        self.add_bezier('e12', (26, 12), ((28.765, 9.235), (32.542, 7.088), (36.371, 6.303)), ((37.042, 6.164), (37.778, 6.008), (38.465, 6.008)), ((38.498, 6.008), (38.531, 6), (38.564, 6)), ((39.259, 6), (39.955, 6.008), (40.642, 6.008)), ((40.871, 6.008), (41.1, 6.008), (41.329, 6.008)), ((41.37, 6.008), (41.403, 6), (41.435, 6)), ((41.624, 6), (41.812, 6), (42, 6)))
        self.add_contour('c0', 'e7', 'e0', 'e8')
        self.add_contour('c1', 'e1', 'e9', 'e2', 'e10', 'e3')
        self.add_contour('c2', 'e4', 'e11', 'e5', 'e12', 'e6')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
