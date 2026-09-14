"""Car (transportation), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e1ae9ac1-dad6-526e-975f-e2ee61a2940d'
SOURCE_PATH = 'icons-json/transportation/car_e1ae9ac1-dad6-526e-975f-e2ee61a2940d.json'
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
        self.add_line('e0', (9, 19), (15, 19))
        self.add_line('e1', (15, 19), (38, 19))
        self.add_line('e2', (44, 28), (44, 31))
        self.add_line('e3', (44, 33), (39, 33))
        self.add_line('e4', (30, 8), (23, 8))
        self.add_line('e5', (17, 34), (30, 34))
        self.add_line('e6', (28, 8), (28, 19))
        self.add_arc('e7-top', (7, 34), (17, 34), radius_x=5, radius_y=6)
        self.add_arc('e7-bottom', (17, 34), (7, 34), radius_x=5, radius_y=6)
        self.add_arc('e8-top', (30, 34), (40, 34), radius_x=5, radius_y=6)
        self.add_arc('e8-bottom', (40, 34), (30, 34), radius_x=5, radius_y=6)
        self.add_bezier('e9', (8, 34), ((7.555, 33.975), (4.718, 33.834), (4.436, 33.145)), ((4.182, 32.517), (4.009, 28.898), (4.009, 28.062)), ((4.009, 27.965), (4, 27.868), (4, 27.783)), ((4, 27.781), (4, 27.78), (4, 27.778)), ((4, 27.655), (4.009, 27.545), (4.009, 27.422)), ((4.009, 23.311), (6.418, 20.588), (9, 19)))
        self.add_bezier('e10', (38, 19), ((38.6, 19), (38.855, 18.954), (39.455, 19.077)), ((42.273, 19.643), (44, 24.443), (44, 28)))
        self.add_bezier('e11', (44, 31), ((44, 31.406), (44, 32.594), (44, 33)))
        self.add_bezier('e12', (39, 19), ((38.945, 18.102), (39.409, 17.169), (39.145, 16.32)), ((38.045, 12.8), (35.664, 9.6), (32.955, 8.468)), ((32.582, 8.308), (32.145, 8), (31.745, 8)), ((31.282, 8), (30.464, 8), (30, 8)))
        self.add_bezier('e13', (23, 8), ((22.855, 8.012), (22.8, 8.012), (22.655, 8.025)), ((18.164, 8.025), (15.845, 14.446), (14, 19)))
        self.add_bezier('e15', (30, 34), ((30.3, 32.769), (30.7, 31.231), (31, 30)))
        self.add_contour('c0', 'e9', 'e0', 'e1', 'e10', 'e2', 'e11', 'e3')
        self.add_contour('c1', 'e12', 'e4', 'e13')
        self.add_contour('c3', 'e5', 'e15')
        self.add_contour('c4', 'e6')
        self.add_contour('e8', 'e8-top', 'e8-bottom', closed=True)
        self.add_contour('e7', 'e7-top', 'e7-bottom', closed=True)
        self.relate('connect', 'c0', 'e7')
        self.relate('connect', 'c0', 'e8')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c3', 'e7')
        self.relate('connect', 'c3', 'e8')
        self.relate('connect', 'c3', 'e8')
        self.relate('connect', 'c4', 'c1')
        self.relate('connect', 'c4', 'c0')
