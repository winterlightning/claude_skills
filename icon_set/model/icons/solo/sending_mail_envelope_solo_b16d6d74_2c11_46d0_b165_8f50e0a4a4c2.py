"""Sending Mail Envelope. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = 'b16d6d74-2c11-46d0-b165-8f50e0a4a4c2'
SOURCE_PATH = 'pictographic-primitives/emails/send email_b16d6d74-2c11-46d0-b165-8f50e0a4a4c2.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'sending-mail-envelope-solo'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    tags = ('sub icon',)
    keywords = ('sub icon', 'sending mail envelope')
    def build(self):
        # Plan: Complete reference subject; shared named joins; direct 48px geometry.
        rounded_rect(self,'envelope',17,8,44,40,3)
        self.add_polyline('fold',(19,11),(30,22),(42,11))
        self.relate('connect','fold','envelope')
        self.add_line('speed-top',(4,19),(9,19))
        self.add_line('speed-bottom',(4,29),(9,29))
