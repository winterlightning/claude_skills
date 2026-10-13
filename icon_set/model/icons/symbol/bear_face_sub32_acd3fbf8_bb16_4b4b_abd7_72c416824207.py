"""Independent 32px profile of bear-face.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'acd3fbf8-bb16-4b4b-abd7-72c416824207'
SOURCE_PATH = 'pictographic-primitives/animals/bear head_acd3fbf8-bb16-4b4b-abd7-72c416824207.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('acd3fbf8-bb16-4b4b-abd7-72c416824207', 'pictographic-primitives/animals/bear head_acd3fbf8-bb16-4b4b-abd7-72c416824207.svg'),)
PROFILE_SOURCE_KEYS = ('solo/bear-face',)
SOLO_SOURCE_ICON_IDS = ('bear-face',)
REFERENCE_EXPORT_SHA256 = '7585ac220148c8852889dfe4481dfe28d32a91b7484d7ebf11d2579eef5c61df'

class Drawing(Sub32):
    icon_id = 'bear-face-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'animals'
    categories = ('animals', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (2, 6), (10, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p1-r1-2', (10, 6), (22, 6))
        self.add_arc('p1-r1-3', (22, 6), (30, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p1-r1-4', (30, 6), (30, 18))
        self.add_arc('p1-r1-5', (30, 18), (2, 18), radius_x=14, radius_y=12, large_arc=False, sweep=True)
        self.add_line('p1-r1-6', (2, 18), (2, 6))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=True)
        self.add_line('p2-r1-1', (10, 14), (10, 14))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (22, 14), (22, 14))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (16, 20), (16, 20))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p3-r1-1')
        self.relate('connect', 'p1-r1-1', 'p4-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p3-r1-1')
        self.relate('connect', 'p1-r1-2', 'p4-r1-1')
        self.relate('connect', 'p1-r1-3', 'p2-r1-1')
        self.relate('connect', 'p1-r1-3', 'p3-r1-1')
        self.relate('connect', 'p1-r1-3', 'p4-r1-1')
        self.relate('connect', 'p1-r1-4', 'p2-r1-1')
        self.relate('connect', 'p1-r1-4', 'p3-r1-1')
        self.relate('connect', 'p1-r1-4', 'p4-r1-1')
        self.relate('connect', 'p1-r1-5', 'p2-r1-1')
        self.relate('connect', 'p1-r1-5', 'p3-r1-1')
        self.relate('connect', 'p1-r1-5', 'p4-r1-1')
        self.relate('connect', 'p1-r1-6', 'p2-r1-1')
        self.relate('connect', 'p1-r1-6', 'p3-r1-1')
        self.relate('connect', 'p1-r1-6', 'p4-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p4-r1-1')
        self.relate('connect', 'p3-r1-1', 'p4-r1-1')
