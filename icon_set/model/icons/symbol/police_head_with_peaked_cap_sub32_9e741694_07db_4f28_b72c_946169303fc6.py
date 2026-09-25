"""Independent 32px profile of police-head-with-peaked-cap.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '9e741694-07db-4f28-b72c-946169303fc6'
SOURCE_PATH = 'pictographic-primitives/avatars/police man_9e741694-07db-4f28-b72c-946169303fc6.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('9e741694-07db-4f28-b72c-946169303fc6', 'pictographic-primitives/avatars/police man_9e741694-07db-4f28-b72c-946169303fc6.svg'),)
PROFILE_SOURCE_KEYS = ('solo/police-head-with-peaked-cap',)
SOLO_SOURCE_ICON_IDS = ('police-head-with-peaked-cap',)
REFERENCE_EXPORT_SHA256 = '5f967c3ad4a15c68a7b386193079b7aab06e573496e186ad55d337d704501577'

class Drawing(Sub32):
    icon_id = 'police-head-with-peaked-cap-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'avatars'
    categories = ('avatars', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (5, 8), (16, 2))
        self.add_line('p1-r1-2', (16, 2), (27, 8))
        self.add_line('p1-r1-3', (27, 8), (24, 13))
        self.add_line('p1-r1-4', (24, 13), (8, 13))
        self.add_line('p1-r1-5', (8, 13), (5, 8))
        self.add_line('p1-r1-6', (5, 8), (5, 8))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_line('p2-r1-1', (5, 8), (27, 8))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_arc('p3-r1-1', (24, 22), (8, 22), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (8, 13), (8, 22))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (24, 22), (24, 13))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_arc('p6-r1-1', (8, 13), (24, 13), radius_x=8, radius_y=6, large_arc=False, sweep=False)
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-3', 'p2-r1-1')
        self.relate('connect', 'p1-r1-3', 'p5-r1-1')
        self.relate('connect', 'p1-r1-3', 'p6-r1-1')
        self.relate('connect', 'p1-r1-4', 'p4-r1-1')
        self.relate('connect', 'p1-r1-4', 'p5-r1-1')
        self.relate('connect', 'p1-r1-4', 'p6-r1-1')
        self.relate('connect', 'p1-r1-5', 'p2-r1-1')
        self.relate('connect', 'p1-r1-5', 'p4-r1-1')
        self.relate('connect', 'p1-r1-5', 'p6-r1-1')
        self.relate('connect', 'p1-r1-6', 'p2-r1-1')
        self.relate('connect', 'p3-r1-1', 'p4-r1-1')
        self.relate('connect', 'p3-r1-1', 'p5-r1-1')
        self.relate('connect', 'p4-r1-1', 'p6-r1-1')
        self.relate('connect', 'p5-r1-1', 'p6-r1-1')
