"""Virtual coin crypto nem (money), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1d6b1b22-3d02-4aab-8da9-157a611f5165'
SOURCE_PATH = 'icons-json/money/virtual coin crypto nem_1d6b1b22-3d02-4aab-8da9-157a611f5165.json'
AUTHOR = 'json_to_solo'

class VirtualCoinCryptoNemMoney(Solo48):
    icon_id = 'virtual-coin-crypto-nem-money'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    aliases = ()
    keywords = ('virtual', 'coin', 'crypto', 'nem', 'money')

    def build(self):
        self.add_line('e0', (31, 26), (25, 21))
        self.add_line('e1', (25, 21), (26, 14))
        self.add_line('e2', (9, 26), (8, 24))
        self.add_line('e3', (35, 33), (38, 28))
        self.add_line('e4', (25, 21), (22, 23))
        self.add_line('e5', (35, 33), (31, 26))
        self.add_arc('e6', (26, 14), (29, 7), radius_x=19)
        self.add_arc('e7-1', (35, 33), (24, 42), radius_x=27)
        self.add_arc('e7-2', (24, 42), (9, 26), radius_x=28)
        self.add_arc('e8-1', (38, 28), (42, 14), radius_x=29, sweep=False)
        self.add_line('e8-2', (42, 14), (42, 12))
        self.add_arc('e8-3', (42, 12), (40, 10), radius_x=3, sweep=False)
        self.add_arc('e8-4', (40, 10), (29, 7), radius_x=29, sweep=False)
        self.add_arc('e9', (22, 23), (8, 24), radius_x=13)
        self.add_line('e10-1', (8, 24), (6, 13))
        self.add_arc('e10-2', (6, 13), (10, 9), radius_x=4)
        self.add_arc('e10-3', (10, 9), (22, 6), radius_x=35)
        self.add_arc('e10-4', (22, 6), (29, 7), radius_x=54)
        self.add_contour('c0', 'e5', 'e0', 'e1', 'e6')
        self.add_contour('c1', 'e7-1', 'e7-2', 'e2')
        self.add_contour('c2', 'e3', 'e8-1', 'e8-2', 'e8-3', 'e8-4')
        self.add_contour('c3', 'e4', 'e9')
        self.add_contour('c4', 'e10-1', 'e10-2', 'e10-3', 'e10-4')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c3', 'c4')
