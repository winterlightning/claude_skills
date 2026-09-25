"""Symbol mountain infantry (war), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '56fac8f8-8d3d-40b1-a35c-415b751a3a8b'
SOURCE_PATH = 'pictographic-primitives/war/symbol mountain infantry_56fac8f8-8d3d-40b1-a35c-415b751a3a8b.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class SymbolMountainInfantry(Solo48):
    icon_id = 'symbol-mountain-infantry'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'war'
    categories = ('war', 'primitives')
    aliases = ()
    keywords = ('symbol', 'mountain', 'infantry', 'war')

    def build(self):
        self.add_line('e0', (19, 21), (17, 18))
        self.add_line('e1', (17, 18), (4, 39))
        self.add_line('e2', (5, 40), (30, 40))
        self.add_line('e3', (19, 21), (30, 40))
        self.add_line('e4', (19, 21), (27, 9))
        self.add_line('e5', (28, 9), (43, 35))
        self.add_line('e6', (42, 40), (30, 40))
        self.add_arc('e7', (4, 39), (5, 40), radius_x=2, sweep=False)
        self.add_arc('e8-1', (27, 9), (27, 8), radius_x=1)
        self.add_line('e8-2', (27, 8), (28, 9))
        self.add_line('e9-1', (43, 35), (44, 37))
        self.add_line('e9-2', (44, 37), (42, 40))
        self.add_contour('c0', 'e0', 'e1', 'e7', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4', 'e8-1', 'e8-2', 'e5', 'e9-1', 'e9-2', 'e6')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
