"""Yen Currency Message Bubble. Currency/semantic symbol explicitly authorized by user. Preserve the enclosing object and recognizable symbol; omit invoice text lines, bill ornaments, and device controls to keep the symbol clear. Related Lucide originals and atomic views: dollar-sign, euro, pound-sterling, japanese-yen, bitcoin, circle-question-mark, info. Typed contours share their real attachment points.
Plan: VRECT_L envelope; construct enclosing subject first, then one central symbol.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._payments_batch01 import circle
from icon_set.model.icons.solo._sub_preparation_symbols import bubble, document, wireless_phone, banknote, moneybag, house, monitor, baht, currency, compact, diagonal_dollar
SOURCE_ICON_ID='16791ce0-2910-4e3b-82ee-8dcb1834e398'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__yen-currency-message-bubble-solo/20260927T145855Z-thuan-mac-1/reference/message yuan sign lines_16791ce0-2910-4e3b-82ee-8dcb1834e398.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='yen-currency-message-bubble-solo'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    categories = ('state', 'other', 'primitives-generate')
    tags=('sub icon',)
    keywords=('sub icon', 'yen currency message bubble')
    def build(self):
        bubble(self)
        currency(self,'yen',22,21)
