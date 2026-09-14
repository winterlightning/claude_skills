"""Hf (text u) (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '38b46b9e-f697-4b17-95a6-2b7297be8148'
SOURCE_PATH = 'icons-json/symbol/hf (text u)_38b46b9e-f697-4b17-95a6-2b7297be8148.json'
AUTHOR = 'json_to_solo'

class HfTextUSymbol(Solo48):
    icon_id = 'hf-text-u-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('hf', 'text', 'u', 'symbol')

    def build(self):
        self.add_line('e0', (8, 4), (8, 27))
        self.add_line('e1', (23, 15), (8, 15))
        self.add_line('e2', (23, 27), (23, 4))
        self.add_line('e3', (35, 8), (35, 27))
        self.add_line('e4', (32, 11), (40, 11))
        self.add_line('e5', (8, 44), (40, 44))
        self.add_bezier('e6', (40, 4), ((39.992, 4), (39.992, 4), (39.983, 4)), ((39.983, 4.118), (39.764, 4), (39.663, 4)), ((38.931, 4), (38.206, 4), (37.474, 4)), ((36.227, 4), (35, 6.755), (35, 8)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e6', 'e3')
        self.add_contour('c4', 'e4')
        self.add_contour('c5', 'e5')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c0')
