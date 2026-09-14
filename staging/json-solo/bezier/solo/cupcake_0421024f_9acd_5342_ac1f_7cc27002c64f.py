"""Cupcake (food), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0421024f-9acd-5342-ac1f-7cc27002c64f'
SOURCE_PATH = 'icons-json/food/cupcake_0421024f-9acd-5342-ac1f-7cc27002c64f.json'
AUTHOR = 'json_to_solo'

class CupcakeFood(Solo48):
    icon_id = 'cupcake-food'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('cupcake', 'food')

    def build(self):
        self.add_line('e0', (24, 44), (24, 32))
        self.add_line('e1', (36, 31), (34, 41))
        self.add_line('e2', (30, 44), (17, 44))
        self.add_line('e3', (14, 41), (12, 31))
        self.add_arc('e4-top', (18, 15), (30, 15), radius_x=6, radius_y=5)
        self.add_arc('e4-bottom', (30, 15), (18, 15), radius_x=6, radius_y=5)
        self.add_bezier('e5', (29, 4), ((28.86, 4), (28.71, 4.009), (28.57, 4.009)), ((26.58, 4.009), (24.86, 5.745), (24.34, 7.345)), ((24.11, 8.027), (24.08, 8.3), (24, 9)))
        self.add_bezier('e6', (29, 18), ((32.93, 19.5), (36.68, 20.291), (39.02, 23.773)), ((39.48, 24.455), (39.99, 25.3), (39.99, 26.118)), ((39.99, 26.191), (40, 26.264), (40, 26.336)), ((40, 26.337), (40, 26.339), (40, 26.34)), ((40, 26.411), (40, 26.483), (40, 26.545)), ((40, 28.682), (37.9, 30.127), (36, 31)))
        self.add_bezier('e7', (36, 31), ((34.4, 31.364), (32.89, 31.864), (31.32, 31.255)), ((30.74, 31.027), (30.2, 30.709), (29.76, 30.3)), ((29.58, 30.145), (29.1, 29.645), (29.07, 29.655)), ((28.87, 29.7), (28.04, 30.827), (27.69, 31.1)), ((26.61, 31.945), (25.38, 32.127), (24, 32.182)), ((22.8, 32.227), (21.55, 31.727), (20.66, 31.018)), ((20.34, 30.764), (19.5, 29.755), (19.35, 29.727)), ((19.12, 29.909), (18.9, 30.091), (18.67, 30.264)), ((18.14, 30.682), (17.57, 31.027), (16.94, 31.282)), ((15.22, 31.973), (13.75, 31.445), (12, 31)))
        self.add_bezier('e8', (34, 41), ((33.7, 42.509), (33.19, 43.991), (31.28, 43.991)), ((31.04, 43.991), (30.8, 44), (30.55, 44)), ((30.37, 44), (30.18, 44), (30, 44)))
        self.add_bezier('e9', (17, 44), ((16.56, 44), (16.11, 43.991), (15.67, 43.991)), ((14.14, 43.991), (14.19, 41.964), (14, 41)))
        self.add_bezier('e10', (12, 31), ((9.96, 29.982), (8.02, 28.291), (8.02, 26)), ((8.01, 25.866), (8, 25.732), (8, 25.597)), ((8, 25.595), (8, 25.593), (8, 25.591)), ((8.01, 25.455), (8.01, 25.327), (8.02, 25.191)), ((8.02, 24.309), (8.43, 23.373), (8.81, 22.573)), ((10.56, 18.964), (14.02, 17.173), (18, 16)))
        self.add_contour('c0', 'e5')
        self.add_contour('c1', 'e6')
        self.add_contour('c2', 'e0')
        self.add_contour('c3', 'e7')
        self.add_contour('c4', 'e1', 'e8', 'e2', 'e9', 'e3')
        self.add_contour('c5', 'e10')
        self.add_contour('e4', 'e4-top', 'e4-bottom', closed=True)
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c0', 'e4')
        self.relate('connect', 'c1', 'e4')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c5', 'e4')
