'Euro: one smooth semicircle with parallel crossbars 8 units apart.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '97a90c1d-c6ec-4a14-bf95-871280f765d5'
SOURCE_PATH = 'pictographic-primitives/money/currency euro_97a90c1d-c6ec-4a14-bf95-871280f765d5.svg'
AUTHOR = 'gpt-6'

class CurrencyEuro(Solo48):
    icon_id = 'currency-euro'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    aliases = ()
    keywords = ('currency', 'euro', 'money')

    def build(self):
        # Euro: one smooth semicircle with parallel crossbars 8 units apart.
        l = self.add_line
        p = self.add_polyline
        link = self.relate

        def a(name, start, end, rx, ry=None, sweep=True):
            self.add_arc(name, start, end, radius_x=rx,
                         radius_y=rx if ry is None else ry, sweep=sweep)

        a('euro',(40,4),(40,44),20,20,sweep=False)
        l('upper',(8,20),(30,20))
        l('lower',(8,28),(30,28))
        link('connect','euro','upper')
        link('connect','euro','lower')
