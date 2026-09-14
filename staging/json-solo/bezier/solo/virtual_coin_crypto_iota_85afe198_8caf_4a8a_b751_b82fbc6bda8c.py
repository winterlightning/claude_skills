"""Virtual coin crypto iota (finance), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '85afe198-8caf-4a8a-b751-b82fbc6bda8c'
SOURCE_PATH = 'icons-json/finance/virtual coin crypto iota_85afe198-8caf-4a8a-b751-b82fbc6bda8c.json'
AUTHOR = 'json_to_solo'

class VirtualCoinCryptoIotaFinance(Solo48):
    icon_id = 'virtual-coin-crypto-iota-finance'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'finance'
    aliases = ()
    keywords = ('virtual', 'coin', 'crypto', 'iota', 'finance')

    def build(self):
        self.add_bezier('e0', (17, 8), ((18.53, 7.264), (20.433, 6.016), (22.167, 6.016)), ((22.306, 6.016), (22.445, 6), (22.593, 6)), ((22.595, 6), (22.598, 6), (22.601, 6)), ((22.77, 6), (22.947, 6.008), (23.125, 6.008)), ((24.376, 6.008), (25.8, 6.442), (26.97, 6.867)), ((29.04, 7.612), (31.061, 8.872), (32.305, 10.737)), ((34.865, 14.575), (33.843, 20.335), (30.775, 23.615)), ((29.989, 24.458), (28.998, 25.435), (28, 26)))
        self.add_bezier('e1', (9, 34), ((7.265, 31.701), (6.016, 28.729), (6.016, 25.759)), ((6.016, 25.55), (6, 25.332), (6, 25.123)), ((6, 25.119), (6, 25.116), (6, 25.113)), ((6, 24.998), (6.016, 24.892), (6.016, 24.777)), ((6.016, 23.558), (6.303, 22.274), (6.687, 21.12)), ((9.436, 12.873), (18.569, 13.825), (25, 17)))
        self.add_bezier('e2', (26, 32), ((32.455, 33.988), (38.662, 31.814), (41.084, 25.121)), ((41.517, 23.918), (41.992, 22.445), (41.992, 21.161)), ((41.992, 21.048), (42, 20.935), (42, 20.823)), ((42, 20.821), (42, 20.819), (42, 20.817)), ((42, 20.711), (41.984, 20.605), (41.984, 20.49)), ((41.984, 19.238), (41.286, 18.219), (41, 17)))
        self.add_bezier('e3', (19, 23), ((17.486, 25.528), (16.489, 28.377), (16.571, 31.372)), ((16.726, 37.156), (22.274, 41.992), (27.96, 41.992)), ((28.075, 41.992), (28.181, 42), (28.295, 42)), ((28.77, 42), (29.525, 42), (30, 42)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
