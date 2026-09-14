"""Virtual coin crypto bytecoin (money), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '257155c1-d52c-4dc8-8a44-b5bad9ac26fd'
SOURCE_PATH = 'icons-json/money/virtual coin crypto bytecoin_257155c1-d52c-4dc8-8a44-b5bad9ac26fd.json'
AUTHOR = 'json_to_solo'

class VirtualCoinCryptoBytecoinMoney(Solo48):
    icon_id = 'virtual-coin-crypto-bytecoin-money'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    aliases = ()
    keywords = ('virtual', 'coin', 'crypto', 'bytecoin', 'money')

    def build(self):
        self.add_line('e0', (6, 24), (13, 24))
        self.add_line('e1', (34, 42), (14, 42))
        self.add_line('e2', (13, 41), (13, 24))
        self.add_line('e3', (35, 24), (13, 24))
        self.add_line('e4', (35, 24), (37, 22))
        self.add_line('e5', (31, 6), (15, 6))
        self.add_line('e6', (13, 8), (13, 24))
        self.add_bezier('e7', (35, 24), ((36.055, 24.385), (36.715, 24.671), (37.672, 25.244)), ((40.126, 26.716), (41.992, 29.686), (41.992, 32.591)), ((41.992, 32.639), (42, 32.68), (42, 32.728)), ((42, 32.728), (42, 32.729), (42, 32.73)), ((42, 32.935), (41.992, 33.139), (41.992, 33.344)), ((41.992, 36.985), (39.3, 40.306), (35.97, 41.525)), ((35.414, 41.73), (34.735, 41.992), (34.129, 41.992)), ((34.08, 41.992), (34.023, 42), (33.974, 42)), ((33.925, 42), (34.049, 42), (34, 42)))
        self.add_bezier('e8', (14, 42), ((13.73, 41.73), (13.27, 41.27), (13, 41)))
        self.add_bezier('e9', (37, 22), ((42, 17.999), (39.824, 9.363), (34.203, 6.818)), ((33.409, 6.458), (32.395, 6.008), (31.495, 6.008)), ((31.454, 6.008), (31.041, 6), (31, 6)))
        self.add_bezier('e10', (15, 6), ((13.797, 6.442), (13.425, 6.814), (13, 8)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e7', 'e1', 'e8', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('c3', 'e4', 'e9', 'e5', 'e10', 'e6')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
