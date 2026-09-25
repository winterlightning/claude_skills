"""Square Barcode Scanning Icon. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = '2d49d0f6-d1d8-4784-9532-65114f883c0c'
SOURCE_PATH = 'pictographic-primitives/shopping/barcode_2d49d0f6-d1d8-4784-9532-65114f883c0c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'square-barcode-scanning-icon-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shopping'
    tags = ('sub icon',)
    keywords = ('sub icon', 'square barcode scanning icon')
    def build(self):
        # Plan: Complete reference subject; shared named joins; direct 48px geometry.
        rounded_rect(self,'outline',6,6,42,42,5)
        for n,x in enumerate((15,24,33)):self.add_line('bar-'+str(n),(x,15),(x,33))
