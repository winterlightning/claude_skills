"""Zoom Out Magnifying Glass. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = '175a065e-b228-4fa8-9503-eb4f350508b7'
SOURCE_PATH = 'pictographic-primitives/state/magnifying glass minus_175a065e-b228-4fa8-9503-eb4f350508b7.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'zoom-out-magnifying-glass-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    tags = ('sub icon',)
    keywords = ('sub icon', 'zoom out magnifying glass')
    def build(self):
        # Plan: Complete reference subject; shared named joins; direct 48px geometry.
        self.add_arc('ring-a',(6,21),(21,6),radius_x=15)
        self.add_arc('ring-b',(21,6),(36,21),radius_x=15)
        self.add_arc('ring-c',(36,21),(30,33),radius_x=15)
        self.add_arc('ring-d',(30,33),(6,21),radius_x=15)
        self.add_contour('lens','ring-a','ring-b','ring-c','ring-d',closed=True)
        self.add_line('handle',(30,33),(42,42))
        self.relate('connect','lens','handle')
        self.add_line('minus',(15,21),(27,21))
