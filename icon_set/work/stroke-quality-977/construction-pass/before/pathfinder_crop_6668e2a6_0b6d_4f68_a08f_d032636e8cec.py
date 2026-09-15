"""Pathfinder crop (design), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6668e2a6-0b6d-4f68-a08f-d032636e8cec'
SOURCE_PATH = 'pictographic-primitives/design/pathfinder crop_6668e2a6-0b6d-4f68-a08f-d032636e8cec.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class PathfinderCrop(Solo48):
    icon_id = 'pathfinder-crop'
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
        self.add_arc('e12', (18, 19), (20, 17), radius_x=3)
        self.add_line('e13', (28, 31), (30, 29))
        self.add_line('e14', (18, 40), (20, 42))
        self.add_line('e15', (40, 42), (42, 40))
        self.add_arc('e16', (42, 19), (40, 17), radius_x=2, sweep=False)
        self.add_line('e17', (8, 31), (6, 29))
        self.add_arc('e18', (6, 8), (8, 6), radius_x=2)
        self.add_arc('e19', (28, 6), (30, 8), radius_x=2)
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
