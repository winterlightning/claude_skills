"""Penguin (animals), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3f2f6b4e-be80-5a0c-9a92-6c85b4d95a12'
SOURCE_PATH = 'icons-json/animals/penguin_3f2f6b4e-be80-5a0c-9a92-6c85b4d95a12.json'
AUTHOR = 'json_to_solo'

class Penguin(Solo48):
    icon_id = 'penguin'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    aliases = ()
    keywords = ('penguin', 'animals')

    def build(self):
        self.add_line('e0', (19, 25), (19, 29))
        self.add_line('e1', (33, 14), (33, 37))
        self.add_line('e2', (37, 44), (11, 44))
        self.add_line('e3', (37, 44), (40, 44))
        self.add_bezier('e4', (17, 20), ((15.341, 21.818), (14.088, 24.127), (13.12, 26.482)), ((11.293, 30.918), (11.326, 36.218), (13.322, 40.582)), ((13.819, 41.673), (14.484, 42.655), (15.141, 43.636)), ((15.267, 43.818), (15.865, 43.845), (16, 44)))
        self.add_bezier('e5', (17, 20), ((17.733, 21.427), (19, 23.3), (19, 25)))
        self.add_bezier('e6', (19, 29), ((19, 33.473), (21.236, 37.364), (25, 39)))
        self.add_bezier('e7', (17, 20), ((16.318, 19.545), (15.874, 19.355), (15.099, 19.082)), ((13.204, 18.427), (10.08, 19.1), (8, 19)))
        self.add_bezier('e8', (13, 14), ((13.362, 12.255), (13.709, 10.518), (14.594, 8.982)), ((16.362, 5.936), (19.958, 4.009), (23.251, 4.009)), ((23.383, 4.009), (23.516, 4), (23.648, 4)), ((23.651, 4), (23.653, 4), (23.655, 4)), ((23.941, 4), (24.219, 4.018), (24.505, 4.018)), ((25.128, 4.018), (25.819, 4.245), (26.408, 4.418)), ((29.937, 5.455), (32.32, 8.691), (33.011, 12.473)), ((33.103, 12.945), (33, 13.518), (33, 14)))
        self.add_bezier('e9', (33, 37), ((33, 38.936), (34.181, 40.609), (35.427, 41.945)), ((35.823, 42.373), (36.379, 42.773), (36.699, 43.264)), ((36.775, 43.418), (36.859, 43.573), (36.935, 43.736)), ((37.204, 44), (36.714, 43.727), (37, 44)))
        self.add_bezier('e10', (13, 14), ((10.895, 14.736), (9.558, 16.1), (8.227, 17.991)), ((8.109, 18.164), (8.101, 18.818), (8, 19)))
        self.add_contour('c0', 'e4')
        self.add_contour('c1', 'e5', 'e0', 'e6')
        self.add_contour('c2', 'e7')
        self.add_contour('c3', 'e8', 'e1', 'e9', 'e2')
        self.add_contour('c4', 'e10')
        self.add_contour('c5', 'e3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c3')
