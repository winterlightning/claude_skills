"""Diagonal Expansion Arrow. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = 'c84b5b94-cfc2-4c80-bb44-468cd2bc0cf6'
SOURCE_PATH = 'pictographic-primitives/interface-essential/expand_c84b5b94-cfc2-4c80-bb44-468cd2bc0cf6.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'diagonal-expansion-arrow-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    tags = ('sub icon',)
    keywords = ('sub icon', 'diagonal expansion arrow')
    def build(self):
        # Plan: Complete reference subject; shared named joins; direct 48px geometry.
        self.add_polyline('stand',(6,42),(6,35),(20,35),(20,42))
        self.add_line('arrow',(21,27),(42,6))
        self.add_polyline('head',(30,6),(42,6),(42,18))
        self.relate('connect','head','arrow')
