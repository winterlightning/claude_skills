"""Dog Profile Circle. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = 'eab5a9ed-7706-42c2-851d-b7c76c820840'
SOURCE_PATH = 'pictographic-primitives/pets/dog head_eab5a9ed-7706-42c2-851d-b7c76c820840.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'dog-profile-circle-solo'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    tags = ('sub icon',)
    keywords = ('sub icon', 'dog profile circle')
    def build(self):
        # Plan: Complete reference subject; shared named joins; direct 48px geometry.
        circle(self,'outline',24,24,20)
        self.add_polyline('dog',(23,43),(23,30),(16,30),(13,23),(22,18),(22,10),(38,30))
        self.relate('connect','outline','dog')
