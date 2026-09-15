"""Hamburger (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8dc1040e-1d03-4e50-a902-d55864c7103f'
SOURCE_PATH = 'pictographic-primitives/symbol/hamburger_8dc1040e-1d03-4e50-a902-d55864c7103f.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class HamburgerSymbol(Solo48):
    icon_id = 'hamburger-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('hamburger', 'symbol')

    def build(self):
        self.add_line('e0', (30, 30), (6, 30))
        self.add_line('e1', (42, 21), (6, 21))
        self.add_line('e2', (16, 8), (30, 8))
        self.add_arc('e3', (42, 30), (30, 30), radius_x=77)
        self.add_arc('e4-1', (42, 30), (40, 37), radius_x=9)
        self.add_arc('e4-2', (40, 37), (33, 40), radius_x=10)
        self.add_line('e4-3', (33, 40), (15, 40))
        self.add_line('e4-4', (15, 40), (9, 38))
        self.add_arc('e4-5', (9, 38), (6, 30), radius_x=10)
        self.add_arc('e5-1', (42, 30), (44, 26), radius_x=5, sweep=False)
        self.add_line('e5-2', (44, 26), (42, 21))
        self.add_line('e6-1', (6, 30), (4, 26))
        self.add_line('e6-2', (4, 26), (6, 21))
        self.add_arc('e7', (6, 21), (16, 8), radius_x=12)
        self.add_line('e8-1', (30, 8), (37, 10))
        self.add_arc('e8-2', (37, 10), (40, 13), radius_x=12)
        self.add_arc('e8-3', (40, 13), (42, 21), radius_x=12)
        self.add_contour('c0', 'e3', 'e0')
        self.add_contour('c1', 'e4-1', 'e4-2', 'e4-3', 'e4-4', 'e4-5')
        self.add_contour('c2', 'e5-1', 'e5-2', 'e1')
        self.add_contour('c3', 'e6-1', 'e6-2')
        self.add_contour('c4', 'e7', 'e2', 'e8-1', 'e8-2', 'e8-3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c3', 'c4')
