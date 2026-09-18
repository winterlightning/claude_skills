"""Independent 32px profile of return-arrow.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'ebf78b1f-7ce3-41f6-9566-d46bf42b53ff'
SOURCE_PATH = 'pictographic-primitives/symbol/return arrow_ebf78b1f-7ce3-41f6-9566-d46bf42b53ff.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('ebf78b1f-7ce3-41f6-9566-d46bf42b53ff', 'pictographic-primitives/symbol/return arrow_ebf78b1f-7ce3-41f6-9566-d46bf42b53ff.svg'),)
PROFILE_SOURCE_KEYS = ('solo/return-arrow',)
SOLO_SOURCE_ICON_IDS = ('return-arrow',)
REFERENCE_EXPORT_SHA256 = '07735889441cedddcdfc51dec0bced501a640b0c343196a2945f11e25cfa4b5b'

class DrawingVariant2(Sub32):
    icon_id = 'return-arrow-sub32-v2'
    related_origin_icon_id = 'return-arrow-sub32'
    variant_label = 'Repair 32px envelope'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        short_axis = 16
        short_half_span = 12
        short_low, short_high = (short_axis - short_half_span, short_axis + short_half_span)
        self.add_line('p1-r1-1', (30, 7), (30, 12))
        self.add_arc('p1-r1-2', (30, 12), (26, 16), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (26, 16), (2, 16))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (12, short_low), (2, 16))
        self.add_line('p2-r1-2', (2, 16), (12, short_high))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.relate('connect', 'p1-r1-3', 'p2-r1-1')
        self.relate('connect', 'p1-r1-3', 'p2-r1-2')
