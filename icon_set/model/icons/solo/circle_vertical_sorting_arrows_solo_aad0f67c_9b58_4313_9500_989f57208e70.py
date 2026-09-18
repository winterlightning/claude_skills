"""Circle Vertical Sorting Arrows. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = 'aad0f67c-9b58-4313-9500-989f57208e70'
SOURCE_PATH = 'pictographic-primitives/other/circle opposite arrows_aad0f67c-9b58-4313-9500-989f57208e70.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'circle-vertical-sorting-arrows-solo'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    tags = ('sub icon',)
    keywords = ('sub icon', 'circle vertical sorting arrows')
    def build(self):
        # Plan: Complete reference subject; shared named joins; direct 48px geometry.
        circle(self,'outline',24,24,20)
        self.add_line('down-shaft',(18,15),(18,31))
        self.add_polyline('down-head',(14,27),(18,31),(20,29))
        self.relate('connect','down-shaft','down-head')
        self.add_line('up-shaft',(30,33),(30,17))
        self.add_polyline('up-head',(28,19),(30,17),(34,21))
        self.relate('connect','up-shaft','up-head')
