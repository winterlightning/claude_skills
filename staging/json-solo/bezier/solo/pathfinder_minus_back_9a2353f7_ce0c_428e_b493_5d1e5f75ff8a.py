"""Pathfinder minus back (design), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9a2353f7-ce0c-428e-b493-5d1e5f75ff8a'
SOURCE_PATH = 'icons-json/design/pathfinder minus back_9a2353f7-ce0c-428e-b493-5d1e5f75ff8a.json'
AUTHOR = 'json_to_solo'

class PathfinderMinusBackDesign(Solo48):
    icon_id = 'pathfinder-minus-back-design'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('pathfinder', 'minus', 'back', 'design')

    def build(self):
        self.add_line('e0', (18, 30), (18, 20))
        self.add_line('e1', (19, 18), (29, 18))
        self.add_line('e2', (18, 30), (29, 30))
        self.add_line('e3', (29, 29), (29, 18))
        self.add_line('e4', (18, 30), (16, 30))
        self.add_line('e5', (29, 18), (29, 16))
        self.add_line('e6', (16, 30), (16, 38))
        self.add_line('e7', (17, 40), (42, 40))
        self.add_line('e8', (44, 38), (44, 17))
        self.add_line('e9', (42, 16), (29, 16))
        self.add_line('e10', (16, 30), (6, 30))
        self.add_line('e11', (4, 29), (4, 10))
        self.add_line('e12', (6, 8), (29, 8))
        self.add_line('e13', (29, 10), (29, 16))
        self.add_bezier('e14', (18, 20), ((18.518, 18.931), (17.864, 18.514), (19, 18)))
        self.add_bezier('e15', (29, 30), ((29.673, 29.545), (28.518, 29.539), (29, 29)))
        self.add_bezier('e16', (16, 38), ((16.1, 38.514), (15.882, 39.259), (16.255, 39.714)), ((16.382, 39.865), (16.873, 39.874), (17, 40)))
        self.add_bezier('e17', (42, 40), ((42.318, 39.857), (42.364, 40), (42.691, 39.899)), ((43.127, 39.739), (43.991, 39.015), (43.991, 38.535)), ((44, 38.459), (44, 38.076), (44, 38)))
        self.add_bezier('e18', (44, 17), ((43.836, 16.874), (43.855, 16.952), (43.664, 16.834)), ((43.2, 16.539), (42.527, 16.101), (42, 16)))
        self.add_bezier('e19', (6, 30), ((5.418, 29.924), (4.755, 29.844), (4.282, 29.432)), ((4.155, 29.322), (4.118, 29.109), (4, 29)))
        self.add_bezier('e20', (4, 10), ((4.555, 8.829), (4.773, 8.48), (6, 8)))
        self.add_bezier('e21', (29, 8), ((29.118, 8.059), (28.773, 8.118), (28.891, 8.185)), ((29.345, 8.539), (28.9, 9.512), (29, 10)))
        self.add_contour('c0', 'e0', 'e14', 'e1')
        self.add_contour('c1', 'e2', 'e15', 'e3')
        self.add_contour('c2', 'e4')
        self.add_contour('c3', 'e5')
        self.add_contour('c4', 'e6', 'e16', 'e7', 'e17', 'e8', 'e18', 'e9')
        self.add_contour('c5', 'e10', 'e19', 'e11', 'e20', 'e12', 'e21', 'e13')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c4', 'c5')
