"""Car engine (transportation), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c52b8c01-47ae-59ce-bbfb-9594b8bcc540'
SOURCE_PATH = 'icons-json/transportation/car engine_c52b8c01-47ae-59ce-bbfb-9594b8bcc540.json'
AUTHOR = 'json_to_solo'

class CarEngineC52b8c01(Solo48):
    icon_id = 'car-engine-c52b8c01'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('car', 'engine', 'transportation')

    def build(self):
        self.add_line('e0', (37, 22), (42, 22))
        self.add_line('e1', (44, 25), (44, 30))
        self.add_line('e2', (40, 34), (37, 34))
        self.add_line('e3', (30, 8), (17, 8))
        self.add_line('e4', (23, 8), (23, 14))
        self.add_line('e5', (9, 25), (4, 25))
        self.add_line('e6', (4, 18), (4, 31))
        self.add_line('e7', (19, 40), (34, 40))
        self.add_line('e8', (37, 37), (37, 19))
        self.add_line('e9', (37, 19), (33, 16))
        self.add_line('e10', (30, 14), (16, 14))
        self.add_line('e11', (15, 14), (9, 18))
        self.add_line('e12', (9, 18), (9, 33))
        self.add_bezier('e13', (42, 22), ((42.827, 22.27), (43.982, 22.63), (43.982, 23.82)), ((43.982, 24.05), (44, 24.29), (44, 24.52)), ((44, 24.68), (44, 24.84), (44, 25)))
        self.add_bezier('e14', (44, 30), ((44, 30.23), (43.991, 30.46), (43.991, 30.69)), ((43.991, 32.34), (42.718, 33.86), (41.218, 34.07)), ((40.918, 34.11), (40.291, 34), (40, 34)))
        self.add_bezier('e15', (9, 33), ((10.927, 34.7), (13.345, 36.35), (15.318, 38)), ((16.236, 38.76), (17.755, 40), (19, 40)))
        self.add_bezier('e16', (34, 40), ((34.064, 40), (34.127, 39.99), (34.182, 39.99)), ((35.536, 39.99), (37, 38.43), (37, 37)))
        self.add_bezier('e17', (33, 16), ((32.118, 15.27), (31.218, 14), (30, 14)))
        self.add_bezier('e18', (16, 14), ((15.709, 14), (15.3, 14), (15, 14)))
        self.add_contour('c0', 'e0', 'e13', 'e1', 'e14', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4')
        self.add_contour('c3', 'e5')
        self.add_contour('c4', 'e6')
        self.add_contour('c5', 'e15', 'e7', 'e16', 'e8', 'e9', 'e17', 'e10', 'e18', 'e11', 'e12', closed=True)
        self.relate('connect', 'c0', 'c5')
        self.relate('connect', 'c0', 'c5')
        self.relate('connect', 'c2', 'c1')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c3', 'c4')
