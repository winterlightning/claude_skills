"""Infinity Symbol Balaclava. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = '484cb3fb-0065-4ca7-ac5f-156d807d114c'
SOURCE_PATH = 'pictographic-primitives/other/criminal_484cb3fb-0065-4ca7-ac5f-156d807d114c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'infinity-symbol-balaclava-solo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    tags = ('sub icon',)
    keywords = ('sub icon', 'infinity symbol balaclava')
    def build(self):
        # Plan: Complete reference subject; shared named joins; direct 48px geometry.
        self.add_bezier('hood',(16,39),((4,31),(7,4),(24,4)),((41,4),(44,31),(32,39)))
        self.add_line('base-1',(32, 39),(40, 44))
        self.add_line('base-2',(40, 44),(8, 44))
        self.add_line('base-3',(8, 44),(16, 39))
        self.add_contour('outline','hood','base-1','base-2','base-3')
        self.add_bezier('eyes',(24,23),((15,11),(11,19),(15,25)),((20,30),(28,16),(33,20)),((38,29),(29,31),(24,23)))
