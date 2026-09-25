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
        self.add_line('p1-r1-1', (10, 6), (22, 6))
        self.add_arc('p1-r1-2', (22, 6), (28, 12), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (28, 12), (28, 18))
        self.add_arc('p1-r1-4', (28, 18), (4, 18), radius_x=12, radius_y=12, large_arc=False, sweep=True)
        self.add_line('p1-r1-5', (4, 18), (4, 12))
        self.add_arc('p1-r1-6', (4, 12), (10, 6), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_arc('p2-r1-1', (4, 12), (2, 7), radius_x=2, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('p2-r1-2', (2, 7), (5, 2), radius_x=3, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('p2-r1-3', (5, 2), (10, 6), radius_x=5, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_arc('p3-r1-1', (22, 6), (27, 2), radius_x=5, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p3-r1-2', (27, 2), (30, 7), radius_x=3, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('p3-r1-3', (30, 7), (28, 12), radius_x=2, radius_y=5, large_arc=False, sweep=True)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
        self.add_line('p4-r1-1', (11, 16), (11, 18))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (21, 16), (21, 18))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-3')
        self.relate('connect', 'p1-r1-1', 'p3-r1-1')
        self.relate('connect', 'p1-r1-2', 'p3-r1-1')
        self.relate('connect', 'p1-r1-2', 'p3-r1-3')
        self.relate('connect', 'p1-r1-3', 'p3-r1-3')
        self.relate('connect', 'p1-r1-5', 'p2-r1-1')
        self.relate('connect', 'p1-r1-6', 'p2-r1-1')
        self.relate('connect', 'p1-r1-6', 'p2-r1-3')
