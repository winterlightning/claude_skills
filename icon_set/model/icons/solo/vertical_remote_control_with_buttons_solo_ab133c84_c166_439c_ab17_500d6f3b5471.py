"""Vertical Remote Control with Buttons. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = 'ab133c84-c166-439c-ab17-500d6f3b5471'
SOURCE_PATH = 'pictographic-primitives/other/remote control_ab133c84-c166-439c-ab17-500d6f3b5471.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'vertical-remote-control-with-buttons-solo'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    tags = ('sub icon',)
    keywords = ('sub icon', 'vertical remote control with buttons')
    def build(self):
        # Plan: Complete reference subject; shared named joins; direct 48px geometry.
        rounded_rect(self,'case',10,4,38,44,5)
        circle(self,'button',24,16,3)
        self.add_polyline('control-v',(24,27),(24,31),(24,35))
        self.add_polyline('control-h',(20,31),(24,31),(28,31))
        self.relate('connect','control-v','control-h')
