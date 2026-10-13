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
        # Adopted from the production stroke edit (Browser Edit by hina).
        self.add_line('p1-r1-1', (4, 9), (16, 2))
        self.add_line('p1-r1-2', (16, 2), (28, 9))
        self.add_line('p1-r1-3', (28, 9), (25, 14))
        self.add_line('p1-r1-4', (25, 14), (7, 14))
        self.add_line('p1-r1-5', (7, 14), (4, 9))
        self.add_line('p1-r1-6', (4, 9), (4, 9))
        self.add_arc('p3-r1-1', (23, 22), (9, 22), radius_x=7, radius_y=8, large_arc=False, sweep=True)
        self.add_line('p4-r1-1', (8, 14), (9, 22))
        self.add_line('p5-r1-1', (23, 22), (24, 14))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate('connect', 'p1-r1-3', 'p5-r1-1')
        self.relate('connect', 'p1-r1-4', 'p4-r1-1')
        self.relate('connect', 'p1-r1-4', 'p5-r1-1')
        self.relate('connect', 'p1-r1-5', 'p4-r1-1')
        self.relate('connect', 'p3-r1-1', 'p4-r1-1')
        self.relate('connect', 'p3-r1-1', 'p5-r1-1')
