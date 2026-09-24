# Repair: shared short-axis extrema retain the full source composition on the legal SUB32 envelope.
"""Independent 32px profile of hard-hat-on-stand-2c1fa7b6.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '2c1fa7b6-a8c3-4407-9935-862250d036d1'
SOURCE_PATH = 'pictographic-primitives/protection/helmet_2c1fa7b6-a8c3-4407-9935-862250d036d1.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('2c1fa7b6-a8c3-4407-9935-862250d036d1', 'pictographic-primitives/protection/helmet_2c1fa7b6-a8c3-4407-9935-862250d036d1.svg'),)
PROFILE_SOURCE_KEYS = ('solo/hard-hat-on-stand-2c1fa7b6',)
SOLO_SOURCE_ICON_IDS = ('hard-hat-on-stand-2c1fa7b6',)
REFERENCE_EXPORT_SHA256 = '12f446f680d96f9ac87f65cc989236605efa365c44c8f0ebc558e2fa3101c561'

class DrawingVariant2(Sub32):
    icon_id = 'hard-hat-on-stand-2c1fa7b6-sub32-v2'
    variant_label = 'Repair 32px envelope'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/protection'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        short_axis = 16
        short_half_span = 12
        (short_low, short_high) = (short_axis - short_half_span, short_axis + short_half_span)
        self.add_arc('p1-r1-1', (5, 16), (16, short_low), radius_x=11, radius_y=12, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (16, short_low), (27, 16), radius_x=11, radius_y=12, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (2, 16), (5, 16))
        self.add_line('p2-r1-2', (5, 16), (16, 16))
        self.add_line('p2-r1-3', (16, 16), (27, 16))
        self.add_line('p2-r1-4', (27, 16), (30, 16))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_line('p3-r1-1', (16, short_low), (16, 10))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (16, 16), (16, short_high))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (9, short_high), (16, short_high))
        self.add_line('p5-r1-2', (16, short_high), (23, short_high))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p2-r1-2')
        self.relate('connect', 'p1-r1-1', 'p3-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-3')
        self.relate('connect', 'p1-r1-2', 'p2-r1-4')
        self.relate('connect', 'p1-r1-2', 'p3-r1-1')
        self.relate('connect', 'p2-r1-2', 'p4-r1-1')
        self.relate('connect', 'p2-r1-3', 'p4-r1-1')
        self.relate('connect', 'p4-r1-1', 'p5-r1-1')
        self.relate('connect', 'p4-r1-1', 'p5-r1-2')
