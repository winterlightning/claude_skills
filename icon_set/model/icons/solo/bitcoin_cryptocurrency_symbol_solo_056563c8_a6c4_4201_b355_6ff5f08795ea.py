"""Bitcoin Cryptocurrency Symbol. Currency/semantic symbol explicitly authorized by user. Preserve the enclosing object and recognizable symbol; omit invoice text lines, bill ornaments, and device controls to keep the symbol clear. Related Lucide originals and atomic views: dollar-sign, euro, pound-sterling, japanese-yen, bitcoin, circle-question-mark, info. Typed contours share their real attachment points.
Plan: CIRCLE envelope; construct enclosing subject first, then one central symbol.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle
from ._sub_preparation_symbols import bubble, document, wireless_phone, banknote, moneybag, house, monitor, baht, currency, compact, diagonal_dollar
SOURCE_ICON_ID='056563c8-a6c4-4201-b355-6ff5f08795ea'
SOURCE_PATH='pictographic-primitives/other/circle bitcoin_056563c8-a6c4-4201-b355-6ff5f08795ea.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='bitcoin-cryptocurrency-symbol-solo'
    keyshape=Keyshape.CIRCLE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    tags=('sub icon',)
    keywords=('sub icon', 'bitcoin cryptocurrency symbol')
    def build(self):
        circle(self,'outline',24,24,20)
        currency(self,'bitcoin',24,24)
