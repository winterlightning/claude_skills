"""Independent 32px profile of downward-trend-arrow.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '082bbc6d-66f5-4ed1-9c07-82e626a9bcbb'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/downtrend arrow_082bbc6d-66f5-4ed1-9c07-82e626a9bcbb.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('082bbc6d-66f5-4ed1-9c07-82e626a9bcbb', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/downtrend arrow_082bbc6d-66f5-4ed1-9c07-82e626a9bcbb.svg'),)
PROFILE_SOURCE_KEYS = ('solo/downward-trend-arrow',)
SOLO_SOURCE_ICON_IDS = ('downward-trend-arrow',)
REFERENCE_EXPORT_SHA256 = '5b85bbb9bea2c62b1cab3c7c20935bea477b55dadcc9394d7ebb4bde2189ec58'

class DrawingVariant2ContainerSymbol(Sub32):
    icon_id = 'downward-trend-arrow-sub32-v2-symbol'
    related_origin_icon_id = 'downward-trend-arrow-sub32-v2'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/downward-trend-arrow-sub32-v2'
    counterpart_icon_id = 'downward-trend-arrow-sub32-v2'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives-generate'
    categories = ('symbol', 'other', 'state', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        short_axis = 16
        short_half_span = 12
        short_low, short_high = (short_axis - short_half_span, short_axis + short_half_span)
        self.add_line('p1-r1-1', (2, short_low), (11, 15))
        self.add_line('p1-r1-2', (11, 15), (17, 8))
        self.add_line('p1-r1-3', (17, 8), (30, short_high))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (22, short_high), (30, short_high))
        self.add_line('p2-r1-2', (30, short_high), (30, 19))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.relate('connect', 'p1-r1-3', 'p2-r1-1')
        self.relate('connect', 'p1-r1-3', 'p2-r1-2')
