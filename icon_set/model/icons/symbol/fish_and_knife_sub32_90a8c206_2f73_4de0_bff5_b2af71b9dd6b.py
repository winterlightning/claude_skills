"""Independent 32px profile of fish-and-knife.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '90a8c206-2f73-4de0-bff5-b2af71b9dd6b'
SOURCE_PATH = 'pictographic-primitives/symbol/fish with knife_90a8c206-2f73-4de0-bff5-b2af71b9dd6b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('90a8c206-2f73-4de0-bff5-b2af71b9dd6b', 'pictographic-primitives/symbol/fish with knife_90a8c206-2f73-4de0-bff5-b2af71b9dd6b.svg'),)
PROFILE_SOURCE_KEYS = ('solo/fish-and-knife',)
SOLO_SOURCE_ICON_IDS = ('fish-and-knife',)
REFERENCE_EXPORT_SHA256 = '3eb9fc62c970bc9bbc2b2cb39da93d59c216dba1e2184ac82518e4bfb0552231'

class Drawing(Sub32):
    icon_id = 'fish-and-knife-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 4), (22, 4))
        self.add_line('p1-r1-2', (22, 4), (22, 12))
        self.add_line('p1-r1-3', (22, 12), (9, 12))
        self.add_arc('p1-r1-4', (9, 12), (2, 4), radius_x=7, radius_y=8, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (22, 4), (30, 4))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_arc('p3-r1-1', (10, 24), (30, 24), radius_x=10, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p3-r1-2', (30, 24), (10, 24), radius_x=10, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_line('p4-r1-1', (2, 20), (10, 24))
        self.add_line('p4-r1-3', (10, 24), (2, 28))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-3', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p3-r1-1', 'p4-r1-1')
        self.relate('connect', 'p3-r1-1', 'p4-r1-3')
        self.relate('connect', 'p3-r1-2', 'p4-r1-1')
        self.relate('connect', 'p3-r1-2', 'p4-r1-3')
