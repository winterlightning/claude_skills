"""Boxing glove (sports), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dbf91214-8ada-5b30-9a04-1c64d7b7b10a'
SOURCE_PATH = 'icons-json/sports/boxing glove_dbf91214-8ada-5b30-9a04-1c64d7b7b10a.json'
AUTHOR = 'json_to_solo'

class BoxingGloveSports(Solo48):
    icon_id = 'boxing-glove-sports'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'sports'
    aliases = ()
    keywords = ('boxing', 'glove', 'sports')

    def build(self):
        self.add_line('e0', (34, 20), (39, 25))
        self.add_line('e1', (15, 44), (32, 44))
        self.add_line('e2', (35, 41), (35, 35))
        self.add_line('e3', (13, 35), (35, 35))
        self.add_line('e4', (13, 35), (10, 31))
        self.add_line('e5', (8, 27), (8, 12))
        self.add_line('e6', (18, 4), (29, 4))
        self.add_line('e7', (40, 11), (40, 26))
        self.add_bezier('e8', (28, 27), ((27.57, 25.464), (26.88, 23.318), (27.71, 21.782)), ((27.9, 21.418), (28.26, 21.091), (28.55, 20.8)), ((30.07, 19.291), (32.26, 18.418), (34, 20)))
        self.add_bezier('e9', (39, 25), ((39.33, 25.3), (39.67, 25.518), (40, 25.818)), ((40, 26.518), (39.99, 27.209), (39.99, 27.909)), ((39.99, 30.827), (37.62, 33.636), (35, 35)))
        self.add_bezier('e10', (13, 35), ((12.11, 35.455), (11.74, 35.445), (11.32, 36.182)), ((10.83, 37.027), (11.05, 38.273), (11.12, 39.182)), ((11.29, 41.409), (11.6, 44), (14.69, 44)), ((14.79, 44), (14.9, 44), (15, 44)))
        self.add_bezier('e11', (32, 44), ((32.08, 43.991), (32.16, 43.991), (32.25, 43.982)), ((33.98, 43.982), (35, 42.409), (35, 41)))
        self.add_bezier('e12', (10, 31), ((8.9, 29.673), (8.53, 28.518), (8, 27)))
        self.add_bezier('e13', (8, 12), ((8.01, 11.864), (8.01, 11.909), (8.02, 11.773)), ((8.02, 11.118), (8.3, 10.418), (8.57, 9.827)), ((9.9, 6.882), (12.94, 4.909), (16.3, 4.264)), ((16.86, 4.155), (17.43, 4), (18, 4)))
        self.add_bezier('e14', (29, 4), ((29.08, 4), (29.16, 4), (29.25, 4)), ((32.64, 4), (36.34, 5.909), (38.32, 8.345)), ((38.9, 9.064), (39.4, 9.891), (39.84, 10.682)), ((39.94, 10.873), (39.9, 10.791), (40, 11)))
        self.add_contour('c0', 'e8', 'e0', 'e9')
        self.add_contour('c1', 'e10', 'e1', 'e11', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('c3', 'e4', 'e12', 'e5', 'e13', 'e6', 'e14', 'e7')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c3', 'c0')
