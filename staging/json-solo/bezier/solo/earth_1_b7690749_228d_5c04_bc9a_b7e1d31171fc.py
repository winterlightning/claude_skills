"""Earth 1 (maps), converted from the icons-json construction graph by json_to_solo --mode bezier. CIRCLE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b7690749-228d-5c04-bc9a-b7e1d31171fc'
SOURCE_PATH = 'icons-json/maps/earth 1_b7690749-228d-5c04-bc9a-b7e1d31171fc.json'
AUTHOR = 'json_to_solo'

class Earth1B7690749(Solo48):
    icon_id = 'earth-1-b7690749'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'maps'
    aliases = ()
    keywords = ('earth', 'maps')

    def build(self):
        self.add_line('e0', (12, 23), (12, 28))
        self.add_line('e1', (23, 35), (25, 33))
        self.add_line('e2', (25, 29), (22, 28))
        self.add_line('e3', (29, 21), (30, 16))
        self.add_line('e4', (36, 11), (41, 14))
        self.add_line('e5', (10, 20), (11, 23))
        self.add_arc('e6-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e6-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_bezier('e7', (5, 19), ((6.791, 20.727), (8.436, 23.073), (11.273, 23.091)), ((11.573, 23.091), (11.7, 23), (12, 23)))
        self.add_bezier('e8', (12, 28), ((12, 31.682), (14.427, 31.136), (15.7, 33.645)), ((16.391, 34.991), (16.245, 36.627), (16.373, 38.091)), ((16.427, 38.7), (16.991, 41.645), (17.364, 41.827)), ((17.4, 41.845), (18.464, 40.882), (18.9, 40.455)), ((20.6, 38.809), (21.345, 36.655), (23, 35)))
        self.add_bezier('e9', (25, 33), ((25.827, 32.173), (26.173, 30.591), (25.745, 29.473)), ((25.582, 29.064), (25.282, 29.291), (25, 29)))
        self.add_bezier('e10', (22, 28), ((21.073, 27.691), (19.418, 25.236), (18.273, 24.536)), ((16.518, 23.455), (13.991, 23.273), (12, 23)))
        self.add_bezier('e11', (41, 34), ((39.945, 32.627), (39.191, 31.327), (38.727, 29.618)), ((38.264, 27.927), (38.336, 26.109), (36.7, 25.064)), ((36.218, 24.755), (35.5, 24.645), (34.927, 24.636)), ((32.9, 24.6), (29.709, 25.873), (28.709, 23.227)), ((28.491, 22.645), (28.8, 21.6), (29, 21)))
        self.add_bezier('e12', (30, 16), ((30.209, 15.364), (30.755, 14.609), (31.145, 14.045)), ((31.827, 13.045), (34.6, 10.3), (36, 11)))
        self.add_bezier('e13', (19, 5), ((18.509, 8.2), (18.082, 11.764), (16.082, 14.473)), ((14.1, 17.173), (10.109, 15.555), (10, 20)))
        self.add_contour('c0', 'e7', 'e0', 'e8', 'e1', 'e9', 'e2', 'e10')
        self.add_contour('c1', 'e11', 'e3', 'e12', 'e4')
        self.add_contour('c2', 'e13', 'e5')
        self.add_contour('e6', 'e6-top', 'e6-bottom', closed=True)
        self.relate('connect', 'c0', 'e6')
        self.relate('connect', 'c1', 'e6')
        self.relate('connect', 'c1', 'e6')
        self.relate('connect', 'c2', 'e6')
        self.relate('connect', 'c2', 'c0')
