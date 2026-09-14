"""Arm flex (health), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '90cac3c3-16d4-5ca2-95e6-98d1851e462d'
SOURCE_PATH = 'icons-json/health/arm flex_90cac3c3-16d4-5ca2-95e6-98d1851e462d.json'
AUTHOR = 'json_to_solo'

class ArmFlexHealth(Solo48):
    icon_id = 'arm-flex-health'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    aliases = ()
    keywords = ('arm', 'flex', 'health')

    def build(self):
        self.add_line('e0', (21, 30), (19, 33))
        self.add_line('e1', (19, 33), (18, 19))
        self.add_line('e2', (18, 19), (21, 17))
        self.add_line('e3', (23, 5), (15, 10))
        self.add_line('e4', (11, 15), (9, 34))
        self.add_line('e5', (13, 44), (40, 44))
        self.add_bezier('e6', (35, 32), ((34.411, 31.109), (33.777, 30.282), (32.994, 29.564)), ((29.566, 26.382), (24.091, 26.664), (21, 30)))
        self.add_bezier('e7', (21, 17), ((22.053, 17.755), (22.754, 18.182), (24.059, 18.291)), ((28.227, 18.645), (31.141, 13.273), (29.583, 9.327)), ((29.204, 8.373), (28.573, 7.655), (27.924, 6.9)), ((27.436, 6.336), (25.836, 4.009), (24.977, 4.009)), ((24.919, 4.009), (24.869, 4), (24.811, 4)), ((24.81, 4), (24.809, 4), (24.808, 4)), ((24.758, 4.009), (24.699, 4.009), (24.648, 4.018)), ((24.227, 4.018), (23.354, 4.773), (23, 5)))
        self.add_bezier('e8', (15, 10), ((13.442, 11.009), (11.269, 12.973), (11, 15)))
        self.add_bezier('e9', (9, 34), ((8.789, 35.573), (8, 38.027), (8, 39.518)), ((8, 39.519), (8, 39.521), (8, 39.522)), ((8, 39.603), (8, 39.683), (8.008, 39.773)), ((8.008, 41.591), (9.322, 43.273), (10.897, 43.827)), ((11.385, 44), (12.034, 43.991), (12.539, 43.991)), ((12.707, 43.991), (12.832, 44), (13, 44)))
        self.add_bezier('e10', (21, 17), ((22.187, 15.791), (21.941, 14.791), (22, 13)))
        self.add_bezier('e11', (40, 28), ((37.499, 28.755), (36.179, 29.518), (35, 32)))
        self.add_contour('c0', 'e6', 'e0', 'e1', 'e2')
        self.add_contour('c1', 'e7', 'e3', 'e8', 'e4', 'e9', 'e5')
        self.add_contour('c2', 'e10')
        self.add_contour('c3', 'e11')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
