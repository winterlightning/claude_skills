"""Cf (text u) (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f3cd7ed4-5031-4ad9-81d5-6b22299bc142'
SOURCE_PATH = 'icons-json/symbol/cf (text u)_f3cd7ed4-5031-4ad9-81d5-6b22299bc142.json'
AUTHOR = 'json_to_solo'

class CfTextUSymbol(Solo48):
    icon_id = 'cf-text-u-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('cf', 'text', 'u', 'symbol')

    def build(self):
        self.add_line('e0', (8, 9), (8, 21))
        self.add_line('e1', (34, 8), (34, 27))
        self.add_line('e2', (31, 11), (40, 11))
        self.add_line('e3', (8, 44), (40, 44))
        self.add_arc('e4-1', (21, 8), (15, 4), radius_x=7, sweep=False)
        self.add_line('e4-2', (15, 4), (11, 5))
        self.add_arc('e4-3', (11, 5), (8, 9), radius_x=5, sweep=False)
        self.add_arc('e5', (8, 21), (21, 23), radius_x=7, sweep=False)
        self.add_line('e6-1', (40, 4), (37, 4))
        self.add_arc('e6-2', (37, 4), (34, 8), radius_x=4, sweep=False)
        self.add_contour('c0', 'e4-1', 'e4-2', 'e4-3', 'e0', 'e5')
        self.add_contour('c1', 'e6-1', 'e6-2', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
