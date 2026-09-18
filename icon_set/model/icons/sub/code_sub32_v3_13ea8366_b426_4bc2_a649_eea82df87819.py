# Variant of code-sub32-v2; parent file remains unchanged.
"""Independent 32px profile of code.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '13ea8366-b426-4bc2-a649-eea82df87819'
SOURCE_PATH = 'pictographic-primitives/programing/code_13ea8366-b426-4bc2-a649-eea82df87819.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('13ea8366-b426-4bc2-a649-eea82df87819', 'pictographic-primitives/programing/code_13ea8366-b426-4bc2-a649-eea82df87819.svg'),)
PROFILE_SOURCE_KEYS = ('solo/code',)
SOLO_SOURCE_ICON_IDS = ('code',)
REFERENCE_EXPORT_SHA256 = 'f93c3fab4228d36eb95d370b213390a76309529e30052be0d14ffe0815fc7df6'

class DrawingVariant3(Sub32):
    icon_id = 'code-sub32-v3'
    variant_of = 'code-sub32-v2'
    variant_label = 'Redraw proportions and source features'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'programing'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Two equally weighted chevrons, restored open width rather than pinched near-vertical brackets.
        for label,sign in [('left',-1),('right',1)]:
         self.add_polyline(label,(16+sign*4,6),(16+sign*14,16),(16+sign*4,26))
