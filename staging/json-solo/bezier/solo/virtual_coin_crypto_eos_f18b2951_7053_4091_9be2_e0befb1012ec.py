"""Virtual coin crypto eos (finance), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f18b2951-7053-4091-9be2-e0befb1012ec'
SOURCE_PATH = 'icons-json/finance/virtual coin crypto eos_f18b2951-7053-4091-9be2-e0befb1012ec.json'
AUTHOR = 'json_to_solo'

class VirtualCoinCryptoEosFinance(Solo48):
    icon_id = 'virtual-coin-crypto-eos-finance'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'finance'
    aliases = ()
    keywords = ('virtual', 'coin', 'crypto', 'eos', 'finance')

    def build(self):
        self.add_line('e0', (34, 16), (37, 26))
        self.add_line('e1', (37, 26), (40, 35))
        self.add_line('e2', (40, 35), (23, 44))
        self.add_line('e3', (34, 16), (24, 40))
        self.add_line('e4', (34, 16), (25, 4))
        self.add_line('e5', (24, 4), (13, 16))
        self.add_line('e6', (24, 40), (23, 44))
        self.add_line('e7', (23, 44), (8, 35))
        self.add_line('e8', (8, 35), (13, 16))
        self.add_line('e9', (24, 40), (13, 16))
        self.add_bezier('e10', (25, 4), ((24.67, 4), (24.33, 4), (24, 4)))
        self.add_contour('c0', 'e0', 'e1', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4', 'e10', 'e5')
        self.add_contour('c3', 'e6', 'e7', 'e8')
        self.add_contour('c4', 'e9')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c3', 'c4')
