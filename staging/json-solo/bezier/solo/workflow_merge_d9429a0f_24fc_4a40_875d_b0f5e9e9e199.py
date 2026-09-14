"""Workflow merge (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd9429a0f-24fc-4a40-875d-b0f5e9e9e199'
SOURCE_PATH = 'icons-json/interface-essential/workflow merge_d9429a0f-24fc-4a40-875d-b0f5e9e9e199.json'
AUTHOR = 'json_to_solo'

class WorkflowMergeD9429a0f(Solo48):
    icon_id = 'workflow-merge-d9429a0f'
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
        self.add_bezier('e4', (35, 33), ((34.453, 30.1), (35.318, 27.982), (33.221, 25.418)), ((31.461, 23.255), (29.735, 23.936), (27.672, 22.855)), ((25.878, 21.909), (24.943, 20.845), (24, 19)))
        self.add_bezier('e5', (13, 33), ((12.461, 29.764), (12.935, 26.291), (15.697, 24.364)), ((17.053, 23.418), (18.636, 23.618), (20.093, 22.982)), ((22.08, 22.118), (23.04, 20.982), (24, 19)))
        self.add_contour('c0', 'e4')
        self.add_contour('c1', 'e5')
        self.add_contour('c2', 'e0')
        self.add_contour('e1', 'e1-top', 'e1-bottom', closed=True)
        self.add_contour('e2', 'e2-top', 'e2-bottom', closed=True)
        self.add_contour('e3', 'e3-top', 'e3-bottom', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'e1')
        self.relate('connect', 'c1', 'e2')
        self.relate('connect', 'c2', 'e3')
