"""Admob logo (_uncategorized_01), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '166238e9-fe64-4404-9aa2-ae5f4b82de80'
SOURCE_PATH = 'icons-json/_uncategorized_01/admob logo_166238e9-fe64-4404-9aa2-ae5f4b82de80.json'
AUTHOR = 'json_to_solo'

class AdmobLogoUncategorized01(Solo48):
    icon_id = 'admob-logo-uncategorized-01'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized_01'
    aliases = ()
    keywords = ('admob', 'logo', '_uncategorized_01')

    def build(self):
        self.add_line('e0', (22, 43), (14, 43))
        self.add_line('e1', (8, 37), (8, 19))
        self.add_line('e2', (40, 19), (40, 39))
        self.add_line('e3', (29, 36), (20, 36))
        self.add_line('e4', (19, 34), (19, 19))
        self.add_line('e5', (29, 19), (29, 36))
        self.add_bezier('e6', (14, 43), ((11.406, 43), (8.008, 39.8), (8.008, 36.945)), ((8.008, 36.873), (8, 37.073), (8, 37)))
        self.add_bezier('e7', (8, 19), ((8, 17.7), (8.421, 16.727), (8.808, 15.509)), ((10.897, 8.973), (16.952, 4.009), (23.453, 4.009)), ((23.519, 4.009), (23.585, 4), (23.652, 4)), ((23.653, 4), (23.654, 4), (23.655, 4)), ((23.924, 4), (24.202, 4.009), (24.472, 4.009)), ((30.771, 4.009), (36.362, 8.573), (38.855, 14.655)), ((39.411, 16.009), (39.983, 17.736), (39.983, 19.236)), ((39.992, 19.309), (39.992, 18.927), (40, 19)))
        self.add_bezier('e8', (40, 39), ((40, 40.618), (38.366, 43.118), (37.044, 43.691)), ((36.514, 43.918), (35.924, 43.982), (35.36, 43.982)), ((35.225, 43.982), (35.082, 44), (34.939, 44)), ((34.935, 44), (34.93, 44), (34.926, 44)), ((34.652, 44), (34.379, 43.982), (34.105, 43.982)), ((31.764, 43.982), (29.76, 42.382), (29.221, 39.855)), ((28.952, 38.582), (29, 37.3), (29, 36)))
        self.add_bezier('e9', (20, 36), ((19.326, 35.318), (19, 35.064), (19, 34)))
        self.add_bezier('e10', (19, 19), ((19, 18.055), (19.545, 16.455), (20.067, 15.736)), ((22.324, 12.618), (26.425, 12.991), (28.286, 16.345)), ((28.623, 16.955), (29, 18.273), (29, 19)))
        self.add_contour('c0', 'e0', 'e6', 'e1', 'e7', 'e2', 'e8')
        self.add_contour('c1', 'e3', 'e9', 'e4', 'e10', 'e5', closed=True)
        self.relate('connect', 'c0', 'c1')
