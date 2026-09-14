"""Fire flame curved (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '30104018-8e47-4b2e-9d72-f1246987add3'
SOURCE_PATH = 'icons-json/symbol/fire flame curved_30104018-8e47-4b2e-9d72-f1246987add3.json'
AUTHOR = 'json_to_solo'

class FireFlameCurved(Solo48):
    icon_id = 'fire-flame-curved'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('fire', 'flame', 'curved', 'symbol')

    def build(self):
        self.add_line('e0', (18, 21), (17, 20))
        self.add_line('e1', (16, 19), (14, 17))
        self.add_line('e2', (17, 20), (16, 19))
        self.add_arc('e3-1', (14, 17), (8, 29), radius_x=16, sweep=False)
        self.add_line('e3-2', (8, 29), (9, 35))
        self.add_line('e3-3', (9, 35), (12, 39))
        self.add_arc('e3-4', (12, 39), (24, 44), radius_x=17, sweep=False)
        self.add_arc('e3-5', (24, 44), (40, 28), radius_x=16, sweep=False)
        self.add_arc('e3-6', (40, 28), (25, 4), radius_x=29, sweep=False)
        self.add_arc('e3-7', (25, 4), (18, 21), radius_x=15)
        self.add_contour('c0', 'e0', 'e2', 'e1', 'e3-1', 'e3-2', 'e3-3', 'e3-4', 'e3-5', 'e3-6', 'e3-7', closed=True)
