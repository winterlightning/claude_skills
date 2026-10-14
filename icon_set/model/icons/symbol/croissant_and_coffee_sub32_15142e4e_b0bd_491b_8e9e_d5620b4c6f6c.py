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
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (2, 18), (30, 18), radius_x=14, radius_y=12, large_arc=False, sweep=False)
        self.add_arc('p1-r1-2', (30, 18), (2, 18), radius_x=30, radius_y=30, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=True)
        self.add_line('p2-r1-1', (8, 2), (20, 2))
        self.add_line('p2-r1-2', (20, 2), (20, 10))
        self.add_arc('p2-r1-3', (20, 10), (18, 12), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p2-r1-4', (18, 12), (10, 12))
        self.add_arc('p2-r1-5', (10, 12), (8, 10), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p2-r1-6', (8, 10), (8, 2))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', closed=True)
        self.add_arc('p3-r1-1', (20, 2), (20, 10), radius_x=8, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-2', 'p3-r1-1')
        self.relate('connect', 'p2-r1-3', 'p3-r1-1')
