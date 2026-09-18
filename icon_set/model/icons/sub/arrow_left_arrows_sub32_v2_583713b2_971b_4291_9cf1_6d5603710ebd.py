# Repair: shared short-axis extrema retain the full source composition on the legal SUB32 envelope.
"""Independent 32px profile of arrow-left-arrows.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '583713b2-971b-4291-9cf1-6d5603710ebd'
SOURCE_PATH = 'pictographic-primitives/arrows/arrow left_583713b2-971b-4291-9cf1-6d5603710ebd.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('583713b2-971b-4291-9cf1-6d5603710ebd', 'pictographic-primitives/arrows/arrow left_583713b2-971b-4291-9cf1-6d5603710ebd.svg'),)
PROFILE_SOURCE_KEYS = ('solo/arrow-left-arrows',)
SOLO_SOURCE_ICON_IDS = ('arrow-left-arrows',)
REFERENCE_EXPORT_SHA256 = 'bdcf96afa24dff1ec1123c7b406523d2ee0fd9212f77c81ce40c94698cc9d38c'

class DrawingVariant2(Sub32):
    icon_id = 'arrow-left-arrows-sub32-v2'
    variant_of = 'arrow-left-arrows-sub32'
    variant_label = 'Repair 32px envelope'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'arrows'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        short_axis = 16
        short_half_span = 12
        (short_low, short_high) = (short_axis - short_half_span, short_axis + short_half_span)
        self.add_line('p1-r1-1', (2, 16), (10, short_high))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (2, 16), (10, short_low))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (2, 16), (30, 16))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
