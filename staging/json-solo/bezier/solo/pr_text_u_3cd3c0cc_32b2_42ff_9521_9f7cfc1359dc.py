"""Pr (text u) (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3cd3c0cc-32b2-42ff-9521-9f7cfc1359dc'
SOURCE_PATH = 'icons-json/symbol/Pr (text u)_3cd3c0cc-32b2-42ff-9521-9f7cfc1359dc.json'
AUTHOR = 'json_to_solo'

class PrTextUSymbol(Solo48):
    icon_id = 'pr-text-u-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('pr', 'text', 'u', 'symbol')

    def build(self):
        self.add_line('e0', (8, 16), (16, 16))
        self.add_line('e1', (16, 4), (8, 4))
        self.add_line('e2', (8, 4), (8, 27))
        self.add_line('e3', (32, 13), (32, 27))
        self.add_line('e4', (8, 44), (40, 44))
        self.add_bezier('e5', (16, 16), ((16.86, 16), (17.94, 15.464), (18.7, 15.109)), ((23.18, 13.045), (23.07, 6.918), (18.76, 4.755)), ((17.97, 4.355), (16.92, 4), (16, 4)))
        self.add_bezier('e6', (40, 13), ((40, 13), (39.99, 13.082), (39.99, 13.082)), ((39.99, 13.018), (39.72, 12.845), (39.67, 12.818)), ((38.63, 12.055), (37.26, 11.673), (35.94, 12.018)), ((33.59, 12.627), (32.62, 15.064), (32, 17)))
        self.add_contour('c0', 'e0', 'e5', 'e1', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e6')
        self.add_contour('c3', 'e4')
        self.relate('connect', 'c2', 'c1')
