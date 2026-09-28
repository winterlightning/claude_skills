'Peercoin: a smooth circular P bowl and a separate crossbar 8 units below it.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e015513e-29e5-48ae-ad99-806d5a1b0b1e'
SOURCE_PATH = 'pictographic-primitives/symbol/peercoin_e015513e-29e5-48ae-ad99-806d5a1b0b1e.svg'
AUTHOR = 'gpt-6'

class Peercoin(Solo48):
    icon_id = 'peercoin'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    categories = ('symbol',)
    aliases = ()
    keywords = ('peercoin', 'symbol')

    def build(self):
        # Peercoin: a smooth circular P bowl and a separate crossbar 8 units below it.
        l = self.add_line
        p = self.add_polyline
        link = self.relate

        def a(name, start, end, rx, ry=None, sweep=True):
            self.add_arc(name, start, end, radius_x=rx,
                         radius_y=rx if ry is None else ry, sweep=sweep)

        l('stem',(16,44),(16,4))
        l('top',(16,4),(28,4))
        a('bowl',(28,4),(28,28),12)
        l('return',(28,28),(16,28))
        self.add_contour('p','stem','top','bowl','return')
        l('bar',(8,36),(32,36))
        link('connect','p','bar')
