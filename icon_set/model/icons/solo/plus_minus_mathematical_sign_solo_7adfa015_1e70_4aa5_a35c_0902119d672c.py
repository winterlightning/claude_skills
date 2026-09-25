"""Plus Minus Mathematical Sign. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = '7adfa015-1e70-4aa5-a35c-0902119d672c'
SOURCE_PATH = 'pictographic-primitives/other/circle plus minus_7adfa015-1e70-4aa5-a35c-0902119d672c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'plus-minus-mathematical-sign-solo'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    tags = ('sub icon',)
    keywords = ('sub icon', 'plus minus mathematical sign')
    def build(self):
        circle(self,'outline',24,24,20)
        self.add_polyline('plus-h',(15,17),(17,17),(19,17))
        self.add_polyline('plus-v',(17,15),(17,17),(17,19))
        self.relate('connect','plus-h','plus-v')
        self.add_line('slash',(16,32),(32,16))
        self.add_line('minus',(29,31),(33,31))
