"""Workflow merge (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd9429a0f-24fc-4a40-875d-b0f5e9e9e199'
SOURCE_PATH = 'pictographic-primitives/interface-essential/workflow merge_d9429a0f-24fc-4a40-875d-b0f5e9e9e199.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class WorkflowMergeInterfaceEssential(Solo48):
    icon_id = 'workflow-merge-interface-essential'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('workflow', 'merge', 'interface-essential')

    def build(self):
        # Plan: exact integer ellipse attachments; split the receiving arcs at the real nodes.
        # Reference: circle geometry and the supplied subject.
        self.add_line('e0', (24, 14), (24, 19))
        self.add_arc('e1-top-node-0', (30, 39), (35, 34), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('e1-top-node-1', (35, 34), (40, 39), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('e1-bottom', (40, 39), (30, 39), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('e2-top-node-0', (8, 39), (13, 34), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('e2-top-node-1', (13, 34), (18, 39), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('e2-bottom', (18, 39), (8, 39), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('e3-top', (19, 9), (29, 9), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('e3-bottom-node-0', (29, 9), (24, 14), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('e3-bottom-node-1', (24, 14), (19, 9), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('e4-1', (35, 34), (33, 25), radius_x=11, radius_y=11, large_arc=False, sweep=False)
        self.add_arc('e4-2', (33, 25), (28, 23), radius_x=9, radius_y=9, large_arc=False, sweep=False)
        self.add_line('e4-3', (28, 23), (24, 19))
        self.add_arc('e5-1', (13, 34), (15, 25), radius_x=9, radius_y=9, large_arc=False, sweep=True)
        self.add_arc('e5-2', (15, 25), (20, 23), radius_x=9, radius_y=9, large_arc=False, sweep=True)
        self.add_arc('e5-3', (20, 23), (24, 19), radius_x=7, radius_y=7, large_arc=False, sweep=False)
        self.add_contour('c0', 'e4-1', 'e4-2', 'e4-3', closed=False)
        self.add_contour('c1', 'e5-1', 'e5-2', 'e5-3', closed=False)
        self.add_contour('c2', 'e0', closed=False)
        self.add_contour('e2', 'e2-top-node-0', 'e2-top-node-1', 'e2-bottom', closed=True)
        self.add_contour('e1', 'e1-top-node-0', 'e1-top-node-1', 'e1-bottom', closed=True)
        self.add_contour('e3', 'e3-top', 'e3-bottom-node-0', 'e3-bottom-node-1', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'e1')
        self.relate('connect', 'c1', 'e2')
        self.relate('connect', 'c2', 'e3')
