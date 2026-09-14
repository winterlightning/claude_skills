"""Finger point (wayfinding), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bae26537-844f-44bd-bc92-cf5af361e501'
SOURCE_PATH = 'icons-json/wayfinding/finger point_bae26537-844f-44bd-bc92-cf5af361e501.json'
AUTHOR = 'json_to_solo'

class FingerPointWayfinding(Solo48):
    icon_id = 'finger-point-wayfinding'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'wayfinding'
    aliases = ()
    keywords = ('finger', 'point', 'wayfinding')

    def build(self):
        self.add_line('e0', (21, 21), (21, 18))
        self.add_line('e1', (28, 21), (28, 19))
        self.add_line('e2', (15, 29), (15, 24))
        self.add_line('e3', (21, 18), (21, 7))
        self.add_line('e4', (15, 7), (15, 24))
        self.add_line('e5', (21, 18), (23, 17))
        self.add_line('e6', (40, 33), (40, 21))
        self.add_line('e7', (28, 19), (30, 18))
        self.add_bezier('e8', (35, 21), ((35, 20.7), (35, 20.3), (35, 20)))
        self.add_bezier('e9', (21, 7), ((20.66, 6.009), (19.95, 4.018), (18.49, 4.018)), ((18.43, 4.009), (18.37, 4.009), (18.3, 4)), ((18.298, 4), (18.296, 4), (18.294, 4)), ((18.176, 4), (18.048, 4.018), (17.93, 4.018)), ((16.42, 4.018), (15.49, 5.964), (15, 7)))
        self.add_bezier('e10', (23, 17), ((25.83, 16.236), (27.09, 16.636), (28, 19)))
        self.add_bezier('e11', (15, 24), ((11.95, 24.191), (8.01, 25.255), (8.01, 28.709)), ((8.01, 28.827), (8, 28.945), (8, 29.064)), ((8, 29.065), (8, 29.066), (8, 29.067)), ((8, 29.129), (8, 29.192), (8.01, 29.255)), ((8.01, 30.345), (8.45, 31.545), (8.79, 32.582)), ((10.38, 37.391), (13.85, 41.391), (19.13, 43.145)), ((20.59, 43.627), (22.1, 43.991), (23.67, 43.991)), ((24.28, 43.991), (24.9, 44), (25.511, 44)), ((25.521, 44), (25.53, 44), (25.54, 44)), ((26.02, 44), (26.5, 43.991), (26.98, 43.991)), ((32.67, 43.991), (39.99, 38.964), (39.99, 33.464)), ((39.99, 33.4), (40, 33.336), (40, 33.273)), ((40, 33.209), (40, 33.064), (40, 33)))
        self.add_bezier('e12', (40, 21), ((38.88, 18.2), (37.27, 18.682), (35, 20)))
        self.add_bezier('e13', (30, 18), ((32.63, 17.645), (33.71, 18.045), (35, 20)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e8')
        self.add_contour('c3', 'e2')
        self.add_contour('c4', 'e3', 'e9', 'e4')
        self.add_contour('c5', 'e5', 'e10')
        self.add_contour('c6', 'e11', 'e6', 'e12')
        self.add_contour('c7', 'e7', 'e13')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c0', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c1', 'c5')
        self.relate('connect', 'c1', 'c7')
        self.relate('connect', 'c5', 'c7')
        self.relate('connect', 'c2', 'c6')
        self.relate('connect', 'c2', 'c7')
        self.relate('connect', 'c6', 'c7')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c6')
        self.relate('connect', 'c4', 'c6')
