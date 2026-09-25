"""Skull Security Protection Shield. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = '6913cf31-3e4e-45e7-8c23-c3afd631eee3'
SOURCE_PATH = 'pictographic-primitives/war/shield skull_6913cf31-3e4e-45e7-8c23-c3afd631eee3.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'skull-security-protection-shield-solo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'war'
    tags = ('sub icon',)
    keywords = ('sub icon', 'skull security protection shield')
    def build(self):
        # Plan: Complete reference subject; shared named joins; direct 48px geometry.
        self.add_bezier('shield',(24,4),((19,7),(14,9),(8,10)),((8,26),(8,35),(24,44)),((40,35),(40,26),(40,10)),((34,9),(29,7),(24,4)))
        self.add_contour('outline','shield',closed=True)
        self.add_bezier('skull',(19,27),((9,15),(19,10),(24,12)),((29,10),(39,15),(29,27)),((29,31),(29,32),(24,32)),((19,32),(19,31),(19,27)))
        self.add_contour('skull-shape','skull',closed=True)
        self.add_dot('eye-left',(20,21))
        self.add_dot('eye-right',(28,21))
