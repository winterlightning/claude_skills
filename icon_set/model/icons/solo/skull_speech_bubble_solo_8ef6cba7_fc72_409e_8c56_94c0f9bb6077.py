"""Skull Speech Bubble. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = '8ef6cba7-fc72-409e-8c56-94c0f9bb6077'
SOURCE_PATH = 'pictographic-primitives/symbol/messages bubble square skull_8ef6cba7-fc72-409e-8c56-94c0f9bb6077.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'skull-speech-bubble-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    tags = ('sub icon',)
    keywords = ('sub icon', 'skull speech bubble')
    def build(self):
        # Plan: Complete reference subject; shared named joins; direct 48px geometry.
        rounded_rect(self,'bubble',6,6,42,34,5)
        self.add_polyline('tail',(14,34),(14,42),(24,34))
        self.relate('connect','bubble','tail')
        self.add_bezier('skull',(19,27),((9,15),(19,10),(24,12)),((29,10),(39,15),(29,27)),((29,31),(29,32),(24,32)),((19,32),(19,31),(19,27)))
        self.add_contour('skull-shape','skull',closed=True)
        self.add_dot('eye-left',(20,21))
        self.add_dot('eye-right',(28,21))
