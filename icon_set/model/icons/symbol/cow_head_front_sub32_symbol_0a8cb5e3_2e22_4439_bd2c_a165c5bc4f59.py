"""Independent 32px profile of cow-head-front.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '0a8cb5e3-2e22-4439-bd2c-a165c5bc4f59'
SOURCE_PATH = 'pictographic-primitives/symbol/bull head_0a8cb5e3-2e22-4439-bd2c-a165c5bc4f59.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('0a8cb5e3-2e22-4439-bd2c-a165c5bc4f59', 'pictographic-primitives/symbol/bull head_0a8cb5e3-2e22-4439-bd2c-a165c5bc4f59.svg'),)
PROFILE_SOURCE_KEYS = ('solo/cow-head-front',)
SOLO_SOURCE_ICON_IDS = ('cow-head-front',)
REFERENCE_EXPORT_SHA256 = '41004d51be8811ac90edff7215b79923799d47b45a94f525f5eb86efb036ea77'

class DrawingContainerSymbol(Sub32):
    icon_id = 'cow-head-front-sub32-symbol'
    related_origin_icon_id = 'cow-head-front-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/cow-head-front-sub32'
    counterpart_icon_id = 'cow-head-front-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (8, 8), (16, 7))
        self.add_line('p1-r1-2', (16, 7), (24, 8))
        self.add_line('p1-r1-3', (24, 8), (22, 25))
        self.add_arc('p1-r1-4', (22, 25), (18, 30), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('p1-r1-5', (18, 30), (14, 30))
        self.add_arc('p1-r1-6', (14, 30), (10, 25), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('p1-r1-7', (10, 25), (8, 8))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', closed=False)
        self.add_line('p2-r1-1', (8, 8), (2, 16))
        self.add_line('p2-r1-2', (2, 16), (9, 19))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (24, 8), (30, 16))
        self.add_line('p3-r1-2', (30, 16), (23, 19))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_arc('p4-r1-1', (4, 2), (8, 8), radius_x=8, radius_y=8, large_arc=False, sweep=False)
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_arc('p5-r1-1', (24, 8), (28, 2), radius_x=8, radius_y=8, large_arc=False, sweep=False)
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p4-r1-1')
        self.relate('connect', 'p1-r1-2', 'p3-r1-1')
        self.relate('connect', 'p1-r1-2', 'p5-r1-1')
        self.relate('connect', 'p1-r1-3', 'p3-r1-1')
        self.relate('connect', 'p1-r1-3', 'p5-r1-1')
        self.relate('connect', 'p1-r1-7', 'p2-r1-1')
        self.relate('connect', 'p1-r1-7', 'p4-r1-1')
        self.relate('connect', 'p2-r1-1', 'p4-r1-1')
        self.relate('connect', 'p3-r1-1', 'p5-r1-1')
