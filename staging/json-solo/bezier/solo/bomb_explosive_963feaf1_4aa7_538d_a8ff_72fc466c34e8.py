"""Bomb explosive (war), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '963feaf1-4aa7-538d-a8ff-72fc466c34e8'
SOURCE_PATH = 'icons-json/war/bomb explosive_963feaf1-4aa7-538d-a8ff-72fc466c34e8.json'
AUTHOR = 'json_to_solo'

class BombExplosiveWar(Solo48):
    icon_id = 'bomb-explosive-war'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'war'
    aliases = ()
    keywords = ('bomb', 'explosive', 'war')

    def build(self):
        self.add_line('e0', (32, 40), (32, 17))
        self.add_line('e1', (29, 14), (24, 14))
        self.add_line('e2', (24, 42), (24, 15))
        self.add_line('e3', (16, 14), (16, 42))
        self.add_line('e4', (20, 12), (21, 8))
        self.add_line('e5', (35, 7), (37, 10))
        self.add_line('e6', (16, 14), (11, 14))
        self.add_line('e7', (8, 17), (8, 39))
        self.add_line('e8', (11, 42), (15, 42))
        self.add_bezier('e9', (24, 42), ((25.71, 41.991), (29.99, 42.609), (31.4, 41.427)), ((31.72, 41.164), (31.83, 40.336), (32, 40)))
        self.add_bezier('e10', (32, 17), ((32, 15.209), (30.89, 14), (29, 14)))
        self.add_bezier('e11', (24, 42), ((23.26, 43.318), (22.99, 44), (21.15, 44)), ((21.131, 44), (21.112, 44), (21.094, 44)), ((19.913, 44), (18.731, 43.991), (17.55, 43.991)), ((16.84, 43.991), (16.47, 43.4), (16, 43)))
        self.add_bezier('e12', (24, 15), ((24, 14.7), (24, 14.3), (24, 14)), ((23.91, 12.136), (21.45, 12.173), (20, 12.182)), ((18.28, 12.2), (16, 11.736), (16, 14)))
        self.add_bezier('e13', (21, 8), ((22.17, 5.964), (23.85, 4.009), (26.58, 4.009)), ((27.446, 4.009), (28.312, 4), (29.179, 4)), ((29.192, 4), (29.206, 4), (29.22, 4)), ((29.29, 4), (29.36, 4.009), (29.44, 4.009)), ((31.82, 4.009), (33.87, 4.955), (35, 7)))
        self.add_bezier('e14', (37, 10), ((37.63, 11.145), (38.83, 12.373), (40, 13)))
        self.add_bezier('e15', (11, 14), ((9.66, 14), (8.01, 14.709), (8.01, 16.145)), ((8.01, 16.2), (8, 16.255), (8, 16.3)), ((8, 16.445), (8, 16.855), (8, 17)))
        self.add_bezier('e16', (8, 39), ((8, 39.127), (8, 39.718), (8, 39.845)), ((8, 41.3), (9.62, 42), (11, 42)))
        self.add_contour('c0', 'e9', 'e0', 'e10', 'e1')
        self.add_contour('c1', 'e11')
        self.add_contour('c2', 'e2', 'e12', 'e3')
        self.add_contour('c3', 'e4', 'e13', 'e5', 'e14')
        self.add_contour('c4', 'e6', 'e15', 'e7', 'e16', 'e8')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c3', 'c2')
