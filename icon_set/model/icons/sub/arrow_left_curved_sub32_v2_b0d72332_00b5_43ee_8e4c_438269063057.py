# Repair: shared short-axis extrema retain the full source composition on the legal SUB32 envelope.
"""Independent 32px profile of arrow-left-curved.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'b0d72332-00b5-43ee-8e4c-438269063057'
SOURCE_PATH = 'pictographic-primitives/symbol/arrow left curved_b0d72332-00b5-43ee-8e4c-438269063057.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('b0d72332-00b5-43ee-8e4c-438269063057', 'pictographic-primitives/symbol/arrow left curved_b0d72332-00b5-43ee-8e4c-438269063057.svg'),)
PROFILE_SOURCE_KEYS = ('solo/arrow-left-curved',)
SOLO_SOURCE_ICON_IDS = ('arrow-left-curved',)
REFERENCE_EXPORT_SHA256 = '62d3063c4a98f4a9e29337c677e42e878b8f1ae3cd8a911517eff1a9eaf67583'

class DrawingVariant2(Sub32):
    icon_id = 'arrow-left-curved-sub32-v2'
    variant_of = 'arrow-left-curved-sub32'
    variant_label = 'Repair 32px envelope'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbols/standalone'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        short_axis = 16
        short_half_span = 12
        (short_low, short_high) = (short_axis - short_half_span, short_axis + short_half_span)
        self.add_line('p1-r1-1', (12, short_low), (2, 15))
        self.add_line('p1-r1-2', (2, 15), (12, 24))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (2, 15), (17, 15))
        self.add_arc('p2-r1-2', (17, 15), (30, short_high), radius_x=13, radius_y=13, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
