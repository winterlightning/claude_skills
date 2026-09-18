"""Euro Currency Coin. Currency/semantic symbol explicitly authorized by user. Preserve the enclosing object and recognizable symbol; omit invoice text lines, bill ornaments, and device controls to keep the symbol clear. Related Lucide originals and atomic views: dollar-sign, euro, pound-sterling, japanese-yen, bitcoin, circle-question-mark, info. Typed contours share their real attachment points.
Plan: CIRCLE envelope; construct enclosing subject first, then one central symbol.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle
from ._sub_preparation_symbols import bubble, document, wireless_phone, banknote, moneybag, house, monitor, baht, currency, compact, diagonal_dollar
SOURCE_ICON_ID='4f00181e-9f16-4ce7-b529-18053abcaa47'
SOURCE_PATH='pictographic-primitives/other/circle euro_4f00181e-9f16-4ce7-b529-18053abcaa47.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='euro-currency-coin-solo'
    keyshape=Keyshape.CIRCLE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/finance' 
    tags=('sub icon',)
    keywords=('sub icon', 'euro currency coin')
    def build(self):
        circle(self,'outline',24,24,20)
        currency(self,'euro',24,24)
