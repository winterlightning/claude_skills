"""Pathfinder crop (design), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6668e2a6-0b6d-4f68-a08f-d032636e8cec'
SOURCE_PATH = 'icons-json/design/pathfinder crop_6668e2a6-0b6d-4f68-a08f-d032636e8cec.json'
AUTHOR = 'json_to_solo'

class PathfinderCropDesign(Solo48):
    icon_id = 'pathfinder-crop-design'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('pathfinder', 'crop', 'design')

    def build(self):
        self.add_line('e0', (18, 31), (18, 19))
        self.add_line('e1', (20, 17), (30, 17))
        self.add_line('e2', (18, 31), (28, 31))
        self.add_line('e3', (30, 29), (30, 17))
        self.add_line('e4', (18, 31), (18, 40))
        self.add_line('e5', (20, 42), (40, 42))
        self.add_line('e6', (42, 40), (42, 19))
        self.add_line('e7', (40, 17), (30, 17))
        self.add_line('e8', (18, 31), (8, 31))
        self.add_line('e9', (6, 29), (6, 8))
        self.add_line('e10', (8, 6), (28, 6))
        self.add_line('e11', (30, 8), (30, 17))
        self.add_bezier('e12', (18, 19), ((18.286, 17.691), (18.945, 17.777), (20, 17)))
        self.add_bezier('e13', (28, 31), ((29.023, 30.558), (29.534, 30.023), (30, 29)))
        self.add_bezier('e14', (18, 40), ((18.335, 40.671), (19.075, 42), (20, 42)))
        self.add_bezier('e15', (40, 42), ((41.105, 42), (42, 41.105), (42, 40)))
        self.add_bezier('e16', (42, 19), ((42, 18.926), (42, 18.935), (42, 18.862)), ((42, 17.79), (40.777, 17.54), (40, 17)))
        self.add_bezier('e17', (8, 31), ((6.945, 30.55), (6.434, 30.055), (6, 29)))
        self.add_bezier('e18', (6, 8), ((6.442, 6.977), (6.961, 6.434), (8, 6)))
        self.add_bezier('e19', (28, 6), ((28.155, 6.057), (28.426, 6.041), (28.59, 6.115)), ((29.114, 6.36), (30, 7.378), (30, 8)))
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
