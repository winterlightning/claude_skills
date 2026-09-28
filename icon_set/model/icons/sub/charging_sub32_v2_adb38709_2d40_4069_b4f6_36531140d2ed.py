# Repair: shared short-axis extrema retain the full source composition on the legal SUB32 envelope.
"""Independent 32px profile of charging.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'adb38709-2d40-4069-b4f6-36531140d2ed'
SOURCE_PATH = 'pictographic-primitives/symbol/charging_adb38709-2d40-4069-b4f6-36531140d2ed.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('adb38709-2d40-4069-b4f6-36531140d2ed', 'pictographic-primitives/symbol/charging_adb38709-2d40-4069-b4f6-36531140d2ed.svg'),)
PROFILE_SOURCE_KEYS = ('solo/charging',)
SOLO_SOURCE_ICON_IDS = ('charging',)
REFERENCE_EXPORT_SHA256 = 'a7bd1ee6fc8cb1c0a8387f9b89e6454b88879a5c6388a71e92a03132fcc17261'

class DrawingVariant2(Sub32):
    icon_id = 'charging-sub32-v2'
    variant_label = 'Repair 32px envelope'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        short_axis = 16
        short_half_span = 12
        (short_low, short_high) = (short_axis - short_half_span, short_axis + short_half_span)
        self.add_line('p1-r1-1', (short_low, 18), (short_low, 26))
        self.add_arc('p1-r1-2', (short_low, 26), (8, 30), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('p1-r1-3', (8, 30), (24, 30))
        self.add_arc('p1-r1-4', (24, 30), (short_high, 26), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('p1-r1-5', (short_high, 26), (short_high, 18))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_line('p2-r1-1', (short_low, 18), (short_high, 18))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (short_low, 18), (short_low, 8))
        self.add_arc('p3-r1-2', (short_low, 8), (6, 6), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p3-r1-3', (6, 6), (12, 6))
        self.add_line('p3-r1-4', (12, 6), (12, 2))
        self.add_line('p3-r1-5', (12, 2), (20, 2))
        self.add_line('p3-r1-6', (20, 2), (20, 6))
        self.add_line('p3-r1-7', (20, 6), (26, 6))
        self.add_arc('p3-r1-9', (26, 6), (short_high, 8), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p3-r1-8', (short_high, 8), (short_high, 18))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', 'p3-r1-6', 'p3-r1-7', 'p3-r1-9', 'p3-r1-8', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p3-r1-1')
        self.relate('connect', 'p1-r1-5', 'p2-r1-1')
        self.relate('connect', 'p1-r1-5', 'p3-r1-8')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-8')
