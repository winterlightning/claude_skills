"""Drone (technology), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6cdf8164-727e-4119-a576-7aff4948255a'
SOURCE_PATH = 'icons-json/technology/drone_6cdf8164-727e-4119-a576-7aff4948255a.json'
AUTHOR = 'json_to_solo'

class DroneTechnology(Solo48):
    icon_id = 'drone-technology'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'technology'
    aliases = ()
    keywords = ('drone', 'technology')

    def build(self):
        self.add_line('e0', (36, 40), (34, 40))
        self.add_line('e1', (36, 22), (41, 22))
        self.add_line('e2', (4, 8), (9, 8))
        self.add_line('e3', (15, 40), (12, 40))
        self.add_line('e4', (36, 8), (44, 8))
        self.add_line('e5', (13, 8), (9, 8))
        self.add_line('e6', (16, 14), (20, 12))
        self.add_line('e7', (33, 14), (39, 14))
        self.add_line('e8', (9, 14), (6, 15))
        self.add_line('e9', (8, 22), (12, 22))
        self.add_line('e10', (9, 14), (9, 8))
        self.add_line('e11', (39, 9), (39, 14))
        self.add_bezier('e12', (31, 24), ((30.218, 24.58), (29.718, 25.16), (28.791, 25.44)), ((26.964, 26), (22.055, 26), (20.218, 25.4)), ((19.245, 25.09), (18.836, 24.61), (18, 24)))
        self.add_bezier('e13', (31, 24), ((34.364, 27.08), (37.391, 30.25), (37.391, 35.33)), ((37.391, 36.54), (37.482, 39.98), (35.918, 39.98)), ((35.882, 39.99), (36.036, 39.99), (36, 40)))
        self.add_bezier('e14', (31, 24), ((32.373, 22.9), (34.236, 22), (36, 22)))
        self.add_bezier('e15', (41, 22), ((42.545, 22), (43.991, 20.33), (43.991, 18.73)), ((43.991, 18.57), (44, 18.41), (44, 18.25)), ((44, 18.17), (44, 18.09), (44, 18.01)), ((44, 14.93), (41.373, 14), (39, 14)))
        self.add_bezier('e16', (12, 40), ((11.864, 39.87), (11.836, 39.91), (11.691, 39.73)), ((11, 38.86), (11.155, 36.58), (11.182, 35.48)), ((11.345, 30.33), (14.609, 27.14), (18, 24)))
        self.add_bezier('e17', (9, 14), ((10.645, 14.14), (14.582, 14.62), (16, 14)))
        self.add_bezier('e18', (20, 12), ((22.509, 10.89), (26.064, 11.11), (28.573, 12.12)), ((30.018, 12.7), (31.4, 14), (33, 14)))
        self.add_bezier('e19', (6, 15), ((4.973, 15.67), (4.009, 16.53), (4.009, 17.96)), ((4.009, 18.06), (4, 18.17), (4, 18.28)), ((4.009, 18.35), (4.009, 18.42), (4.018, 18.5)), ((4.018, 20.46), (6.364, 22), (8, 22)))
        self.add_bezier('e20', (12, 22), ((14.036, 22), (16.336, 22.8), (18, 24)))
        self.add_bezier('e21', (40, 8), ((39.7, 8.33), (39.3, 8.67), (39, 9)))
        self.add_contour('c0', 'e12')
        self.add_contour('c1', 'e13', 'e0')
        self.add_contour('c2', 'e14', 'e1', 'e15')
        self.add_contour('c3', 'e2')
        self.add_contour('c4', 'e3', 'e16')
        self.add_contour('c5', 'e4')
        self.add_contour('c6', 'e5')
        self.add_contour('c7', 'e17', 'e6', 'e18', 'e7')
        self.add_contour('c8', 'e8', 'e19', 'e9', 'e20')
        self.add_contour('c9', 'e10')
        self.add_contour('c10', 'e21', 'e11')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c0', 'c8')
        self.relate('connect', 'c4', 'c8')
        self.relate('connect', 'c10', 'c2')
        self.relate('connect', 'c10', 'c7')
        self.relate('connect', 'c2', 'c7')
        self.relate('connect', 'c3', 'c6')
        self.relate('connect', 'c3', 'c9')
        self.relate('connect', 'c6', 'c9')
        self.relate('connect', 'c7', 'c8')
        self.relate('connect', 'c7', 'c9')
        self.relate('connect', 'c8', 'c9')
        self.relate('connect', 'c10', 'c5')
