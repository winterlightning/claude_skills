"""Th (text u) (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6dd6160e-f919-4957-8eda-70be2a33d023'
SOURCE_PATH = 'icons-json/symbol/th (text u)_6dd6160e-f919-4957-8eda-70be2a33d023.json'
AUTHOR = 'json_to_solo'

class ThTextU(Solo48):
    icon_id = 'th-text-u'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('th', 'text', 'u', 'symbol')

    def build(self):
        self.add_line('e0', (8, 4), (22, 4))
        self.add_line('e1', (16, 27), (16, 4))
        self.add_line('e2', (31, 4), (31, 27))
        self.add_line('e3', (40, 19), (40, 27))
        self.add_line('e4', (8, 44), (40, 44))
        self.add_arc('e5-1', (31, 15), (37, 12), radius_x=4)
        self.add_arc('e5-2', (37, 12), (40, 17), radius_x=6)
        self.add_line('e5-3', (40, 17), (40, 19))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e5-1', 'e5-2', 'e5-3', 'e3')
        self.add_contour('c4', 'e4')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c3', 'c2')
