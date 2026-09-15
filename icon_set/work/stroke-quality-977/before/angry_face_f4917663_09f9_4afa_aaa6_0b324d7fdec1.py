"""Angry face (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f4917663-09f9-4afa-aaa6-0b324d7fdec1'
SOURCE_PATH = 'pictographic-primitives/symbol/angry face_f4917663-09f9-4afa-aaa6-0b324d7fdec1.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class AngryFaceSymbol(Solo48):
    icon_id = 'angry-face-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('angry', 'face', 'symbol')

    def build(self):
        self.add_line('sym-e0', (30, 13), (42, 6))
        self.add_line('sym-e1', (36, 20), (39, 18))
        self.add_line('sym-e2', (39, 18), (36, 20))
        self.add_line('sym-e3', (39, 18), (39, 18))
        self.add_arc('sym-e4', (24, 26), (37, 33), radius_x=16)
        self.add_line('sym-e5', (37, 33), (40, 42))
        self.add_line('sym-e6', (18, 13), (6, 6))
        self.add_line('sym-e7', (12, 20), (9, 18))
        self.add_line('sym-e8', (9, 18), (12, 20))
        self.add_line('sym-e9', (9, 18), (9, 18))
        self.add_arc('sym-e10', (24, 26), (11, 33), radius_x=16, sweep=False)
        self.add_line('sym-e11', (11, 33), (8, 42))
        self.add_contour('sym-c0', 'sym-e0')
        self.add_contour('sym-c1', 'sym-e1', 'sym-e2', closed=True)
        self.add_contour('sym-c2', 'sym-e3', closed=True)
        self.add_contour('sym-c3', 'sym-e4', 'sym-e5')
        self.add_contour('sym-c4', 'sym-e6')
        self.add_contour('sym-c5', 'sym-e7', 'sym-e8', closed=True)
        self.add_contour('sym-c6', 'sym-e9', closed=True)
        self.add_contour('sym-c7', 'sym-e10', 'sym-e11')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c3', 'sym-c7')
        self.relate('connect', 'sym-c5', 'sym-c6')
        self.relate('connect', 'sym-c5', 'sym-c6')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c5', 'sym-c6')
        self.relate('connect', 'sym-c1', 'sym-c2')
