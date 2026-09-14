'Layered currency: regular diamonds and separated layer strokes with deliberate straight edges.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '573e6276-1546-4e04-a069-78d9e36ee390'
SOURCE_PATH = 'icons-json/design/virtual coin cyrpto currency_573e6276-1546-4e04-a069-78d9e36ee390.json'
AUTHOR = 'gpt-6'

class VirtualCoinCyrptoCurrency(Solo48):
    icon_id = 'virtual-coin-cyrpto-currency'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('virtual', 'coin', 'cyrpto', 'currency', 'design')

    def build(self):
        # Layered currency: one clear diamond and two equally spaced lower layers, preserving all three levels.
        l = self.add_line
        p = self.add_polyline
        link = self.relate

        def a(name, start, end, rx, ry=None, sweep=True):
            self.add_arc(name, start, end, radius_x=rx,
                         radius_y=rx if ry is None else ry, sweep=sweep)

        p('top',(8,12),(24,4),(40,12),(24,20),(8,12))
        p('middle',(8,24),(24,32),(40,24))
        p('bottom',(8,36),(24,44),(40,36))
