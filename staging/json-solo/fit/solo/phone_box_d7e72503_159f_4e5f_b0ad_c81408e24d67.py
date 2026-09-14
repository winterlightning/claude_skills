"""Phone box (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd7e72503-159f-4e5f-b0ad-c81408e24d67'
SOURCE_PATH = 'icons-json/symbol/phone box_d7e72503-159f-4e5f-b0ad-c81408e24d67.json'
AUTHOR = 'json_to_solo'

class PhoneBoxD7e72503(Solo48):
    icon_id = 'phone-box-d7e72503'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('phone', 'box', 'symbol')

    def build(self):
        self.add_line('e0', (36, 15), (36, 44))
        self.add_line('e1', (36, 29), (12, 29))
        self.add_line('e2', (40, 44), (8, 44))
        self.add_line('e3', (12, 44), (12, 13))
        self.add_line('e4', (40, 13), (8, 13))
        self.add_arc('e5-1', (12, 13), (13, 10), radius_x=4)
        self.add_arc('e5-2', (13, 10), (17, 6), radius_x=10)
        self.add_arc('e5-3', (17, 6), (24, 4), radius_x=14)
        self.add_line('e5-4', (24, 4), (29, 5))
        self.add_arc('e5-5', (29, 5), (33, 7), radius_x=14)
        self.add_arc('e5-6', (33, 7), (36, 15), radius_x=9)
        self.add_contour('c0', 'e5-1', 'e5-2', 'e5-3', 'e5-4', 'e5-5', 'e5-6', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c5', 'e4')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c0', 'c5')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c3', 'c2')
