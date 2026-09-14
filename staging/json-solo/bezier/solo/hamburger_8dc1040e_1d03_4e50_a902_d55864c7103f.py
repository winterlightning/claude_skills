"""Hamburger (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8dc1040e-1d03-4e50-a902-d55864c7103f'
SOURCE_PATH = 'icons-json/symbol/hamburger_8dc1040e-1d03-4e50-a902-d55864c7103f.json'
AUTHOR = 'json_to_solo'

class Hamburger8dc1040e(Solo48):
    icon_id = 'hamburger-8dc1040e'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('hamburger', 'symbol')

    def build(self):
        self.add_line('e0', (30, 30), (6, 30))
        self.add_line('e1', (42, 21), (6, 21))
        self.add_line('e2', (16, 8), (30, 8))
        self.add_bezier('e3', (42, 30), ((38.073, 30.48), (33.945, 30), (30, 30)))
        self.add_bezier('e4', (42, 30), ((41.845, 31.507), (42.018, 33.162), (41.427, 34.602)), ((40.1, 37.811), (36.818, 40), (33.091, 40)), ((33.038, 40), (32.985, 40), (32.932, 40)), ((29.603, 40), (26.274, 39.983), (22.945, 39.983)), ((20.973, 39.983), (19, 39.966), (17.036, 39.949)), ((13.891, 39.924), (11.3, 40), (8.827, 37.878)), ((7.836, 36.977), (7.064, 35.806), (6.618, 34.594)), ((6.055, 33.061), (6.155, 31.6), (6, 30)))
        self.add_bezier('e5', (42, 30), ((42.636, 28.989), (43.982, 27.528), (43.982, 26.274)), ((43.982, 26.088), (44, 25.903), (44, 25.718)), ((44, 25.716), (44, 25.714), (44, 25.713)), ((44, 25.605), (43.991, 25.489), (43.991, 25.381)), ((43.991, 24.227), (42.545, 21.96), (42, 21)))
        self.add_bezier('e6', (6, 30), ((5.4, 28.888), (4.018, 27.326), (4.018, 26.013)), ((4.009, 25.886), (4.009, 25.768), (4, 25.642)), ((4, 25.64), (4, 25.638), (4, 25.637)), ((4, 25.52), (4.009, 25.396), (4.018, 25.28)), ((4.018, 24.413), (5.618, 21.775), (6, 21)))
        self.add_bezier('e7', (6, 21), ((6.091, 19.425), (5.909, 18.24), (6.355, 16.699)), ((7.264, 13.524), (9.464, 10.855), (12.482, 9.145)), ((13.482, 8.589), (14.945, 8.328), (16, 8)))
        self.add_bezier('e8', (30, 8), ((30.436, 8), (31.236, 8), (31.673, 8)), ((32.845, 8), (34.209, 8.556), (35.227, 9.044)), ((40.209, 11.402), (42.464, 15.989), (42, 21)))
        self.add_contour('c0', 'e3', 'e0')
        self.add_contour('c1', 'e4')
        self.add_contour('c2', 'e5', 'e1')
        self.add_contour('c3', 'e6')
        self.add_contour('c4', 'e7', 'e2', 'e8')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c3', 'c4')
