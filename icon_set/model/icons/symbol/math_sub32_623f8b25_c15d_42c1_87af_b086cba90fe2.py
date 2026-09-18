"""Independent 32px profile of math.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '623f8b25-c15d-42c1-87af-b086cba90fe2'
SOURCE_PATH = 'pictographic-primitives/symbol/math_623f8b25-c15d-42c1-87af-b086cba90fe2.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('623f8b25-c15d-42c1-87af-b086cba90fe2', 'pictographic-primitives/symbol/math_623f8b25-c15d-42c1-87af-b086cba90fe2.svg'),)
PROFILE_SOURCE_KEYS = ('solo/math',)
SOLO_SOURCE_ICON_IDS = ('math',)
REFERENCE_EXPORT_SHA256 = 'a666c1504052e1c32615f88779df6030d03842680d349129d1a4f68bd795e04f'

class Drawing(Sub32):
    icon_id = 'math-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (16, 2), (16, 13))
        self.add_line('p1-r1-2', (16, 13), (5, 13))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (16, 24), (16, 13))
        self.add_line('p2-r1-2', (16, 13), (27, 13))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (5, 30), (27, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p2-r1-2')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-2')
