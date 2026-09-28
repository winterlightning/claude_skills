"""Yuan Currency Money Bill. Currency/semantic symbol explicitly authorized by user. Preserve the enclosing object and recognizable symbol; omit invoice text lines, bill ornaments, and device controls to keep the symbol clear. Related Lucide originals and atomic views: dollar-sign, euro, pound-sterling, japanese-yen, bitcoin, circle-question-mark, info. Typed contours share their real attachment points.
Plan: HRECT_L envelope; construct enclosing subject first, then one central symbol.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle
from ._sub_preparation_symbols import bubble, document, wireless_phone, banknote, moneybag, house, monitor, baht, currency, compact, diagonal_dollar
SOURCE_ICON_ID='5fe07eb3-8a47-4dac-8a74-c9f75cebee8a'
SOURCE_PATH='pictographic-primitives/other/money bill yuan_5fe07eb3-8a47-4dac-8a74-c9f75cebee8a.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='yuan-currency-money-bill-solo'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    categories = ('other', 'state', 'primitives-generate')
    tags=('sub icon',)
    keywords=('sub icon', 'yuan currency money bill')
    def build(self):
        banknote(self)
        compact(self,'yen',24,24)
