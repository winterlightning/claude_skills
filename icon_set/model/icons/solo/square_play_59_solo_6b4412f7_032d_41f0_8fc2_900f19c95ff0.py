"""Square Media Play Button. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = '6b4412f7-032d-41f0-8fc2-900f19c95ff0'
SOURCE_PATH = 'pictographic-primitives/other/square play_6b4412f7-032d-41f0-8fc2-900f19c95ff0.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'square-play-59-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    tags = ('sub icon',)
    keywords = ('sub icon', 'square media play button')
    def build(self):
        # Plan: Complete reference subject; shared named joins; direct 48px geometry.
        rounded_rect(self,'outline',6,6,42,42,5)
        self.add_polyline('play',(18,15),(32,24),(18,33),closed=True)
