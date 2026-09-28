"""Independent 32px profile of angry-face-symbol.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'f4917663-09f9-4afa-aaa6-0b324d7fdec1'
SOURCE_PATH = 'pictographic-primitives/symbol/angry face_f4917663-09f9-4afa-aaa6-0b324d7fdec1.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('f4917663-09f9-4afa-aaa6-0b324d7fdec1', 'pictographic-primitives/symbol/angry face_f4917663-09f9-4afa-aaa6-0b324d7fdec1.svg'),)
PROFILE_SOURCE_KEYS = ('solo/angry-face-symbol',)
SOLO_SOURCE_ICON_IDS = ('angry-face-symbol',)
REFERENCE_EXPORT_SHA256 = '9e3dbd96ce152f1b2ab6b28536cfcf4398f0ef44d9628fd767a3619bb1580ed1'

class Drawing(Sub32):
    icon_id = 'angry-face-symbol-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 2), (11, 7))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (30, 2), (21, 7))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (4, 11), (7, 13))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (28, 11), (25, 13))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_bezier('p5-r1-1', (4, 30), ((6, 23), (7, 18), (16, 18)))
        self.add_bezier('p5-r1-2', (16, 18), ((25, 18), (26, 23), (28, 30)))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', closed=False)
