"""Zr (text u) (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e0213832-3fb9-47a5-854c-3831a4aa94c2'
SOURCE_PATH = 'icons-json/symbol/zr (text u)_e0213832-3fb9-47a5-854c-3831a4aa94c2.json'
AUTHOR = 'json_to_solo'

class ZrTextUSymbol(Solo48):
    icon_id = 'zr-text-u-symbol'
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
        self.add_bezier('e5', (40, 13), ((40, 13), (39.992, 13.082), (39.992, 13.082)), ((39.992, 13.018), (39.747, 12.845), (39.714, 12.818)), ((38.821, 12.073), (37.659, 11.736), (36.547, 11.945)), ((34.248, 12.391), (32.648, 14.8), (32, 17)))
        self.add_contour('c0', 'e0', 'e1', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e5')
        self.add_contour('c3', 'e4')
        self.relate('connect', 'c2', 'c1')
