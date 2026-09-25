"""Independent 32px profile of paint-bucket-spill.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'aebdb949-dd90-42b9-8053-6c7b6b0e29e8'
SOURCE_PATH = 'pictographic-primitives/symbol/paint_aebdb949-dd90-42b9-8053-6c7b6b0e29e8.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('aebdb949-dd90-42b9-8053-6c7b6b0e29e8', 'pictographic-primitives/symbol/paint_aebdb949-dd90-42b9-8053-6c7b6b0e29e8.svg'),)
PROFILE_SOURCE_KEYS = ('solo/paint-bucket-spill',)
SOLO_SOURCE_ICON_IDS = ('paint-bucket-spill',)
REFERENCE_EXPORT_SHA256 = 'f4cf26f4b1310c3e3dfbb0cfe29829e395a331af58a0e871b9c9426ef66f7e3e'

class Drawing(Sub32):
    icon_id = 'paint-bucket-spill-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (2, 5), (5, 2), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-2', (5, 2), (22, 2))
        self.add_arc('p1-r1-3', (22, 2), (30, 10), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_line('p1-r1-4', (30, 10), (30, 16))
        self.add_arc('p1-r1-5', (30, 16), (27, 19), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p1-r1-6', (27, 19), (24, 16), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-7', (24, 16), (22, 14))
        self.add_arc('p1-r1-8', (22, 14), (16, 14), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-9', (16, 14), (16, 9))
        self.add_line('p1-r1-10', (16, 9), (5, 9))
        self.add_arc('p1-r1-11', (5, 9), (2, 6), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-12', (2, 6), (2, 5))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', closed=False)
        self.add_line('p2-r1-1', (5, 9), (8, 30))
        self.add_line('p2-r1-2', (8, 30), (25, 30))
        self.add_line('p2-r1-3', (25, 30), (27, 19))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.relate('connect', 'p1-r1-5', 'p2-r1-3')
        self.relate('connect', 'p1-r1-6', 'p2-r1-3')
        self.relate('connect', 'p1-r1-10', 'p2-r1-1')
        self.relate('connect', 'p1-r1-11', 'p2-r1-1')
