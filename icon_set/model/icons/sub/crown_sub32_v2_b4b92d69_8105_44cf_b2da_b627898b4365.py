# Repair: shared short-axis extrema retain the full source composition on the legal SUB32 envelope.
"""Independent 32px profile of crown.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'b4b92d69-8105-44cf-b2da-b627898b4365'
SOURCE_PATH = 'pictographic-primitives/symbol/crown_b4b92d69-8105-44cf-b2da-b627898b4365.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('b4b92d69-8105-44cf-b2da-b627898b4365', 'pictographic-primitives/symbol/crown_b4b92d69-8105-44cf-b2da-b627898b4365.svg'),)
PROFILE_SOURCE_KEYS = ('solo/crown',)
SOLO_SOURCE_ICON_IDS = ('crown',)
REFERENCE_EXPORT_SHA256 = '3c694a13eedd26df1abf44210f5000490b4acd9fff374ca167fc98bf5d0fa0b2'

class DrawingVariant2(Sub32):
    icon_id = 'crown-sub32-v2'
    variant_of = 'crown-sub32'
    variant_label = 'Repair 32px envelope'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        short_axis = 16
        short_half_span = 12
        (short_low, short_high) = (short_axis - short_half_span, short_axis + short_half_span)
        self.add_line('p1-r1-1', (2, 8), (10, 15))
        self.add_line('p1-r1-2', (10, 15), (16, short_low))
        self.add_line('p1-r1-3', (16, short_low), (22, 15))
        self.add_line('p1-r1-4', (22, 15), (30, 8))
        self.add_line('p1-r1-5', (30, 8), (28, short_high))
        self.add_line('p1-r1-6', (28, short_high), (4, short_high))
        self.add_line('p1-r1-7', (4, short_high), (2, 8))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', closed=False)
