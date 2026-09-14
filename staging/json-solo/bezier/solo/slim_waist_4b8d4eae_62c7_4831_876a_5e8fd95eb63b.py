"""Slim waist (beauty), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4b8d4eae-62c7-4831-876a-5e8fd95eb63b'
SOURCE_PATH = 'icons-json/beauty/slim waist_4b8d4eae-62c7-4831-876a-5e8fd95eb63b.json'
AUTHOR = 'json_to_solo'

class SlimWaistBeauty(Solo48):
    icon_id = 'slim-waist-beauty'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'beauty'
    aliases = ()
    keywords = ('slim', 'waist', 'beauty')

    def build(self):
        self.add_line('e0', (13, 37), (19, 39))
        self.add_line('e1', (29, 39), (35, 37))
        self.add_line('e2', (16, 18), (20, 17))
        self.add_line('e3', (27, 17), (32, 17))
        self.add_line('e4', (36, 32), (40, 36))
        self.add_line('e5', (21, 6), (23, 8))
        self.add_bezier('e6', (7, 6), ((6.566, 7.031), (6.016, 8.086), (6.016, 9.232)), ((6.016, 9.379), (6, 9.535), (6, 9.682)), ((6, 9.895), (6.016, 10.107), (6.016, 10.32)), ((6.016, 12.701), (7.342, 14.992), (9.125, 16.489)), ((9.927, 17.16), (11.141, 17.419), (12, 18)))
        self.add_bezier('e7', (6, 42), ((6.008, 41.959), (6.008, 41.926), (6.016, 41.894)), ((6.016, 40.601), (7.031, 38.735), (7.726, 37.688)), ((7.939, 37.377), (8.463, 36.535), (8.545, 36.51)), ((9.207, 36.273), (12.092, 36.738), (13, 37)))
        self.add_bezier('e8', (19, 39), ((22.125, 39.892), (25.875, 39.892), (29, 39)))
        self.add_bezier('e9', (35, 37), ((36.645, 36.534), (38.29, 36.131), (40, 36)))
        self.add_bezier('e10', (42, 42), ((42, 41.926), (41.984, 41.861), (41.984, 41.787)), ((41.984, 40.462), (41.043, 38.335), (40.372, 37.222)), ((40.143, 36.862), (40.27, 36.335), (40, 36)))
        self.add_bezier('e11', (41, 6), ((41.393, 6.99), (41.992, 8.062), (41.992, 9.15)), ((41.992, 9.355), (42, 9.559), (42, 9.764)), ((42, 9.829), (41.992, 9.895), (41.992, 9.96)), ((41.992, 12.333), (40.585, 14.599), (38.752, 16.006)), ((37.991, 16.587), (36.843, 16.55), (36, 17)))
        self.add_bezier('e12', (12, 18), ((13.293, 18.147), (14.724, 18.507), (16, 18)))
        self.add_bezier('e13', (20, 17), ((22.291, 16.084), (24.652, 16.607), (27, 17)))
        self.add_bezier('e14', (32, 17), ((33.694, 17.278), (34.208, 17.295), (36, 17)))
        self.add_bezier('e15', (12, 18), ((13.947, 22.189), (14.787, 26.61), (12.562, 30.979)), ((11.719, 32.64), (10.178, 33.568), (9, 35)))
        self.add_bezier('e16', (36, 17), ((35.485, 18.17), (35.168, 19.778), (34.825, 21.014)), ((33.957, 24.147), (33.914, 29.39), (36, 32)))
        self.add_bezier('e17', (23, 8), ((23.237, 8.205), (24.262, 8.667), (24.36, 8.643)), ((24.646, 8.291), (24.933, 7.939), (25.219, 7.587)), ((25.825, 6.843), (26.149, 6.417), (27, 6)))
        self.add_bezier('e18', (24, 32), ((24, 31.73), (24, 31.27), (24, 31)))
        self.add_contour('c0', 'e6')
        self.add_contour('c1', 'e7', 'e0', 'e8', 'e1', 'e9')
        self.add_contour('c2', 'e10')
        self.add_contour('c3', 'e11')
        self.add_contour('c4', 'e12', 'e2', 'e13', 'e3', 'e14')
        self.add_contour('c5', 'e15')
        self.add_contour('c6', 'e16', 'e4')
        self.add_contour('c7', 'e5', 'e17')
        self.add_contour('c8', 'e18')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c0', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c6')
        self.relate('connect', 'c2', 'c6')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c6')
        self.relate('connect', 'c4', 'c6')
