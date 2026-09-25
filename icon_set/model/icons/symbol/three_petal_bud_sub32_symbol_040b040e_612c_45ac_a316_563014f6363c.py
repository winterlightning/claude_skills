"""Independent 32px profile of three-petal-bud.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '040b040e-612c-45ac-a316-563014f6363c'
SOURCE_PATH = 'pictographic-primitives/nature/plant_040b040e-612c-45ac-a316-563014f6363c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('040b040e-612c-45ac-a316-563014f6363c', 'pictographic-primitives/nature/plant_040b040e-612c-45ac-a316-563014f6363c.svg'), ('a1b3fc44-cc28-4906-bcdc-64d15a515143', 'pictographic-primitives/nature/plant_a1b3fc44-cc28-4906-bcdc-64d15a515143.svg'))
PROFILE_SOURCE_KEYS = ('solo/three-petal-bud', 'solo/three-petal-bud-alternate')
SOLO_SOURCE_ICON_IDS = ('three-petal-bud', 'three-petal-bud-alternate')
REFERENCE_EXPORT_SHA256 = 'ca34f41c0fa1a193fbea671268c7ff351a91c65cb473e17c65027700acc98b7f'

class DrawingContainerSymbol(Sub32):
    icon_id = 'three-petal-bud-sub32-symbol'
    related_origin_icon_id = 'three-petal-bud-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/three-petal-bud-sub32'
    counterpart_icon_id = 'three-petal-bud-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'nature'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (5, 8), (12, 12))
        self.add_arc('p1-r1-2', (12, 12), (16, 2), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (16, 2), (20, 12), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_line('p1-r1-4', (20, 12), (27, 8))
        self.add_arc('p1-r1-5', (27, 8), (16, 24), radius_x=11, radius_y=17, large_arc=False, sweep=True)
        self.add_arc('p1-r1-6', (16, 24), (5, 8), radius_x=11, radius_y=17, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_line('p2-r1-1', (16, 24), (16, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.relate('connect', 'p1-r1-5', 'p2-r1-1')
        self.relate('connect', 'p1-r1-6', 'p2-r1-1')
