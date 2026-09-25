"""Euro Currency Message Bubble. Currency/semantic symbol explicitly authorized by user. Preserve the enclosing object and recognizable symbol; omit invoice text lines, bill ornaments, and device controls to keep the symbol clear. Related Lucide originals and atomic views: dollar-sign, euro, pound-sterling, japanese-yen, bitcoin, circle-question-mark, info. Typed contours share their real attachment points.
Plan: VRECT_L envelope; construct enclosing subject first, then one central symbol.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle
from ._sub_preparation_symbols import bubble, document, wireless_phone, banknote, moneybag, house, monitor, baht, currency, compact, diagonal_dollar
SOURCE_ICON_ID='49b4a1e0-42a5-42a0-917b-1ab0956b857f'
SOURCE_PATH='pictographic-primitives/other/message euro sign lines_49b4a1e0-42a5-42a0-917b-1ab0956b857f.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='euro-currency-message-bubble-solo'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    categories = ('other', 'state', 'primitives-generate')
    tags=('sub icon',)
    keywords=('sub icon', 'euro currency message bubble')
    def build(self):
        bubble(self)
        currency(self,'euro',24,21)
