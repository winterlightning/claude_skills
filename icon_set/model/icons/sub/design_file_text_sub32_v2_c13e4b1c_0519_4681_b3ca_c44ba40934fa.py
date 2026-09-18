# Repair: shared short-axis extrema retain the full source composition on the legal SUB32 envelope.
"""Independent 32px profile of design-file-text.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'c13e4b1c-0519-4681-b3ca-c44ba40934fa'
SOURCE_PATH = 'pictographic-primitives/tools/design file text_c13e4b1c-0519-4681-b3ca-c44ba40934fa.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('c13e4b1c-0519-4681-b3ca-c44ba40934fa', 'pictographic-primitives/tools/design file text_c13e4b1c-0519-4681-b3ca-c44ba40934fa.svg'),)
PROFILE_SOURCE_KEYS = ('solo/design-file-text',)
SOLO_SOURCE_ICON_IDS = ('design-file-text',)
REFERENCE_EXPORT_SHA256 = '86890b5881117e6262a25912263e13f458b3ad05034d5c75e3ae88315bb4b2b0'

class DrawingVariant2(Sub32):
    icon_id = 'design-file-text-sub32-v2'
    variant_of = 'design-file-text-sub32'
    variant_label = 'Repair 32px envelope'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'tools'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        short_axis = 16
        short_half_span = 12
        (short_low, short_high) = (short_axis - short_half_span, short_axis + short_half_span)
        self.add_line('p1-r1-1', (short_low, 6), (short_low, 2))
        self.add_line('p1-r1-2', (short_low, 2), (short_high, 2))
        self.add_line('p1-r1-3', (short_high, 2), (short_high, 6))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (16, 30), (16, 2))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (12, 30), (20, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
