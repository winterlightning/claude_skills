"""Car (transportation), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'edd4874e-4e76-4ead-a51d-24426b253623'
SOURCE_PATH = 'icons-json/transportation/car_edd4874e-4e76-4ead-a51d-24426b253623.json'
AUTHOR = 'json_to_solo'

class Car(Solo48):
    icon_id = 'car'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('car', 'transportation')

    def build(self):
        self.add_line('e0', (29, 34), (19, 34))
        self.add_line('e1', (27, 8), (27, 20))
        self.add_line('e2', (12, 20), (16, 13))
        self.add_line('e3', (20, 8), (31, 8))
        self.add_line('e4', (37, 12), (39, 20))
        self.add_line('e5', (12, 20), (39, 20))
        self.add_arc('e6-top', (9, 35), (19, 35), radius_x=5)
        self.add_arc('e6-bottom', (19, 35), (9, 35), radius_x=5)
        self.add_arc('e7-top', (30, 35), (40, 35), radius_x=5)
        self.add_arc('e7-bottom', (40, 35), (30, 35), radius_x=5)
        self.add_bezier('e8', (39, 35), ((42.109, 33.72), (43.991, 32.54), (43.991, 28.59)), ((43.991, 28.37), (44, 28.15), (44, 27.93)), ((44, 27.927), (44, 27.923), (44, 27.92)), ((44, 27.703), (44, 27.497), (44, 27.28)), ((44, 23.56), (41.845, 21.59), (39, 20)))
        self.add_bezier('e9', (9, 35), ((6.845, 33.82), (5.718, 32.96), (4.636, 30.5)), ((4.345, 29.81), (4.009, 29), (4.009, 28.22)), ((4.009, 28.122), (4, 28.023), (4, 27.925)), ((4, 27.923), (4, 27.922), (4, 27.92)), ((4, 27.81), (4.009, 27.69), (4.009, 27.58)), ((4.009, 26.65), (4.373, 25.68), (4.718, 24.86)), ((6.264, 21.22), (8.5, 20), (12, 20)))
        self.add_bezier('e10', (16, 13), ((16.973, 11.13), (17.8, 8.92), (19.755, 8.1)), ((19.945, 8.02), (19.809, 8.07), (20, 8)))
        self.add_bezier('e11', (31, 8), ((31.082, 8), (31.445, 8), (31.527, 8)), ((33.7, 8), (36.245, 9.79), (37, 12)))
        self.add_contour('c0', 'e8')
        self.add_contour('c1', 'e0')
        self.add_contour('c2', 'e9')
        self.add_contour('c3', 'e1')
        self.add_contour('c4', 'e2', 'e10', 'e3', 'e11', 'e4')
        self.add_contour('c5', 'e5')
        self.add_contour('e6', 'e6-top', 'e6-bottom', closed=True)
        self.add_contour('e7', 'e7-top', 'e7-bottom', closed=True)
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c0', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c1', 'e6')
        self.relate('connect', 'c2', 'e6')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c5')
