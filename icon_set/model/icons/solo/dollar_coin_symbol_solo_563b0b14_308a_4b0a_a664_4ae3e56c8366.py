"""Dollar Coin Symbol. Currency/semantic symbol explicitly authorized by user. Preserve the enclosing object and recognizable symbol; omit invoice text lines, bill ornaments, and device controls to keep the symbol clear. Related Lucide originals and atomic views: dollar-sign, euro, pound-sterling, japanese-yen, bitcoin, circle-question-mark, info. Typed contours share their real attachment points.
Plan: CIRCLE envelope; construct enclosing subject first, then one central symbol.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle
from ._sub_preparation_symbols import bubble, document, wireless_phone, banknote, moneybag, house, monitor, baht, currency, compact, diagonal_dollar
SOURCE_ICON_ID='563b0b14-308a-4b0a-a664-4ae3e56c8366'
SOURCE_PATH='pictographic-primitives/other/circle dollar_563b0b14-308a-4b0a-a664-4ae3e56c8366.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='dollar-coin-symbol-solo'
    keyshape=Keyshape.CIRCLE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    categories = ('state', 'other', 'primitives-generate')
    tags=('sub icon',)
    keywords=('sub icon', 'dollar coin symbol')
    def build(self):
        circle(self,'outline',24,24,20)
        currency(self,'dollar',24,24)
