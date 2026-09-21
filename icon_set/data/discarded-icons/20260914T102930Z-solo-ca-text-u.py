"""Ca (text u) (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8c402655-e593-48d7-b819-f0043a385dd2'
SOURCE_PATH = 'icons-json/symbol/ca (text u)_8c402655-e593-48d7-b819-f0043a385dd2.json'
AUTHOR = 'json_to_solo'

class CaTextU(Solo48):
    icon_id = 'ca-text-u'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('ca', 'text', 'u', 'symbol')

    def build(self):
        self.add_line('e0', (8, 9), (8, 21))
        self.add_line('e1', (40, 27), (40, 23))
        self.add_line('e2', (8, 44), (40, 44))
        self.add_arc('e3-1', (19, 8), (14, 4), radius_x=6, sweep=False)
        self.add_line('e3-2', (14, 4), (10, 5))
        self.add_line('e3-3', (10, 5), (8, 9))
        self.add_arc('e4-1', (8, 21), (11, 26), radius_x=6, sweep=False)
        self.add_arc('e4-2', (11, 26), (19, 23), radius_x=6, sweep=False)
        self.add_arc('e5-1', (40, 23), (32, 26), radius_x=6)
        self.add_arc('e5-2', (32, 26), (28, 19), radius_x=6)
        self.add_arc('e5-3', (28, 19), (34, 12), radius_x=7)
        self.add_arc('e5-4', (34, 12), (40, 17), radius_x=6)
        self.add_line('e5-5', (40, 17), (40, 23))
        self.add_contour('c0', 'e3-1', 'e3-2', 'e3-3', 'e0', 'e4-1', 'e4-2')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e5-1', 'e5-2', 'e5-3', 'e5-4', 'e5-5', closed=True)
