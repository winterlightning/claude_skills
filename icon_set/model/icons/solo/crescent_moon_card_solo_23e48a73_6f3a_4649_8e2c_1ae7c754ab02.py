"""Crescent Moon Card. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = '23e48a73-6f3a-4649-8e2c-1ae7c754ab02'
SOURCE_PATH = 'pictographic-primitives/other/card moon_23e48a73-6f3a-4649-8e2c-1ae7c754ab02.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'crescent-moon-card-solo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    tags = ('sub icon',)
    keywords = ('sub icon', 'crescent moon card')
    def build(self):
        # Plan: Complete reference subject; shared named joins; direct 48px geometry.
        rounded_rect(self,'card',8,4,40,44,5)
        self.add_bezier('moon',(27,14),((14,14),(14,34),(27,34)),((20,28),(20,20),(27,14)))
        self.add_contour('crescent','moon',closed=True)
