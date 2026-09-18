"""Circular Success Verification Check Mark. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.
Circle owns the envelope; one continuous ascending check.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = '9990b35d-e41d-404f-a3cb-caa71cc3b51f'
SOURCE_PATH = 'pictographic-primitives/other/circle check_9990b35d-e41d-404f-a3cb-caa71cc3b51f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'circular-success-verification-check-mark-solo'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    tags = ('sub icon',)
    keywords = ('sub icon', 'circular success verification check mark')
    def build(self):
        # Plan: Circle owns the envelope; one continuous ascending check.
        circle(self,'outline',24,24,20)
        self.add_polyline('check',(15,24),(21,30),(33,18))
