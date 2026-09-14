"""Table lamp retro (outdoors), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a4f7565d-8e1a-4df0-9790-479c0cfc344d'
SOURCE_PATH = 'icons-json/outdoors/table lamp retro_a4f7565d-8e1a-4df0-9790-479c0cfc344d.json'
AUTHOR = 'json_to_solo'

class TableLampRetroOutdoors(Solo48):
    icon_id = 'table-lamp-retro-outdoors'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    aliases = ()
    keywords = ('table', 'lamp', 'retro', 'outdoors')

    def build(self):
        self.add_line('e0', (17, 44), (24, 44))
        self.add_line('e1', (31, 44), (24, 44))
        self.add_line('e2', (26, 21), (28, 24))
        self.add_line('e3', (36, 22), (40, 25))
        self.add_line('e4', (22, 21), (20, 24))
        self.add_line('e5', (24, 20), (24, 44))
        self.add_bezier('e6', (24, 4), ((24, 4.609), (24, 5.391), (24, 6)))
        self.add_bezier('e7', (24, 20), ((24.564, 20.3), (25.554, 20.518), (26, 21)))
        self.add_bezier('e8', (28, 24), ((28.093, 24.055), (28.404, 24.1), (28.497, 24.155)), ((28.691, 24.191), (29.069, 24.109), (29.272, 24.055)), ((30.24, 23.764), (30.956, 22.636), (31.764, 22.036)), ((33.027, 21.109), (34.771, 21.2), (36, 22)))
        self.add_bezier('e9', (40, 25), ((40, 24.3), (39.983, 23.509), (39.983, 22.809)), ((39.983, 22.282), (39.983, 21.745), (39.983, 21.209)), ((39.992, 21.091), (39.992, 20.973), (40, 20.845)), ((40, 20.727), (40, 20.6), (39.992, 20.482)), ((39.992, 18.891), (39.242, 17.127), (38.636, 15.718)), ((35.789, 9.155), (30.577, 6.136), (24, 6)))
        self.add_bezier('e10', (24, 20), ((23.436, 20.3), (22.446, 20.518), (22, 21)))
        self.add_bezier('e11', (20, 24), ((19.672, 24.018), (19.208, 24.136), (18.863, 24.064)), ((18.366, 23.945), (17.945, 23.5), (17.583, 23.136)), ((16.455, 22), (15.225, 20.809), (13.549, 21.1)), ((11.722, 21.418), (11.04, 23.091), (9.608, 24.073)), ((9.162, 24.382), (8.211, 25.036), (8.152, 25)), ((8.109, 24.464), (8.076, 23.918), (8.034, 23.382)), ((8.025, 23.327), (8.025, 23.264), (8.017, 23.209)), ((8.017, 23.084), (8, 22.95), (8, 22.824)), ((8, 22.822), (8, 22.82), (8, 22.818)), ((8, 22.464), (8.017, 22.118), (8.017, 21.764)), ((8.017, 19.918), (8.497, 17.936), (9.154, 16.245)), ((11.815, 9.418), (17.255, 6.109), (24, 6)))
        self.add_contour('c0', 'e6')
        self.add_contour('c1', 'e0')
        self.add_contour('c2', 'e1')
        self.add_contour('c3', 'e7', 'e2', 'e8', 'e3', 'e9')
        self.add_contour('c4', 'e10', 'e4', 'e11')
        self.add_contour('c5', 'e5')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c5')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c4', 'c5')
