"""Car (transportation), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1d48915e-d0dd-4c2f-b660-e1fc2f54ced4'
SOURCE_PATH = 'icons-json/transportation/car_1d48915e-d0dd-4c2f-b660-e1fc2f54ced4.json'
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
        self.add_arc('e10', (8, 34), (4, 30), radius_x=4)
        self.add_arc('e11', (4, 23), (9, 18), radius_x=6)
        self.add_line('e12', (13, 10), (17, 8))
        self.add_line('e13', (26, 8), (29, 9))
        self.add_line('e14', (33, 17), (34, 18))
        self.add_arc('e15', (41, 20), (44, 24), radius_x=5)
        self.add_line('e16', (44, 30), (42, 34))
        self.add_contour('c0', 'e10', 'e0', 'e11', 'e1', 'e12', 'e2', 'e13', 'e3', 'e14', 'e4', 'e15', 'e5', 'e16', 'e6')
        self.add_contour('c1', 'e7')
        self.add_contour('e9', 'e9-top', 'e9-bottom', closed=True)
        self.add_contour('e8', 'e8-top', 'e8-bottom', closed=True)
        self.relate('connect', 'c0', 'e9')
        self.relate('connect', 'c0', 'e8')
        self.relate('connect', 'c1', 'e9')
        self.relate('connect', 'c1', 'e8')
