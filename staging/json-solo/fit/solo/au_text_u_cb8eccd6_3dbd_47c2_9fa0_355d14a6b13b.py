"""Au (text u) (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
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
        self.add_arc('e6-1', (17, 6), (15, 4), radius_x=2, sweep=False)
        self.add_arc('e6-2', (15, 4), (14, 5), radius_x=1, sweep=False)
        self.add_arc('e7-1', (31, 22), (37, 26), radius_x=4, sweep=False)
        self.add_arc('e7-2', (37, 26), (40, 22), radius_x=5, sweep=False)
        self.add_contour('c0', 'e0', 'e6-1', 'e6-2', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3', 'e7-1', 'e7-2')
        self.add_contour('c3', 'e4')
        self.add_contour('c4', 'e5')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c2', 'c3')
