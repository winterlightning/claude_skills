"""Traditional Ram Horn Shofar. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = 'b899b610-48c3-460c-9017-034a792ae9cb'
SOURCE_PATH = 'pictographic-primitives/other/shofar_b899b610-48c3-460c-9017-034a792ae9cb.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'traditional-ram-horn-shofar-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    tags = ('sub icon',)
    keywords = ('sub icon', 'traditional ram horn shofar')
    def build(self):
        # Plan: Complete reference subject; shared named joins; direct 48px geometry.
        rounded_rect(self,'mouth',20,6,42,14,4)
        self.add_bezier('outer',(36,14),((36,35),(27,36),(13,36)))
        self.add_bezier('inner',(13,26),((21,28),(26,26),(26,14)))
        
        rounded_rect(self,'bell',6,26,14,42,4)
        self.relate('connect','mouth','outer','inner')
        self.relate('connect','bell','outer','inner')
