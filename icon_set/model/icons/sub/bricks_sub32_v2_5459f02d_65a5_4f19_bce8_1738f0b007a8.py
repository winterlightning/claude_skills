# Repair: shared short-axis extrema retain the full source composition on the legal SUB32 envelope.
"""Independent 32px profile of bricks.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '5459f02d-65a5-4f19-bce8-1738f0b007a8'
SOURCE_PATH = 'pictographic-primitives/symbol/bricks_5459f02d-65a5-4f19-bce8-1738f0b007a8.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('5459f02d-65a5-4f19-bce8-1738f0b007a8', 'pictographic-primitives/symbol/bricks_5459f02d-65a5-4f19-bce8-1738f0b007a8.svg'),)
PROFILE_SOURCE_KEYS = ('solo/bricks',)
SOLO_SOURCE_ICON_IDS = ('bricks',)
REFERENCE_EXPORT_SHA256 = 'd7af8b7820f94956a689bbe59a0130c164469de5c181717d45a77a0e6a7f2d1a'

class DrawingVariant2(Sub32):
    icon_id = 'bricks-sub32-v2'
    variant_of = 'bricks-sub32'
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
        self.add_line('p1-r1-1', (2, short_low), (12, short_low))
        self.add_line('p1-r1-2', (12, short_low), (30, short_low))
        self.add_line('p1-r1-3', (30, short_low), (30, 16))
        self.add_line('p1-r1-4', (30, 16), (30, short_high))
        self.add_line('p1-r1-5', (30, short_high), (20, short_high))
        self.add_line('p1-r1-6', (20, short_high), (2, short_high))
        self.add_line('p1-r1-7', (2, short_high), (2, 16))
        self.add_line('p1-r1-8', (2, 16), (2, short_low))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_line('p2-r1-1', (2, 16), (12, 16))
        self.add_line('p2-r1-2', (12, 16), (20, 16))
        self.add_line('p2-r1-3', (20, 16), (30, 16))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_line('p3-r1-1', (12, short_low), (12, 16))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (20, 16), (20, short_high))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p3-r1-1')
        self.relate('connect', 'p1-r1-2', 'p3-r1-1')
        self.relate('connect', 'p1-r1-3', 'p2-r1-3')
        self.relate('connect', 'p1-r1-4', 'p2-r1-3')
        self.relate('connect', 'p1-r1-5', 'p4-r1-1')
        self.relate('connect', 'p1-r1-6', 'p4-r1-1')
        self.relate('connect', 'p1-r1-7', 'p2-r1-1')
        self.relate('connect', 'p1-r1-8', 'p2-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-2', 'p3-r1-1')
        self.relate('connect', 'p2-r1-2', 'p4-r1-1')
        self.relate('connect', 'p2-r1-3', 'p4-r1-1')
