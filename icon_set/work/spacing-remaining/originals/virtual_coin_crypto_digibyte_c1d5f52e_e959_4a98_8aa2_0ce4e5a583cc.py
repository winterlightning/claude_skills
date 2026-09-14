'Digibyte coin: circular rim, a smooth D bowl and regularly spaced currency ticks.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c1d5f52e-e959-4a98-8aa2-0ce4e5a583cc'
SOURCE_PATH = 'icons-json/money/virtual coin crypto digibyte_c1d5f52e-e959-4a98-8aa2-0ce4e5a583cc.json'
AUTHOR = 'gpt-6'

class VirtualCoinCryptoDigibyte(Solo48):
    icon_id = 'virtual-coin-crypto-digibyte'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    aliases = ()
    keywords = ('virtual', 'coin', 'crypto', 'digibyte', 'money')

    def build(self):
        # Digibyte: true circular rim, a clean D counter and short external currency ticks.
        l = self.add_line
        p = self.add_polyline
        link = self.relate

        def a(name, start, end, rx, ry=None, sweep=True):
            self.add_arc(name, start, end, radius_x=rx,
                         radius_y=rx if ry is None else ry, sweep=sweep)

        def c(name, x, y, radius):
            a(name+'-top', (x-radius,y), (x+radius,y), radius)
            a(name+'-bottom', (x+radius,y), (x-radius,y), radius)
            self.add_contour(name, name+'-top', name+'-bottom', closed=True)

        c('coin',24,24,20)
        l('top',(18,16),(26,16))
        a('bowl',(26,16),(26,32),8)
        l('bottom',(26,32),(18,32))
        l('stem',(18,32),(18,16))
        self.add_contour('d','top','bowl','bottom','stem',closed=True)
        # A single pair of currency ticks preserves the emblem without crowding the bowl.
        l('top-tick',(24,13),(24,16))
        l('bottom-tick',(24,32),(24,35))
        link('connect','top-tick','d')
        link('connect','bottom-tick','d')
