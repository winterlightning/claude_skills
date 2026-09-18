"""Money Bag with Dollar Sign. Currency/semantic symbol explicitly authorized by user. Preserve the enclosing object and recognizable symbol; omit invoice text lines, bill ornaments, and device controls to keep the symbol clear. Related Lucide originals and atomic views: dollar-sign, euro, pound-sterling, japanese-yen, bitcoin, circle-question-mark, info. Typed contours share their real attachment points.
Plan: VRECT_L envelope; construct enclosing subject first, then one central symbol.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle
from ._sub_preparation_symbols import bubble, document, wireless_phone, banknote, moneybag, house, monitor, baht, currency, compact, diagonal_dollar
SOURCE_ICON_ID='e362c0ea-dba3-4194-90fc-c3ab21b70d2b'
SOURCE_PATH='pictographic-primitives/other/pouch dollar_e362c0ea-dba3-4194-90fc-c3ab21b70d2b.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='money-bag-with-dollar-sign-solo'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/finance' 
    tags=('sub icon',)
    keywords=('sub icon', 'money bag with dollar sign')
    def build(self):
        moneybag(self)
        compact(self,'dollar',24,26)
