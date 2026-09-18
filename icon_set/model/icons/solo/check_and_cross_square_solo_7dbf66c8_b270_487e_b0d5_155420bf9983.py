"""Check and Cross Square. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = '7dbf66c8-b270-487e-b0d5-155420bf9983'
SOURCE_PATH = 'pictographic-primitives/other/rectangle remove and check_7dbf66c8-b270-487e-b0d5-155420bf9983.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'check-and-cross-square-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    tags = ('sub icon',)
    keywords = ('sub icon', 'check and cross square')
    def build(self):
        # Plan: Complete reference subject; shared named joins; direct 48px geometry.
        rounded_rect(self,'outline',6,6,42,42,5)
        self.add_polyline('check',(15,17),(18,20),(22,15))
        self.add_line('divider',(18,34),(30,14))
        self.add_line('cross-a',(29,27),(34,32))
        self.add_line('cross-b',(29,32),(34,27))
        self.relate('connect','cross-a','cross-b')
