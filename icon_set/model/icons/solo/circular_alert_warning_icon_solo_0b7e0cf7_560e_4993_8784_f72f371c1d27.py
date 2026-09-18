"""Circular Alert Warning Icon. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = '0b7e0cf7-560e-4993-8784-f72f371c1d27'
SOURCE_PATH = 'pictographic-primitives/state/circle with exclamation mark_0b7e0cf7-560e-4993-8784-f72f371c1d27.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'circular-alert-warning-icon-solo'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    tags = ('sub icon',)
    keywords = ('sub icon', 'circular alert warning icon')
    def build(self):
        # Plan: Complete reference subject; shared named joins; direct 48px geometry.
        circle(self,'outline',24,24,20)
        self.add_line('stem',(24,13),(24,25))
        self.add_dot('dot',(24,34))
