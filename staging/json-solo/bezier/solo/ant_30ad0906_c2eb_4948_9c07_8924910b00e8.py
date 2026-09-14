"""Ant (_uncategorized_03), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '30ad0906-c2eb-4948-9c07-8924910b00e8'
SOURCE_PATH = 'icons-json/_uncategorized_03/ant_30ad0906-c2eb-4948-9c07-8924910b00e8.json'
AUTHOR = 'json_to_solo'

class Ant30ad0906(Solo48):
    icon_id = 'ant-30ad0906'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized_03'
    aliases = ()
    keywords = ('ant', '_uncategorized_03')

    def build(self):
        self.add_line('e0', (8, 26), (14, 22))
        self.add_line('e1', (14, 22), (20, 26))
        self.add_line('e2', (9, 41), (15, 30))
        self.add_line('e3', (15, 30), (21, 30))
        self.add_line('e4', (39, 41), (34, 31))
        self.add_line('e5', (33, 30), (27, 30))
        self.add_line('e6', (40, 26), (35, 22))
        self.add_line('e7', (34, 22), (28, 26))
        self.add_line('e8', (22, 30), (27, 30))
        self.add_line('e9', (26, 21), (22, 21))
        self.add_line('e10', (27, 21), (27, 23))
        self.add_bezier('e11', (13, 4), ((16.798, 6.109), (19.122, 7.891), (21, 12)))
        self.add_bezier('e12', (34, 31), ((33.714, 30.655), (33.32, 30.3), (33, 30)))
        self.add_bezier('e13', (35, 22), ((34.722, 22), (34.278, 22), (34, 22)))
        self.add_bezier('e14', (35, 4), ((31.429, 6.173), (29.642, 9.118), (28, 13)))
        self.add_bezier('e15', (27, 30), ((28.221, 31.273), (28.901, 32.7), (29.398, 34.491)), ((30.232, 37.527), (29.061, 41.427), (26.518, 43.118)), ((25.878, 43.545), (25.187, 43.991), (24.404, 43.991)), ((24.363, 43.991), (24.321, 44), (24.28, 44)), ((24.279, 44), (24.279, 44), (24.278, 44)), ((24.16, 44), (24.042, 43.991), (23.924, 43.991)), ((23.183, 43.991), (22.383, 43.618), (21.768, 43.191)), ((19.251, 41.445), (18.08, 37.891), (18.754, 34.791)), ((19.158, 32.909), (19.787, 31.345), (21, 30)))
        self.add_bezier('e16', (27, 30), ((27.632, 28.436), (27.781, 27.691), (28, 26)))
        self.add_bezier('e17', (27, 23), ((27.539, 23.982), (27.806, 24.782), (28, 26)))
        self.add_bezier('e18', (21, 30), ((20.116, 28.491), (20.143, 27.782), (20, 26)))
        self.add_bezier('e19', (21, 12), ((24.166, 10.3), (25.187, 11.027), (28, 13)))
        self.add_bezier('e20', (21, 12), ((20.663, 12.545), (19.891, 13.3), (19.621, 13.9)), ((18.779, 15.791), (19.133, 18.109), (20.446, 19.655)), ((20.985, 20.291), (21.352, 20.491), (22, 21)))
        self.add_bezier('e21', (28, 13), ((28.337, 13.6), (28.952, 14.291), (29.187, 14.945)), ((30.257, 17.909), (28.055, 19.709), (26, 21)))
        self.add_bezier('e22', (20, 26), ((20.126, 23.455), (20.198, 22.5), (22, 21)))
        self.add_contour('c0', 'e11')
        self.add_contour('c1', 'e0', 'e1')
        self.add_contour('c2', 'e2', 'e3')
        self.add_contour('c3', 'e4', 'e12', 'e5')
        self.add_contour('c4', 'e6', 'e13', 'e7')
        self.add_contour('c5', 'e14')
        self.add_contour('c6', 'e8')
        self.add_contour('c7', 'e15')
        self.add_contour('c8', 'e16')
        self.add_contour('c9', 'e9')
        self.add_contour('c10', 'e10', 'e17')
        self.add_contour('c11', 'e18')
        self.add_contour('c12', 'e19')
        self.add_contour('c13', 'e20')
        self.add_contour('c14', 'e21')
        self.add_contour('c15', 'e22')
        self.relate('connect', 'c0', 'c12')
        self.relate('connect', 'c0', 'c13')
        self.relate('connect', 'c12', 'c13')
        self.relate('connect', 'c1', 'c11')
        self.relate('connect', 'c1', 'c15')
        self.relate('connect', 'c11', 'c15')
        self.relate('connect', 'c3', 'c6')
        self.relate('connect', 'c3', 'c7')
        self.relate('connect', 'c3', 'c8')
        self.relate('connect', 'c6', 'c7')
        self.relate('connect', 'c6', 'c8')
        self.relate('connect', 'c7', 'c8')
        self.relate('connect', 'c10', 'c4')
        self.relate('connect', 'c10', 'c8')
        self.relate('connect', 'c4', 'c8')
        self.relate('connect', 'c12', 'c14')
        self.relate('connect', 'c12', 'c5')
        self.relate('connect', 'c14', 'c5')
        self.relate('connect', 'c13', 'c15')
        self.relate('connect', 'c13', 'c9')
        self.relate('connect', 'c15', 'c9')
