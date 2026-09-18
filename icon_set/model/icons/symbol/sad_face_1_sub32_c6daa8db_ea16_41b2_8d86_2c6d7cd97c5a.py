"""Independent 32px profile of sad-face-1.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'c6daa8db-ea16-41b2-8d86-2c6d7cd97c5a'
SOURCE_PATH = 'pictographic-primitives/symbol/sad face 1_c6daa8db-ea16-41b2-8d86-2c6d7cd97c5a.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('c6daa8db-ea16-41b2-8d86-2c6d7cd97c5a', 'pictographic-primitives/symbol/sad face 1_c6daa8db-ea16-41b2-8d86-2c6d7cd97c5a.svg'),)
PROFILE_SOURCE_KEYS = ('solo/sad-face-1',)
SOLO_SOURCE_ICON_IDS = ('sad-face-1',)
REFERENCE_EXPORT_SHA256 = 'e820c4393ead1b7f98c41c5f1f90b0630950d86bd2ca7c2e47b46aa3cd08480e'

class Drawing(Sub32):
    icon_id = 'sad-face-1-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (8, 10), (8, 5))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (23, 10), (23, 5))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_bezier('p3-r1-1', (2, 27), ((4, 24), (6, 22), (9, 20)))
        self.add_bezier('p3-r1-2', (9, 20), ((11, 19), (13, 18), (16, 18)))
        self.add_bezier('p3-r1-3', (16, 18), ((21, 18), (27, 22), (30, 27)))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
