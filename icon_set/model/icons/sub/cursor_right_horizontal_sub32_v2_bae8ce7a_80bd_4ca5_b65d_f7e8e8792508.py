# Repair: shared short-axis extrema retain the full source composition on the legal SUB32 envelope.
"""Independent 32px profile of cursor-right-horizontal.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'bae8ce7a-80bd-4ca5-b65d-f7e8e8792508'
SOURCE_PATH = 'pictographic-primitives/state/cursor right horizontal_bae8ce7a-80bd-4ca5-b65d-f7e8e8792508.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('bae8ce7a-80bd-4ca5-b65d-f7e8e8792508', 'pictographic-primitives/state/cursor right horizontal_bae8ce7a-80bd-4ca5-b65d-f7e8e8792508.svg'),)
PROFILE_SOURCE_KEYS = ('solo/cursor-right-horizontal',)
SOLO_SOURCE_ICON_IDS = ('cursor-right-horizontal',)
REFERENCE_EXPORT_SHA256 = '3eb2ff3240f7b4f6bd34dc943255f3e9dfe6f737dcbd507db8752f7e117b78a4'

class DrawingVariant2(Sub32):
    icon_id = 'cursor-right-horizontal-sub32-v2'
    variant_of = 'cursor-right-horizontal-sub32'
    variant_label = 'Repair 32px envelope'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Mirrored cursor outline; the notch is an intentional corner, not a spurious arc.
        self.add_line('edge-0',(30, 16),(2, 4))
        self.add_line('edge-1',(2, 4),(6, 16))
        self.add_line('edge-2',(6, 16),(2, 28))
        self.add_line('edge-3',(2, 28),(30, 16))
        self.add_contour('path-1-1','edge-0','edge-1','edge-2','edge-3',closed=True)
