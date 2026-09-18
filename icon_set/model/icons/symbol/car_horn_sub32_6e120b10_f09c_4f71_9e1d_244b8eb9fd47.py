"""Independent 32px profile of car-horn.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '6e120b10-f09c-4f71-9e1d-244b8eb9fd47'
SOURCE_PATH = 'pictographic-primitives/transportation/horn_6e120b10-f09c-4f71-9e1d-244b8eb9fd47.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('6e120b10-f09c-4f71-9e1d-244b8eb9fd47', 'pictographic-primitives/transportation/horn_6e120b10-f09c-4f71-9e1d-244b8eb9fd47.svg'),)
PROFILE_SOURCE_KEYS = ('solo/car-horn',)
SOLO_SOURCE_ICON_IDS = ('car-horn',)
REFERENCE_EXPORT_SHA256 = 'af3318d9d06e136eac0f445c02586cb0e8e0dea711af5402a7a29813dfad5498'

class Drawing(Sub32):
    icon_id = 'car-horn-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/transportation'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 10), (12, 16))
        self.add_line('p1-r1-2', (12, 16), (2, 22))
        self.add_line('p1-r1-3', (2, 22), (2, 10))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (12, 16), (19, 16))
        self.add_line('p2-r1-2', (19, 16), (27, 16))
        self.add_line('p2-r1-3', (27, 16), (29, 16))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_line('p3-r1-1', (19, 16), (19, 23))
        self.add_arc('p3-r1-2', (19, 23), (23, 27), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_arc('p3-r1-3', (23, 27), (27, 23), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('p3-r1-4', (27, 23), (27, 16))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.add_line('p4-r1-1', (19, 5), (22, 5))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (27, 5), (30, 5))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-2', 'p3-r1-1')
        self.relate('connect', 'p2-r1-2', 'p3-r1-4')
        self.relate('connect', 'p2-r1-3', 'p3-r1-4')
