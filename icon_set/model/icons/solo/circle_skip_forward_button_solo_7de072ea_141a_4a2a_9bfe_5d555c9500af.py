"""Circle Skip Forward Button. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = '7de072ea-141a-4a2a-9bfe-5d555c9500af'
SOURCE_PATH = 'pictographic-primitives/other/circle button next_7de072ea-141a-4a2a-9bfe-5d555c9500af.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'circle-skip-forward-button-solo'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('other', 'state', 'primitives-generate')
    tags = ('sub icon',)
    keywords = ('sub icon', 'circle skip forward button')
    def build(self):
        # Plan: Complete reference subject; shared named joins; direct 48px geometry.
        circle(self,'outline',24,24,20)
        self.add_polyline('play',(16,17),(24,24),(16,31),closed=True)
        self.add_line('stop',(33,18),(33,30))
