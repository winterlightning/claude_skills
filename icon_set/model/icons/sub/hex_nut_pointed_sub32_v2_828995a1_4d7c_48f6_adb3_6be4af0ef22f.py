# Repair: shared short-axis extrema retain the full source composition on the legal SUB32 envelope.
"""Independent 32px profile of hex-nut-pointed.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '828995a1-4d7c-48f6-adb3-6be4af0ef22f'
SOURCE_PATH = 'pictographic-primitives/symbol/nut_828995a1-4d7c-48f6-adb3-6be4af0ef22f.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('828995a1-4d7c-48f6-adb3-6be4af0ef22f', 'pictographic-primitives/symbol/nut_828995a1-4d7c-48f6-adb3-6be4af0ef22f.svg'),)
PROFILE_SOURCE_KEYS = ('solo/hex-nut-pointed',)
SOLO_SOURCE_ICON_IDS = ('hex-nut-pointed',)
REFERENCE_EXPORT_SHA256 = '714a5e94343ceac986c7d3aa80a34a1afd7a80bd43ed3ab05ee53d84a1faadb3'

class DrawingVariant2(Sub32):
    icon_id = 'hex-nut-pointed-sub32-v2'
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
        self.add_line('p1-r1-1', (16, 2), (short_high, 9))
        self.add_line('p1-r1-2', (short_high, 9), (short_high, 23))
        self.add_line('p1-r1-3', (short_high, 23), (16, 30))
        self.add_line('p1-r1-4', (16, 30), (short_low, 23))
        self.add_line('p1-r1-5', (short_low, 23), (short_low, 9))
        self.add_line('p1-r1-6', (short_low, 9), (16, 2))
        self.add_line('p1-r1-7', (16, 2), (16, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', closed=False)
        self.add_arc('p2-r1-1', (11, 16), (21, 16), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('p2-r1-2', (21, 16), (11, 16), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
