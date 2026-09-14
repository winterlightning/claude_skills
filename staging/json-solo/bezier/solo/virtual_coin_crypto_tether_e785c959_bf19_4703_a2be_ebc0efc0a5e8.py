"""Virtual coin crypto tether (money), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e785c959-bf19-4703-a2be-ebc0efc0a5e8'
SOURCE_PATH = 'icons-json/money/virtual coin crypto tether_e785c959-bf19-4703-a2be-ebc0efc0a5e8.json'
AUTHOR = 'json_to_solo'

class VirtualCoinCryptoTetherMoney(Solo48):
    icon_id = 'virtual-coin-crypto-tether-money'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    aliases = ()
    keywords = ('virtual', 'coin', 'crypto', 'tether', 'money')

    def build(self):
        self.add_line('e0', (6, 6), (24, 6))
        self.add_line('e1', (24, 21), (24, 6))
        self.add_line('e2', (41, 6), (24, 6))
        self.add_line('e3', (24, 42), (24, 37))
        self.add_bezier('e4', (38, 21), ((39.072, 21.188), (41.984, 22.118), (41.984, 23.885)), ((41.992, 23.966), (42, 24.039), (42, 24.111)), ((42, 24.112), (42, 24.113), (42, 24.115)), ((42, 26.635), (37.435, 27.895), (35.504, 28.402)), ((28.901, 30.128), (20.326, 30.153), (13.666, 28.647)), ((11.539, 28.165), (9.461, 27.6), (7.587, 26.455)), ((7.178, 26.201), (6, 25.227), (6, 24.687)), ((6, 24.515), (6.016, 24.344), (6.016, 24.172)), ((6.016, 22.724), (8.217, 21.415), (9.461, 20.981)), ((9.567, 20.948), (9.854, 20.752), (9.935, 20.752)), ((9.968, 20.785), (9.993, 20.809), (10.025, 20.842)), ((10.05, 20.801), (9.975, 21.041), (10, 21)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e4')
        self.add_contour('c4', 'e3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
