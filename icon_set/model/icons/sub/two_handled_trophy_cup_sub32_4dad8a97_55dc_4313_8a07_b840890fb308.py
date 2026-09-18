"""Independent 32px profile of two-handled-trophy-cup.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '4dad8a97-55dc-4313-8a07-b840890fb308'
SOURCE_PATH = 'pictographic-primitives/business/trophy_4dad8a97-55dc-4313-8a07-b840890fb308.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('4dad8a97-55dc-4313-8a07-b840890fb308', 'pictographic-primitives/business/trophy_4dad8a97-55dc-4313-8a07-b840890fb308.svg'),)
PROFILE_SOURCE_KEYS = ('solo/two-handled-trophy-cup',)
SOLO_SOURCE_ICON_IDS = ('two-handled-trophy-cup',)
REFERENCE_EXPORT_SHA256 = 'b632626be315f61c5a7e24cc37fca51c68633baace38d917f2f98d429d074062'

class Drawing(Sub32):
    icon_id = 'two-handled-trophy-cup-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'business'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (10, 2), (22, 2))
        self.add_line('p1-r1-2', (22, 2), (22, 8))
        self.add_line('p1-r1-3', (22, 8), (22, 14))
        self.add_arc('p1-r1-4', (22, 14), (16, 21), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('p1-r1-5', (16, 21), (10, 14), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('p1-r1-6', (10, 14), (10, 8))
        self.add_line('p1-r1-7', (10, 8), (10, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', closed=False)
        self.add_arc('p2-r1-1', (10, 2), (2, 8), radius_x=8, radius_y=6, large_arc=False, sweep=False)
        self.add_arc('p2-r1-2', (2, 8), (10, 14), radius_x=8, radius_y=6, large_arc=False, sweep=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_arc('p3-r1-1', (22, 2), (30, 8), radius_x=8, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('p3-r1-2', (30, 8), (22, 14), radius_x=8, radius_y=6, large_arc=False, sweep=True)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_line('p4-r1-1', (16, 21), (16, 30))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (8, 30), (16, 30))
        self.add_line('p5-r1-2', (16, 30), (24, 30))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-1', 'p3-r1-1')
        self.relate("connect", 'p1-r1-2', 'p3-r1-1')
        self.relate("connect", 'p1-r1-3', 'p3-r1-2')
        self.relate("connect", 'p1-r1-4', 'p3-r1-2')
        self.relate("connect", 'p1-r1-4', 'p4-r1-1')
        self.relate("connect", 'p1-r1-5', 'p2-r1-2')
        self.relate("connect", 'p1-r1-5', 'p4-r1-1')
        self.relate("connect", 'p1-r1-6', 'p2-r1-2')
        self.relate("connect", 'p1-r1-7', 'p2-r1-1')
        self.relate("connect", 'p4-r1-1', 'p5-r1-1')
        self.relate("connect", 'p4-r1-1', 'p5-r1-2')
