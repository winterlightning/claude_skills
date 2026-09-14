"""Workflow collaborate (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '81793d6a-dc99-4a1d-8a9b-e3030578ccdb'
SOURCE_PATH = 'icons-json/interface-essential/workflow collaborate_81793d6a-dc99-4a1d-8a9b-e3030578ccdb.json'
AUTHOR = 'json_to_solo'

class WorkflowCollaborateInterfaceEssential(Solo48):
    icon_id = 'workflow-collaborate-interface-essential'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('workflow', 'collaborate', 'interface-essential')

    def build(self):
        self.add_line('e0', (13, 33), (13, 26))
        self.add_line('e1', (21, 26), (13, 26))
        self.add_line('e2', (13, 17), (13, 26))
        self.add_arc('e3-top', (8, 39), (18, 39), radius_x=5)
        self.add_arc('e3-bottom', (18, 39), (8, 39), radius_x=5)
        self.add_arc('e4-top', (30, 9), (40, 9), radius_x=5)
        self.add_arc('e4-bottom', (40, 9), (30, 9), radius_x=5)
        self.add_arc('e5-top', (8, 9), (18, 9), radius_x=5)
        self.add_arc('e5-bottom', (18, 9), (8, 9), radius_x=5)
        self.add_bezier('e6', (34, 15), ((33.562, 16.336), (33.314, 17.6), (32.632, 18.818)), ((30.223, 23.091), (25.606, 26), (21, 26)))
        self.add_bezier('e7', (13, 15), ((13, 15.609), (13, 16.391), (13, 17)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e6', 'e1')
        self.add_contour('c2', 'e7', 'e2')
        self.add_contour('e4', 'e4-top', 'e4-bottom', closed=True)
        self.add_contour('e5', 'e5-top', 'e5-bottom', closed=True)
        self.add_contour('e3', 'e3-top', 'e3-bottom', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'e3')
        self.relate('connect', 'c1', 'e4')
        self.relate('connect', 'c2', 'e5')
