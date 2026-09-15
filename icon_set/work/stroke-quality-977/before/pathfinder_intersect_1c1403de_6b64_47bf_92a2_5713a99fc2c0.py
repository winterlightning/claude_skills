"""Pathfinder intersect (design), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1c1403de-6b64-47bf-92a2-5713a99fc2c0'
SOURCE_PATH = 'pictographic-primitives/design/pathfinder intersect_1c1403de-6b64-47bf-92a2-5713a99fc2c0.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class PathfinderIntersect(Solo48):
    icon_id = 'pathfinder-intersect'
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
        self.add_line('e12', (18, 19), (20, 17))
        self.add_line('e13', (31, 29), (28, 31))
        self.add_line('e14', (18, 40), (20, 42))
        self.add_arc('e15', (40, 42), (42, 40), radius_x=2, sweep=False)
        self.add_line('e16', (42, 19), (40, 17))
        self.add_line('e17', (31, 8), (28, 6))
        self.add_arc('e18', (8, 6), (6, 8), radius_x=2, sweep=False)
        self.add_line('e19', (6, 29), (8, 31))
        self.add_contour('c0', 'e0', 'e12', 'e1', 'e2', 'e13', 'e3', closed=True)
        self.add_contour('c1', 'e4', 'e14', 'e5', 'e15', 'e6', 'e16', 'e7', 'e8', 'e17', 'e9', 'e18', 'e10', 'e19', 'e11', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
