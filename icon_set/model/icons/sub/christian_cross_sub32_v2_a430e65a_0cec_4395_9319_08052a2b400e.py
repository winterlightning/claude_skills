# Repair: shared short-axis extrema retain the full source composition on the legal SUB32 envelope.
"""Independent 32px profile of christian-cross.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'a430e65a-0cec-4395-9319-08052a2b400e'
SOURCE_PATH = 'pictographic-primitives/symbol/christian cross_a430e65a-0cec-4395-9319-08052a2b400e.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('a430e65a-0cec-4395-9319-08052a2b400e', 'pictographic-primitives/symbol/christian cross_a430e65a-0cec-4395-9319-08052a2b400e.svg'),)
PROFILE_SOURCE_KEYS = ('solo/christian-cross',)
SOLO_SOURCE_ICON_IDS = ('christian-cross',)
REFERENCE_EXPORT_SHA256 = '3349d8466bfedff457b6eedef8358c7bda1836b9c909c78d378e036486cf3a57'

class DrawingVariant2(Sub32):
    icon_id = 'christian-cross-sub32-v2'
    variant_of = 'christian-cross-sub32'
    variant_label = 'Repair 32px envelope'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        short_axis = 16
        short_half_span = 12
        (short_low, short_high) = (short_axis - short_half_span, short_axis + short_half_span)
        self.add_line('p1-r1-1', (16, 2), (16, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (short_low, 12), (short_high, 12))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
