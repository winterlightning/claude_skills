"""Vertical DNA Double Helix. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = '3c216074-a57a-436c-81d8-30276fe1614e'
SOURCE_PATH = 'pictographic-primitives/other/dna vertical_3c216074-a57a-436c-81d8-30276fe1614e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'vertical-dna-double-helix-solo'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    tags = ('sub icon',)
    keywords = ('sub icon', 'vertical dna double helix')
    def build(self):
        # Plan: Complete reference subject; shared named joins; direct 48px geometry.
        self.add_bezier('strand-a',(10,4),((10,17),(38,31),(38,44)))
        self.add_bezier('strand-b',(38,4),((38,17),(10,31),(10,44)))
        self.relate('connect','strand-a','strand-b')
        self.add_line('rung-top',(10,4),(38,4))
        self.add_line('rung-bottom',(10,44),(38,44))
        self.relate('connect','strand-a','rung-top','rung-bottom')
        self.relate('connect','strand-b','rung-top','rung-bottom')
