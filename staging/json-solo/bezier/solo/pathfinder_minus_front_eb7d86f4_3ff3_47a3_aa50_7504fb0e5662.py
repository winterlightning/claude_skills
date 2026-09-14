"""Pathfinder minus front (design), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'eb7d86f4-3ff3-47a3-aa50-7504fb0e5662'
SOURCE_PATH = 'icons-json/design/pathfinder minus front_eb7d86f4-3ff3-47a3-aa50-7504fb0e5662.json'
AUTHOR = 'json_to_solo'

class PathfinderMinusFrontDesign(Solo48):
    icon_id = 'pathfinder-minus-front-design'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('pathfinder', 'minus', 'front', 'design')

    def build(self):
        self.add_line('e0', (18, 29), (18, 38))
        self.add_line('e1', (19, 40), (42, 40))
        self.add_line('e2', (44, 38), (44, 19))
        self.add_line('e3', (42, 17), (30, 17))
        self.add_line('e4', (18, 29), (18, 19))
        self.add_line('e5', (19, 17), (30, 17))
        self.add_line('e6', (18, 29), (6, 29))
        self.add_line('e7', (4, 28), (4, 10))
        self.add_line('e8', (5, 8), (29, 8))
        self.add_line('e9', (30, 9), (30, 17))
        self.add_bezier('e10', (18, 38), ((18.082, 38.522), (17.664, 39.242), (18.045, 39.714)), ((18.191, 39.882), (18.855, 39.857), (19, 40)))
        self.add_bezier('e11', (42, 40), ((42.155, 39.941), (42.518, 39.966), (42.664, 39.916)), ((43.136, 39.747), (43.727, 39.2), (43.909, 38.762)), ((43.964, 38.619), (43.936, 38.143), (44, 38)))
        self.add_bezier('e12', (44, 19), ((43.918, 18.857), (43.955, 18.619), (43.882, 18.476)), ((43.545, 17.836), (42.636, 17.286), (42, 17)))
        self.add_bezier('e13', (18, 19), ((18.173, 18.2), (18.436, 17.598), (19, 17)))
        self.add_bezier('e14', (6, 29), ((5.464, 28.907), (4.745, 28.96), (4.291, 28.615)), ((4.145, 28.505), (4.127, 28.118), (4, 28)))
        self.add_bezier('e15', (4, 10), ((4, 9.865), (4.009, 9.415), (4.009, 9.28)), ((4.009, 8.632), (4.591, 8.387), (5, 8)))
        self.add_bezier('e16', (29, 8), ((29.136, 8.101), (29.791, 8.059), (29.909, 8.16)), ((30.127, 8.345), (29.836, 8.781), (30, 9)))
        self.add_contour('c0', 'e0', 'e10', 'e1', 'e11', 'e2', 'e12', 'e3')
        self.add_contour('c1', 'e4', 'e13', 'e5')
        self.add_contour('c2', 'e6', 'e14', 'e7', 'e15', 'e8', 'e16', 'e9')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
