"""Yen Currency Document. Currency/semantic symbol explicitly authorized by user. Preserve the enclosing object and recognizable symbol; omit invoice text lines, bill ornaments, and device controls to keep the symbol clear. Related Lucide originals and atomic views: dollar-sign, euro, pound-sterling, japanese-yen, bitcoin, circle-question-mark, info. Typed contours share their real attachment points.
Plan: VRECT_L envelope; construct enclosing subject first, then one central symbol.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle
from ._sub_preparation_symbols import bubble, document, wireless_phone, banknote, moneybag, house, monitor, baht, currency, compact, diagonal_dollar
SOURCE_ICON_ID='b3374daa-5cf7-4d59-b44f-d2f472d4ca67'
SOURCE_PATH='pictographic-primitives/other/yuan bill_b3374daa-5cf7-4d59-b44f-d2f472d4ca67.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='yen-currency-document-solo'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    tags=('sub icon',)
    keywords=('sub icon', 'yen currency document')
    def build(self):
        document(self)
        currency(self,'yen',24,26)
