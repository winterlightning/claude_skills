"""Virtual coin crypto neo (money), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '555f1941-497e-4f75-b7d0-9c1ff71ed51f'
SOURCE_PATH = 'icons-json/money/virtual coin crypto neo_555f1941-497e-4f75-b7d0-9c1ff71ed51f.json'
AUTHOR = 'gpt-6'

class VirtualCoinCryptoNeo(Solo48):
    icon_id = 'virtual-coin-crypto-neo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    aliases = ()
    keywords = ('virtual', 'coin', 'crypto', 'neo', 'money')

    def build(self):
        self.add_line('e0', (40, 13), (40, 39))
        self.add_line('e1', (40, 39), (23, 30))
        self.add_line('e2', (8, 12), (23, 20))
        self.add_line('e3', (8, 12), (24, 4))
        self.add_line('e4', (25, 4), (39, 11))
        self.add_line('e5', (39, 11), (23, 20))
        self.add_line('e7', (9, 36), (23, 44))
        self.add_line('e8', (23, 44), (23, 20))
        self.add_line('e9', (39, 11), (40, 13))
        self.add_arc('e10', (24, 4), (25, 4), radius_x=75, radius_y=75, large_arc=False, sweep=False)
        self.add_line('e11', (8, 12), (8, 35))
        self.add_arc('e12', (8, 35), (9, 36), radius_x=1, radius_y=1, large_arc=False, sweep=False)
        self.add_contour('c0', 'e9', 'e0', 'e1', closed=False)
        self.add_contour('c1', 'e2', closed=False)
        self.add_contour('c2', 'e3', 'e10', 'e4', 'e5', closed=False)
        self.add_contour('c3', 'e11', 'e12', 'e7', 'e8', closed=False)
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c0', 'c3')
