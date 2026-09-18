"""Independent 32px profile of phone-with-down-arrow.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '14b5fcaa-27a4-4bd9-8940-7690a86b2fe1'
SOURCE_PATH = 'pictographic-primitives/symbol/phone with down arrow_14b5fcaa-27a4-4bd9-8940-7690a86b2fe1.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('14b5fcaa-27a4-4bd9-8940-7690a86b2fe1', 'pictographic-primitives/symbol/phone with down arrow_14b5fcaa-27a4-4bd9-8940-7690a86b2fe1.svg'),)
PROFILE_SOURCE_KEYS = ('solo/phone-with-down-arrow',)
SOLO_SOURCE_ICON_IDS = ('phone-with-down-arrow',)
REFERENCE_EXPORT_SHA256 = '6d59e59faac650060dd379c21f1326f2b68af82b1c6a8ac06bb179ed5806a02d'

class Drawing(Sub32):
    icon_id = 'phone-with-down-arrow-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (30, 2), (21, 11))
        self.add_line('p1-r1-2', (21, 11), (28, 11))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (21, 4), (21, 11))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_bezier('p3-r1-1', (16, 26), ((17, 25), (19, 24), (20, 22)))
        self.add_bezier('p3-r1-2', (20, 22), ((21, 21), (22, 20), (22, 20)))
        self.add_bezier('p3-r1-3', (22, 20), ((23, 20), (24, 21), (25, 21)))
        self.add_line('p3-r1-4', (25, 21), (28, 24))
        self.add_bezier('p3-r1-5', (28, 24), ((28, 24), (28, 25), (28, 25)))
        self.add_bezier('p3-r1-6', (28, 25), ((28, 26), (27, 27), (27, 28)))
        self.add_bezier('p3-r1-7', (27, 28), ((26, 29), (25, 30), (25, 30)))
        self.add_bezier('p3-r1-8', (25, 30), ((24, 30), (24, 30), (23, 30)))
        self.add_bezier('p3-r1-9', (23, 30), ((23, 30), (23, 30), (23, 30)))
        self.add_bezier('p3-r1-10', (23, 30), ((21, 30), (18, 28), (16, 26)))
        self.add_bezier('p3-r1-11', (16, 26), ((12, 23), (8, 19), (5, 15)))
        self.add_bezier('p3-r1-12', (5, 15), ((4, 13), (2, 10), (2, 8)))
        self.add_bezier('p3-r1-13', (2, 8), ((2, 8), (2, 7), (2, 7)))
        self.add_bezier('p3-r1-14', (2, 7), ((2, 7), (2, 7), (2, 7)))
        self.add_bezier('p3-r1-15', (2, 7), ((2, 6), (2, 5), (3, 5)))
        self.add_bezier('p3-r1-16', (3, 5), ((3, 4), (5, 2), (6, 2)))
        self.add_bezier('p3-r1-17', (6, 2), ((7, 2), (7, 2), (7, 3)))
        self.add_line('p3-r1-18', (7, 3), (11, 6))
        self.add_bezier('p3-r1-19', (11, 6), ((11, 6), (11, 7), (11, 8)))
        self.add_bezier('p3-r1-20', (11, 8), ((11, 8), (11, 9), (11, 10)))
        self.add_line('p3-r1-21', (11, 10), (5, 14))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', 'p3-r1-6', 'p3-r1-7', 'p3-r1-8', 'p3-r1-9', 'p3-r1-10', 'p3-r1-11', 'p3-r1-12', 'p3-r1-13', 'p3-r1-14', 'p3-r1-15', 'p3-r1-16', 'p3-r1-17', 'p3-r1-18', 'p3-r1-19', 'p3-r1-20', 'p3-r1-21', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
