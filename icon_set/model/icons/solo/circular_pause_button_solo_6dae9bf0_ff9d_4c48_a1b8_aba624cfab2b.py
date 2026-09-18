"""Circular Pause Button. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = '6dae9bf0-ff9d-4c48-a1b8-aba624cfab2b'
SOURCE_PATH = 'pictographic-primitives/other/circle pause_6dae9bf0-ff9d-4c48-a1b8-aba624cfab2b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'circular-pause-button-solo'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    tags = ('sub icon',)
    keywords = ('sub icon', 'circular pause button')
    def build(self):
        # Plan: Complete reference subject; shared named joins; direct 48px geometry.
        circle(self,'outline',24,24,20)
        self.add_line('pause-left',(19,15),(19,33))
        self.add_line('pause-right',(29,15),(29,33))
