"""Circular Question Mark Symbol. Currency/semantic symbol explicitly authorized by user. Preserve the enclosing object and recognizable symbol; omit invoice text lines, bill ornaments, and device controls to keep the symbol clear. Related Lucide originals and atomic views: dollar-sign, euro, pound-sterling, japanese-yen, bitcoin, circle-question-mark, info. Typed contours share their real attachment points.
Plan: CIRCLE envelope; construct enclosing subject first, then one central symbol.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle
from ._sub_preparation_symbols import bubble, document, wireless_phone, banknote, moneybag, house, monitor, baht, currency, compact, diagonal_dollar
SOURCE_ICON_ID='c356687a-8779-4296-879a-5477d3e84e2f'
SOURCE_PATH='pictographic-primitives/other/circle question_c356687a-8779-4296-879a-5477d3e84e2f.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='circular-question-mark-symbol-solo'
    keyshape=Keyshape.CIRCLE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/finance' 
    tags=('sub icon',)
    keywords=('sub icon', 'circular question mark symbol')
    def build(self):
        circle(self,'outline',24,24,20)
        currency(self,'question',24,24)
