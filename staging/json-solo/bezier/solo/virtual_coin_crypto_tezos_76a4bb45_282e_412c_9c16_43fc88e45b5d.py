"""Virtual coin crypto tezos (money), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '76a4bb45-282e-412c-9c16-43fc88e45b5d'
SOURCE_PATH = 'icons-json/money/virtual coin crypto tezos_76a4bb45-282e-412c-9c16-43fc88e45b5d.json'
AUTHOR = 'json_to_solo'

class VirtualCoinCryptoTezosMoney(Solo48):
    icon_id = 'virtual-coin-crypto-tezos-money'
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
        self.add_bezier('e6', (25, 32), ((22.499, 33.591), (18.728, 33.545), (17.12, 30.564)), ((16.876, 30.109), (16, 29.518), (16, 29)))
        self.add_bezier('e7', (24, 40), ((25.752, 41.736), (28.093, 43.991), (30.602, 43.991)), ((30.677, 44), (30.751, 44), (30.826, 44)), ((30.827, 44), (30.828, 44), (30.829, 44)), ((30.981, 44), (31.133, 43.982), (31.284, 43.982)), ((35.916, 43.982), (39.992, 39.427), (39.992, 34.473)), ((39.992, 34.392), (40, 34.303), (40, 34.222)), ((40, 34.221), (40, 34.219), (40, 34.218)), ((40, 33.964), (39.992, 33.709), (39.992, 33.455)), ((39.992, 29.318), (37.196, 25.282), (33.499, 24.182)), ((32.354, 23.845), (31.128, 23.991), (30, 24)))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e6', 'e3')
        self.add_contour('c3', 'e7', 'e4', 'e5')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
