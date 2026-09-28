"""Question Speech Bubble. Currency/semantic symbol explicitly authorized by user. Preserve the enclosing object and recognizable symbol; omit invoice text lines, bill ornaments, and device controls to keep the symbol clear. Related Lucide originals and atomic views: dollar-sign, euro, pound-sterling, japanese-yen, bitcoin, circle-question-mark, info. Typed contours share their real attachment points.
Plan: VRECT_L envelope; construct enclosing subject first, then one central symbol.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle
from ._sub_preparation_symbols import bubble, document, wireless_phone, banknote, moneybag, house, monitor, baht, currency, compact, diagonal_dollar
SOURCE_ICON_ID='68af2538-81c2-4191-8424-bca1c4ce8a16'
SOURCE_PATH='pictographic-primitives/messages/messages bubble square question_68af2538-81c2-4191-8424-bca1c4ce8a16.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='question-speech-bubble-solo'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/finance' 
    tags=('sub icon',)
    keywords=('sub icon', 'question speech bubble')
    def build(self):
        bubble(self)
        currency(self,'question',24,21)
