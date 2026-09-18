"""Square Video Play Button. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = '94471a3a-03a7-46be-8c90-49f47745960a'
SOURCE_PATH = 'pictographic-primitives/other/media_94471a3a-03a7-46be-8c90-49f47745960a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'square-play-32-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    tags = ('sub icon',)
    keywords = ('sub icon', 'square video play button')
    def build(self):
        # Plan: Complete reference subject; shared named joins; direct 48px geometry.
        rounded_rect(self,'outline',6,6,42,42,5)
        self.add_polyline('play',(18,15),(32,24),(18,33),closed=True)
