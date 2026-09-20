# Repair: shared short-axis extrema retain the full source composition on the legal SUB32 envelope.
"""Independent 32px profile of play-button-symbol.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'b593497e-6dda-4831-9cc0-f15dcd54f48c'
SOURCE_PATH = 'pictographic-primitives/symbol/play button_b593497e-6dda-4831-9cc0-f15dcd54f48c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('b593497e-6dda-4831-9cc0-f15dcd54f48c', 'pictographic-primitives/symbol/play button_b593497e-6dda-4831-9cc0-f15dcd54f48c.svg'),)
PROFILE_SOURCE_KEYS = ('solo/play-button-symbol',)
SOLO_SOURCE_ICON_IDS = ('play-button-symbol',)
REFERENCE_EXPORT_SHA256 = 'c96d0f111f9ebd88410f8787ac0c141263d9a1dcf6a44a0e3ce9d025ed3c054b'

class DrawingVariant2(Sub32):
    icon_id = 'play-button-symbol-sub32-v2'
    variant_of = 'play-button-symbol-sub32'
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
        self.add_line('p1-r1-1', (short_high, 16), (short_low, 2))
        self.add_line('p1-r1-2', (short_low, 2), (short_low, 30))
        self.add_line('p1-r1-3', (short_low, 30), (short_high, 16))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
