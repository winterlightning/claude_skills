"""Pinkie finger (wayfinding), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '307644e3-5d18-46e1-b564-4ac253bb9dd6'
SOURCE_PATH = 'icons-json/wayfinding/pinkie finger_307644e3-5d18-46e1-b564-4ac253bb9dd6.json'
AUTHOR = 'json_to_solo'

class PinkieFingerWayfinding(Solo48):
    icon_id = 'pinkie-finger-wayfinding'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'wayfinding'
    aliases = ()
    keywords = ('pinkie', 'finger', 'wayfinding')

    def build(self):
        self.add_line('e0', (15, 24), (15, 20))
        self.add_line('e1', (8, 22), (8, 32))
        self.add_line('e2', (40, 32), (40, 7))
        self.add_line('e3', (32, 8), (32, 24))
        self.add_line('e4', (22, 15), (23, 17))
        self.add_line('e5', (23, 17), (23, 24))
        self.add_line('e6', (23, 24), (23, 21))
        self.add_line('e7', (30, 14), (32, 17))
        self.add_bezier('e8', (15, 20), ((12.94, 19.1), (10.69, 18.4), (8.85, 20.364)), ((8.47, 20.755), (8.01, 21.455), (8.01, 22)), ((8.01, 22.064), (8, 21.936), (8, 22)))
        self.add_bezier('e9', (8, 32), ((8, 33.191), (8.52, 34.755), (9, 35.845)), ((11.45, 41.382), (17.27, 43.991), (23.61, 43.991)), ((23.738, 43.991), (23.876, 44), (24.004, 44)), ((24.006, 44), (24.008, 44), (24.01, 44)), ((24.49, 44), (24.96, 43.991), (25.44, 43.991)), ((31.76, 43.991), (36.74, 41.709), (39.05, 36.145)), ((39.52, 35.009), (39.99, 33.6), (39.99, 32.364)), ((39.99, 32.3), (40, 32.064), (40, 32)))
        self.add_bezier('e10', (40, 7), ((40, 6.936), (39.99, 6.609), (39.99, 6.545)), ((39.99, 4.809), (38.08, 4.009), (36.45, 4.009)), ((36.253, 4.009), (36.056, 4), (35.859, 4)), ((35.856, 4), (35.853, 4), (35.85, 4)), ((35.71, 4), (35.57, 4.018), (35.42, 4.018)), ((32.85, 4.018), (32, 5.918), (32, 8)))
        self.add_bezier('e11', (32, 24), ((32, 23.7), (32, 23.3), (32, 23)))
        self.add_bezier('e12', (15, 20), ((15.02, 17.6), (15.23, 15.273), (18.15, 14.345)), ((19.56, 13.9), (20.79, 14.318), (22, 15)))
        self.add_bezier('e13', (23, 17), ((23.26, 16.245), (23.45, 15.1), (23.93, 14.409)), ((25.36, 12.382), (28.16, 12.873), (30, 14)))
        self.add_contour('c0', 'e0', 'e8', 'e1', 'e9', 'e2', 'e10', 'e3', 'e11')
        self.add_contour('c1', 'e12', 'e4', 'e5', 'e6')
        self.add_contour('c2', 'e13', 'e7')
        self.relate('connect', 'c2', 'c0')
