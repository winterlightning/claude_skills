"""Pa (text u) (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '443d8fb3-2e9d-434a-8f52-35b60151f3e1'
SOURCE_PATH = 'icons-json/symbol/pa (text u)_443d8fb3-2e9d-434a-8f52-35b60151f3e1.json'
AUTHOR = 'json_to_solo'

class PaTextUSymbol(Solo48):
    icon_id = 'pa-text-u-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('pa', 'text', 'u', 'symbol')

    def build(self):
        self.add_line('e0', (8, 16), (15, 16))
        self.add_line('e1', (15, 4), (8, 4))
        self.add_line('e2', (8, 4), (8, 27))
        self.add_line('e3', (40, 27), (40, 23))
        self.add_line('e4', (8, 44), (40, 44))
        self.add_arc('e5-1', (15, 16), (20, 10), radius_x=6, sweep=False)
        self.add_arc('e5-2', (20, 10), (15, 4), radius_x=6, sweep=False)
        self.add_arc('e6-1', (40, 23), (32, 26), radius_x=6)
        self.add_arc('e6-2', (32, 26), (29, 17), radius_x=7)
        self.add_arc('e6-3', (29, 17), (35, 12), radius_x=7)
        self.add_arc('e6-4', (35, 12), (40, 17), radius_x=5)
        self.add_line('e6-5', (40, 17), (40, 23))
        self.add_contour('c0', 'e0', 'e5-1', 'e5-2', 'e1', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4')
        self.add_contour('c3', 'e6-1', 'e6-2', 'e6-3', 'e6-4', 'e6-5', closed=True)
