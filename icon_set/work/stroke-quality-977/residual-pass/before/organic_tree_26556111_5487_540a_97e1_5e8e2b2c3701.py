"""Organic tree (ecology), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '26556111-5487-540a-97e1-5e8e2b2c3701'
SOURCE_PATH = 'pictographic-primitives/ecology/organic tree_26556111-5487-540a-97e1-5e8e2b2c3701.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class OrganicTreeEcology(Solo48):
    icon_id = 'organic-tree-ecology'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'ecology'
    aliases = ()
    keywords = ('organic', 'tree', 'ecology')

    def build(self):
        self.add_line('e0', (24, 44), (24, 12))
        self.add_line('e1', (31, 21), (24, 27))
        self.add_line('e2', (17, 21), (24, 27))
        self.add_line('e3', (19, 34), (29, 34))
        self.add_arc('e4-1', (29, 34), (40, 24), radius_x=11, sweep=False)
        self.add_arc('e4-2', (40, 24), (34, 15), radius_x=11, sweep=False)
        self.add_arc('e4-3', (34, 15), (32, 7), radius_x=8, sweep=False)
        self.add_line('e4-4', (32, 7), (29, 5))
        self.add_line('e4-5', (29, 5), (24, 4))
        self.add_line('e4-6', (24, 4), (19, 5))
        self.add_arc('e4-7', (19, 5), (16, 7), radius_x=10, sweep=False)
        self.add_arc('e4-8', (16, 7), (14, 15), radius_x=7, sweep=False)
        self.add_arc('e4-9', (14, 15), (8, 24), radius_x=11, sweep=False)
        self.add_arc('e4-10', (8, 24), (19, 34), radius_x=11, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3', 'e4-1', 'e4-2', 'e4-3', 'e4-4', 'e4-5', 'e4-6', 'e4-7', 'e4-8', 'e4-9', 'e4-10', closed=True)
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c2', 'c0')
