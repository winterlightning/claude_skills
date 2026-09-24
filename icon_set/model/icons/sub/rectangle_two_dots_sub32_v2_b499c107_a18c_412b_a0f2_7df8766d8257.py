# Repair: shared short-axis extrema retain the full source composition on the legal SUB32 envelope.
"""Independent 32px profile of rectangle-two-dots.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'b499c107-a18c-412b-a0f2-7df8766d8257'
SOURCE_PATH = 'pictographic-primitives/state/rectangle two dots_b499c107-a18c-412b-a0f2-7df8766d8257.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('b499c107-a18c-412b-a0f2-7df8766d8257', 'pictographic-primitives/state/rectangle two dots_b499c107-a18c-412b-a0f2-7df8766d8257.svg'),)
PROFILE_SOURCE_KEYS = ('solo/rectangle-two-dots',)
SOLO_SOURCE_ICON_IDS = ('rectangle-two-dots',)
REFERENCE_EXPORT_SHA256 = '2c7636d3ef9d193664f845cbb32204d9b75605a28e17bd34ee7683e4c74bdb0b'

class DrawingVariant2(Sub32):
    icon_id = 'rectangle-two-dots-sub32-v2'
    variant_label = 'Repair 32px envelope'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        short_axis = 16
        short_half_span = 12
        (short_low, short_high) = (short_axis - short_half_span, short_axis + short_half_span)
        self.add_line('p1-r1-1', (8, 2), (20, 2))
        self.add_line('p1-r1-2', (20, 2), (24, 2))
        self.add_arc('p1-r1-3', (24, 2), (short_high, 5), radius_x=4, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-4', (short_high, 5), (short_high, 16))
        self.add_line('p1-r1-5', (short_high, 16), (short_high, 27))
        self.add_arc('p1-r1-6', (short_high, 27), (24, 30), radius_x=4, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-7', (24, 30), (20, 30))
        self.add_line('p1-r1-8', (20, 30), (8, 30))
        self.add_arc('p1-r1-9', (8, 30), (short_low, 27), radius_x=4, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-10', (short_low, 27), (short_low, 16))
        self.add_line('p1-r1-11', (short_low, 16), (short_low, 5))
        self.add_arc('p1-r1-12', (short_low, 5), (8, 2), radius_x=4, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', closed=False)
        self.add_line('p2-r1-1', (16, 10), (16, 10))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (16, 22), (16, 22))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
