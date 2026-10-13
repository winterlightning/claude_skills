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
    keyshape = Keyshape.HRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'protection'
    categories = ('protection', 'state', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Adopted from the production stroke edit (Browser Edit by hina).
        self.add_line('p1-r1-1', (30, 26), (2, 26))
        self.add_line('p2-r1-1', (20, 6), (12, 6))
        self.add_line('p2-r1-2', (12, 6), (12, 8))
        self.add_line('p2-r1-3', (12, 8), (12, 9))
        self.add_arc('p2-r1-4', (12, 9), (5, 20), radius_x=17, radius_y=16, large_arc=False, sweep=False)
        self.add_arc('p2-r1-5', (5, 20), (5, 26), radius_x=41, radius_y=38, large_arc=False, sweep=False)
        self.add_line('p3-r1-1', (12, 16), (12, 9))
        self.add_arc('p4-r1-1', (20, 9), (27, 20), radius_x=17, radius_y=16, large_arc=False, sweep=True)
        self.add_arc('p4-r1-2', (27, 20), (27, 26), radius_x=41, radius_y=38, large_arc=False, sweep=True)
        self.add_line('p5-r1-1', (20, 16), (20, 8))
        self.add_line('p5-r1-2', (20, 8), (20, 6))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', closed=False)
        self.relate('connect', 'p2-r1-1', 'p5-r1-2')
        self.relate('connect', 'p2-r1-3', 'p3-r1-1')
        self.relate('connect', 'p2-r1-4', 'p3-r1-1')
        # Declared joints: these strokes meet or cross on purpose.
        self.relate('connect', 'path-1-1', 'path-2-1')
        self.relate('connect', 'path-1-1', 'path-4-1')
        self.relate('connect', 'path-5-1', 'path-4-1')
