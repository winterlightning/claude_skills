"""Pathfinder divide (design), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '90cf1274-1815-44c2-8417-50d32a479cfd'
SOURCE_PATH = 'icons-json/design/pathfinder divide_90cf1274-1815-44c2-8417-50d32a479cfd.json'
AUTHOR = 'json_to_solo'

class PathfinderDivideDesign(Solo48):
    icon_id = 'pathfinder-divide-design'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('pathfinder', 'divide', 'design')

    def build(self):
        self.add_line('e0', (18, 30), (18, 20))
        self.add_line('e1', (19, 18), (30, 18))
        self.add_line('e2', (18, 30), (29, 30))
        self.add_line('e3', (30, 28), (30, 18))
        self.add_line('e4', (18, 30), (18, 38))
        self.add_line('e5', (19, 40), (42, 40))
        self.add_line('e6', (44, 38), (44, 20))
        self.add_line('e7', (42, 18), (30, 18))
        self.add_line('e8', (18, 30), (6, 30))
        self.add_line('e9', (4, 28), (4, 10))
        self.add_line('e10', (6, 8), (29, 8))
        self.add_line('e11', (30, 10), (30, 18))
        self.add_bezier('e12', (18, 20), ((18.527, 18.989), (17.918, 18.505), (19, 18)))
        self.add_bezier('e13', (29, 30), ((30.127, 29.52), (29.5, 29.019), (30, 28)))
        self.add_bezier('e14', (18, 38), ((18.618, 39.095), (17.809, 39.478), (19, 40)))
        self.add_bezier('e15', (42, 40), ((42.691, 40), (43.582, 39.36), (43.864, 38.821)), ((43.955, 38.661), (43.927, 38.168), (44, 38)))
        self.add_bezier('e16', (44, 20), ((44, 19.941), (43.991, 19.68), (43.991, 19.621)), ((43.991, 18.922), (42.718, 18), (42, 18)))
        self.add_bezier('e17', (6, 30), ((4.764, 29.427), (4.545, 29.162), (4, 28)))
        self.add_bezier('e18', (4, 10), ((4.091, 9.823), (4.064, 9.314), (4.173, 9.137)), ((4.582, 8.48), (5.336, 8.295), (6, 8)))
        self.add_bezier('e19', (29, 8), ((30.145, 8.463), (29.491, 8.956), (30, 10)))
        self.add_contour('c0', 'e0', 'e12', 'e1')
        self.add_contour('c1', 'e2', 'e13', 'e3')
        self.add_contour('c2', 'e4', 'e14', 'e5', 'e15', 'e6', 'e16', 'e7')
        self.add_contour('c3', 'e8', 'e17', 'e9', 'e18', 'e10', 'e19', 'e11')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
