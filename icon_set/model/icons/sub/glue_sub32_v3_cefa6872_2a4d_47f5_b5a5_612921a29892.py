# Variant of glue-sub32-v2; parent file remains unchanged.
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

class DrawingVariant3(Sub32):
    icon_id = 'glue-sub32-v3'
    variant_of = 'glue-sub32-v2'
    variant_label = 'Redraw proportions and source features'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'design'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Slender glue bottle with a rounded nozzle and controlled tapered body.
        self.add_bezier('nozzle-left',(12,12),((13,9),(13,2),(16,2)))
        self.add_bezier('nozzle-right',(16,2),((19,2),(19,9),(20,12)))
        self.add_contour('nozzle','nozzle-left','nozzle-right')
        self.add_line('shoulder',(12,12),(20,12))
        self.add_bezier('right',(20,12),((22,12),(24,25),(24,27)))
        self.add_bezier('br',(24,27),((24,30),(21,30),(20,30)))
        self.add_line('base',(20,30),(12,30))
        self.add_bezier('bl',(12,30),((11,30),(8,30),(8,27)))
        self.add_bezier('left',(8,27),((8,25),(10,12),(12,12)))
        self.add_contour('body','shoulder','right','br','base','bl','left',closed=True)
        for a,b in [('nozzle-left','shoulder'),('nozzle-left','left'),('nozzle-right','shoulder'),('nozzle-right','right')]:self.relate('connect',a,b)
