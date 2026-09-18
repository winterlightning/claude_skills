# Repair: shared short-axis extrema retain the full source composition on the legal SUB32 envelope.
"""Independent 32px profile of right-arrow.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '00490efd-9861-4d7c-ac36-6c42f80772ec'
SOURCE_PATH = 'pictographic-primitives/transportation/right arrow_00490efd-9861-4d7c-ac36-6c42f80772ec.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('00490efd-9861-4d7c-ac36-6c42f80772ec', 'pictographic-primitives/transportation/right arrow_00490efd-9861-4d7c-ac36-6c42f80772ec.svg'),)
PROFILE_SOURCE_KEYS = ('solo/right-arrow',)
SOLO_SOURCE_ICON_IDS = ('right-arrow',)
REFERENCE_EXPORT_SHA256 = '494e522ff7d2595ff653da6fb5afd9ba1ccaed436aaa2f8b265fbcdd73758533'

class DrawingVariant2(Sub32):
    icon_id = 'right-arrow-sub32-v2'
    variant_of = 'right-arrow-sub32'
    variant_label = 'Repair 32px envelope'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'transportation'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        short_axis = 16
        short_half_span = 12
        (short_low, short_high) = (short_axis - short_half_span, short_axis + short_half_span)
        self.add_line('p1-r1-1', (2, 11), (2, 21))
        self.add_line('p1-r1-2', (2, 21), (18, 21))
        self.add_line('p1-r1-3', (18, 21), (18, short_high))
        self.add_line('p1-r1-4', (18, short_high), (30, 16))
        self.add_line('p1-r1-5', (30, 16), (18, short_low))
        self.add_line('p1-r1-6', (18, short_low), (18, 11))
        self.add_line('p1-r1-7', (18, 11), (2, 11))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', closed=False)
