"""Independent 32px profile of fragmented-brain.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'fc4c0825-2444-4f46-a5a5-c79974a41e25'
SOURCE_PATH = 'pictographic-primitives/symbol/fragmented brain_fc4c0825-2444-4f46-a5a5-c79974a41e25.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('fc4c0825-2444-4f46-a5a5-c79974a41e25', 'pictographic-primitives/symbol/fragmented brain_fc4c0825-2444-4f46-a5a5-c79974a41e25.svg'),)
PROFILE_SOURCE_KEYS = ('solo/fragmented-brain',)
SOLO_SOURCE_ICON_IDS = ('fragmented-brain',)
REFERENCE_EXPORT_SHA256 = '6cd7d2a64f86bf6bfbc1b8f7aaa9063cca619d5bd06f831e7a1ec81be0a614e7'

class Drawing(Sub32):
    icon_id = 'fragmented-brain-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (5, 13), ((8, 8), (15, 5), (20, 5)))
        self.add_bezier('p1-r1-2', (20, 5), ((23, 5), (24, 6), (26, 8)))
        self.add_bezier('p1-r1-3', (26, 8), ((28, 10), (30, 9), (30, 12)))
        self.add_bezier('p1-r1-4', (30, 12), ((30, 15), (27, 17), (24, 18)))
        self.add_line('p1-r1-5', (24, 18), (8, 26))
        self.add_bezier('p1-r1-6', (8, 26), ((6, 27), (6, 27), (5, 27)))
        self.add_bezier('p1-r1-7', (5, 27), ((3, 27), (2, 26), (2, 23)))
        self.add_bezier('p1-r1-8', (2, 23), ((2, 20), (3, 17), (5, 13)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_line('p2-r1-1', (5, 13), (17, 15))
        self.add_line('p2-r1-2', (17, 15), (24, 18))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (8, 26), (17, 15))
        self.add_line('p3-r1-2', (17, 15), (26, 8))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p3-r1-2')
        self.relate('connect', 'p1-r1-3', 'p3-r1-2')
        self.relate('connect', 'p1-r1-4', 'p2-r1-2')
        self.relate('connect', 'p1-r1-5', 'p2-r1-2')
        self.relate('connect', 'p1-r1-5', 'p3-r1-1')
        self.relate('connect', 'p1-r1-6', 'p3-r1-1')
        self.relate('connect', 'p1-r1-8', 'p2-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-2')
        self.relate('connect', 'p2-r1-2', 'p3-r1-1')
        self.relate('connect', 'p2-r1-2', 'p3-r1-2')
