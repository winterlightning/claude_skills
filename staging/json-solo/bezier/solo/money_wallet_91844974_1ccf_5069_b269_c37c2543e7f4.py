"""Money wallet (finance), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '91844974-1ccf-5069-b269-c37c2543e7f4'
SOURCE_PATH = 'icons-json/finance/money wallet_91844974-1ccf-5069-b269-c37c2543e7f4.json'
AUTHOR = 'json_to_solo'

class MoneyWalletFinance(Solo48):
    icon_id = 'money-wallet-finance'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'finance'
    aliases = ()
    keywords = ('money', 'wallet', 'finance')

    def build(self):
        self.add_line('e0', (41, 19), (41, 12))
        self.add_line('e1', (37, 8), (9, 8))
        self.add_line('e2', (4, 11), (4, 36))
        self.add_line('e3', (8, 40), (36, 40))
        self.add_line('e4', (41, 34), (41, 28))
        self.add_line('e5', (33, 28), (41, 28))
        self.add_line('e6', (43, 19), (34, 19))
        self.add_bezier('e7', (41, 12), ((41, 9.819), (39.364, 8), (37, 8)))
        self.add_bezier('e8', (9, 8), ((8.873, 8), (8.282, 8), (8.155, 8.008)), ((6.409, 8.008), (4.955, 9.086), (4.282, 10.526)), ((4.164, 10.779), (4, 10.722), (4, 11)))
        self.add_bezier('e9', (4, 36), ((4, 36.135), (4, 36.051), (4.009, 36.185)), ((4.009, 37.853), (6.027, 40), (8, 40)))
        self.add_bezier('e10', (36, 40), ((36.173, 40), (36.164, 39.983), (36.336, 39.983)), ((38.473, 39.983), (40.536, 38.787), (41.1, 36.8)), ((41.336, 35.966), (41, 34.851), (41, 34)))
        self.add_bezier('e11', (34, 19), ((30.482, 19), (29.182, 21.128), (29.382, 24.185)), ((29.5, 25.987), (30.791, 28), (33, 28)))
        self.add_bezier('e12', (41, 28), ((42.264, 28), (43.618, 27.208), (43.909, 26.063)), ((44, 25.364), (43.964, 24.497), (43.991, 23.773)), ((44, 23.663), (44, 23.545), (44, 23.427)), ((44, 23.225), (43.982, 23.015), (43.982, 22.804)), ((43.982, 22.248), (43.982, 21.684), (43.982, 21.12)), ((43.991, 21.036), (43.991, 20.943), (44, 20.859)), ((44, 20.855), (44, 20.851), (44, 20.847)), ((44, 20.598), (44, 20.35), (44, 20.101)), ((44, 19.638), (43.3, 19.303), (43, 19)))
        self.add_contour('c0', 'e0', 'e7', 'e1', 'e8', 'e2', 'e9', 'e3', 'e10', 'e4')
        self.add_contour('c1', 'e11', 'e5', 'e12', 'e6', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
