"""Gauge (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f851be15-9995-4280-9f7a-d66f70d256fd'
SOURCE_PATH = 'icons-json/symbol/gauge_f851be15-9995-4280-9f7a-d66f70d256fd.json'
AUTHOR = 'json_to_solo'

class GaugeSymbol(Solo48):
    icon_id = 'gauge-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('gauge', 'symbol')

    def build(self):
        self.add_line('e0', (31, 13), (31, 6))
        self.add_line('e1', (13, 13), (17, 18))
        self.add_line('e2', (6, 32), (13, 32))
        self.add_line('e3', (42, 22), (37, 26))
        self.add_line('e4', (37, 26), (27, 32))
        self.add_line('e5', (36, 33), (42, 22))
        self.add_bezier('e6', (27, 32), ((24.259, 33.825), (23.051, 37.909), (25.473, 40.585)), ((26.217, 41.411), (27.428, 41.992), (28.557, 41.992)), ((28.614, 42), (28.67, 42), (28.726, 42)), ((28.727, 42), (28.728, 42), (28.729, 42)), ((28.835, 41.992), (28.942, 41.992), (29.048, 41.984)), ((31.904, 41.984), (33.949, 37.083), (35.013, 35.103)), ((35.405, 34.383), (35.615, 33.72), (36, 33)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3', 'e4', 'e6', 'e5', closed=True)
