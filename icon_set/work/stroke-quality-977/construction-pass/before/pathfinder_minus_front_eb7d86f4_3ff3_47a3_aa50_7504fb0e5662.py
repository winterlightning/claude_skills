"""Pathfinder minus front (design), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'eb7d86f4-3ff3-47a3-aa50-7504fb0e5662'
SOURCE_PATH = 'pictographic-primitives/design/pathfinder minus front_eb7d86f4-3ff3-47a3-aa50-7504fb0e5662.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class PathfinderMinusFront(Solo48):
    icon_id = 'pathfinder-minus-front'
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
        self.add_arc('e10', (18, 38), (19, 40), radius_x=2, sweep=False)
        self.add_arc('e11', (42, 40), (44, 38), radius_x=2, sweep=False)
        self.add_arc('e12', (44, 19), (42, 17), radius_x=3, sweep=False)
        self.add_line('e13', (18, 19), (19, 17))
        self.add_arc('e14', (6, 29), (4, 28), radius_x=2)
        self.add_line('e15', (4, 10), (5, 8))
        self.add_arc('e16', (29, 8), (30, 9), radius_x=1)
        self.add_contour('c0', 'e0', 'e10', 'e1', 'e11', 'e2', 'e12', 'e3')
        self.add_contour('c1', 'e4', 'e13', 'e5')
        self.add_contour('c2', 'e6', 'e14', 'e7', 'e15', 'e8', 'e16', 'e9')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
