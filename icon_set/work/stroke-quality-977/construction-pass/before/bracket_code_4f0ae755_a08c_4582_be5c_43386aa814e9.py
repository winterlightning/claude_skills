"""Bracket code (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4f0ae755-a08c-4582-be5c-43386aa814e9'
SOURCE_PATH = 'pictographic-primitives/symbol/bracket code_4f0ae755-a08c-4582-be5c-43386aa814e9.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class BracketCode(Solo48):
    icon_id = 'bracket-code'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('bracket', 'code', 'symbol')

    def build(self):
        self.add_line('sym-e0', (4, 24), (6, 26))
        self.add_arc('sym-e1', (6, 26), (8, 28), radius_x=8)
        self.add_line('sym-e2', (8, 28), (9, 32))
        self.add_arc('sym-e3', (9, 32), (12, 39), radius_x=6, sweep=False)
        self.add_line('sym-e4', (12, 39), (15, 40))
        self.add_line('sym-e5', (44, 24), (42, 26))
        self.add_arc('sym-e6', (42, 26), (40, 28), radius_x=8, sweep=False)
        self.add_line('sym-e7', (40, 28), (39, 32))
        self.add_arc('sym-e8', (39, 32), (36, 39), radius_x=6)
        self.add_line('sym-e9', (36, 39), (33, 40))
        self.add_line('sym-e10', (4, 24), (6, 22))
        self.add_arc('sym-e11', (6, 22), (8, 20), radius_x=7, sweep=False)
        self.add_line('sym-e12', (8, 20), (9, 16))
        self.add_arc('sym-e13', (9, 16), (12, 9), radius_x=6)
        self.add_line('sym-e14', (12, 9), (15, 8))
        self.add_line('sym-e15', (44, 24), (42, 22))
        self.add_arc('sym-e16', (42, 22), (40, 20), radius_x=7)
        self.add_arc('sym-e17', (40, 20), (39, 16), radius_x=9)
        self.add_arc('sym-e18', (39, 16), (36, 9), radius_x=6, sweep=False)
        self.add_arc('sym-e19', (36, 9), (33, 8), radius_x=11, sweep=False)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4')
        self.add_contour('sym-c1', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9')
        self.add_contour('sym-c2', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14')
        self.add_contour('sym-c3', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c3')
