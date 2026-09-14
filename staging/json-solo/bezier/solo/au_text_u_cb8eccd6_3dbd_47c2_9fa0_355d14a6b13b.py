"""Au (text u) (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cb8eccd6-3dbd-47c2-9fa0-355d14a6b13b'
SOURCE_PATH = 'icons-json/symbol/au (text u)_cb8eccd6-3dbd-47c2-9fa0-355d14a6b13b.json'
AUTHOR = 'json_to_solo'

class AuTextUSymbol(Solo48):
    icon_id = 'au-text-u-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('au', 'text', 'u', 'symbol')

    def build(self):
        self.add_line('e0', (23, 27), (17, 6))
        self.add_line('e1', (14, 5), (8, 27))
        self.add_line('e2', (11, 19), (21, 19))
        self.add_line('e3', (31, 12), (31, 22))
        self.add_line('e4', (40, 12), (40, 27))
        self.add_line('e5', (8, 44), (40, 44))
        self.add_bezier('e6', (17, 6), ((16.714, 4.982), (16.48, 4.018), (15.411, 4.018)), ((15.309, 4.009), (15.2, 4.009), (15.091, 4)), ((15.079, 4), (15.067, 4), (15.056, 4)), ((14.335, 4), (14.398, 4.481), (14, 5)))
        self.add_bezier('e7', (31, 22), ((31, 26.873), (37.996, 27.664), (39.655, 23.618)), ((39.806, 23.236), (39.992, 22.736), (39.992, 22.309)), ((39.992, 22.264), (40, 22.045), (40, 22)))
        self.add_contour('c0', 'e0', 'e6', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3', 'e7')
        self.add_contour('c3', 'e4')
        self.add_contour('c4', 'e5')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c2', 'c3')
