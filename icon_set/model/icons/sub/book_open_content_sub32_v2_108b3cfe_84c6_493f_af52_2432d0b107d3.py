# Repair: shared short-axis extrema retain the full source composition on the legal SUB32 envelope.
"""Independent 32px profile of book-open-content.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '108b3cfe-84c6-493f-af52-2432d0b107d3'
SOURCE_PATH = 'pictographic-primitives/content/book open_108b3cfe-84c6-493f-af52-2432d0b107d3.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('108b3cfe-84c6-493f-af52-2432d0b107d3', 'pictographic-primitives/content/book open_108b3cfe-84c6-493f-af52-2432d0b107d3.svg'), ('710c81fd-6fdd-45a1-b7ed-cc8825ddf0d9', 'pictographic-primitives/content/book open_710c81fd-6fdd-45a1-b7ed-cc8825ddf0d9.svg'))
PROFILE_SOURCE_KEYS = ('solo/book-open-content', 'solo/book-open-710c81fd')
SOLO_SOURCE_ICON_IDS = ('book-open-content', 'book-open-710c81fd')
REFERENCE_EXPORT_SHA256 = '77c6dc5b8bab4d8f30757792fff10e69dd92fce16df28f325d55ae7fd293fd4b'

class DrawingVariant2(Sub32):
    icon_id = 'book-open-content-sub32-v2'
    variant_of = 'book-open-content-sub32'
    variant_label = 'Repair 32px envelope'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'content'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        short_axis = 16
        short_half_span = 12
        (short_low, short_high) = (short_axis - short_half_span, short_axis + short_half_span)
        self.add_line('p1-r1-1', (2, short_low), (16, 8))
        self.add_line('p1-r1-2', (16, 8), (30, short_low))
        self.add_line('p1-r1-3', (30, short_low), (30, 24))
        self.add_line('p1-r1-4', (30, 24), (16, short_high))
        self.add_line('p1-r1-5', (16, short_high), (2, 24))
        self.add_line('p1-r1-6', (2, 24), (2, short_low))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_line('p2-r1-1', (16, 8), (16, short_high))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (8, 15), (10, 16))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (22, 16), (24, 15))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-4', 'p2-r1-1')
        self.relate('connect', 'p1-r1-5', 'p2-r1-1')
