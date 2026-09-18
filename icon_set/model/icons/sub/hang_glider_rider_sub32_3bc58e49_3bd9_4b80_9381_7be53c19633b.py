"""Independent 32px profile of hang-glider-rider.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '3bc58e49-3bd9-4b80-9381-7be53c19633b'
SOURCE_PATH = 'pictographic-primitives/symbol/paragliding_3bc58e49-3bd9-4b80-9381-7be53c19633b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('3bc58e49-3bd9-4b80-9381-7be53c19633b', 'pictographic-primitives/symbol/paragliding_3bc58e49-3bd9-4b80-9381-7be53c19633b.svg'),)
PROFILE_SOURCE_KEYS = ('solo/hang-glider-rider',)
SOLO_SOURCE_ICON_IDS = ('hang-glider-rider',)
REFERENCE_EXPORT_SHA256 = 'b99858b30b85ab2548d6820740644165b32a23c754f92671152e031082a8dc37'

class Drawing(Sub32):
    icon_id = 'hang-glider-rider-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/symbols'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 5), (30, 5))
        self.add_line('p1-r1-2', (30, 5), (20, 10))
        self.add_line('p1-r1-3', (20, 10), (10, 15))
        self.add_line('p1-r1-4', (10, 15), (2, 5))
        self.add_line('p1-r1-5', (2, 5), (2, 5))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_line('p2-r1-1', (20, 10), (19, 20))
        self.add_line('p2-r1-2', (19, 20), (22, 27))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_arc('p3-r1-1', (2, 24), (13, 23), radius_x=17, radius_y=6, large_arc=False, sweep=False)
        self.add_line('p3-r1-2', (13, 23), (19, 20))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_arc('p4-r1-1', (26, 17), (30, 17), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('p4-r1-2', (30, 17), (26, 17), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.relate("connect", 'p1-r1-2', 'p2-r1-1')
        self.relate("connect", 'p1-r1-3', 'p2-r1-1')
        self.relate("connect", 'p2-r1-1', 'p3-r1-2')
        self.relate("connect", 'p2-r1-2', 'p3-r1-2')
