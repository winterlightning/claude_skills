"""Computer Display Screen with Stand. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = '8d7f3cd4-f98b-4ae1-b9de-7232643f178a'
SOURCE_PATH = 'pictographic-primitives/computers/batch-02/monitor_8d7f3cd4-f98b-4ae1-b9de-7232643f178a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'computer-display-screen-with-stand-solo'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    tags = ('sub icon',)
    keywords = ('sub icon', 'computer display screen with stand')
    def build(self):
        # Plan: Complete reference subject; shared named joins; direct 48px geometry.
        rounded_rect(self,'screen',4,8,44,31,4)
        self.add_line('stem',(24,31),(24,40))
        self.add_line('foot',(16,40),(32,40))
        self.relate('connect','screen','stem')
        self.relate('connect','stem','foot')
