# Repair: shared short-axis extrema retain the full source composition on the legal SUB32 envelope.
"""Independent 32px profile of cursor-left-horizontal.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'a19d3d8c-ca4f-4084-a880-3c773e5774a7'
SOURCE_PATH = 'pictographic-primitives/state/cursor left horizontal_a19d3d8c-ca4f-4084-a880-3c773e5774a7.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('a19d3d8c-ca4f-4084-a880-3c773e5774a7', 'pictographic-primitives/state/cursor left horizontal_a19d3d8c-ca4f-4084-a880-3c773e5774a7.svg'),)
PROFILE_SOURCE_KEYS = ('solo/cursor-left-horizontal',)
SOLO_SOURCE_ICON_IDS = ('cursor-left-horizontal',)
REFERENCE_EXPORT_SHA256 = '4255c657daa0a84c620723a902bf730d4c3625c815b9af27862404e1aac07a82'

class DrawingVariant2(Sub32):
    icon_id = 'cursor-left-horizontal-sub32-v2'
    variant_label = 'Repair 32px envelope'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Mirrored cursor outline; the notch is an intentional corner, not a spurious arc.
        self.add_line('edge-0',(2, 16),(30, 4))
        self.add_line('edge-1',(30, 4),(26, 16))
        self.add_line('edge-2',(26, 16),(30, 28))
        self.add_line('edge-3',(30, 28),(2, 16))
        self.add_contour('path-1-1','edge-0','edge-1','edge-2','edge-3',closed=True)
