# Independent container symbol; edit separately from linked side sub-icon.
"""Independent 32px profile of flame.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '949214a5-cd3d-46da-8416-617e71942aa0'
SOURCE_PATH = 'pictographic-primitives/fire/flame_949214a5-cd3d-46da-8416-617e71942aa0.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('949214a5-cd3d-46da-8416-617e71942aa0', 'pictographic-primitives/fire/flame_949214a5-cd3d-46da-8416-617e71942aa0.svg'),)
PROFILE_SOURCE_KEYS = ('solo/flame',)
SOLO_SOURCE_ICON_IDS = ('flame',)
REFERENCE_EXPORT_SHA256 = '02bd12553efd78629895b3a8335281f6168608b2ee89ce0610a24695ceb51fe9'

class DrawingContainerSymbol(Sub32):
    icon_id = 'flame-sub32-symbol'
    variant_of = 'flame-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/flame-sub32'
    counterpart_icon_id = 'flame-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'fire'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (16, 2), ((21, 4), (22, 8), (22, 11)))
        self.add_bezier('p1-r1-2', (22, 11), ((22, 13), (22, 15), (21, 17)))
        self.add_bezier('p1-r1-3', (21, 17), ((21, 18), (21, 19), (21, 19)))
        self.add_bezier('p1-r1-4', (21, 19), ((21, 20), (21, 20), (21, 20)))
        self.add_bezier('p1-r1-5', (21, 20), ((23, 20), (25, 18), (26, 15)))
        self.add_bezier('p1-r1-6', (26, 15), ((26, 17), (27, 18), (27, 20)))
        self.add_bezier('p1-r1-7', (27, 20), ((27, 27), (22, 30), (16, 30)))
        self.add_bezier('p1-r1-8', (16, 30), ((9, 30), (5, 26), (5, 21)))
        self.add_bezier('p1-r1-9', (5, 21), ((5, 12), (17, 10), (17, 4)))
        self.add_bezier('p1-r1-10', (17, 4), ((17, 4), (16, 3), (16, 2)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', closed=False)
