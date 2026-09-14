"""Virtual coin crypto ethereum (money), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '67825865-6811-4208-a6d5-b06708666fe0'
SOURCE_PATH = 'icons-json/money/virtual coin crypto ethereum_67825865-6811-4208-a6d5-b06708666fe0.json'
AUTHOR = 'json_to_solo'

class VirtualCoinCryptoEthereumMoney(Solo48):
    icon_id = 'virtual-coin-crypto-ethereum-money'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    aliases = ()
    keywords = ('virtual', 'coin', 'crypto', 'ethereum', 'money')

    def build(self):
        self.add_line('sym-e0', (24, 44), (24, 44))
        self.add_line('sym-e1', (24, 44), (8, 32))
        self.add_line('sym-e2', (24, 31), (24, 31))
        self.add_line('sym-e3', (24, 31), (9, 21))
        self.add_bezier('sym-e4', (9, 21), ((8.92, 20.873), (9.08, 21.127), (9, 21)))
        self.add_bezier('sym-e5', (9, 21), ((8.97, 20.791), (9, 20.182), (9, 20)))
        self.add_line('sym-e6', (9, 20), (24, 4))
        self.add_line('sym-e7', (24, 4), (24, 4))
        self.add_line('sym-e8', (24, 4), (39, 20))
        self.add_bezier('sym-e9', (39, 20), ((39, 20.182), (39.03, 20.791), (39, 21)))
        self.add_bezier('sym-e10', (39, 21), ((38.92, 21.127), (39.08, 20.873), (39, 21)))
        self.add_line('sym-e11', (39, 21), (24, 31))
        self.add_line('sym-e12', (40, 32), (24, 44))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1')
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', closed=True)
        self.add_contour('sym-c2', 'sym-e12')
        self.relate('connect', 'sym-c0', 'sym-c2')
