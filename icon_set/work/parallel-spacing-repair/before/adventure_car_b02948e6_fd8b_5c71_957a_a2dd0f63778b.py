"""Adventure car (transportation), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b02948e6-fd8b-5c71-957a-a2dd0f63778b'
SOURCE_PATH = 'icons-json/transportation/adventure car_b02948e6-fd8b-5c71-957a-a2dd0f63778b.json'
AUTHOR = 'json_to_solo'

class AdventureCar(Solo48):
    icon_id = 'adventure-car'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('adventure', 'car', 'transportation')

    def build(self):
        self.add_line('e0', (32, 23), (40, 24))
        self.add_line('e1', (44, 28), (44, 32))
        self.add_line('e2', (32, 23), (30, 16))
        self.add_line('e3', (27, 16), (16, 16))
        self.add_line('e4', (12, 18), (6, 23))
        self.add_line('e5', (32, 23), (21, 23))
        self.add_line('e6', (21, 23), (21, 16))
        self.add_line('e7', (10, 33), (4, 33))
        self.add_line('e8', (29, 33), (21, 33))
        self.add_line('e9', (6, 33), (6, 8))
        self.add_arc('e10-top', (29, 34), (39, 34), radius_x=5, radius_y=6)
        self.add_arc('e10-bottom', (39, 34), (29, 34), radius_x=5, radius_y=6)
        self.add_arc('e11-top', (11, 34), (21, 34), radius_x=5, radius_y=6)
        self.add_arc('e11-bottom', (21, 34), (11, 34), radius_x=5, radius_y=6)
        self.add_arc('e12-1', (40, 24), (44, 25), radius_x=4)
        self.add_line('e12-2', (44, 25), (44, 28))
        self.add_arc('e13-1', (44, 32), (43, 33), radius_x=1)
        self.add_line('e13-2', (43, 33), (39, 33))
        self.add_line('e14', (30, 16), (27, 16))
        self.add_arc('e15', (16, 16), (12, 18), radius_x=9, sweep=False)
        self.add_contour('c0', 'e0', 'e12-1', 'e12-2', 'e1', 'e13-1', 'e13-2')
        self.add_contour('c1', 'e2', 'e14', 'e3', 'e15', 'e4')
        self.add_contour('c2', 'e5', 'e6')
        self.add_contour('c3', 'e7')
        self.add_contour('c4', 'e8')
        self.add_contour('c5', 'e9')
        self.add_contour('e10', 'e10-top', 'e10-bottom', closed=True)
        self.add_contour('e11', 'e11-top', 'e11-bottom', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'e10')
        self.relate('connect', 'c1', 'c5')
        self.relate('connect', 'c2', 'c1')
        self.relate('connect', 'c3', 'e11')
        self.relate('connect', 'c4', 'e10')
        self.relate('connect', 'c4', 'e11')
        self.relate('connect', 'c5', 'c3')
