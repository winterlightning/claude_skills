# Repair: shared short-axis extrema retain the full source composition on the legal SUB32 envelope.
"""Independent 32px profile of helmet-97a9265b.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '97a9265b-3cf4-420c-8a2b-da7cd9955c06'
SOURCE_PATH = 'pictographic-primitives/protection/helmet_97a9265b-3cf4-420c-8a2b-da7cd9955c06.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('97a9265b-3cf4-420c-8a2b-da7cd9955c06', 'pictographic-primitives/protection/helmet_97a9265b-3cf4-420c-8a2b-da7cd9955c06.svg'),)
PROFILE_SOURCE_KEYS = ('solo/helmet-97a9265b',)
SOLO_SOURCE_ICON_IDS = ('helmet-97a9265b',)
REFERENCE_EXPORT_SHA256 = '04c494d966925f7e4a9092b4ccb17e1b6ce5f838845333982014520fbea6a0c0'

class DrawingVariant2(Sub32):
    icon_id = 'helmet-97a9265b-sub32-v2'
    variant_label = 'Repair 32px envelope'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'protection'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        short_axis = 16
        short_half_span = 12
        (short_low, short_high) = (short_axis - short_half_span, short_axis + short_half_span)
        self.add_line('p1-r1-1', (2, short_high), (2, 20))
        self.add_arc('p1-r1-2', (2, 20), (16, 6), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (16, 6), (30, 20), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_line('p1-r1-4', (30, 20), (30, short_high))
        self.add_line('p1-r1-5', (30, short_high), (2, short_high))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_line('p2-r1-1', (16, short_low), (16, 6))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (16, 6), (16, 16))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p3-r1-1')
        self.relate('connect', 'p1-r1-3', 'p2-r1-1')
        self.relate('connect', 'p1-r1-3', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
