"""Independent 32px profile of wheelchair-accessible.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'da29f68e-5632-431d-92e7-4ee9f999acb8'
SOURCE_PATH = 'pictographic-primitives/symbol/wheelchair_da29f68e-5632-431d-92e7-4ee9f999acb8.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('da29f68e-5632-431d-92e7-4ee9f999acb8', 'pictographic-primitives/symbol/wheelchair_da29f68e-5632-431d-92e7-4ee9f999acb8.svg'),)
PROFILE_SOURCE_KEYS = ('solo/wheelchair-accessible',)
SOLO_SOURCE_ICON_IDS = ('wheelchair-accessible',)
REFERENCE_EXPORT_SHA256 = '628c4b176c82ac2974b34469f9b2489870b6ccc915ab01b84fda940c9fb63018'

class DrawingContainerSymbol(Sub32):
    icon_id = 'wheelchair-accessible-sub32-symbol'
    related_origin_icon_id = 'wheelchair-accessible-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/wheelchair-accessible-sub32'
    counterpart_icon_id = 'wheelchair-accessible-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Wheelchair (access symbol): head dot, back, seat, leg forward, wheel arc around the seat.
        self.add_arc('head-1', (12, 4), (16, 4), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('head-2', (16, 4), (12, 4), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('head', 'head-1', 'head-2', closed=True)
        self.add_polyline('body', (14, 14), (14, 20), (22, 20), (26, 28), (30, 28))
        self.add_arc('wheel', (4, 14), (12, 30), radius_x=10, radius_y=10, large_arc=False, sweep=False)
