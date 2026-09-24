"""Independent 32px profile of glue.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'cefa6872-2a4d-47f5-b5a5-612921a29892'
SOURCE_PATH = 'pictographic-primitives/design/glue_cefa6872-2a4d-47f5-b5a5-612921a29892.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('cefa6872-2a4d-47f5-b5a5-612921a29892', 'pictographic-primitives/design/glue_cefa6872-2a4d-47f5-b5a5-612921a29892.svg'),)
PROFILE_SOURCE_KEYS = ('solo/glue',)
SOLO_SOURCE_ICON_IDS = ('glue',)
REFERENCE_EXPORT_SHA256 = 'c0778f3bb21ab5c5d84b97410539ef606102d7154b60dd3c60fcbe3567e4094d'

class DrawingVariant2(Sub32):
    icon_id = 'glue-sub32-v2'
    variant_label = 'Repair 32px envelope'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'design'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        short_axis = 16
        short_half_span = 12
        (short_low, short_high) = (short_axis - short_half_span, short_axis + short_half_span)
        self.add_bezier('p1-r1-1', (10, 13), ((14, 3), (14, 2), (16, 2)))
        self.add_bezier('p1-r1-4', (16, 2), ((18, 2), (18, 3), (22, 13)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (10, 13), (22, 13))
        self.add_bezier('p2-r1-2', (22, 13), ((24, 13), (25, 14), (26, 18)))
        self.add_bezier('p2-r1-3', (26, 18), ((27, 22), (28, 23), (28, 26)))
        self.add_bezier('p2-r1-4', (short_high, 26), ((short_high, 29), (25, 30), (22, 30)))
        self.add_line('p2-r1-5', (22, 30), (10, 30))
        self.add_bezier('p2-r1-6', (10, 30), ((7, 30), (short_low, 29), (short_low, 26)))
        self.add_bezier('p2-r1-7', (4, 26), ((4, 23), (5, 22), (6, 18)))
        self.add_bezier('p2-r1-8', (6, 18), ((7, 14), (8, 13), (10, 13)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', 'p2-r1-8', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p2-r1-8')
        self.relate('connect', 'p1-r1-4', 'p2-r1-1')
        self.relate('connect', 'p1-r1-4', 'p2-r1-2')
