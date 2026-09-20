"""Independent 32px profile of paint-can-drip.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '0cdb0ad7-55f3-4be1-82d1-3b7d166ba704'
SOURCE_PATH = 'pictographic-primitives/symbol/paint_0cdb0ad7-55f3-4be1-82d1-3b7d166ba704.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('0cdb0ad7-55f3-4be1-82d1-3b7d166ba704', 'pictographic-primitives/symbol/paint_0cdb0ad7-55f3-4be1-82d1-3b7d166ba704.svg'),)
PROFILE_SOURCE_KEYS = ('solo/paint-can-drip',)
SOLO_SOURCE_ICON_IDS = ('paint-can-drip',)
REFERENCE_EXPORT_SHA256 = '384afe7e8f43b725693b32aca4d8d7a94ffd829657e230df9d6a6b1db9d47946'

class Drawing(Sub32):
    icon_id = 'paint-can-drip-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/symbols'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 9), (2, 2))
        self.add_line('p1-r1-2', (2, 2), (30, 2))
        self.add_line('p1-r1-3', (30, 2), (30, 14))
        self.add_line('p1-r1-4', (30, 14), (30, 27))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_arc('p2-r1-1', (30, 27), (27, 30), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (27, 30), (7, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_arc('p4-r1-1', (7, 30), (4, 27), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (4, 27), (4, 9))
        self.add_line('p5-r1-2', (4, 9), (2, 9))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', closed=False)
        self.add_line('p6-r1-1', (4, 9), (11, 9))
        self.add_line('p6-r1-2', (11, 9), (11, 20))
        self.add_arc('p6-r1-3', (11, 20), (18, 20), radius_x=3.5, radius_y=3.5, large_arc=False, sweep=False)
        self.add_line('p6-r1-4', (18, 20), (18, 13))
        self.add_arc('p6-r1-5', (18, 13), (24, 13), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p6-r1-6', (24, 13), (24, 14))
        self.add_arc('p6-r1-7', (24, 14), (30, 14), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_contour('path-6-1', 'p6-r1-1', 'p6-r1-2', 'p6-r1-3', 'p6-r1-4', 'p6-r1-5', 'p6-r1-6', 'p6-r1-7', closed=False)
        self.relate("connect", 'p1-r1-1', 'p5-r1-2')
        self.relate("connect", 'p1-r1-3', 'p6-r1-7')
        self.relate("connect", 'p1-r1-4', 'p2-r1-1')
        self.relate("connect", 'p1-r1-4', 'p6-r1-7')
        self.relate("connect", 'p2-r1-1', 'p3-r1-1')
        self.relate("connect", 'p3-r1-1', 'p4-r1-1')
        self.relate("connect", 'p4-r1-1', 'p5-r1-1')
        self.relate("connect", 'p5-r1-1', 'p6-r1-1')
        self.relate("connect", 'p5-r1-2', 'p6-r1-1')
