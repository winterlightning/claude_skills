"""Independent 32px profile of croissant-and-coffee.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '15142e4e-b0bd-491b-8e9e-d5620b4c6f6c'
SOURCE_PATH = 'pictographic-primitives/symbol/croissant_15142e4e-b0bd-491b-8e9e-d5620b4c6f6c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('15142e4e-b0bd-491b-8e9e-d5620b4c6f6c', 'pictographic-primitives/symbol/croissant_15142e4e-b0bd-491b-8e9e-d5620b4c6f6c.svg'),)
PROFILE_SOURCE_KEYS = ('solo/croissant-and-coffee',)
SOLO_SOURCE_ICON_IDS = ('croissant-and-coffee',)
REFERENCE_EXPORT_SHA256 = '49f2c19e7cd3cb42a54cb419ffb8001b344061a6f6ffc5c1846dfc42088649b4'

class Drawing(Sub32):
    icon_id = 'croissant-and-coffee-sub32'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (9, 5), (19, 5))
        self.add_line('p1-r1-2', (19, 5), (19, 10))
        self.add_arc('p1-r1-3', (19, 10), (17, 12), radius_x=1.4142135623730951, radius_y=1.4142135623730951, large_arc=False, sweep=True)
        self.add_line('p1-r1-4', (17, 12), (10, 12))
        self.add_arc('p1-r1-5', (10, 12), (9, 10), radius_x=1.118033988749895, radius_y=1.118033988749895, large_arc=False, sweep=True)
        self.add_line('p1-r1-6', (9, 10), (9, 5))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_arc('p2-r1-1', (19, 5), (19, 10), radius_x=6, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_arc('p3-r1-1', (30, 13), (24, 24), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p3-r1-2', (24, 24), (8, 24), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p3-r1-3', (8, 24), (2, 13), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p3-r1-4', (2, 13), (8, 17), radius_x=14, radius_y=14, large_arc=False, sweep=False)
        self.add_arc('p3-r1-5', (8, 17), (24, 17), radius_x=14, radius_y=7, large_arc=False, sweep=False)
        self.add_arc('p3-r1-6', (24, 17), (30, 13), radius_x=14, radius_y=14, large_arc=False, sweep=False)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', 'p3-r1-6', closed=False)
        self.add_line('p4-r1-1', (8, 24), (10, 24))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (24, 24), (22, 24))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-3', 'p2-r1-1')
        self.relate('connect', 'p3-r1-1', 'p5-r1-1')
        self.relate('connect', 'p3-r1-2', 'p4-r1-1')
        self.relate('connect', 'p3-r1-2', 'p5-r1-1')
        self.relate('connect', 'p3-r1-3', 'p4-r1-1')
