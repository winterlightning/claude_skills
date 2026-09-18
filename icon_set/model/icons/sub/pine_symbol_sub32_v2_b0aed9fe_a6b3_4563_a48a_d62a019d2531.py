# Repair: shared short-axis extrema retain the full source composition on the legal SUB32 envelope.
"""Independent 32px profile of pine-symbol.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'b0aed9fe-a6b3-4563-a48a-d62a019d2531'
SOURCE_PATH = 'pictographic-primitives/symbol/pine_b0aed9fe-a6b3-4563-a48a-d62a019d2531.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('b0aed9fe-a6b3-4563-a48a-d62a019d2531', 'pictographic-primitives/symbol/pine_b0aed9fe-a6b3-4563-a48a-d62a019d2531.svg'), ('f98a2e8b-5ad3-4faa-93ec-ec561d2f996b', 'pictographic-primitives/symbol/pine_f98a2e8b-5ad3-4faa-93ec-ec561d2f996b.svg'))
PROFILE_SOURCE_KEYS = ('solo/pine-symbol', 'solo/pine-f98a2e8b')
SOLO_SOURCE_ICON_IDS = ('pine-symbol', 'pine-f98a2e8b')
REFERENCE_EXPORT_SHA256 = '746c6de1f8be97b9810f9d07fdd8faa4a5977bd8a13de4603e35417e73b71eaa'

class DrawingVariant2(Sub32):
    icon_id = 'pine-symbol-sub32-v2'
    variant_of = 'pine-symbol-sub32'
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
        self.add_line('p1-r1-1', (16, 2), (24, 12))
        self.add_line('p1-r1-2', (24, 12), (20, 12))
        self.add_bezier('p1-r1-3', (20, 12), ((20, 18), (24, 23), (short_high, 26)))
        self.add_line('p1-r1-4', (short_high, 26), (16, 26))
        self.add_line('p1-r1-5', (16, 26), (short_low, 26))
        self.add_bezier('p1-r1-6', (short_low, 26), ((8, 23), (12, 18), (12, 12)))
        self.add_line('p1-r1-7', (12, 12), (8, 12))
        self.add_line('p1-r1-8', (8, 12), (16, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_line('p2-r1-1', (16, 26), (16, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.relate('connect', 'p1-r1-4', 'p2-r1-1')
        self.relate('connect', 'p1-r1-5', 'p2-r1-1')
