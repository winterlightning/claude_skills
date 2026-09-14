"""Pathfinder intersect (design), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1c1403de-6b64-47bf-92a2-5713a99fc2c0'
SOURCE_PATH = 'icons-json/design/pathfinder intersect_1c1403de-6b64-47bf-92a2-5713a99fc2c0.json'
AUTHOR = 'json_to_solo'

class PathfinderIntersectDesign(Solo48):
    icon_id = 'pathfinder-intersect-design'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('pathfinder', 'intersect', 'design')

    def build(self):
        self.add_line('e0', (18, 31), (18, 19))
        self.add_line('e1', (20, 17), (31, 17))
        self.add_line('e2', (31, 17), (31, 29))
        self.add_line('e3', (28, 31), (18, 31))
        self.add_line('e4', (18, 31), (18, 40))
        self.add_line('e5', (20, 42), (40, 42))
        self.add_line('e6', (42, 40), (42, 19))
        self.add_line('e7', (40, 17), (31, 17))
        self.add_line('e8', (31, 17), (31, 8))
        self.add_line('e9', (28, 6), (8, 6))
        self.add_line('e10', (6, 8), (6, 29))
        self.add_line('e11', (8, 31), (18, 31))
        self.add_bezier('e12', (18, 19), ((18.286, 18.329), (19.1, 17), (20, 17)))
        self.add_bezier('e13', (31, 29), ((30.943, 29.106), (30.439, 29.122), (30.382, 29.228)), ((29.858, 30.128), (28.957, 30.845), (28, 31)))
        self.add_bezier('e14', (18, 40), ((18.483, 40.949), (19.051, 41.542), (20, 42)))
        self.add_bezier('e15', (40, 42), ((41.047, 41.55), (41.558, 41.006), (42, 40)))
        self.add_bezier('e16', (42, 19), ((42, 18.967), (41.992, 19.025), (41.992, 18.993)), ((41.992, 18.355), (40.622, 17), (40, 17)))
        self.add_bezier('e17', (31, 8), ((31, 7.845), (30.423, 8.16), (30.382, 8.013)), ((30.03, 6.802), (29.047, 6.401), (28, 6)))
        self.add_bezier('e18', (8, 6), ((7.125, 6.556), (6, 7.047), (6, 8.283)), ((6, 8.34), (6, 7.943), (6, 8)))
        self.add_bezier('e19', (6, 29), ((6.458, 30.039), (6.977, 30.542), (8, 31)))
        self.add_contour('c0', 'e0', 'e12', 'e1', 'e2', 'e13', 'e3', closed=True)
        self.add_contour('c1', 'e4', 'e14', 'e5', 'e15', 'e6', 'e16', 'e7', 'e8', 'e17', 'e9', 'e18', 'e10', 'e19', 'e11', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
