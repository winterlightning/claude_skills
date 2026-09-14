"""Bitcoin (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cee74690-6aad-4510-80ad-577d64d63524'
SOURCE_PATH = 'icons-json/symbol/bitcoin_cee74690-6aad-4510-80ad-577d64d63524.json'
AUTHOR = 'json_to_solo'

class BitcoinSymbol(Solo48):
    icon_id = 'bitcoin-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('bitcoin', 'symbol')

    def build(self):
        self.add_line('e0', (30, 39), (14, 39))
        self.add_line('e1', (14, 39), (14, 9))
        self.add_line('e2', (29, 9), (8, 9))
        self.add_line('e3', (33, 24), (14, 24))
        self.add_line('e4', (26, 4), (26, 9))
        self.add_line('e5', (17, 4), (17, 9))
        self.add_line('e6', (8, 39), (17, 39))
        self.add_line('e7', (17, 39), (17, 44))
        self.add_line('e8', (26, 44), (26, 39))
        self.add_bezier('e9', (33, 24), ((37.062, 25.555), (39.975, 26.809), (39.975, 30.7)), ((39.988, 30.827), (39.988, 30.964), (40, 31.091)), ((40, 31.095), (40, 31.1), (40, 31.105)), ((40, 31.391), (39.975, 31.677), (39.975, 31.973)), ((39.975, 35.891), (35.034, 39), (30, 39)))
        self.add_bezier('e10', (33, 24), ((35.006, 22.7), (36.874, 21.445), (37.957, 19.582)), ((40, 14.545), (36.36, 9), (29, 9)))
        self.add_contour('c0', 'e9', 'e0', 'e1')
        self.add_contour('c1', 'e10', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('c3', 'e4')
        self.add_contour('c4', 'e5')
        self.add_contour('c5', 'e6', 'e7')
        self.add_contour('c6', 'e8')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c5')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c2', 'c0')
        self.relate('connect', 'c3', 'c1')
        self.relate('connect', 'c4', 'c1')
        self.relate('connect', 'c5', 'c0')
        self.relate('connect', 'c6', 'c0')
