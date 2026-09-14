"""Dollar (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2c47b147-c2f7-4c49-8513-824a167aa784'
SOURCE_PATH = 'icons-json/symbol/dollar_2c47b147-c2f7-4c49-8513-824a167aa784.json'
AUTHOR = 'json_to_solo'

class DollarSymbol(Solo48):
    icon_id = 'dollar-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('dollar', 'symbol')

    def build(self):
        self.add_line('e0', (29, 25), (21, 24))
        self.add_line('e1', (24, 8), (24, 4))
        self.add_line('e2', (24, 44), (24, 8))
        self.add_bezier('e3', (8, 33), ((9.68, 36.927), (13.632, 39.327), (20.64, 40.182)), ((21.664, 40.3), (22.896, 40.564), (23.936, 40.555)), ((24.752, 40.555), (25.664, 40.391), (26.48, 40.309)), ((27.984, 40.155), (29.744, 40.045), (31.152, 39.673)), ((35.824, 38.427), (40, 35.409), (40, 32.364)), ((40, 32.363), (40, 32.362), (40, 32.361)), ((40, 32.298), (40, 32.244), (40, 32.182)), ((40, 32.045), (39.984, 31.909), (39.984, 31.773)), ((39.984, 28.255), (34.792, 25.655), (29, 25)))
        self.add_bezier('e4', (21, 24), ((14.84, 23.3), (8.016, 20.718), (8.016, 16.782)), ((8.016, 16.636), (8, 16.5), (8, 16.364)), ((8, 15.327), (8.8, 14.191), (9.568, 13.273)), ((12.816, 9.355), (17.2, 9.018), (24, 8)))
        self.add_bezier('e5', (24, 8), ((26.336, 8.282), (29.104, 8.173), (31.168, 8.927)), ((35.424, 10.464), (37.216, 13.245), (38, 16)))
        self.add_contour('c0', 'e3', 'e0', 'e4', 'e1')
        self.add_contour('c1', 'e2', 'e5')
