"""Plant (nature), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '93a59e45-5521-49b0-9911-63d35bb7f98a'
SOURCE_PATH = 'icons-json/nature/plant_93a59e45-5521-49b0-9911-63d35bb7f98a.json'
AUTHOR = 'json_to_solo'

class Plant(Solo48):
    icon_id = 'plant'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature'
    aliases = ()
    keywords = ('plant', 'nature')

    def build(self):
        self.add_line('e0', (24, 35), (22, 29))
        self.add_line('e1', (22, 29), (20, 26))
        self.add_line('e2', (29, 26), (31, 23))
        self.add_line('e3', (19, 23), (20, 26))
        self.add_line('e4', (24, 42), (24, 36))
        self.add_bezier('e5', (29, 26), ((27.969, 27.538), (26.806, 28.721), (25.939, 30.365)), ((25.211, 31.748), (24.622, 33.56), (24, 35)))
        self.add_bezier('e6', (31, 23), ((32.71, 21.29), (36.911, 20.637), (39.251, 20.335)), ((39.496, 20.302), (42, 20.024), (42, 20.105)), ((42, 20.14), (42, 20.175), (42, 20.209)), ((42, 22.393), (41.355, 24.604), (40.396, 26.553)), ((37.23, 33.016), (30.799, 35.395), (24, 36)))
        self.add_bezier('e7', (29, 26), ((29.303, 24.601), (29.637, 22.773), (29.801, 21.333)), ((30.284, 17.185), (29.326, 13.102), (27.011, 9.625)), ((26.446, 8.774), (25.833, 7.972), (25.154, 7.203)), ((24.802, 6.802), (24.442, 6.401), (24.09, 6)), ((24.085, 6.005), (24.08, 6), (24.075, 6)), ((23.761, 6), (23.447, 6.668), (23.133, 6.99)), ((22.437, 7.71), (21.815, 8.487), (21.251, 9.314)), ((18.109, 13.887), (17.683, 17.747), (19, 23)))
        self.add_bezier('e8', (19, 25), ((19.262, 25.524), (19.681, 25.517), (20, 26)))
        self.add_bezier('e9', (20, 26), ((16.686, 23.3), (13.953, 21.431), (9.682, 20.506)), ((8.774, 20.31), (7.841, 20.187), (6.916, 20.138)), ((6.835, 20.138), (6.753, 20.13), (6.671, 20.13)), ((6.45, 20.122), (6.221, 20.105), (6, 20.097)), ((6, 20.122), (6, 20.146), (6, 20.171)), ((6, 21.72), (6.441, 23.36), (6.916, 24.818)), ((8.872, 30.848), (14.395, 34.465), (20.318, 35.839)), ((21.521, 36.117), (22.781, 35.902), (24, 36)))
        self.add_contour('c0', 'e5', 'e0', 'e1')
        self.add_contour('c1', 'e2', 'e6')
        self.add_contour('c2', 'e7', 'e3')
        self.add_contour('c3', 'e8')
        self.add_contour('c4', 'e9')
        self.add_contour('c5', 'e4')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c1', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c3', 'c2')
        self.relate('connect', 'c3', 'c4')
