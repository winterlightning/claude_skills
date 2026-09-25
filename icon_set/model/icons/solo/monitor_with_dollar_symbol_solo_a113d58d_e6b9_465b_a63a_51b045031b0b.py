"""Monitor with Dollar Symbol. Currency/semantic symbol explicitly authorized by user. Preserve the enclosing object and recognizable symbol; omit invoice text lines, bill ornaments, and device controls to keep the symbol clear. Related Lucide originals and atomic views: dollar-sign, euro, pound-sterling, japanese-yen, bitcoin, circle-question-mark, info. Typed contours share their real attachment points.
Plan: VRECT_L envelope; construct enclosing subject first, then one central symbol.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle
from ._sub_preparation_symbols import bubble, document, wireless_phone, banknote, moneybag, house, monitor, baht, currency, compact, diagonal_dollar
SOURCE_ICON_ID='a113d58d-e6b9-465b-a63a-51b045031b0b'
SOURCE_PATH='pictographic-primitives/symbol/monitor dollar sign_a113d58d-e6b9-465b-a63a-51b045031b0b.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='monitor-with-dollar-symbol-solo'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'symbol'
    categories = ('symbol', 'state')
    tags=('sub icon',)
    keywords=('sub icon', 'monitor with dollar symbol')
    def build(self):
        monitor(self)
        compact(self,'dollar',24,22)
