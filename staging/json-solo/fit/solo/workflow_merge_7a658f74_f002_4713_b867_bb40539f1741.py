"""Workflow merge (diagrams), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7a658f74-f002-4713-b867-bb40539f1741'
SOURCE_PATH = 'icons-json/diagrams/workflow merge_7a658f74-f002-4713-b867-bb40539f1741.json'
AUTHOR = 'json_to_solo'

class WorkflowMergeDiagrams(Solo48):
    icon_id = 'workflow-merge-diagrams'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'diagrams'
    aliases = ()
    keywords = ('workflow', 'merge', 'diagrams')

    def build(self):
        self.add_line('e0', (14, 33), (14, 26))
        self.add_line('e1', (27, 26), (14, 26))
        self.add_line('e2', (14, 15), (14, 26))
        self.add_arc('e3-top', (8, 39), (20, 39), radius_x=6, radius_y=5)
        self.add_arc('e3-bottom', (20, 39), (8, 39), radius_x=6, radius_y=5)
        self.add_arc('e4-top', (28, 26), (40, 26), radius_x=6, radius_y=5)
        self.add_arc('e4-bottom', (40, 26), (28, 26), radius_x=6, radius_y=5)
        self.add_arc('e5-top', (8, 9), (20, 9), radius_x=6, radius_y=5)
        self.add_arc('e5-bottom', (20, 9), (8, 9), radius_x=6, radius_y=5)
        self.add_arc('e6', (28, 26), (27, 26), radius_x=27, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e6', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('e4', 'e4-top', 'e4-bottom', closed=True)
        self.add_contour('e5', 'e5-top', 'e5-bottom', closed=True)
        self.add_contour('e3', 'e3-top', 'e3-bottom', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'e3')
        self.relate('connect', 'c1', 'e4')
        self.relate('connect', 'c2', 'e5')
