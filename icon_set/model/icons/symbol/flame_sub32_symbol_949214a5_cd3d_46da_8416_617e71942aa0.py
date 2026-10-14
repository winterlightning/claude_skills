"""Independent 32px profile of flame.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '949214a5-cd3d-46da-8416-617e71942aa0'
SOURCE_PATH = 'pictographic-primitives/fire/flame_949214a5-cd3d-46da-8416-617e71942aa0.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('949214a5-cd3d-46da-8416-617e71942aa0', 'pictographic-primitives/fire/flame_949214a5-cd3d-46da-8416-617e71942aa0.svg'),)
PROFILE_SOURCE_KEYS = ('solo/flame',)
SOLO_SOURCE_ICON_IDS = ('flame',)
REFERENCE_EXPORT_SHA256 = '02bd12553efd78629895b3a8335281f6168608b2ee89ce0610a24695ceb51fe9'

class DrawingContainerSymbol(Sub32):
    icon_id = 'flame-sub32-symbol'
    related_origin_icon_id = 'flame-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/flame-sub32'
    counterpart_icon_id = 'flame-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'fire'
    categories = ('fire', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Flame with an inner flick, the flick 4 units clear of the outer edge.
        self.add_bezier('f-1', (16, 2), ((21.833333, 4), (23, 8), (23, 11)))
        self.add_bezier('f-2', (23, 11), ((23, 14), (21, 17), (18, 19)))
        self.add_bezier('f-3', (18, 19), ((21, 19), (25.833333, 17), (27, 14)))
        self.add_bezier('f-4', (27, 14), ((27, 16), (28, 18), (28, 20)))
        self.add_bezier('f-5', (28, 20), ((28, 27), (22.545455, 30), (16, 30)))
        self.add_bezier('f-6', (16, 30), ((8.363636, 30), (4, 26), (4, 21)))
        self.add_bezier('f-7', (4, 21), ((4, 12), (16, 13), (16, 2)))
        self.add_contour('flame', 'f-1', 'f-2', 'f-3', 'f-4', 'f-5', 'f-6', 'f-7', closed=True)
