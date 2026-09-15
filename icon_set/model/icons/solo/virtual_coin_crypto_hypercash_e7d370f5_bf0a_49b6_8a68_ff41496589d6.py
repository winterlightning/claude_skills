'Hypercash: consistent double stems and a clean angular currency body.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e7d370f5-bf0a-49b6-8a68-ff41496589d6'
SOURCE_PATH = 'pictographic-primitives/money/virtual coin crypto hypercash_e7d370f5-bf0a-49b6-8a68-ff41496589d6.svg'
AUTHOR = 'gpt-6'

class VirtualCoinCryptoHypercash(Solo48):
    icon_id = 'virtual-coin-crypto-hypercash'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    aliases = ()
    keywords = ('virtual', 'coin', 'crypto', 'hypercash', 'money')

    def build(self):
        # Hypercash: consistent double stems and a clean angular currency body.
        l = self.add_line
        p = self.add_polyline
        link = self.relate

        def a(name, start, end, rx, ry=None, sweep=True):
            self.add_arc(name, start, end, radius_x=rx,
                         radius_y=rx if ry is None else ry, sweep=sweep)

        for x in (20,28):
            l(f'stem-{x}',(x,6),(x,42))
        p('outline',(42,18),(42,14),(14,14),(6,24),(14,34),(42,34),(42,30))
        l('bar',(14,24),(28,24))
        for x in (20,28):
            link('connect',f'stem-{x}','outline')
            link('connect',f'stem-{x}','bar')
