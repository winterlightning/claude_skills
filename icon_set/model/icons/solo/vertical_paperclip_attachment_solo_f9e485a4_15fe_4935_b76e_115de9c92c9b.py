"""Vertical Paperclip Attachment. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = 'f9e485a4-15fe-4935-b76e-115de9c92c9b'
SOURCE_PATH = 'pictographic-primitives/other/attachment vertical_f9e485a4-15fe-4935-b76e-115de9c92c9b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'vertical-paperclip-attachment-solo'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    tags = ('sub icon',)
    keywords = ('sub icon', 'vertical paperclip attachment')
    def build(self):
        # Plan: Complete reference subject; shared named joins; direct 48px geometry.
        self.add_arc('outer',(10,18),(38,18),radius_x=14)
        self.add_line('right',(38,18),(38,35))
        self.add_arc('bottom',(38,35),(20,35),radius_x=9)
        self.add_line('inner-left',(20,35),(20,20))
        self.add_arc('inner-top',(20,20),(28,20),radius_x=4)
        self.add_line('inner-right',(28,20),(28,33))
        self.add_contour('paperclip','outer','right','bottom','inner-left','inner-top','inner-right')
