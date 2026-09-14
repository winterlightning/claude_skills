"""Symbol signals (war), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c6618147-1dc8-4bda-b8da-afdb428106a0'
SOURCE_PATH = 'icons-json/war/symbol signals_c6618147-1dc8-4bda-b8da-afdb428106a0.json'
AUTHOR = 'json_to_solo'

class SymbolSignalsWar(Solo48):
    icon_id = 'symbol-signals-war'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'war'
    aliases = ()
    keywords = ('symbol', 'signals', 'war')

    def build(self):
        self.add_line('e0', (4, 11), (23, 33))
        self.add_line('e1', (23, 33), (23, 19))
        self.add_line('e2', (23, 19), (24, 17))
        self.add_line('e3', (24, 17), (44, 39))
        self.add_line('e4', (4, 11), (4, 38))
        self.add_line('e5', (6, 40), (42, 40))
        self.add_line('e6', (42, 40), (44, 39))
        self.add_line('e7', (6, 8), (42, 8))
        self.add_line('e8', (44, 10), (44, 39))
        self.add_bezier('e9', (4, 38), ((4.545, 39.34), (4.764, 39.44), (6, 40)))
        self.add_bezier('e10', (4, 11), ((4, 10.77), (4.018, 10.54), (4.018, 10.31)), ((4.018, 9.36), (4.673, 8.02), (5.691, 8.02)), ((5.727, 8.01), (5.955, 8.01), (6, 8)))
        self.add_bezier('e11', (42, 8), ((42.145, 8.06), (42.491, 8.04), (42.636, 8.1)), ((43.482, 8.43), (43.709, 9.23), (44, 10)))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3')
        self.add_contour('c1', 'e4', 'e9', 'e5', 'e6')
        self.add_contour('c2', 'e10', 'e7', 'e11', 'e8')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
