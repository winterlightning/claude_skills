"""Wireless Mobile Yuan Payment. Currency/semantic symbol explicitly authorized by user. Preserve the enclosing object and recognizable symbol; omit invoice text lines, bill ornaments, and device controls to keep the symbol clear. Related Lucide originals and atomic views: dollar-sign, euro, pound-sterling, japanese-yen, bitcoin, circle-question-mark, info. Typed contours share their real attachment points.
Plan: VRECT_L envelope; construct enclosing subject first, then one central symbol.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle
from ._sub_preparation_symbols import bubble, document, wireless_phone, banknote, moneybag, house, monitor, baht, currency, compact, diagonal_dollar
SOURCE_ICON_ID='54325bec-9e76-47f3-ae84-9ced16fe0a3a'
SOURCE_PATH='pictographic-primitives/other/mobile phone yuan sign wireless_54325bec-9e76-47f3-ae84-9ced16fe0a3a.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='wireless-mobile-yuan-payment-solo'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    categories = ('state', 'other', 'primitives-generate')
    tags=('sub icon',)
    keywords=('sub icon', 'wireless mobile yuan payment')
    def build(self):
        wireless_phone(self)
        compact(self,'yen',24,28)
