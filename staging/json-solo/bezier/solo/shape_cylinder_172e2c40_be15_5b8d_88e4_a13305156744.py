"""Shape cylinder (design), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '172e2c40-be15-5b8d-88e4-a13305156744'
SOURCE_PATH = 'icons-json/design/shape cylinder_172e2c40-be15-5b8d-88e4-a13305156744.json'
AUTHOR = 'json_to_solo'

class ShapeCylinderDesign(Solo48):
    icon_id = 'shape-cylinder-design'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('shape', 'cylinder', 'design')

    def build(self):
        self.add_bezier('sym-e0', (24, 44), ((23.953, 44), (24.047, 44), (24, 44)))
        self.add_bezier('sym-e1', (24, 44), ((19.46, 44), (10.48, 42.982), (8, 39)))
        self.add_bezier('sym-e2', (8, 39), ((8, 38.791), (8.09, 39.218), (8, 39)))
        self.add_line('sym-e3', (8, 39), (8, 10))
        self.add_bezier('sym-e4', (8, 10), ((8.01, 10.082), (8, 10.918), (8, 11)))
        self.add_bezier('sym-e5', (8, 11), ((8.71, 11.409), (9.29, 11.6), (10, 12)))
        self.add_bezier('sym-e6', (10, 12), ((11.67, 12.945), (14.11, 13.636), (16, 14)))
        self.add_bezier('sym-e7', (16, 14), ((18.439, 14.476), (21.048, 14), (24, 14)))
        self.add_bezier('sym-e8', (24, 14), ((26.952, 14), (29.561, 14.476), (32, 14)))
        self.add_bezier('sym-e9', (32, 14), ((33.89, 13.636), (36.33, 12.945), (38, 12)))
        self.add_bezier('sym-e10', (38, 12), ((38.71, 11.6), (39.29, 11.409), (40, 11)))
        self.add_bezier('sym-e11', (40, 11), ((40, 10.918), (39.99, 10.082), (40, 10)))
        self.add_line('sym-e12', (40, 10), (40, 39))
        self.add_bezier('sym-e13', (40, 39), ((39.91, 39.218), (40, 38.791), (40, 39)))
        self.add_bezier('sym-e14', (40, 39), ((37.52, 42.982), (28.54, 44), (24, 44)))
        self.add_bezier('sym-e15', (24, 44), ((23.953, 44), (24.047, 44), (24, 44)))
        self.add_bezier('sym-e16', (8, 10), ((8, 9.573), (8, 9.427), (8, 9)))
        self.add_bezier('sym-e17', (8, 9), ((8, 7.445), (9.67, 6.573), (11, 6)))
        self.add_bezier('sym-e18', (11, 6), ((14.43, 4.518), (18.22, 4), (22, 4)))
        self.add_bezier('sym-e19', (22, 4), ((22.48, 4), (23.52, 4), (24, 4)))
        self.add_bezier('sym-e20', (24, 4), ((24.077, 4), (23.923, 4), (24, 4)))
        self.add_bezier('sym-e21', (24, 4), ((24.077, 4), (23.923, 4), (24, 4)))
        self.add_bezier('sym-e22', (24, 4), ((24.48, 4), (25.52, 4), (26, 4)))
        self.add_bezier('sym-e23', (26, 4), ((29.78, 4), (33.57, 4.518), (37, 6)))
        self.add_bezier('sym-e24', (37, 6), ((38.33, 6.573), (40, 7.445), (40, 9)))
        self.add_bezier('sym-e25', (40, 9), ((40, 9.427), (40, 9.573), (40, 10)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', closed=True)
        self.add_contour('sym-c1', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
