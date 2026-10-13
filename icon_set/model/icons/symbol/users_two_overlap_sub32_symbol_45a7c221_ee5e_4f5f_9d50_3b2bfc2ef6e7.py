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
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Two users: a person in front (right) and one behind (left), 4 units apart.
        self.add_arc('head-front-1', (18, 8), (26, 8), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('head-front-2', (26, 8), (18, 8), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('head-front', 'head-front-1', 'head-front-2', closed=True)
        self.add_arc('head-back-1', (4, 8), (8, 8), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('head-back-2', (8, 8), (4, 8), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('head-back', 'head-back-1', 'head-back-2', closed=True)
        self.add_arc('body-front', (14, 28), (30, 28), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_bezier('body-back', (2, 28), ((2, 22), (4, 18), (8, 18)))
