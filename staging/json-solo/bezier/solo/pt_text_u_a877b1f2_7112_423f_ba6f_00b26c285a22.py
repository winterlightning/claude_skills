"""Pt (text u) (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a877b1f2-7112-423f-ba6f-00b26c285a22'
SOURCE_PATH = 'icons-json/symbol/pt (text u)_a877b1f2-7112-423f-ba6f-00b26c285a22.json'
AUTHOR = 'json_to_solo'

class PtTextUSymbol(Solo48):
    icon_id = 'pt-text-u-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('pt', 'text', 'u', 'symbol')

    def build(self):
        self.add_line('e0', (8, 16), (15, 16))
        self.add_line('e1', (15, 4), (8, 4))
        self.add_line('e2', (8, 4), (8, 27))
        self.add_line('e3', (34, 4), (34, 20))
        self.add_line('e4', (30, 10), (38, 10))
        self.add_line('e5', (8, 44), (40, 44))
        self.add_bezier('e6', (15, 16), ((15.45, 16), (16.02, 15.627), (16.45, 15.518)), ((21.59, 14.191), (21.96, 7.145), (17.65, 4.791)), ((16.89, 4.373), (15.89, 4), (15, 4)))
        self.add_bezier('e7', (34, 20), ((34, 22.191), (34.55, 25.791), (37.21, 26.609)), ((38.15, 26.9), (39.04, 27.091), (40, 27)))
        self.add_contour('c0', 'e0', 'e6', 'e1', 'e2')
        self.add_contour('c1', 'e3', 'e7')
        self.add_contour('c2', 'e4')
        self.add_contour('c3', 'e5')
