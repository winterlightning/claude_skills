"""Pu (text u) (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e41d9405-ab74-46da-af5a-21bfd17b16e3'
SOURCE_PATH = 'icons-json/symbol/pu (text u)_e41d9405-ab74-46da-af5a-21bfd17b16e3.json'
AUTHOR = 'json_to_solo'

class PuTextUSymbol(Solo48):
    icon_id = 'pu-text-u-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('pu', 'text', 'u', 'symbol')

    def build(self):
        self.add_line('e0', (8, 16), (15, 16))
        self.add_line('e1', (16, 4), (8, 4))
        self.add_line('e2', (8, 4), (8, 27))
        self.add_line('e3', (30, 12), (30, 22))
        self.add_line('e4', (40, 12), (40, 27))
        self.add_line('e5', (8, 44), (40, 44))
        self.add_bezier('e6', (15, 16), ((15.38, 16), (15.85, 15.664), (16.22, 15.582)), ((21.27, 14.409), (23.22, 7.409), (18.6, 4.791)), ((17.87, 4.373), (16.88, 4), (16, 4)))
        self.add_bezier('e7', (30, 22), ((30, 26.791), (37.74, 27.727), (39.59, 23.682)), ((39.78, 23.273), (39.99, 22.764), (39.99, 22.318)), ((39.99, 22.273), (40, 22.045), (40, 22)))
        self.add_contour('c0', 'e0', 'e6', 'e1', 'e2')
        self.add_contour('c1', 'e3', 'e7')
        self.add_contour('c2', 'e4')
        self.add_contour('c3', 'e5')
        self.relate('connect', 'c1', 'c2')
