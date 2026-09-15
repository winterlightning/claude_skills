"""Workflow exit door (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '73ac8a38-46a1-4e9c-bdc8-7cf6914289d0'
SOURCE_PATH = 'pictographic-primitives/interface-essential/workflow exit door_73ac8a38-46a1-4e9c-bdc8-7cf6914289d0.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class WorkflowExitDoor(Solo48):
    icon_id = 'workflow-exit-door'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('workflow', 'exit', 'door', 'interface-essential')

    def build(self):
        # Plan: exact integer ellipse attachments; split the receiving arcs at the real nodes.
        # Reference: circle geometry and the supplied subject.
        self.add_line('e0', (13, 4), (14, 10))
        self.add_line('e1', (13, 44), (14, 20))
        self.add_line('e2', (35, 30), (34, 19))
        self.add_line('e3', (30, 15), (20, 15))
        self.add_arc('e4-top-node-0', (30, 35), (35, 30), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('e4-top-node-1', (35, 30), (40, 35), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('e4-bottom', (40, 35), (30, 35), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('e5-top-node-0', (8, 15), (14, 10), radius_x=6, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('e5-top-node-1', (14, 10), (20, 15), radius_x=6, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('e5-bottom-node-0', (20, 15), (14, 20), radius_x=6, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('e5-bottom-node-1', (14, 20), (8, 15), radius_x=6, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('e6', (34, 19), (30, 15), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_contour('c0', 'e0', closed=False)
        self.add_contour('c1', 'e1', closed=False)
        self.add_contour('c2', 'e2', 'e6', 'e3', closed=False)
        self.add_contour('e4', 'e4-top-node-0', 'e4-top-node-1', 'e4-bottom', closed=True)
        self.add_contour('e5', 'e5-top-node-0', 'e5-top-node-1', 'e5-bottom-node-0', 'e5-bottom-node-1', closed=True)
        self.relate('connect', 'c0', 'e5')
        self.relate('connect', 'c1', 'e5')
        self.relate('connect', 'c2', 'e4')
        self.relate('connect', 'c2', 'e5')
