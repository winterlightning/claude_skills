"""Exclamation Point Warning Triangle. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.
Rounded triangular warning silhouette; separated stem and dot.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = '42f29bd3-1507-484e-98bb-b90c40309892'
SOURCE_PATH = 'pictographic-primitives/other/warning triangle_42f29bd3-1507-484e-98bb-b90c40309892.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'exclamation-point-warning-triangle-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    tags = ('sub icon',)
    keywords = ('sub icon', 'exclamation point warning triangle')
    def build(self):
        # Plan: Rounded triangular warning silhouette; separated stem and dot.
        self.add_bezier('triangle',(24,6),((22,6),(21,9),(20,11)),((15,20),(10,30),(6,38)),((6,41),(7,42),(10,42)),((19,42),(29,42),(38,42)),((41,42),(42,41),(42,38)),((37,28),(30,15),(27,9)),((26,7),(25,6),(24,6)))
        self.add_contour('outline','triangle',closed=True)
        self.add_line('warning-stem',(24,22),(24,25))
        self.add_dot('warning-dot',(24,33))
