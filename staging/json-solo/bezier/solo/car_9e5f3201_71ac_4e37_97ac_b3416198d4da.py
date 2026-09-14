"""Car (transportation), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9e5f3201-71ac-4e37-97ac-b3416198d4da'
SOURCE_PATH = 'icons-json/transportation/car_9e5f3201-71ac-4e37-97ac-b3416198d4da.json'
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
        self.add_line('e0', (19, 35), (30, 35))
        self.add_line('e1', (9, 21), (39, 21))
        self.add_line('e2', (38, 21), (33, 11))
        self.add_line('e3', (29, 8), (19, 8))
        self.add_line('e4', (14, 13), (11, 21))
        self.add_line('e5', (11, 21), (14, 13))
        self.add_arc('e6-top', (9, 35), (19, 35), radius_x=5)
        self.add_arc('e6-bottom', (19, 35), (9, 35), radius_x=5)
        self.add_bezier('e7', (9, 35), ((8.318, 34.75), (8.082, 34.51), (7.4, 34.26)), ((7.1, 34.15), (6.782, 33.82), (6.527, 33.6)), ((4.891, 32.21), (4.009, 30.04), (4.009, 27.77)), ((4.009, 27.681), (4, 27.583), (4, 27.494)), ((4, 27.493), (4, 27.491), (4, 27.49)), ((4, 27.43), (4.009, 27.37), (4.009, 27.31)), ((4.009, 23.97), (5.891, 21), (9, 21)))
        self.add_bezier('e8', (39, 21), ((41.918, 21), (43.991, 24.08), (43.991, 27.19)), ((43.991, 27.436), (44, 27.682), (44, 27.928)), ((44, 27.932), (44, 27.936), (44, 27.94)), ((44, 28.27), (43.991, 28.61), (43.991, 28.95)), ((43.991, 32.61), (41.9, 33.92), (39, 35)))
        self.add_bezier('e9', (39, 35), ((38.418, 32.26), (37.009, 29.18), (34.055, 29.84)), ((33.191, 30.03), (32.409, 30.44), (31.818, 31.17)), ((30.927, 32.28), (30.309, 33.58), (30, 35)))
        self.add_bezier('e10', (39, 35), ((38.582, 37.46), (37.845, 39.98), (35.236, 39.98)), ((35.102, 39.99), (34.968, 40), (34.825, 40)), ((34.823, 40), (34.82, 40), (34.818, 40)), ((34.755, 39.99), (34.682, 39.99), (34.609, 39.98)), ((31.836, 39.98), (30.591, 37.51), (30, 35)))
        self.add_bezier('e11', (33, 11), ((32.3, 9.46), (31.055, 8.01), (29.382, 8.01)), ((29.245, 8.01), (29.109, 8), (28.973, 8)), ((28.827, 8), (29.145, 8), (29, 8)))
        self.add_bezier('e12', (19, 8), ((18.855, 8), (19.173, 8.01), (19.036, 8.01)), ((17.236, 8.01), (15.327, 9.78), (14.491, 11.42)), ((14.236, 11.93), (14.182, 12.47), (14, 13)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e7', 'e1', 'e8')
        self.add_contour('c2', 'e9')
        self.add_contour('c3', 'e10')
        self.add_contour('c4', 'e2', 'e11', 'e3', 'e12', 'e4', 'e5')
        self.add_contour('e6', 'e6-top', 'e6-bottom', closed=True)
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c0', 'e6')
        self.relate('connect', 'c1', 'e6')
        self.relate('connect', 'c4', 'c1')
        self.relate('connect', 'c4', 'c1')
