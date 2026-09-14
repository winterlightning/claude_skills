"""Pr (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '55570d4b-1ccd-4b43-bac8-4449335b0c0c'
SOURCE_PATH = 'icons-json/symbol/Pr_55570d4b-1ccd-4b43-bac8-4449335b0c0c.json'
AUTHOR = 'json_to_solo'

class PrSymbol(Solo48):
    icon_id = 'pr-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('pr', 'symbol')

    def build(self):
        self.add_line('e0', (4, 25), (14, 25))
        self.add_line('e1', (14, 8), (4, 8))
        self.add_line('e2', (4, 8), (4, 40))
        self.add_line('e3', (33, 20), (33, 40))
        self.add_bezier('e4', (14, 25), ((14.545, 25), (15.191, 24.76), (15.727, 24.63)), ((22.636, 22.9), (23.564, 12.69), (17.545, 9.14)), ((16.518, 8.53), (15.173, 8), (14, 8)))
        self.add_bezier('e5', (44, 21), ((44, 21), (43.991, 20.99), (43.991, 20.99)), ((43.991, 20.78), (43.191, 20.31), (43.064, 20.22)), ((41.945, 19.48), (40.655, 19.12), (39.355, 19.27)), ((35.982, 19.65), (33.909, 22.7), (33, 26)))
        self.add_contour('c0', 'e0', 'e4', 'e1', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e5')
        self.relate('connect', 'c2', 'c1')
