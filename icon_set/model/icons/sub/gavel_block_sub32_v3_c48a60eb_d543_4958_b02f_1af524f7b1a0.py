# Variant of gavel-block-sub32-v2; parent file remains unchanged.
"""Independent 32px profile of gavel-block.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'c48a60eb-d543-4958-b02f-1af524f7b1a0'
SOURCE_PATH = 'pictographic-primitives/state/gavel block_c48a60eb-d543-4958-b02f-1af524f7b1a0.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('c48a60eb-d543-4958-b02f-1af524f7b1a0', 'pictographic-primitives/state/gavel block_c48a60eb-d543-4958-b02f-1af524f7b1a0.svg'),)
PROFILE_SOURCE_KEYS = ('solo/gavel-block',)
SOLO_SOURCE_ICON_IDS = ('gavel-block',)
REFERENCE_EXPORT_SHA256 = '0851de1ce8150de5219a856397da403d2043c3417ce49fc05e222e3f7950695b'

class DrawingVariant3(Sub32):
    icon_id = 'gavel-block-sub32-v3'
    variant_of = 'gavel-block-sub32'
    variant_label = 'Redraw proportions and source features'
    keyshape = Keyshape.HRECT_S
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Restore the shallow rectangular block proportions; this is a component, not a whole gavel.
        self.add_polyline('block',(2,10),(30,10),(30,22),(2,22),closed=True)
