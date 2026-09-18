# Repair: shared short-axis extrema retain the full source composition on the legal SUB32 envelope.
"""Independent 32px profile of check-interface-essential.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'e3edb211-f9b6-4e4c-8769-db85e43e229f'
SOURCE_PATH = 'pictographic-primitives/interface-essential/check_e3edb211-f9b6-4e4c-8769-db85e43e229f.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('e3edb211-f9b6-4e4c-8769-db85e43e229f', 'pictographic-primitives/interface-essential/check_e3edb211-f9b6-4e4c-8769-db85e43e229f.svg'),)
PROFILE_SOURCE_KEYS = ('solo/check-interface-essential',)
SOLO_SOURCE_ICON_IDS = ('check-interface-essential',)
REFERENCE_EXPORT_SHA256 = '281e56f7b26a5e3a8097c192b0cfab91d74cc716d605ac4caf2df3065cab8fe5'

class DrawingVariant2(Sub32):
    icon_id = 'check-interface-essential-sub32-v2'
    variant_of = 'check-interface-essential-sub32'
    variant_label = 'Repair 32px envelope'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        short_axis = 16
        short_half_span = 12
        (short_low, short_high) = (short_axis - short_half_span, short_axis + short_half_span)
        self.add_line('p1-r1-1', (30, short_low), (13, short_high))
        self.add_line('p1-r1-2', (13, short_high), (2, 16))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
