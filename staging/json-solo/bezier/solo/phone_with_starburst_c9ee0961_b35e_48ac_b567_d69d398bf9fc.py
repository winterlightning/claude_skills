"""Phone with starburst (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c9ee0961-b35e-48ac-b567-d69d398bf9fc'
SOURCE_PATH = 'icons-json/symbol/phone with starburst_c9ee0961-b35e-48ac-b567-d69d398bf9fc.json'
AUTHOR = 'json_to_solo'

class PhoneWithStarburstSymbol(Solo48):
    icon_id = 'phone-with-starburst-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('phone', 'with', 'starburst', 'symbol')

    def build(self):
        self.add_line('e0', (24, 14), (24, 8))
        self.add_line('e1', (35, 15), (37, 10))
        self.add_line('e2', (11, 10), (14, 15))
        self.add_line('e3', (37, 40), (41, 40))
        self.add_line('e4', (7, 40), (15, 39))
        self.add_bezier('e5', (41, 40), ((41.073, 40), (41.418, 39.99), (41.491, 39.99)), ((42.918, 39.99), (43.991, 38.48), (43.991, 36.98)), ((43.991, 36.291), (44, 35.602), (44, 34.922)), ((44, 34.912), (44, 34.901), (44, 34.89)), ((44, 34.56), (43.991, 34.23), (43.991, 33.9)), ((43.991, 32.8), (43.682, 31.59), (43.309, 30.59)), ((41.764, 26.4), (37.927, 24.67), (34.136, 23.9)), ((32.218, 23.5), (30.3, 23.25), (28.355, 23.11)), ((23.145, 22.72), (17.509, 22.72), (12.427, 24.19)), ((10.3, 24.81), (7.991, 25.71), (6.445, 27.53)), ((4.627, 29.67), (4.018, 32.36), (4.018, 35.21)), ((4.018, 35.682), (4, 36.165), (4, 36.637)), ((4, 36.645), (4, 36.652), (4, 36.66)), ((4, 38.1), (4.855, 39.98), (6.345, 39.98)), ((6.473, 39.99), (6.873, 39.99), (7, 40)))
        self.add_bezier('e6', (15, 39), ((16.273, 38.04), (16.545, 37.21), (16.682, 35.49)), ((16.718, 35.12), (16.909, 32.82), (17.264, 32.6)), ((17.409, 32.51), (19.836, 32.57), (20.145, 32.57)), ((22.709, 32.53), (25.273, 32.54), (27.836, 32.6)), ((28.382, 32.61), (30.727, 32.66), (31.009, 33.07)), ((31.4, 33.64), (31.391, 34.19), (31.473, 34.84)), ((31.718, 36.95), (32.045, 39.36), (34.336, 39.78)), ((34.873, 39.88), (35.464, 39.98), (36, 39.98)), ((36.245, 39.98), (36.755, 40), (37, 40)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3', 'e5', 'e4', 'e6', closed=True)
