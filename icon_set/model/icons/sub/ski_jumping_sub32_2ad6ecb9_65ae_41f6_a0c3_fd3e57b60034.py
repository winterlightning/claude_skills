"""Independent 32px profile of ski-jumping.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '2ad6ecb9-65ae-41f6-a0c3-fd3e57b60034'
SOURCE_PATH = 'pictographic-primitives/symbol/snow jumping_2ad6ecb9-65ae-41f6-a0c3-fd3e57b60034.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('2ad6ecb9-65ae-41f6-a0c3-fd3e57b60034', 'pictographic-primitives/symbol/snow jumping_2ad6ecb9-65ae-41f6-a0c3-fd3e57b60034.svg'),)
PROFILE_SOURCE_KEYS = ('solo/ski-jumping',)
SOLO_SOURCE_ICON_IDS = ('ski-jumping',)
REFERENCE_EXPORT_SHA256 = '088da368a26089e36048a8104fb8f151e13a028c97d19ddde86b07f4da733bb4'

class Drawing(Sub32):
    icon_id = 'ski-jumping-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/symbols'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (13, 6), ((13, 4), (14, 2), (16, 2)))
        self.add_bezier('p1-r1-2', (16, 2), ((18, 2), (20, 4), (20, 6)))
        self.add_bezier('p1-r1-3', (20, 6), ((20, 7), (18, 9), (16, 9)))
        self.add_bezier('p1-r1-4', (16, 9), ((14, 9), (13, 7), (13, 6)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (10, 13), (8, 17))
        self.add_bezier('p2-r1-2', (8, 17), ((7, 17), (6, 18), (6, 18)))
        self.add_bezier('p2-r1-3', (6, 18), ((5, 19), (5, 19), (5, 20)))
        self.add_bezier('p2-r1-4', (5, 20), ((5, 21), (5, 22), (6, 22)))
        self.add_bezier('p2-r1-5', (6, 22), ((6, 23), (7, 23), (8, 23)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
        self.add_line('p3-r1-1', (10, 30), (24, 16))
        self.add_line('p3-r1-2', (24, 16), (27, 13))
        self.add_line('p3-r1-3', (27, 13), (27, 9))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
