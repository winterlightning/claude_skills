"""Mobile Contactless Payment. Currency/semantic symbol explicitly authorized by user. Preserve the enclosing object and recognizable symbol; omit invoice text lines, bill ornaments, and device controls to keep the symbol clear. Related Lucide originals and atomic views: dollar-sign, euro, pound-sterling, japanese-yen, bitcoin, circle-question-mark, info. Typed contours share their real attachment points.
Plan: VRECT_L envelope; construct enclosing subject first, then one central symbol.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._payments_batch01 import compact_currency
from icon_set.model.icons.solo._sub_preparation_symbols import bubble, document, wireless_phone, banknote, moneybag, house, monitor, baht, currency, compact, diagonal_dollar
SOURCE_ICON_ID='8d317b81-2d88-4d5c-9090-0c063df565b3'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__mobile-contactless-payment-solo/20260927T153322Z-thuan-mac-1/reference/mobile phone dollar sign wireless_8d317b81-2d88-4d5c-9090-0c063df565b3.svg'
AUTHOR="gpt-6"
class Drawing(Solo48):
    icon_id='mobile-contactless-payment-solo'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    categories = ('state', 'other', 'primitives-generate')
    tags=('sub icon',)
    keywords=('sub icon', 'mobile contactless payment')
    def build(self):
        # Two wireless arcs over a handset, with a compact currency mark inside.
        wireless_phone(self)
        self.add_bezier('signal-inner',(17,14),((21,12),(27,12),(31,14)))
        self.add_polyline('dollar',(28,22),(20,22),(28,28),(20,34),(28,34))
        self.add_line('dollar-stem-top',(24,21),(24,22))
        self.add_line('dollar-stem-bottom',(24,34),(24,35))
        self.relate('connect','dollar','dollar-stem-top','dollar-stem-bottom')
