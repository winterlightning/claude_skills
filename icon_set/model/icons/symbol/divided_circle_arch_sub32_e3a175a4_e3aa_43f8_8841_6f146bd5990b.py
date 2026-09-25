"""Independent 32px profile of divided-circle-arch.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'e3a175a4-e3aa-43f8-8841-6f146bd5990b'
SOURCE_PATH = 'pictographic-primitives/symbol/divided face_e3a175a4-e3aa-43f8-8841-6f146bd5990b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('e3a175a4-e3aa-43f8-8841-6f146bd5990b', 'pictographic-primitives/symbol/divided face_e3a175a4-e3aa-43f8-8841-6f146bd5990b.svg'),)
PROFILE_SOURCE_KEYS = ('solo/divided-circle-arch',)
SOLO_SOURCE_ICON_IDS = ('divided-circle-arch',)
REFERENCE_EXPORT_SHA256 = '63d53e16a827c00bcec908509508624fe8b48a6eddc84acce2a14eec43000213'

class Drawing(Sub32):
    icon_id = 'divided-circle-arch-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (16, 2), (16, 30), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (16, 30), (16, 2), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (16, 2), (16, 20))
        self.add_line('p2-r1-2', (16, 20), (16, 30))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_arc('p3-r1-1', (10, 23), (16, 20), radius_x=6, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p3-r1-2', (16, 20), (22, 23), radius_x=6, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p2-r1-2')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-2')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-2')
        self.relate('connect', 'p2-r1-2', 'p3-r1-1')
        self.relate('connect', 'p2-r1-2', 'p3-r1-2')
