"""Secure Lock with Checkmark. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = 'ed0c948e-0d83-4215-8410-7cd5b4fdaf4d'
SOURCE_PATH = 'pictographic-primitives/other/check lock_ed0c948e-0d83-4215-8410-7cd5b4fdaf4d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'secure-lock-with-checkmark-solo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    tags = ('sub icon',)
    keywords = ('sub icon', 'secure lock with checkmark')
    def build(self):
        # Plan: Complete reference subject; shared named joins; direct 48px geometry.
        rounded_rect(self,'body',8,20,40,44,4)
        self.add_line('shackle-left',(15,20),(15,13))
        self.add_arc('shackle-top',(15,13),(33,13),radius_x=9)
        self.add_line('shackle-right',(33,13),(33,20))
        self.add_contour('shackle','shackle-left','shackle-top','shackle-right')
        self.relate('connect','body','shackle')
        self.add_polyline('check',(17,31),(22,35),(30,29))
