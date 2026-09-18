"""Independent 32px profile of snowflake-1.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '360fc91b-24b0-485d-863b-30511134cdd1'
SOURCE_PATH = 'pictographic-primitives/state/snowflake 1_360fc91b-24b0-485d-863b-30511134cdd1.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('360fc91b-24b0-485d-863b-30511134cdd1', 'pictographic-primitives/state/snowflake 1_360fc91b-24b0-485d-863b-30511134cdd1.svg'),)
PROFILE_SOURCE_KEYS = ('solo/snowflake-1',)
SOLO_SOURCE_ICON_IDS = ('snowflake-1',)
REFERENCE_EXPORT_SHA256 = '2a67d9c556f299dc943f665f409ac583a7dec61147fe709ffd5aabfd3e4c5778'

class Drawing(Sub32):
    icon_id = 'snowflake-1-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'state'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (16, 2), (16, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (9, 16), (23, 16))
        self.add_line('p2-r1-2', (23, 16), (27, 21))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (21, 26), (16, 22))
        self.add_line('p3-r1-2', (16, 22), (11, 26))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_line('p4-r1-1', (30, 16), (23, 16))
        self.add_line('p4-r1-2', (23, 16), (27, 11))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_line('p5-r1-1', (21, 7), (16, 11))
        self.add_line('p5-r1-2', (16, 11), (11, 7))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', closed=False)
        self.add_line('p6-r1-1', (5, 21), (9, 16))
        self.add_line('p6-r1-2', (9, 16), (2, 16))
        self.add_contour('path-6-1', 'p6-r1-1', 'p6-r1-2', closed=False)
        self.add_line('p7-r1-1', (5, 11), (9, 16))
        self.add_contour('path-7-1', 'p7-r1-1', closed=False)
        self.relate("connect", 'p2-r1-1', 'p4-r1-1')
        self.relate("connect", 'p2-r1-1', 'p4-r1-2')
        self.relate("connect", 'p2-r1-1', 'p6-r1-1')
        self.relate("connect", 'p2-r1-1', 'p6-r1-2')
        self.relate("connect", 'p2-r1-1', 'p7-r1-1')
        self.relate("connect", 'p2-r1-2', 'p4-r1-1')
        self.relate("connect", 'p2-r1-2', 'p4-r1-2')
        self.relate("connect", 'p6-r1-1', 'p7-r1-1')
        self.relate("connect", 'p6-r1-2', 'p7-r1-1')
