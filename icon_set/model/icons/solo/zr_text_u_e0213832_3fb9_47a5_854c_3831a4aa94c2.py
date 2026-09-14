"""Zr (text u) (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e0213832-3fb9-47a5-854c-3831a4aa94c2'
SOURCE_PATH = 'icons-json/symbol/zr (text u)_e0213832-3fb9-47a5-854c-3831a4aa94c2.json'
AUTHOR = 'json_to_solo'

class ZrTextU(Solo48):
    icon_id = 'zr-text-u'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('zr', 'text', 'u', 'symbol')

    def build(self):
        self.add_line('e0', (8, 4), (24, 4))
        self.add_line('e1', (24, 4), (10, 27))
        self.add_line('e2', (10, 27), (24, 27))
        self.add_line('e3', (32, 13), (32, 27))
        self.add_line('e4', (8, 44), (40, 44))
        self.add_arc('e5', (40, 13), (32, 17), radius_x=5, sweep=False)
        self.add_contour('c0', 'e0', 'e1', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e5')
        self.add_contour('c3', 'e4')
        self.relate('connect', 'c2', 'c1')
