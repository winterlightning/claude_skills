"""Car (transportation), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '38792ded-1850-5f89-8b9a-dc4c3354c564'
SOURCE_PATH = 'icons-json/transportation/car_38792ded-1850-5f89-8b9a-dc4c3354c564.json'
AUTHOR = 'json_to_solo'

class Car38792ded(Solo48):
    icon_id = 'car-38792ded'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('car', 'transportation')

    def build(self):
        self.add_line('e0', (44, 30), (44, 26))
        self.add_line('e1', (43, 23), (36, 19))
        self.add_line('e2', (36, 19), (29, 10))
        self.add_line('e3', (24, 8), (16, 8))
        self.add_line('e4', (8, 12), (5, 15))
        self.add_line('e5', (4, 18), (4, 30))
        self.add_line('e6', (31, 34), (18, 34))
        self.add_line('e7', (19, 19), (23, 19))
        self.add_arc('e8-top', (31, 34), (41, 34), radius_x=5, radius_y=6)
        self.add_arc('e8-bottom', (41, 34), (31, 34), radius_x=5, radius_y=6)
        self.add_arc('e9-top', (8, 34), (18, 34), radius_x=5, radius_y=6)
        self.add_arc('e9-bottom', (18, 34), (8, 34), radius_x=5, radius_y=6)
        self.add_bezier('e10', (40, 34), ((41.364, 33.902), (42.955, 33.698), (43.7, 31.914)), ((43.8, 31.692), (44, 31.335), (44, 31.065)), ((44, 30.757), (44, 30.308), (44, 30)))
        self.add_bezier('e11', (44, 26), ((44, 25.397), (43.991, 25.243), (43.991, 24.64)), ((43.991, 23.84), (43.345, 23.529), (43, 23)))
        self.add_bezier('e12', (29, 10), ((28.055, 8.72), (26.745, 8), (25.382, 8)), ((24.927, 8), (24.464, 8), (24, 8)))
        self.add_bezier('e13', (16, 8), ((15.709, 8), (15.236, 8.012), (14.945, 8.012)), ((13.373, 8.025), (11.127, 8), (9.727, 9.046)), ((8.945, 9.735), (8.655, 11.114), (8, 12)))
        self.add_bezier('e14', (5, 15), ((4.527, 15.64), (4.245, 17.212), (4, 18)))
        self.add_bezier('e15', (4, 30), ((4, 30.086), (4, 30.326), (4, 30.412)), ((4, 31.077), (4.327, 31.717), (4.645, 32.172)), ((5.745, 33.698), (7.509, 33.926), (9, 34)))
        self.add_contour('c0', 'e10', 'e0', 'e11', 'e1', 'e2', 'e12', 'e3', 'e13', 'e4', 'e14', 'e5', 'e15')
        self.add_contour('c1', 'e6')
        self.add_contour('c2', 'e7')
        self.add_contour('e8', 'e8-top', 'e8-bottom', closed=True)
        self.add_contour('e9', 'e9-top', 'e9-bottom', closed=True)
        self.relate('connect', 'c0', 'e8')
        self.relate('connect', 'c0', 'e9')
        self.relate('connect', 'c1', 'e8')
        self.relate('connect', 'c1', 'e9')
