"""Dress (clothes), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6d38ebdf-a077-54d8-b2cd-fd37cdddfcde'
SOURCE_PATH = 'icons-json/clothes/dress_6d38ebdf-a077-54d8-b2cd-fd37cdddfcde.json'
AUTHOR = 'json_to_solo'

class Dress6d38ebdf(Solo48):
    icon_id = 'dress-6d38ebdf'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'clothes'
    aliases = ()
    keywords = ('dress', 'clothes')

    def build(self):
        self.add_line('e0', (33, 9), (33, 4))
        self.add_line('e1', (16, 9), (16, 4))
        self.add_bezier('e2', (33, 9), ((33.3, 9.391), (33.67, 9.309), (33.87, 9.755)), ((34.71, 11.609), (32.5, 15.509), (32.02, 17.309)), ((31.87, 17.855), (31.58, 18.582), (31.65, 19.164)), ((31.83, 20.7), (33.59, 23.364), (34.34, 24.882)), ((36.06, 28.355), (37.44, 31.918), (38.65, 35.564)), ((39.004, 36.629), (40, 39.446), (40, 40.627)), ((40, 40.646), (40, 40.664), (40, 40.682)), ((40, 40.827), (36.86, 42.027), (36.33, 42.182)), ((32.45, 43.309), (28.35, 43.991), (24.26, 43.991)), ((24.171, 43.991), (24.093, 44), (24.004, 44)), ((24.003, 44), (24.001, 44), (24, 44)), ((23.91, 44), (23.83, 43.991), (23.74, 43.991)), ((19.64, 43.991), (15.53, 43.273), (11.63, 42.164)), ((10.45, 41.818), (9.31, 41.327), (8.2, 40.836)), ((8.13, 40.8), (8.07, 40.773), (8, 40.745)), ((8, 40.727), (8, 40.708), (8, 40.69)), ((8, 39.496), (9.006, 37.09), (9.4, 35.9)), ((10.69, 31.964), (12.24, 28.182), (14.07, 24.427)), ((14.71, 23.127), (16.24, 20.809), (16.48, 19.527)), ((16.95, 16.982), (14.48, 13.382), (14.87, 10.718)), ((14.98, 9.936), (15.58, 9.655), (16, 9)))
        self.add_bezier('e3', (33, 9), ((29.55, 8.636), (26.5, 8.791), (24, 11)))
        self.add_bezier('e4', (16, 9), ((19.42, 8.636), (21.6, 8.827), (24, 11)))
        self.add_contour('c0', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e0')
        self.add_contour('c3', 'e4')
        self.add_contour('c4', 'e1')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c3', 'c4')
