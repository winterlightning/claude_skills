"""Mobile Contactless Payment. Currency/semantic symbol explicitly authorized by user. Preserve the enclosing object and recognizable symbol; omit invoice text lines, bill ornaments, and device controls to keep the symbol clear. Related Lucide originals and atomic views: dollar-sign, euro, pound-sterling, japanese-yen, bitcoin, circle-question-mark, info. Typed contours share their real attachment points.
Plan: VRECT_L envelope; construct enclosing subject first, then one central symbol.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle
from ._sub_preparation_symbols import bubble, document, wireless_phone, banknote, moneybag, house, monitor, baht, currency, compact, diagonal_dollar
SOURCE_ICON_ID='8d317b81-2d88-4d5c-9090-0c063df565b3'
SOURCE_PATH='pictographic-primitives/other/mobile phone dollar sign wireless_8d317b81-2d88-4d5c-9090-0c063df565b3.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='mobile-contactless-payment-solo'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    categories = ('state', 'other', 'primitives-generate')
    tags=('sub icon',)
    keywords=('sub icon', 'mobile contactless payment')
    def build(self):
        wireless_phone(self)
        compact(self,'dollar',24,26)
