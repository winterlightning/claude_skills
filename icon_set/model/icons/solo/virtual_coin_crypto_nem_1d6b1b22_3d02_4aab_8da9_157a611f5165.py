"""Virtual coin crypto nem (money), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1d6b1b22-3d02-4aab-8da9-157a611f5165'
SOURCE_PATH = 'icons-json/money/virtual coin crypto nem_1d6b1b22-3d02-4aab-8da9-157a611f5165.json'
AUTHOR = 'json_to_solo'

class VirtualCoinCryptoNem(Solo48):
    icon_id = 'virtual-coin-crypto-nem'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    aliases = ()
    keywords = ('virtual', 'coin', 'crypto', 'nem', 'money')

    def build(self):
        self.add_line('e0', (31, 26), (25, 21))
        self.add_line('e1', (25, 21), (26, 14))
        self.add_line('e2', (9, 26), (8, 24))
        self.add_line('e3', (35, 33), (38, 28))
        self.add_line('e4', (25, 21), (22, 23))
        self.add_bezier('e5', (35, 33), ((34.002, 30.783), (32.923, 27.645), (31, 26)))
        self.add_bezier('e6', (26, 14), ((26.335, 11.333), (27.658, 9.242), (29, 7)))
        self.add_bezier('e7', (35, 33), ((34.746, 33.385), (34.015, 33.745), (33.728, 34.121)), ((31.904, 36.477), (29.883, 38.506), (27.445, 40.225)), ((26.684, 40.765), (25.162, 42), (24.245, 42)), ((24.244, 42), (24.243, 42), (24.242, 42)), ((24.169, 42), (24.089, 42), (24.016, 42)), ((22.691, 42), (20.367, 40.004), (19.255, 39.169)), ((14.828, 35.847), (11.324, 30.975), (9, 26)))
        self.add_bezier('e8', (38, 28), ((38.491, 27.264), (38.735, 26.487), (39.12, 25.685)), ((40.895, 21.995), (41.992, 17.905), (41.992, 13.789)), ((41.992, 13.717), (42, 13.636), (42, 13.563)), ((42, 13.562), (42, 13.561), (42, 13.56)), ((42, 13.265), (41.992, 12.963), (41.992, 12.668)), ((41.992, 10.803), (40.454, 10.017), (38.965, 9.314)), ((35.79, 7.816), (32.436, 7.491), (29, 7)))
        self.add_bezier('e9', (22, 23), ((21.411, 23.589), (20.547, 24.442), (19.786, 24.794)), ((17.095, 26.021), (14.018, 26.078), (11.22, 25.162)), ((10.312, 24.867), (8.769, 24.327), (8, 24)))
        self.add_bezier('e10', (8, 24), ((6.658, 20.711), (6.008, 17.209), (6.008, 13.625)), ((6.008, 13.513), (6, 13.4), (6, 13.287)), ((6, 13.285), (6, 13.284), (6, 13.282)), ((6, 12.946), (6.008, 12.619), (6.008, 12.284)), ((6.008, 10.574), (8.095, 9.845), (9.379, 9.207)), ((12.382, 7.702), (15.663, 6.818), (18.976, 6.327)), ((19.835, 6.196), (20.719, 6.016), (21.595, 6.016)), ((21.758, 6.016), (21.93, 6), (22.094, 6)), ((22.096, 6), (22.098, 6), (22.1, 6)), ((22.228, 6), (22.349, 6.008), (22.478, 6.008)), ((23.255, 6.008), (24.033, 6.18), (24.802, 6.278)), ((26.168, 6.458), (27.634, 6.82), (29, 7)))
        self.add_contour('c0', 'e5', 'e0', 'e1', 'e6')
        self.add_contour('c1', 'e7', 'e2')
        self.add_contour('c2', 'e3', 'e8')
        self.add_contour('c3', 'e4', 'e9')
        self.add_contour('c4', 'e10')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c3', 'c4')
