"""British Pound Sterling Message Bubble. Currency/semantic symbol explicitly authorized by user. Preserve the enclosing object and recognizable symbol; omit invoice text lines, bill ornaments, and device controls to keep the symbol clear. Related Lucide originals and atomic views: dollar-sign, euro, pound-sterling, japanese-yen, bitcoin, circle-question-mark, info. Typed contours share their real attachment points.
Plan: VRECT_L envelope; construct enclosing subject first, then one central symbol.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle
from ._sub_preparation_symbols import bubble, document, wireless_phone, banknote, moneybag, house, monitor, baht, currency, compact, diagonal_dollar
SOURCE_ICON_ID='c6889dfd-e645-43b6-bcaf-969ba67629d7'
SOURCE_PATH='pictographic-primitives/other/message pound sign lines_c6889dfd-e645-43b6-bcaf-969ba67629d7.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='british-pound-sterling-message-bubble-solo'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    tags=('sub icon',)
    keywords=('sub icon', 'british pound sterling message bubble')
    def build(self):
        bubble(self)
        currency(self,'pound',24,21)
