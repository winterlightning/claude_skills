"""Workflow collaborate (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '81793d6a-dc99-4a1d-8a9b-e3030578ccdb'
SOURCE_PATH = 'pictographic-primitives/interface-essential/workflow collaborate_81793d6a-dc99-4a1d-8a9b-e3030578ccdb.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class WorkflowCollaborate(Solo48):
    icon_id = 'workflow-collaborate'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('workflow', 'collaborate', 'interface-essential')

    def build(self):
        # Plan: exact integer ellipse attachments; split the receiving arcs at the real nodes.
        # Reference: circle geometry and the supplied subject.
        self.add_line('e0', (13, 34), (13, 26))
        self.add_line('e1', (21, 26), (13, 26))
        self.add_line('e2', (13, 17), (13, 26))
        self.add_arc('e3-top-node-0', (8, 39), (13, 34), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('e3-top-node-1', (13, 34), (18, 39), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('e3-bottom', (18, 39), (8, 39), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('e4-top', (30, 9), (40, 9), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('e4-bottom-node-0', (40, 9), (35, 14), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('e4-bottom-node-1', (35, 14), (30, 9), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('e5-top', (8, 9), (18, 9), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('e5-bottom-node-0', (18, 9), (13, 14), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('e5-bottom-node-1', (13, 14), (8, 9), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('e6', (35, 14), (21, 26), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('e7', (13, 14), (13, 17), radius_x=16, radius_y=16, large_arc=False, sweep=False)
        self.add_contour('c0', 'e0', closed=False)
        self.add_contour('c1', 'e6', 'e1', closed=False)
        self.add_contour('c2', 'e7', 'e2', closed=False)
        self.add_contour('e3', 'e3-top-node-0', 'e3-top-node-1', 'e3-bottom', closed=True)
        self.add_contour('e4', 'e4-top', 'e4-bottom-node-0', 'e4-bottom-node-1', closed=True)
        self.add_contour('e5', 'e5-top', 'e5-bottom-node-0', 'e5-bottom-node-1', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'e3')
        self.relate('connect', 'c1', 'e4')
        self.relate('connect', 'c2', 'e5')
