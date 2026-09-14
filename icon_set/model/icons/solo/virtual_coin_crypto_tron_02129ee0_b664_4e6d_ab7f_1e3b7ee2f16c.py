"""Virtual coin crypto tron (money), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '02129ee0-b664-4e6d-ab7f-1e3b7ee2f16c'
SOURCE_PATH = 'icons-json/money/virtual coin crypto tron_02129ee0-b664-4e6d-ab7f-1e3b7ee2f16c.json'
AUTHOR = 'json_to_solo'

class VirtualCoinCryptoTron(Solo48):
    icon_id = 'virtual-coin-crypto-tron'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    aliases = ()
    keywords = ('virtual', 'coin', 'crypto', 'tron', 'money')

    def build(self):
        self.add_line('e0', (21, 44), (21, 20))
        self.add_line('e1', (8, 4), (21, 20))
        self.add_line('e2', (40, 17), (36, 10))
        self.add_line('e3', (34, 9), (8, 4))
        self.add_line('e4', (8, 4), (19, 39))
        self.add_line('e5', (19, 39), (21, 44))
        self.add_line('e6', (21, 44), (31, 30))
        self.add_line('e7', (31, 30), (40, 17))
        self.add_line('e8', (40, 17), (21, 20))
        self.add_arc('e9', (36, 10), (34, 9), radius_x=3, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e9', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
