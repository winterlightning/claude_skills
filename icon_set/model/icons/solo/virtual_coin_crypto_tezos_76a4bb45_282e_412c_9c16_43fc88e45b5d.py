"""Virtual coin crypto tezos (money), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '76a4bb45-282e-412c-9c16-43fc88e45b5d'
SOURCE_PATH = 'icons-json/money/virtual coin crypto tezos_76a4bb45-282e-412c-9c16-43fc88e45b5d.json'
AUTHOR = 'json_to_solo'

class VirtualCoinCryptoTezos(Solo48):
    icon_id = 'virtual-coin-crypto-tezos'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    aliases = ()
    keywords = ('virtual', 'coin', 'crypto', 'tezos', 'money')

    def build(self):
        self.add_line('e0', (14, 4), (16, 4))
        self.add_line('e1', (16, 4), (16, 12))
        self.add_line('e2', (8, 12), (16, 12))
        self.add_line('e3', (16, 29), (16, 12))
        self.add_line('e4', (30, 24), (37, 12))
        self.add_line('e5', (37, 12), (16, 12))
        self.add_arc('e6', (25, 32), (16, 29), radius_x=6)
        self.add_arc('e7-1', (24, 40), (31, 44), radius_x=9, sweep=False)
        self.add_arc('e7-2', (31, 44), (35, 43), radius_x=9, sweep=False)
        self.add_arc('e7-3', (35, 43), (39, 39), radius_x=10, sweep=False)
        self.add_line('e7-4', (39, 39), (40, 34))
        self.add_arc('e7-5', (40, 34), (30, 24), radius_x=10, sweep=False)
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e6', 'e3')
        self.add_contour('c3', 'e7-1', 'e7-2', 'e7-3', 'e7-4', 'e7-5', 'e4', 'e5')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
