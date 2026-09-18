"""Financial Candlestick Chart. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = '0baca945-4ec6-4025-95ae-cd2fad5c8bac'
SOURCE_PATH = 'pictographic-primitives/other/trading_0baca945-4ec6-4025-95ae-cd2fad5c8bac.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'financial-candlestick-chart-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    tags = ('sub icon',)
    keywords = ('sub icon', 'financial candlestick chart')
    def build(self):
        for x,y in ((10,26),(24,18),(38,10)):
         rounded_rect(self,'body-'+str(x),x-4,y,x+4,y+12,2)
         self.add_line('wick-top-'+str(x),(x,y-4),(x,y))
         self.add_line('wick-bottom-'+str(x),(x,y+12),(x,y+16))
         self.relate('connect','body-'+str(x),'wick-top-'+str(x),'wick-bottom-'+str(x))
