"""Virtual coin crypto theta (money), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5edd978b-2940-4a04-a431-c81f9ac66790'
SOURCE_PATH = 'icons-json/money/virtual coin crypto theta_5edd978b-2940-4a04-a431-c81f9ac66790.json'
AUTHOR = 'json_to_solo'

class VirtualCoinCryptoThetaMoney(Solo48):
    icon_id = 'virtual-coin-crypto-theta-money'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    aliases = ()
    keywords = ('virtual', 'coin', 'crypto', 'theta', 'money')

    def build(self):
        self.add_line('e0', (24, 13), (24, 18))
        self.add_line('e1', (18, 18), (24, 18))
        self.add_line('e2', (30, 18), (24, 18))
        self.add_line('e3', (18, 29), (24, 29))
        self.add_line('e4', (24, 34), (24, 29))
        self.add_line('e5', (29, 29), (24, 29))
        self.add_line('e6', (38, 4), (10, 4))
        self.add_line('e7', (8, 7), (8, 41))
        self.add_line('e8', (10, 44), (37, 44))
        self.add_line('e9', (40, 41), (40, 7))
        self.add_bezier('e10', (10, 4), ((9.78, 4.118), (9.56, 4.109), (9.36, 4.264)), ((8.66, 4.8), (8.01, 5.709), (8.01, 6.564)), ((8.01, 6.618), (8, 6.945), (8, 7)))
        self.add_bezier('e11', (8, 41), ((8, 41.073), (8, 41.418), (8.01, 41.5)), ((8.01, 42.173), (8.92, 43.982), (9.87, 43.982)), ((9.91, 43.991), (9.96, 43.991), (10, 44)))
        self.add_bezier('e12', (37, 44), ((37.28, 43.918), (37.54, 43.927), (37.82, 43.818)), ((38.83, 43.391), (40, 42.091), (40, 41)))
        self.add_bezier('e13', (40, 7), ((40, 6.927), (39.99, 6.591), (39.99, 6.527)), ((39.99, 5.655), (39.37, 4.745), (38.6, 4.273)), ((38.46, 4.191), (38.33, 4.1), (38.19, 4.009)), ((38.13, 4.009), (38.07, 4), (38.01, 4)), ((38.01, 4), (38, 4), (38, 4)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.add_contour('c5', 'e5')
        self.add_contour('c6', 'e6', 'e10', 'e7', 'e11', 'e8', 'e12', 'e9', 'e13', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c4', 'c5')
