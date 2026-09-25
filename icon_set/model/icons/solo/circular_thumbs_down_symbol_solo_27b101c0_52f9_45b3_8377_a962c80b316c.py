"""Circular Thumbs Down Symbol. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = '27b101c0-52f9-45b3-8377-a962c80b316c'
SOURCE_PATH = 'pictographic-primitives/state/circle thumbs down_27b101c0-52f9-45b3-8377-a962c80b316c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'circular-thumbs-down-symbol-solo'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    categories = ('state',)
    tags = ('sub icon',)
    keywords = ('sub icon', 'circular thumbs down symbol')
    def build(self):
        # Plan: Complete reference subject; shared named joins; direct 48px geometry.
        circle(self,'outline',24,24,20)
        self.add_bezier('thumb',(15,17),((19,17),(20,19),(22,23)),((24,25),(26,30),(27,33)),((28,35),(31,33),(30,29)),((30,26),(29,24),(29,24)),((32,24),(33,24),(33,20)),((32,17),(32,14),(30,15)),((23,14),(21,14),(18,16)),((16,16),(15,16),(15,17)))
        self.add_contour('hand','thumb',closed=True)
