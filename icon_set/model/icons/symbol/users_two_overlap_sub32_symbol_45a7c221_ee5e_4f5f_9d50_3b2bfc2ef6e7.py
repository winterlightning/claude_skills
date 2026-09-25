"""Independent 32px profile of users-two-overlap.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '45a7c221-ee5e-4f5f-9d50-3b2bfc2ef6e7'
SOURCE_PATH = 'pictographic-primitives/symbol/two persons_45a7c221-ee5e-4f5f-9d50-3b2bfc2ef6e7.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('45a7c221-ee5e-4f5f-9d50-3b2bfc2ef6e7', 'pictographic-primitives/symbol/two persons_45a7c221-ee5e-4f5f-9d50-3b2bfc2ef6e7.svg'),)
PROFILE_SOURCE_KEYS = ('solo/users-two-overlap',)
SOLO_SOURCE_ICON_IDS = ('users-two-overlap',)
REFERENCE_EXPORT_SHA256 = '6cb9bfc0e94a523cb8e8699ac8ae9c422a582350f343bb074f9cda8dba52c6a4'

class DrawingContainerSymbol(Sub32):
    icon_id = 'users-two-overlap-sub32-symbol'
    related_origin_icon_id = 'users-two-overlap-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/users-two-overlap-sub32'
    counterpart_icon_id = 'users-two-overlap-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (3, 8), (9, 8), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (9, 8), (3, 8), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_arc('p2-r1-1', (17, 10), (29, 10), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('p2-r1-2', (29, 10), (17, 10), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (2, 24), (2, 23))
        self.add_arc('p3-r1-2', (2, 23), (6, 17), radius_x=4, radius_y=6, large_arc=False, sweep=True)
        self.add_line('p3-r1-3', (6, 17), (9, 17))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
        self.add_arc('p4-r1-1', (13, 27), (30, 27), radius_x=8.5, radius_y=5.3125, large_arc=False, sweep=True)
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
