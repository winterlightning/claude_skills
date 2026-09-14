"""Workflow merge 1 (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8a5b276f-efd5-4b4c-a767-4819ad682ec2'
SOURCE_PATH = 'icons-json/interface-essential/workflow merge 1_8a5b276f-efd5-4b4c-a767-4819ad682ec2.json'
AUTHOR = 'json_to_solo'

class WorkflowMerge1InterfaceEssential(Solo48):
    icon_id = 'workflow-merge-1-interface-essential'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('workflow', 'merge', 'interface-essential')

    def build(self):
        self.add_line('e0', (24, 18), (24, 20))
        self.add_arc('e1-top', (30, 39), (40, 39), radius_x=5)
        self.add_arc('e1-bottom', (40, 39), (30, 39), radius_x=5)
        self.add_arc('e2-top', (8, 39), (18, 39), radius_x=5)
        self.add_arc('e2-bottom', (18, 39), (8, 39), radius_x=5)
        self.add_arc('e3-top', (18, 10), (30, 10), radius_x=6)
        self.add_arc('e3-bottom', (30, 10), (18, 10), radius_x=6)
        self.add_bezier('e4', (35, 33), ((35.699, 29.8), (34.021, 25.991), (31.015, 24.891)), ((29.491, 24.327), (28.101, 24.755), (26.602, 23.773)), ((25.347, 22.945), (24.733, 21.336), (24, 20)))
        self.add_bezier('e5', (13, 33), ((13.194, 30.118), (13.246, 27.818), (15.596, 25.818)), ((17.448, 24.227), (18.728, 25.027), (20.573, 24.191)), ((22.248, 23.445), (23.065, 21.6), (24, 20)))
        self.add_bezier('e6', (24, 17), ((24, 17.3), (24, 17.7), (24, 18)))
        self.add_contour('c0', 'e4')
        self.add_contour('c1', 'e5')
        self.add_contour('c2', 'e6', 'e0')
        self.add_contour('e1', 'e1-top', 'e1-bottom', closed=True)
        self.add_contour('e2', 'e2-top', 'e2-bottom', closed=True)
        self.add_contour('e3', 'e3-top', 'e3-bottom', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'e1')
        self.relate('connect', 'c1', 'e2')
        self.relate('connect', 'c2', 'e3')
