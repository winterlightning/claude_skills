"""House Property Value. Currency/semantic symbol explicitly authorized by user. Preserve the enclosing object and recognizable symbol; omit invoice text lines, bill ornaments, and device controls to keep the symbol clear. Related Lucide originals and atomic views: dollar-sign, euro, pound-sterling, japanese-yen, bitcoin, circle-question-mark, info. Typed contours share their real attachment points.
Plan: SQUARE envelope; construct enclosing subject first, then one central symbol.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle
from ._sub_preparation_symbols import bubble, document, wireless_phone, banknote, moneybag, house, monitor, baht, currency, compact, diagonal_dollar
SOURCE_ICON_ID='ec996bcb-4c1a-4d3c-84fb-8218d5fa19b8'
SOURCE_PATH='pictographic-primitives/symbol/house dollar_ec996bcb-4c1a-4d3c-84fb-8218d5fa19b8.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='house-property-value-solo'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/finance' 
    tags=('sub icon',)
    keywords=('sub icon', 'house property value')
    def build(self):
        house(self)
        compact(self,'dollar',24,31)
