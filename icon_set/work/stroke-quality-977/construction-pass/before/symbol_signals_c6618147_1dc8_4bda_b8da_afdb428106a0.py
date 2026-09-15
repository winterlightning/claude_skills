"""Symbol signals (war), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c6618147-1dc8-4bda-b8da-afdb428106a0'
SOURCE_PATH = 'pictographic-primitives/war/symbol signals_c6618147-1dc8-4bda-b8da-afdb428106a0.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class SymbolSignals(Solo48):
    icon_id = 'symbol-signals'
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
        self.add_arc('e9', (4, 38), (6, 40), radius_x=3, sweep=False)
        self.add_arc('e10-1', (4, 11), (4, 10), radius_x=9, sweep=False)
        self.add_arc('e10-2', (4, 10), (6, 8), radius_x=2)
        self.add_arc('e11', (42, 8), (44, 10), radius_x=2)
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3')
        self.add_contour('c1', 'e4', 'e9', 'e5', 'e6')
        self.add_contour('c2', 'e10-1', 'e10-2', 'e7', 'e11', 'e8')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
