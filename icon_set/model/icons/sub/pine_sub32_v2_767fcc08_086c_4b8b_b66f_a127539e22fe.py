# Repair: shared short-axis extrema retain the full source composition on the legal SUB32 envelope.
"""Independent 32px profile of pine.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '767fcc08-086c-4b8b-b66f-a127539e22fe'
SOURCE_PATH = 'pictographic-primitives/symbol/pine_767fcc08-086c-4b8b-b66f-a127539e22fe.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('767fcc08-086c-4b8b-b66f-a127539e22fe', 'pictographic-primitives/symbol/pine_767fcc08-086c-4b8b-b66f-a127539e22fe.svg'),)
PROFILE_SOURCE_KEYS = ('solo/pine',)
SOLO_SOURCE_ICON_IDS = ('pine',)
REFERENCE_EXPORT_SHA256 = '0ffc2defca9e0efc479b8fcb429eb7912108500290dd9fbbc7f56cca7114b531'

class DrawingVariant2(Sub32):
    icon_id = 'pine-sub32-v2'
    variant_of = 'pine-sub32'
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
        self.add_line('p1-r1-1', (16, 17), (16, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (16, 2), (short_low, 22))
        self.add_line('p2-r1-2', (short_low, 22), (short_high, 22))
        self.add_line('p2-r1-3', (short_high, 22), (16, 2))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
