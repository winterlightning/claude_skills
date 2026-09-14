"""Skiing snow scooter (sports), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a0980517-7981-47f9-b740-8ade748f0d74'
SOURCE_PATH = 'icons-json/sports/skiing snow scooter_a0980517-7981-47f9-b740-8ade748f0d74.json'
AUTHOR = 'json_to_solo'

class SkiingSnowScooterSports(Solo48):
    icon_id = 'skiing-snow-scooter-sports'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'sports'
    aliases = ()
    keywords = ('skiing', 'snow', 'scooter', 'sports')

    def build(self):
        self.add_line('e0', (33, 25), (41, 25))
        self.add_line('e1', (21, 8), (27, 8))
        self.add_line('e2', (30, 40), (37, 40))
        self.add_line('e3', (44, 36), (42, 39))
        self.add_line('e4', (42, 39), (40, 40))
        self.add_line('e5', (40, 40), (37, 40))
        self.add_line('e6', (33, 33), (37, 40))
        self.add_line('e7', (33, 33), (26, 33))
        self.add_line('e8', (20, 33), (26, 33))
        self.add_line('e9', (13, 29), (6, 34))
        self.add_line('e10', (7, 40), (21, 40))
        self.add_line('e11', (13, 29), (5, 20))
        self.add_line('e12', (6, 15), (11, 15))
        self.add_line('e13', (12, 15), (16, 19))
        self.add_line('e14', (36, 17), (41, 25))
        self.add_bezier('e15', (27, 8), ((27.2, 8.123), (27.136, 8.086), (27.336, 8.234)), ((28.973, 9.44), (29.982, 11.982), (31, 14)))
        self.add_bezier('e16', (33, 33), ((34.873, 33), (38.155, 33.329), (39.873, 32.357)), ((41.745, 31.286), (42.409, 27.228), (41, 25)))
        self.add_bezier('e17', (13, 29), ((14, 30.046), (18.782, 33), (20, 33)))
        self.add_bezier('e18', (6, 34), ((4.727, 35.575), (4, 37.378), (5.427, 39.2)), ((5.709, 39.52), (6.209, 39.988), (6.582, 39.988)), ((6.627, 39.988), (6.955, 40), (7, 40)))
        self.add_bezier('e19', (21, 40), ((23.882, 38.794), (25.036, 36.594), (26, 33)))
        self.add_bezier('e20', (5, 20), ((4.678, 19.431), (4, 19.004), (4, 18.24)), ((4, 18.228), (4, 18.215), (4, 18.203)), ((4, 16.763), (5.236, 15.591), (6, 15)))
        self.add_bezier('e21', (11, 15), ((11.3, 15), (11.7, 15), (12, 15)))
        self.add_bezier('e22', (16, 19), ((17.127, 20.145), (18.327, 19.668), (19.609, 19.618)), ((21.136, 19.569), (23.655, 19.705), (24.982, 18.695)), ((25.527, 18.265), (26, 17.662), (26.455, 17.083)), ((28.264, 14.757), (28.482, 14.148), (31, 14)))
        self.add_bezier('e23', (31, 14), ((32.6, 14.209), (34.891, 15.24), (36, 17)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e15')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3', 'e4', 'e5')
        self.add_contour('c4', 'e6')
        self.add_contour('c5', 'e16')
        self.add_contour('c6', 'e7')
        self.add_contour('c7', 'e17', 'e8')
        self.add_contour('c8', 'e9', 'e18', 'e10', 'e19')
        self.add_contour('c9', 'e11', 'e20', 'e12', 'e21', 'e13', 'e22')
        self.add_contour('c10', 'e23', 'e14')
        self.relate('connect', 'c0', 'c10')
        self.relate('connect', 'c0', 'c5')
        self.relate('connect', 'c10', 'c5')
        self.relate('connect', 'c1', 'c10')
        self.relate('connect', 'c1', 'c9')
        self.relate('connect', 'c10', 'c9')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c4', 'c6')
        self.relate('connect', 'c5', 'c6')
        self.relate('connect', 'c6', 'c7')
        self.relate('connect', 'c6', 'c8')
        self.relate('connect', 'c7', 'c8')
        self.relate('connect', 'c7', 'c8')
        self.relate('connect', 'c7', 'c9')
        self.relate('connect', 'c8', 'c9')
