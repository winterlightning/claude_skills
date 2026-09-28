# Variant of ecology-leaf-sub32-v2; parent file remains unchanged.
"""Independent 32px profile of ecology-leaf.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'd816c758-0f95-4958-9d90-ed19c3a68e77'
SOURCE_PATH = 'pictographic-primitives/ecology/ecology leaf_d816c758-0f95-4958-9d90-ed19c3a68e77.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('d816c758-0f95-4958-9d90-ed19c3a68e77', 'pictographic-primitives/ecology/ecology leaf_d816c758-0f95-4958-9d90-ed19c3a68e77.svg'), ('164d9e51-fa44-4293-94e6-d83af50f3387', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/leaf right_164d9e51-fa44-4293-94e6-d83af50f3387.svg'))
PROFILE_SOURCE_KEYS = ('solo/ecology-leaf',)
SOLO_SOURCE_ICON_IDS = ('ecology-leaf',)
REFERENCE_EXPORT_SHA256 = '3ed5069bfc0e588adb918c6a94a4e9604c79f6fe0df2f1a8f5693ff3058dbf1d'

class DrawingVariant3(Sub32):
    icon_id = 'ecology-leaf-sub32-v3'
    variant_of = 'ecology-leaf-sub32-v2'
    variant_label = 'Redraw proportions and source features'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'ecology'
    categories = ('primitives', 'ecology')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Rebuild a smooth organic leaf body and curved vein; remove wavering bumps in the lower contour.
        self.add_bezier('right',(30,4),((30,20),(23,28),(12,28)))
        self.add_bezier('lower-left',(12,28),((6,28),(4,24),(4,18)))
        self.add_bezier('upper-left',(4,18),((4,12),(8,8),(14,8)))
        self.add_bezier('tip',(14,8),((22,8),(26,8),(30,4)))
        self.add_contour('leaf','right','lower-left','upper-left','tip',closed=True)
        self.add_bezier('vein',(2,28),((8,21),(13,17),(22,13)))
        self.relate('connect','leaf','vein')
