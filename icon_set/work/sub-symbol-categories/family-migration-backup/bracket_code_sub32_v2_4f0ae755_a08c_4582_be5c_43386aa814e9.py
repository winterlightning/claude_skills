# Repair: shared short-axis extrema retain the full source composition on the legal SUB32 envelope.
"""Independent 32px profile of bracket-code.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '4f0ae755-a08c-4582-be5c-43386aa814e9'
SOURCE_PATH = 'pictographic-primitives/symbol/bracket code_4f0ae755-a08c-4582-be5c-43386aa814e9.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('4f0ae755-a08c-4582-be5c-43386aa814e9', 'pictographic-primitives/symbol/bracket code_4f0ae755-a08c-4582-be5c-43386aa814e9.svg'),)
PROFILE_SOURCE_KEYS = ('solo/bracket-code',)
SOLO_SOURCE_ICON_IDS = ('bracket-code',)
REFERENCE_EXPORT_SHA256 = '38561f4b731b4faec54d3b9621fdfc86a49413c66637a004c80256c9e4529cc9'

class DrawingVariant2(Sub32):
    icon_id = 'bracket-code-sub32-v2'
    variant_of = 'bracket-code-sub32'
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
        self.add_bezier('p1-r1-1', (10, short_low), ((3, short_low), (7, 13), (2, 16)))
        self.add_bezier('p1-r1-2', (2, 16), ((7, 19), (3, short_high), (10, short_high)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_bezier('p2-r1-1', (22, short_low), ((29, short_low), (25, 13), (30, 16)))
        self.add_bezier('p2-r1-2', (30, 16), ((25, 19), (29, short_high), (22, short_high)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
