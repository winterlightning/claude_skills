"""Car (transportation), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f903e1a1-941a-408a-8df4-b2eabe61a716'
SOURCE_PATH = 'icons-json/transportation/car_f903e1a1-941a-408a-8df4-b2eabe61a716.json'
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
        self.add_line('e8-1', (39, 35), (43, 33))
        self.add_line('e8-2', (43, 33), (44, 28))
        self.add_line('e8-3', (44, 28), (43, 23))
        self.add_line('e8-4', (43, 23), (39, 20))
        self.add_arc('e9-1', (9, 35), (4, 28), radius_x=9)
        self.add_arc('e9-2', (4, 28), (12, 20), radius_x=8)
        self.add_arc('e10', (16, 13), (20, 8), radius_x=6)
        self.add_arc('e11-1', (31, 8), (34, 9), radius_x=5)
        self.add_arc('e11-2', (34, 9), (37, 12), radius_x=6)
        self.add_contour('c0', 'e8-1', 'e8-2', 'e8-3', 'e8-4')
        self.add_contour('c1', 'e0')
        self.add_contour('c2', 'e9-1', 'e9-2')
        self.add_contour('c3', 'e1')
        self.add_contour('c4', 'e2', 'e10', 'e3', 'e11-1', 'e11-2', 'e4')
        self.add_contour('c5', 'e5')
        self.add_contour('e7', 'e7-top', 'e7-bottom', closed=True)
        self.add_contour('e6', 'e6-top', 'e6-bottom', closed=True)
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
