"""Pen (design), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '89b07141-ab83-413d-a1df-ba05b5cce4d7'
SOURCE_PATH = 'pictographic-primitives/design/pen_89b07141-ab83-413d-a1df-ba05b5cce4d7.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class Pen89b07141(Solo48):
    icon_id = 'pen-89b07141'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('pen', 'design')

    def build(self):
        self.add_arc('sym-e0', (40, 8), (41, 9), radius_x=6)
        self.add_arc('sym-e1', (41, 9), (42, 11), radius_x=6)
        self.add_line('sym-e2', (42, 11), (42, 12))
        self.add_arc('sym-e3', (42, 12), (40, 16), radius_x=5)
        self.add_line('sym-e4', (40, 16), (18, 37))
        self.add_arc('sym-e5', (18, 37), (15, 39), radius_x=11, sweep=False)
        self.add_line('sym-e6', (15, 39), (6, 42))
        self.add_line('sym-e7', (6, 42), (9, 33))
        self.add_arc('sym-e8', (9, 33), (11, 30), radius_x=11, sweep=False)
        self.add_line('sym-e9', (11, 30), (32, 8))
        self.add_arc('sym-e10', (32, 8), (36, 6), radius_x=5)
        self.add_line('sym-e11', (36, 6), (37, 6))
        self.add_arc('sym-e12', (37, 6), (39, 7), radius_x=6)
        self.add_arc('sym-e13', (39, 7), (40, 8), radius_x=6)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', closed=True)
