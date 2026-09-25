"""Clipboard with checkmark. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = 'c6e3c13b-a55a-4543-8d6f-5f9c7b2ff0e3'
SOURCE_PATH = 'pictographic-primitives/symbol/clipboard check_c6e3c13b-a55a-4543-8d6f-5f9c7b2ff0e3.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'clipboard-with-checkmark-solo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    categories = ('symbol', 'state')
    tags = ('sub icon',)
    keywords = ('sub icon', 'clipboard with checkmark')
    def build(self):
        # Plan: Complete reference subject; shared named joins; direct 48px geometry.
        self.add_polyline('board',(16,8),(8,8),(8,44),(40,44),(40,8),(32,8))
        rounded_rect(self,'clip',16,4,32,14,4)
        self.relate('connect','clip','board')
        self.add_polyline('check',(17,29),(22,34),(31,25))
