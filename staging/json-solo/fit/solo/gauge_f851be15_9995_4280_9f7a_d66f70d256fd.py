"""Gauge (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
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
        self.add_arc('e6-1', (27, 32), (25, 40), radius_x=6, sweep=False)
        self.add_arc('e6-2', (25, 40), (29, 42), radius_x=5, sweep=False)
        self.add_arc('e6-3', (29, 42), (36, 33), radius_x=12, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3', 'e4', 'e6-1', 'e6-2', 'e6-3', 'e5', closed=True)
