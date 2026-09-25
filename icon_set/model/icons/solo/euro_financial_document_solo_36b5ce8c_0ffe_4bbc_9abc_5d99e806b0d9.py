"""Euro Financial Document. Currency/semantic symbol explicitly authorized by user. Preserve the enclosing object and recognizable symbol; omit invoice text lines, bill ornaments, and device controls to keep the symbol clear. Related Lucide originals and atomic views: dollar-sign, euro, pound-sterling, japanese-yen, bitcoin, circle-question-mark, info. Typed contours share their real attachment points.
Plan: VRECT_L envelope; construct enclosing subject first, then one central symbol.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle
from ._sub_preparation_symbols import bubble, document, wireless_phone, banknote, moneybag, house, monitor, baht, currency, compact, diagonal_dollar
SOURCE_ICON_ID='36b5ce8c-0ffe-4bbc-9abc-5d99e806b0d9'
SOURCE_PATH='pictographic-primitives/other/euro bill_36b5ce8c-0ffe-4bbc-9abc-5d99e806b0d9.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='euro-financial-document-solo'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    tags=('sub icon',)
    keywords=('sub icon', 'euro financial document')
    def build(self):
        document(self)
        currency(self,'euro',24,26)
