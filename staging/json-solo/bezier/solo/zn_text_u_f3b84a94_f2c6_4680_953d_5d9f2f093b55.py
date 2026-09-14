"""Zn (text u) (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f3b84a94-f2c6-4680-953d-5d9f2f093b55'
SOURCE_PATH = 'icons-json/symbol/zn (text u)_f3b84a94-f2c6-4680-953d-5d9f2f093b55.json'
AUTHOR = 'json_to_solo'

class ZnTextUSymbol(Solo48):
    icon_id = 'zn-text-u-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('zn', 'text', 'u', 'symbol')

    def build(self):
        self.add_line('e0', (8, 4), (23, 4))
        self.add_line('e1', (23, 4), (10, 27))
        self.add_line('e2', (10, 27), (23, 27))
        self.add_line('e3', (32, 12), (32, 27))
        self.add_line('e4', (40, 17), (40, 27))
        self.add_line('e5', (8, 44), (40, 44))
        self.add_bezier('e6', (32, 16), ((32.505, 14.573), (32.808, 13.127), (34.223, 12.573)), ((36.707, 11.591), (39.983, 13.218), (39.983, 16.355)), ((39.983, 16.482), (40, 16.873), (40, 17)))
        self.add_contour('c0', 'e0', 'e1', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e6', 'e4')
        self.add_contour('c3', 'e5')
        self.relate('connect', 'c2', 'c1')
