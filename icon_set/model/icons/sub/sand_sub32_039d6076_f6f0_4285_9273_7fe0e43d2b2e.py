"""Independent 32px profile of sand.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '039d6076-f6f0-4285-9273-7fe0e43d2b2e'
SOURCE_PATH = 'pictographic-primitives/state/sand_039d6076-f6f0-4285-9273-7fe0e43d2b2e.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('039d6076-f6f0-4285-9273-7fe0e43d2b2e', 'pictographic-primitives/state/sand_039d6076-f6f0-4285-9273-7fe0e43d2b2e.svg'),)
PROFILE_SOURCE_KEYS = ('solo/sand',)
SOLO_SOURCE_ICON_IDS = ('sand',)
REFERENCE_EXPORT_SHA256 = 'db243ce3cbb6059099dbd79c7244b776ccc3c7a24a2cc1c936775dbfbda8dbfc'

class Drawing(Sub32):
    icon_id = 'sand-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'state'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 27), (15, 5))
        self.add_arc('p1-r1-2', (15, 5), (17, 5), radius_x=28, radius_y=28, large_arc=False, sweep=False)
        self.add_line('p1-r1-3', (17, 5), (30, 27))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (10, 27), (10, 27))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_arc('p3-r1-1', (16, 18), (15, 18), radius_x=17, radius_y=17, large_arc=False, sweep=True)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_arc('p4-r1-1', (22, 26), (21, 26), radius_x=23, radius_y=23, large_arc=False, sweep=False)
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
