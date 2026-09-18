"""Independent 32px profile of batch-01-laptop.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '0eca8bb8-75fe-4501-aa58-53ce337798cc'
SOURCE_PATH = 'pictographic-primitives/computers/batch-01/laptop_0eca8bb8-75fe-4501-aa58-53ce337798cc.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('0eca8bb8-75fe-4501-aa58-53ce337798cc', 'pictographic-primitives/computers/batch-01/laptop_0eca8bb8-75fe-4501-aa58-53ce337798cc.svg'),)
PROFILE_SOURCE_KEYS = ('solo/batch-01-laptop',)
SOLO_SOURCE_ICON_IDS = ('batch-01-laptop',)
REFERENCE_EXPORT_SHA256 = '7a8d541adbc07580400536eb9000ec61fff450b9862a40b2700ca972491e9215'

class Drawing(Sub32):
    icon_id = 'batch-01-laptop-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'computers'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (5, 20), (5, 8))
        self.add_arc('p1-r1-2', (5, 8), (8, 5), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (8, 5), (24, 5))
        self.add_arc('p1-r1-4', (24, 5), (27, 8), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-5', (27, 8), (27, 20))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_line('p2-r1-1', (5, 20), (27, 20))
        self.add_line('p2-r1-2', (27, 20), (30, 24))
        self.add_bezier('p2-r1-3', (30, 24), ((30, 27), (29, 27), (26, 27)))
        self.add_line('p2-r1-4', (26, 27), (6, 27))
        self.add_bezier('p2-r1-5', (6, 27), ((3, 27), (2, 27), (2, 24)))
        self.add_line('p2-r1-6', (2, 24), (5, 20))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-1', 'p2-r1-6')
        self.relate("connect", 'p1-r1-5', 'p2-r1-1')
        self.relate("connect", 'p1-r1-5', 'p2-r1-2')
