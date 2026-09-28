"""Independent 32px profile of helmet-d5b67122.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'd5b67122-8eaa-475e-8ad0-0d51c15807ab'
SOURCE_PATH = 'pictographic-primitives/protection/helmet_d5b67122-8eaa-475e-8ad0-0d51c15807ab.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('d5b67122-8eaa-475e-8ad0-0d51c15807ab', 'pictographic-primitives/protection/helmet_d5b67122-8eaa-475e-8ad0-0d51c15807ab.svg'),)
PROFILE_SOURCE_KEYS = ('solo/helmet-d5b67122',)
SOLO_SOURCE_ICON_IDS = ('helmet-d5b67122',)
REFERENCE_EXPORT_SHA256 = 'ef4d35f716e8a78bb97617de1e25b23dfcccdaf0dc8bb4d25604baef4e643336'

class DrawingContainerSymbol(Sub32):
    icon_id = 'helmet-d5b67122-sub32-symbol'
    related_origin_icon_id = 'helmet-d5b67122-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/helmet-d5b67122-sub32'
    counterpart_icon_id = 'helmet-d5b67122-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'protection'
    categories = ('protection', 'state', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (30, 27), (2, 27))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (19, 5), (13, 5))
        self.add_line('p2-r1-2', (13, 5), (13, 8))
        self.add_line('p2-r1-3', (13, 8), (13, 9))
        self.add_arc('p2-r1-4', (13, 9), (5, 21), radius_x=17, radius_y=17, large_arc=False, sweep=False)
        self.add_arc('p2-r1-5', (5, 21), (5, 27), radius_x=41, radius_y=41, large_arc=False, sweep=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
        self.add_line('p3-r1-1', (13, 20), (13, 9))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_arc('p4-r1-1', (20, 9), (27, 21), radius_x=17, radius_y=17, large_arc=False, sweep=True)
        self.add_arc('p4-r1-2', (27, 21), (27, 27), radius_x=41, radius_y=41, large_arc=False, sweep=True)
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_line('p5-r1-1', (20, 20), (20, 8))
        self.add_line('p5-r1-2', (20, 8), (19, 5))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', closed=False)
        self.relate('connect', 'p2-r1-1', 'p5-r1-2')
        self.relate('connect', 'p2-r1-3', 'p3-r1-1')
        self.relate('connect', 'p2-r1-4', 'p3-r1-1')
