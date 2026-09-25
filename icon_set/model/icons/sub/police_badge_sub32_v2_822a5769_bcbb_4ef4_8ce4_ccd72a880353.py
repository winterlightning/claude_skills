# Repair: shared short-axis extrema retain the full source composition on the legal SUB32 envelope.
"""Independent 32px profile of police-badge.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '822a5769-bcbb-4ef4-8ce4-ccd72a880353'
SOURCE_PATH = 'pictographic-primitives/symbol/police badge_822a5769-bcbb-4ef4-8ce4-ccd72a880353.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('822a5769-bcbb-4ef4-8ce4-ccd72a880353', 'pictographic-primitives/symbol/police badge_822a5769-bcbb-4ef4-8ce4-ccd72a880353.svg'),)
PROFILE_SOURCE_KEYS = ('solo/police-badge',)
SOLO_SOURCE_ICON_IDS = ('police-badge',)
REFERENCE_EXPORT_SHA256 = '79a309493ff448944ee8402a5e6957126fbc8e8caedb861cebb1e880550d95b4'

class DrawingVariant2(Sub32):
    icon_id = 'police-badge-sub32-v2'
    variant_of = 'police-badge-sub32'
    variant_label = 'Repair 32px envelope'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        short_axis = 16
        short_half_span = 12
        (short_low, short_high) = (short_axis - short_half_span, short_axis + short_half_span)
        self.add_bezier('p1-r1-1', (short_low, 6), ((8, 3), (12, 2), (16, 2)))
        self.add_bezier('p1-r1-2', (16, 2), ((20, 2), (24, 3), (short_high, 6)))
        self.add_line('p1-r1-3', (short_high, 6), (short_high, 15))
        self.add_bezier('p1-r1-4', (short_high, 15), ((short_high, 23), (22, 28), (16, 30)))
        self.add_bezier('p1-r1-5', (16, 30), ((10, 28), (short_low, 23), (short_low, 15)))
        self.add_line('p1-r1-6', (short_low, 15), (short_low, 6))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_line('p2-r1-1', (16, 12), (16, 16))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
