# Variant of pine-symbol-sub32-v2; parent file remains unchanged.
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

class DrawingVariant3(Sub32):
    icon_id = 'pine-symbol-sub32-v3'
    variant_of = 'pine-symbol-sub32-v2'
    variant_label = 'Redraw proportions and source features'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Straight sloping pine branches and paired shoulders; remove the inward-bowed trunk-like sides.
        self.add_polyline('branches',(16,2),(9,12),(13,12),(6,24),(26,24),(19,12),(23,12),closed=True)
        self.add_line('trunk',(16,24),(16,30));self.relate('connect','trunk','branches-4')
