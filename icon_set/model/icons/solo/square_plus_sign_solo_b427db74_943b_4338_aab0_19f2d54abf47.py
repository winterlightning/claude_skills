"""Square Plus Sign. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = 'b427db74-943b-4338-aab0-19f2d54abf47'
SOURCE_PATH = 'pictographic-primitives/other/square add_b427db74-943b-4338-aab0-19f2d54abf47.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'square-plus-sign-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    tags = ('sub icon',)
    keywords = ('sub icon', 'square plus sign')
    def build(self):
        # Plan: Complete reference subject; shared named joins; direct 48px geometry.
        rounded_rect(self,'outline',6,6,42,42,5)
        self.add_polyline('h',(15,24),(24,24),(33,24))
        self.add_polyline('v',(24,15),(24,24),(24,33))
        self.relate('connect','h','v')
