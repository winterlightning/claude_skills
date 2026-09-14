"""Car (transportation), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4ecb7b0f-c4d1-5669-81fe-5c2d48418656'
SOURCE_PATH = 'icons-json/transportation/car_4ecb7b0f-c4d1-5669-81fe-5c2d48418656.json'
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
        self.add_line('e0', (30, 34), (18, 34))
        self.add_line('e1', (20, 8), (20, 19))
        self.add_line('e2', (36, 19), (6, 19))
        self.add_line('e3', (6, 19), (11, 10))
        self.add_line('e4', (16, 8), (24, 8))
        self.add_line('e5', (29, 10), (36, 19))
        self.add_arc('e6-top', (30, 34), (40, 34), radius_x=5, radius_y=6)
        self.add_arc('e6-bottom', (40, 34), (30, 34), radius_x=5, radius_y=6)
        self.add_arc('e7-top', (8, 34), (18, 34), radius_x=5, radius_y=6)
        self.add_arc('e7-bottom', (18, 34), (8, 34), radius_x=5, radius_y=6)
        self.add_bezier('e8', (39, 34), ((40.991, 33.877), (43.982, 33.711), (43.982, 30.043)), ((43.982, 29.686), (44, 29.342), (44, 28.985)), ((44, 28.973), (44, 28.962), (44, 28.951)), ((44, 28.248), (43.991, 27.546), (43.991, 26.831)), ((43.991, 22.708), (41.773, 19.778), (38.836, 19.225)), ((37.855, 19.04), (36.991, 19.025), (36, 19)))
        self.add_bezier('e9', (9, 34), ((8.264, 33.963), (6.791, 33.994), (6.091, 33.637)), ((4, 32.554), (4.018, 29.378), (4.018, 26.769)), ((4.018, 26.437), (4, 26.117), (4, 25.785)), ((4, 25.378), (4.018, 24.972), (4.018, 24.554)), ((4.018, 23.975), (4.018, 23.397), (4.018, 22.831)), ((4.018, 22.634), (4, 22.449), (4, 22.252)), ((4, 22.248), (4, 22.243), (4, 22.238)), ((4, 21.948), (4, 21.657), (4, 21.366)), ((4, 20.542), (4.691, 19.615), (5, 19)))
        self.add_bezier('e10', (11, 10), ((11.964, 8.474), (13.891, 8.012), (15.373, 8.012)), ((15.527, 8.012), (15.855, 8), (16, 8)))
        self.add_bezier('e11', (24, 8), ((24.473, 8), (24.936, 8), (25.409, 8)), ((26.745, 8), (28.064, 8.732), (29, 10)))
        self.add_contour('c0', 'e8')
        self.add_contour('c1', 'e0')
        self.add_contour('c2', 'e9')
        self.add_contour('c3', 'e1')
        self.add_contour('c4', 'e2', 'e3', 'e10', 'e4', 'e11', 'e5', closed=True)
        self.add_contour('e6', 'e6-top', 'e6-bottom', closed=True)
        self.add_contour('e7', 'e7-top', 'e7-bottom', closed=True)
        self.relate('connect', 'c0', 'e6')
        self.relate('connect', 'c1', 'e6')
        self.relate('connect', 'c1', 'e7')
        self.relate('connect', 'c2', 'e7')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c4')
