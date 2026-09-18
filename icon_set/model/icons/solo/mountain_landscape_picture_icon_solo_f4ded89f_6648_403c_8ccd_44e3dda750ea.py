"""Mountain Landscape Picture Icon. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.
Framed landscape, sun and unequal mountain peaks; frame contact must be checked.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = 'f4ded89f-6648-403c-8ccd-44e3dda750ea'
SOURCE_PATH = 'pictographic-primitives/images/image_f4ded89f-6648-403c-8ccd-44e3dda750ea.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'mountain-landscape-picture-icon-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    tags = ('sub icon',)
    keywords = ('sub icon', 'mountain landscape picture icon')
    def build(self):
        # Plan: Framed landscape, sun and unequal mountain peaks; frame contact must be checked.
        rounded_rect(self,'frame',6,6,42,42,5)
        circle(self,'sun',18,18,3)
        self.add_polyline('mountains',(6,37),(17,30),(23,36),(32,25),(42,37))
        self.relate('connect','frame','mountains')
