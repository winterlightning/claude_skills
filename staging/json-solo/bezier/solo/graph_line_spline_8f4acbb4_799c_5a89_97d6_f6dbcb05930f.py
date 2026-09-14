"""Graph line spline (business), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8f4acbb4-799c-5a89-97d6-f6dbcb05930f'
SOURCE_PATH = 'icons-json/business/graph line spline_8f4acbb4-799c-5a89-97d6-f6dbcb05930f.json'
AUTHOR = 'json_to_solo'

class GraphLineSplineBusiness(Solo48):
    icon_id = 'graph-line-spline-business'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'business'
    aliases = ()
    keywords = ('graph', 'line', 'spline', 'business')

    def build(self):
        self.add_line('e0', (26, 15), (29, 19))
        self.add_line('e1', (40, 19), (43, 13))
        self.add_line('e2', (44, 27), (41, 31))
        self.add_line('e3', (15, 32), (4, 40))
        self.add_line('e4', (4, 40), (4, 8))
        self.add_line('e5', (4, 40), (44, 40))
        self.add_bezier('e6', (4, 28), ((5.6, 27.874), (7.2, 28.017), (8.673, 27.36)), ((13.873, 25.053), (13.782, 17.221), (17.591, 13.541)), ((19.873, 11.326), (22.727, 11.604), (24.9, 13.743)), ((25.2, 14.046), (25.773, 14.646), (26, 15)))
        self.add_bezier('e7', (29, 19), ((31.155, 22.326), (34.036, 24.236), (37.818, 21.684)), ((38.782, 21.044), (39.527, 20.019), (40, 19)))
        self.add_bezier('e8', (41, 31), ((40.518, 31.749), (40.064, 32.101), (39.318, 32.615)), ((33.391, 36.716), (30.173, 30.333), (25, 29.112)), ((21.109, 28.194), (17.973, 29.937), (15, 32)))
        self.add_contour('c0', 'e6', 'e0', 'e7', 'e1')
        self.add_contour('c1', 'e2', 'e8', 'e3', 'e4')
        self.add_contour('c2', 'e5')
        self.relate('connect', 'c0', 'c1')
