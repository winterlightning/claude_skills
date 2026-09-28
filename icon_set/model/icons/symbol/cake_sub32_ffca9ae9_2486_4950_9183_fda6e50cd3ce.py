"""Independent 32px profile of cake.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'ffca9ae9-2486-4950-9183-fda6e50cd3ce'
SOURCE_PATH = 'pictographic-primitives/symbol/cake_ffca9ae9-2486-4950-9183-fda6e50cd3ce.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('ffca9ae9-2486-4950-9183-fda6e50cd3ce', 'pictographic-primitives/symbol/cake_ffca9ae9-2486-4950-9183-fda6e50cd3ce.svg'),)
PROFILE_SOURCE_KEYS = ('solo/cake',)
SOLO_SOURCE_ICON_IDS = ('cake',)
REFERENCE_EXPORT_SHA256 = '921f03620541456e7f0f05d229e210e31f40004e3c6e13290aa26f9f0c708fc1'

class Drawing(Sub32):
    icon_id = 'cake-sub32'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (13, 8), (20, 8), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (20, 8), (13, 8), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_bezier('p2-r1-1', (2, 20), ((2, 13), (8, 8), (13, 8)))
        self.add_arc('p2-r1-2', (13, 8), (17, 12), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_arc('p2-r1-3', (17, 12), (20, 8), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('p2-r1-4', (20, 8), (30, 20))
        self.add_line('p2-r1-5', (30, 20), (30, 27))
        self.add_line('p2-r1-6', (30, 27), (2, 27))
        self.add_line('p2-r1-7', (2, 27), (2, 20))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', closed=False)
        self.add_line('p3-r1-1', (2, 20), (30, 20))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p2-r1-2')
        self.relate('connect', 'p1-r1-1', 'p2-r1-3')
        self.relate('connect', 'p1-r1-1', 'p2-r1-4')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-2')
        self.relate('connect', 'p1-r1-2', 'p2-r1-3')
        self.relate('connect', 'p1-r1-2', 'p2-r1-4')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-4', 'p3-r1-1')
        self.relate('connect', 'p2-r1-5', 'p3-r1-1')
        self.relate('connect', 'p2-r1-7', 'p3-r1-1')
