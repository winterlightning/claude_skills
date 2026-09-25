"""Virtual coin crypto ethereum (money), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '67825865-6811-4208-a6d5-b06708666fe0'
SOURCE_PATH = 'pictographic-primitives/money/virtual coin crypto ethereum_67825865-6811-4208-a6d5-b06708666fe0.svg'
AUTHOR = 'gpt-6'

class VirtualCoinCryptoEthereum(Solo48):
    icon_id = 'virtual-coin-crypto-ethereum'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    categories = ('primitives', 'money')
    aliases = ()
    keywords = ('virtual', 'coin', 'crypto', 'ethereum', 'money')

    def build(self):
        self.add_line('sym-e1', (24, 44), (8, 32))
        self.add_line('sym-e3', (24, 31), (9, 21))
        self.add_line('sym-e5', (9, 21), (9, 20))
        self.add_line('sym-e6', (9, 20), (24, 4))
        self.add_line('sym-e8', (24, 4), (39, 20))
        self.add_line('sym-e9', (39, 20), (39, 21))
        self.add_line('sym-e11', (39, 21), (24, 31))
        self.add_line('sym-e12', (40, 32), (24, 44))
        self.add_contour('sym-c0', 'sym-e1', closed=False)
        self.add_contour('sym-c1', 'sym-e3', 'sym-e5', 'sym-e6', 'sym-e8', 'sym-e9', 'sym-e11', closed=True)
        self.add_contour('sym-c2', 'sym-e12', closed=False)
        self.relate('connect', 'sym-c0', 'sym-c2')
