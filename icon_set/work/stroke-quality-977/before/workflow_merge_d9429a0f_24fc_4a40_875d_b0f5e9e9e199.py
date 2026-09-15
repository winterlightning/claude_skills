"""Workflow merge (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd9429a0f-24fc-4a40-875d-b0f5e9e9e199'
SOURCE_PATH = 'pictographic-primitives/interface-essential/workflow merge_d9429a0f-24fc-4a40-875d-b0f5e9e9e199.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class WorkflowMergeInterfaceEssential(Solo48):
    icon_id = 'workflow-merge-interface-essential'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('workflow', 'merge', 'interface-essential')

    def build(self):
        self.add_line('e0', (24, 15), (24, 19))
        self.add_arc('e1-top', (30, 39), (40, 39), radius_x=5)
        self.add_arc('e1-bottom', (40, 39), (30, 39), radius_x=5)
        self.add_arc('e2-top', (8, 39), (18, 39), radius_x=5)
        self.add_arc('e2-bottom', (18, 39), (8, 39), radius_x=5)
        self.add_arc('e3-top', (19, 9), (29, 9), radius_x=5)
        self.add_arc('e3-bottom', (29, 9), (19, 9), radius_x=5)
        self.add_arc('e4-1', (35, 33), (33, 25), radius_x=11, sweep=False)
        self.add_arc('e4-2', (33, 25), (28, 23), radius_x=9, sweep=False)
        self.add_line('e4-3', (28, 23), (24, 19))
        self.add_arc('e5-1', (13, 33), (15, 25), radius_x=9)
        self.add_arc('e5-2', (15, 25), (20, 23), radius_x=9)
        self.add_arc('e5-3', (20, 23), (24, 19), radius_x=7, sweep=False)
        self.add_contour('c0', 'e4-1', 'e4-2', 'e4-3')
        self.add_contour('c1', 'e5-1', 'e5-2', 'e5-3')
        self.add_contour('c2', 'e0')
        self.add_contour('e2', 'e2-top', 'e2-bottom', closed=True)
        self.add_contour('e1', 'e1-top', 'e1-bottom', closed=True)
        self.add_contour('e3', 'e3-top', 'e3-bottom', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'e1')
        self.relate('connect', 'c1', 'e2')
        self.relate('connect', 'c2', 'e3')
