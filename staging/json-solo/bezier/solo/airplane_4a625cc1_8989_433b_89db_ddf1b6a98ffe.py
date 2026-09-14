"""Airplane (other), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4a625cc1-8989-433b-89db-ddf1b6a98ffe'
SOURCE_PATH = 'icons-json/other/airplane_4a625cc1-8989-433b-89db-ddf1b6a98ffe.json'
AUTHOR = 'json_to_solo'

class Airplane4a625cc1(Solo48):
    icon_id = 'airplane-4a625cc1'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'other'
    aliases = ()
    keywords = ('airplane', 'other')

    def build(self):
        self.add_line('e0', (4, 28), (11, 39))
        self.add_line('e1', (18, 39), (41, 20))
        self.add_line('e2', (29, 15), (17, 8))
        self.add_line('e3', (16, 8), (12, 11))
        self.add_line('e4', (12, 11), (20, 23))
        self.add_line('e5', (20, 23), (14, 28))
        self.add_line('e6', (14, 28), (8, 25))
        self.add_line('e7', (8, 25), (4, 28))
        self.add_bezier('e8', (11, 39), ((11.536, 39.756), (12.655, 39.971), (13.382, 39.971)), ((13.564, 39.985), (13.745, 39.985), (13.927, 40)), ((13.946, 40), (13.965, 40), (13.984, 40)), ((15.192, 40), (16.935, 39.859), (18, 39)))
        self.add_bezier('e9', (41, 20), ((42.333, 18.926), (44, 16.076), (44, 13.546)), ((44, 13.506), (44, 13.465), (44, 13.425)), ((44, 9.76), (41.418, 8), (39.445, 8)), ((39.282, 8), (39.127, 8), (38.964, 8)), ((35.918, 8), (31.845, 12.833), (29, 15)))
        self.add_bezier('e10', (17, 8), ((16.7, 8), (16.3, 8), (16, 8)))
        self.add_contour('c0', 'e0', 'e8', 'e1', 'e9', 'e2', 'e10', 'e3', 'e4', 'e5', 'e6', 'e7', closed=True)
