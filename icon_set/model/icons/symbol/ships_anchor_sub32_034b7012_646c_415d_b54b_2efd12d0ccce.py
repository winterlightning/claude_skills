"""Independent 32px profile of ships-anchor.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '034b7012-646c-415d-b54b-2efd12d0ccce'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-08/anchor_034b7012-646c-415d-b54b-2efd12d0ccce.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('034b7012-646c-415d-b54b-2efd12d0ccce', 'pictographic-primitives/landmarks/batch-08/anchor_034b7012-646c-415d-b54b-2efd12d0ccce.svg'),)
PROFILE_SOURCE_KEYS = ('solo/ships-anchor',)
SOLO_SOURCE_ICON_IDS = ('ships-anchor',)
REFERENCE_EXPORT_SHA256 = '60a66a1c5bc3ff9e639f029537ed35c48012bba3db573551ae282aa329c9a3d3'

class Drawing(Sub32):
    icon_id = 'ships-anchor-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'landmarks'
    categories = ('landmarks', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (16, 8), (16, 2), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (16, 2), (16, 8), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (16, 8), (16, 14))
        self.add_line('p2-r1-2', (16, 14), (16, 30))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (10, 14), (16, 14))
        self.add_line('p3-r1-2', (16, 14), (22, 14))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_line('p4-r1-1', (7, 21), (2, 18))
        self.add_arc('p4-r1-2', (2, 18), (16, 30), radius_x=14, radius_y=12, large_arc=False, sweep=False)
        self.add_arc('p4-r1-3', (16, 30), (30, 18), radius_x=14, radius_y=12, large_arc=False, sweep=False)
        self.add_line('p4-r1-4', (30, 18), (25, 21))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-2')
        self.relate('connect', 'p2-r1-2', 'p3-r1-1')
        self.relate('connect', 'p2-r1-2', 'p3-r1-2')
        self.relate('connect', 'p2-r1-2', 'p4-r1-2')
        self.relate('connect', 'p2-r1-2', 'p4-r1-3')
