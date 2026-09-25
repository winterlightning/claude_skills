'Tapered basket: symmetric sides, a clear handle and a single clean rim.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0a53e128-acca-4f35-86c4-09a5c10e5d62'
SOURCE_PATH = 'pictographic-primitives/shopping/shopping basket 1_0a53e128-acca-4f35-86c4-09a5c10e5d62.svg'
AUTHOR = 'gpt-6'

class ShoppingBasket1(Solo48):
    icon_id = 'shopping-basket-1'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shopping'
    categories = ('shopping', 'primitives')
    aliases = ()
    keywords = ('shopping', 'basket')

    def build(self):
        # Tapered basket: symmetric sides, a clear handle and a single clean rim.
        l = self.add_line
        p = self.add_polyline
        link = self.relate

        def a(name, start, end, rx, ry=None, sweep=True):
            self.add_arc(name, start, end, radius_x=rx,
                         radius_y=rx if ry is None else ry, sweep=sweep)

        p('body',(8,16),(12,42),(36,42),(40,16))
        l('rim',(6,16),(42,16))
        p('handle',(16,16),(16,6),(32,6),(32,16))
        link('connect','body','rim')
        link('connect','handle','rim')
