"""Pathfinder divide (design), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '90cf1274-1815-44c2-8417-50d32a479cfd'
SOURCE_PATH = 'pictographic-primitives/design/pathfinder divide_90cf1274-1815-44c2-8417-50d32a479cfd.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class PathfinderDivide(Solo48):
    icon_id = 'pathfinder-divide'
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
        self.add_line('e12', (18, 20), (19, 18))
        self.add_line('e13', (29, 30), (30, 28))
        self.add_arc('e14', (18, 38), (19, 40), radius_x=2, sweep=False)
        self.add_arc('e15', (42, 40), (44, 38), radius_x=2, sweep=False)
        self.add_arc('e16', (44, 20), (42, 18), radius_x=2, sweep=False)
        self.add_arc('e17', (6, 30), (4, 28), radius_x=3)
        self.add_arc('e18', (4, 10), (6, 8), radius_x=2)
        self.add_arc('e19', (29, 8), (30, 10), radius_x=2)
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
