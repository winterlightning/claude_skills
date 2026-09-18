# Repair: shared short-axis extrema retain the full source composition on the legal SUB32 envelope.
"""Independent 32px profile of flame-59aa3cfd.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '59aa3cfd-2acc-46bd-93c4-3b4a7c6f64b1'
SOURCE_PATH = 'pictographic-primitives/products/flame_59aa3cfd-2acc-46bd-93c4-3b4a7c6f64b1.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('59aa3cfd-2acc-46bd-93c4-3b4a7c6f64b1', 'pictographic-primitives/products/flame_59aa3cfd-2acc-46bd-93c4-3b4a7c6f64b1.svg'),)
PROFILE_SOURCE_KEYS = ('solo/flame-59aa3cfd',)
SOLO_SOURCE_ICON_IDS = ('flame-59aa3cfd',)
REFERENCE_EXPORT_SHA256 = '3218057023c3d16ce533700b62b7417f15ec19faf503dfe7dca76fa4623d8b28'

class DrawingVariant2(Sub32):
    icon_id = 'flame-59aa3cfd-sub32-v2'
    variant_of = 'flame-59aa3cfd-sub32'
    variant_label = 'Repair 32px envelope'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'products'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        short_axis = 16
        short_half_span = 12
        (short_low, short_high) = (short_axis - short_half_span, short_axis + short_half_span)
        self.add_bezier('p1-r1-1', (16, 2), ((16, 10), (short_high, 12), (short_high, 20)))
        self.add_bezier('p1-r1-2', (short_high, 20), ((short_high, 26), (22, 30), (16, 30)))
        self.add_bezier('p1-r1-3', (16, 30), ((10, 30), (short_low, 26), (short_low, 20)))
        self.add_bezier('p1-r1-4', (short_low, 20), ((short_low, 12), (16, 10), (16, 2)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
