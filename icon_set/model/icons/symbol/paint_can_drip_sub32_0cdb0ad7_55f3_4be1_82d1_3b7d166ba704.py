"""Independent 32px profile of paint-can-drip.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
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
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Paint can: rim band, body, and one drip 8 units wide hanging from the rim.
        self.add_line('p1-r1-1', (2, 10), (2, 2))
        self.add_line('p1-r1-2', (2, 2), (30, 2))
        self.add_line('p1-r1-3', (30, 2), (30, 10))
        self.add_line('p1-r1-4', (30, 10), (28, 10))
        self.add_line('p1-r1-5', (28, 10), (20, 10))
        self.add_line('p1-r1-6', (20, 10), (12, 10))
        self.add_line('p1-r1-7', (12, 10), (4, 10))
        self.add_line('p1-r1-8', (4, 10), (2, 10))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=True)
        self.add_line('p2-r1-1', (4, 10), (4, 27))
        self.add_arc('p2-r1-2', (4, 27), (7, 30), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_line('p2-r1-3', (7, 30), (25, 30))
        self.add_arc('p2-r1-4', (25, 30), (28, 27), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_line('p2-r1-5', (28, 27), (28, 10))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
        self.add_line('p3-r1-1', (12, 10), (12, 18))
        self.add_arc('p3-r1-2', (12, 18), (20, 18), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('p3-r1-3', (20, 18), (20, 10))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
        for a, b in (('p1-r1-7', 'p2-r1-1'), ('p1-r1-8', 'p2-r1-1'), ('p1-r1-4', 'p2-r1-5'), ('p1-r1-5', 'p2-r1-5'),
                     ('p1-r1-6', 'p3-r1-1'), ('p1-r1-7', 'p3-r1-1'), ('p1-r1-5', 'p3-r1-3'), ('p1-r1-6', 'p3-r1-3')):
            self.relate('connect', a, b)
