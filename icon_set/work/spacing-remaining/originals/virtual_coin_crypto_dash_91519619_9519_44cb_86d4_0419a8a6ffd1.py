'Dash coin: a true circular rim and a clean inner mark with evenly spaced horizontal strokes.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '91519619-9519-44cb-86d4-0419a8a6ffd1'
SOURCE_PATH = 'icons-json/money/virtual coin crypto dash_91519619-9519-44cb-86d4-0419a8a6ffd1.json'
AUTHOR = 'gpt-6'

class VirtualCoinCryptoDash(Solo48):
    icon_id = 'virtual-coin-crypto-dash'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    aliases = ()
    keywords = ('virtual', 'coin', 'crypto', 'dash', 'money')

    def build(self):
        # Dash coin: a true circular rim and a clean inner mark with evenly spaced horizontal strokes.
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
        l('top',(19,15),(29,15))
        a('round',(29,15),(33,19),4)
        p('return',(33,19),(30,33),(18,33))
        link('connect','top','round')
        link('connect','round','return')
        l('dash',(13,24),(23,24))
