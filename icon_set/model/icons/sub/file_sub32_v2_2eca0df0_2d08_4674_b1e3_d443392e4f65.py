# Repair: shared short-axis extrema retain the full source composition on the legal SUB32 envelope.
"""Independent 32px profile of file.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '2eca0df0-2d08-4674-b1e3-d443392e4f65'
SOURCE_PATH = 'pictographic-primitives/emails/file_2eca0df0-2d08-4674-b1e3-d443392e4f65.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('2eca0df0-2d08-4674-b1e3-d443392e4f65', 'pictographic-primitives/emails/file_2eca0df0-2d08-4674-b1e3-d443392e4f65.svg'),)
PROFILE_SOURCE_KEYS = ('solo/file',)
SOLO_SOURCE_ICON_IDS = ('file',)
REFERENCE_EXPORT_SHA256 = '3b7710ac62c7e414ce5a4f147f85a78c1fffc5b361529d98d7cd2c1357ad93eb'

class DrawingVariant2(Sub32):
    icon_id = 'file-sub32-v2'
    variant_of = 'file-sub32'
    variant_label = 'Repair 32px envelope'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'emails'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        short_axis = 16
        short_half_span = 12
        (short_low, short_high) = (short_axis - short_half_span, short_axis + short_half_span)
        self.add_line('p1-r1-1', (short_low, 2), (22, 2))
        self.add_line('p1-r1-2', (22, 2), (26, 8))
        self.add_line('p1-r1-3', (26, 8), (short_high, 8))
        self.add_line('p1-r1-4', (short_high, 8), (short_high, 30))
        self.add_line('p1-r1-5', (short_high, 30), (short_low, 30))
        self.add_line('p1-r1-6', (short_low, 30), (short_low, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
