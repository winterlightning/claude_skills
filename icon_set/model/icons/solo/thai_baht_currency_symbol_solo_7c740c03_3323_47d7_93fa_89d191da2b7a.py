"""Thai Baht Currency Symbol. Currency/semantic symbol explicitly authorized by user. Preserve the enclosing object and recognizable symbol; omit invoice text lines, bill ornaments, and device controls to keep the symbol clear. Related Lucide originals and atomic views: dollar-sign, euro, pound-sterling, japanese-yen, bitcoin, circle-question-mark, info. Typed contours share their real attachment points.
Plan: VRECT_L envelope; construct enclosing subject first, then one central symbol.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle
from ._sub_preparation_symbols import bubble, document, wireless_phone, banknote, moneybag, house, monitor, baht, currency, compact, diagonal_dollar
SOURCE_ICON_ID='7c740c03-3323-47d7-93fa-89d191da2b7a'
SOURCE_PATH='pictographic-primitives/other/baht sign_7c740c03-3323-47d7-93fa-89d191da2b7a.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='thai-baht-currency-symbol-solo'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    categories = ('symbol', 'state', 'other', 'primitives-generate')
    tags=('sub icon',)
    keywords=('sub icon', 'thai baht currency symbol')
    def build(self):
        baht(self)
