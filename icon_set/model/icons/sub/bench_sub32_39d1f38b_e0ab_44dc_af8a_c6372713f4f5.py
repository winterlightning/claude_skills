"""Independent 32px profile of bench.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '39d1f38b-e0ab-44dc-af8a-c6372713f4f5'
SOURCE_PATH = 'pictographic-primitives/furnitures/bench_39d1f38b-e0ab-44dc-af8a-c6372713f4f5.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('39d1f38b-e0ab-44dc-af8a-c6372713f4f5', 'pictographic-primitives/furnitures/bench_39d1f38b-e0ab-44dc-af8a-c6372713f4f5.svg'),)
PROFILE_SOURCE_KEYS = ('solo/bench',)
SOLO_SOURCE_ICON_IDS = ('bench',)
REFERENCE_EXPORT_SHA256 = 'a8dc2f8a7916d6e08bd38c2da837f3492e1dacb0c29494f2d59fb1b65f01c854'

class Drawing(Sub32):
    icon_id = 'bench-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'furnitures'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (5, 5), (10, 5))
        self.add_line('p1-r1-2', (10, 5), (22, 5))
        self.add_line('p1-r1-3', (22, 5), (27, 5))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (2, 16), (8, 16))
        self.add_line('p2-r1-2', (8, 16), (24, 16))
        self.add_line('p2-r1-3', (24, 16), (30, 16))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_line('p3-r1-1', (10, 5), (8, 16))
        self.add_line('p3-r1-2', (8, 16), (5, 27))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_line('p4-r1-1', (22, 5), (24, 16))
        self.add_line('p4-r1-2', (24, 16), (27, 27))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.relate("connect", 'p1-r1-1', 'p3-r1-1')
        self.relate("connect", 'p1-r1-2', 'p3-r1-1')
        self.relate("connect", 'p1-r1-2', 'p4-r1-1')
        self.relate("connect", 'p1-r1-3', 'p4-r1-1')
        self.relate("connect", 'p2-r1-1', 'p3-r1-1')
        self.relate("connect", 'p2-r1-1', 'p3-r1-2')
        self.relate("connect", 'p2-r1-2', 'p3-r1-1')
        self.relate("connect", 'p2-r1-2', 'p3-r1-2')
        self.relate("connect", 'p2-r1-2', 'p4-r1-1')
        self.relate("connect", 'p2-r1-2', 'p4-r1-2')
        self.relate("connect", 'p2-r1-3', 'p4-r1-1')
        self.relate("connect", 'p2-r1-3', 'p4-r1-2')
