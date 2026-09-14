"""Car (transportation), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'eaa7f06c-57de-4d21-aaa7-d89d24b33193'
SOURCE_PATH = 'icons-json/transportation/car_eaa7f06c-57de-4d21-aaa7-d89d24b33193.json'
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
        self.add_line('e7-1', (9, 35), (6, 33))
        self.add_line('e7-2', (6, 33), (4, 27))
        self.add_arc('e7-3', (4, 27), (9, 21), radius_x=7)
        self.add_arc('e8-1', (39, 21), (43, 24), radius_x=5)
        self.add_line('e8-2', (43, 24), (44, 28))
        self.add_line('e8-3', (44, 28), (43, 33))
        self.add_line('e8-4', (43, 33), (39, 35))
        self.add_arc('e9-1', (39, 35), (36, 30), radius_x=6, sweep=False)
        self.add_arc('e9-2', (36, 30), (30, 35), radius_x=5, sweep=False)
        self.add_arc('e10-1', (39, 35), (35, 40), radius_x=5)
        self.add_arc('e10-2', (35, 40), (30, 35), radius_x=5)
        self.add_arc('e11', (33, 11), (29, 8), radius_x=5, sweep=False)
        self.add_arc('e12', (19, 8), (14, 13), radius_x=5, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e7-1', 'e7-2', 'e7-3', 'e1', 'e8-1', 'e8-2', 'e8-3', 'e8-4')
        self.add_contour('c2', 'e9-1', 'e9-2')
        self.add_contour('c3', 'e10-1', 'e10-2')
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
