"""Fragile break (shipping), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '92fd8d38-d5e6-50e0-8460-12389b9969ac'
SOURCE_PATH = 'icons-json/shipping/fragile break_92fd8d38-d5e6-50e0-8460-12389b9969ac.json'
AUTHOR = 'json_to_solo'

class FragileBreak(Solo48):
    icon_id = 'fragile-break'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shipping'
    aliases = ()
    keywords = ('fragile', 'break', 'shipping')

    def build(self):
        self.add_line('e0', (24, 44), (24, 30))
        self.add_line('e1', (17, 44), (33, 44))
        self.add_line('e2', (24, 4), (38, 4))
        self.add_line('e3', (38, 4), (40, 17))
        self.add_line('e4', (8, 19), (10, 4))
        self.add_line('e5', (10, 4), (19, 4))
        self.add_line('e6', (19, 4), (17, 9))
        self.add_line('e7', (17, 9), (23, 13))
        self.add_line('e8', (23, 13), (18, 16))
        self.add_line('e9-1', (40, 17), (39, 23))
        self.add_arc('e9-2', (39, 23), (28, 30), radius_x=15)
        self.add_arc('e9-3', (28, 30), (8, 19), radius_x=16)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e3', 'e9-1', 'e9-2', 'e9-3', 'e4', 'e5', 'e6', 'e7', 'e8')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
