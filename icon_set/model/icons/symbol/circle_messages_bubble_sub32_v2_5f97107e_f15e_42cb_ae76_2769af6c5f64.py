"""Independent 32px profile of circle-messages-bubble.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '5f97107e-f15e-42cb-ae76-2769af6c5f64'
SOURCE_PATH = 'pictographic-primitives/other/circle messages bubble_5f97107e-f15e-42cb-ae76-2769af6c5f64.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('5f97107e-f15e-42cb-ae76-2769af6c5f64', 'pictographic-primitives/other/circle messages bubble_5f97107e-f15e-42cb-ae76-2769af6c5f64.svg'),)
PROFILE_SOURCE_KEYS = ('solo/circle-messages-bubble',)
SOLO_SOURCE_ICON_IDS = ('circle-messages-bubble',)
REFERENCE_EXPORT_SHA256 = 'e688e2475e4f07622b32ed03f9a56ccea952e8dc7464a55ed0d4c25bd1a5780d'

class DrawingVariant2(Sub32):
    icon_id = 'circle-messages-bubble-sub32-v2'
    related_origin_icon_id = 'circle-messages-bubble-sub32'
    variant_label = 'Repair 32px envelope'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives-generate'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        short_axis = 16
        short_half_span = 12
        short_low, short_high = (short_axis - short_half_span, short_axis + short_half_span)
        self.add_bezier('p1-r1-1', (2, 15), ((2, 10), (8, short_low), (16, short_low)))
        self.add_bezier('p1-r1-2', (16, short_low), ((24, short_low), (30, 10), (30, 15)))
        self.add_bezier('p1-r1-3', (30, 15), ((30, 21), (24, 26), (16, 26)))
        self.add_bezier('p1-r1-4', (16, 26), ((13, 26), (11, 25), (10, 24)))
        self.add_line('p1-r1-5', (10, 24), (3, short_high))
        self.add_line('p1-r1-6', (3, short_high), (6, 22))
        self.add_bezier('p1-r1-7', (6, 22), ((3, 20), (2, 18), (2, 15)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', closed=False)
