"""Car (transportation), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1d48915e-d0dd-4c2f-b660-e1fc2f54ced4'
SOURCE_PATH = 'icons-json/transportation/car_1d48915e-d0dd-4c2f-b660-e1fc2f54ced4.json'
AUTHOR = 'json_to_solo'

class Car1d48915e(Solo48):
    icon_id = 'car-1d48915e'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('car', 'transportation')

    def build(self):
        self.add_line('e0', (4, 30), (4, 23))
        self.add_line('e1', (9, 18), (13, 10))
        self.add_line('e2', (17, 8), (26, 8))
        self.add_line('e3', (29, 9), (33, 17))
        self.add_line('e4', (34, 18), (41, 20))
        self.add_line('e5', (44, 24), (44, 30))
        self.add_line('e6', (42, 34), (39, 34))
        self.add_line('e7', (17, 34), (30, 34))
        self.add_arc('e8-top', (30, 34), (40, 34), radius_x=5, radius_y=6)
        self.add_arc('e8-bottom', (40, 34), (30, 34), radius_x=5, radius_y=6)
        self.add_arc('e9-top', (7, 34), (17, 34), radius_x=5, radius_y=6)
        self.add_arc('e9-bottom', (17, 34), (7, 34), radius_x=5, radius_y=6)
        self.add_bezier('e10', (8, 34), ((6.482, 33.778), (4.764, 33.095), (4.127, 30.966)), ((4.055, 30.708), (4.064, 30.258), (4, 30)))
        self.add_bezier('e11', (4, 23), ((4.064, 22.742), (4.045, 22.24), (4.109, 21.994)), ((4.918, 19.052), (7.064, 19.2), (8.882, 18.326)), ((9.109, 18.215), (8.791, 18.135), (9, 18)))
        self.add_bezier('e12', (13, 10), ((13.6, 8.794), (15.927, 8), (17, 8)))
        self.add_bezier('e13', (26, 8), ((26.173, 8), (26.173, 8.025), (26.345, 8.025)), ((27.164, 8.025), (28.327, 8.471), (29, 9)))
        self.add_bezier('e14', (33, 17), ((34.036, 18.686), (32.909, 16.523), (34, 18)))
        self.add_bezier('e15', (41, 20), ((42.036, 20.345), (43.491, 21.846), (43.891, 23.225)), ((43.964, 23.471), (43.936, 23.742), (44, 24)))
        self.add_bezier('e16', (44, 30), ((44, 30.209), (44, 30.56), (44, 30.769)), ((44, 32.32), (42.845, 33.286), (42, 34)))
        self.add_contour('c0', 'e10', 'e0', 'e11', 'e1', 'e12', 'e2', 'e13', 'e3', 'e14', 'e4', 'e15', 'e5', 'e16', 'e6')
        self.add_contour('c1', 'e7')
        self.add_contour('e8', 'e8-top', 'e8-bottom', closed=True)
        self.add_contour('e9', 'e9-top', 'e9-bottom', closed=True)
        self.relate('connect', 'c0', 'e9')
        self.relate('connect', 'c0', 'e8')
        self.relate('connect', 'c1', 'e9')
        self.relate('connect', 'c1', 'e8')
