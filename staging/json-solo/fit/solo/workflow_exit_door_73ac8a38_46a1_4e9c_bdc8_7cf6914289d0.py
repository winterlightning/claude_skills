"""Workflow exit door (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '73ac8a38-46a1-4e9c-bdc8-7cf6914289d0'
SOURCE_PATH = 'icons-json/interface-essential/workflow exit door_73ac8a38-46a1-4e9c-bdc8-7cf6914289d0.json'
AUTHOR = 'json_to_solo'

class WorkflowExitDoorInterfaceEssential(Solo48):
    icon_id = 'workflow-exit-door-interface-essential'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('workflow', 'exit', 'door', 'interface-essential')

    def build(self):
        self.add_line('e0', (13, 4), (13, 9))
        self.add_line('e1', (13, 44), (13, 20))
        self.add_line('e2', (34, 30), (34, 19))
        self.add_line('e3', (30, 15), (20, 15))
        self.add_arc('e4-top', (30, 35), (40, 35), radius_x=5)
        self.add_arc('e4-bottom', (40, 35), (30, 35), radius_x=5)
        self.add_arc('e5-top', (8, 15), (20, 15), radius_x=6, radius_y=5)
        self.add_arc('e5-bottom', (20, 15), (8, 15), radius_x=6, radius_y=5)
        self.add_arc('e6', (34, 19), (30, 15), radius_x=4, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e6', 'e3')
        self.add_contour('e4', 'e4-top', 'e4-bottom', closed=True)
        self.add_contour('e5', 'e5-top', 'e5-bottom', closed=True)
        self.relate('connect', 'c0', 'e5')
        self.relate('connect', 'c1', 'e5')
        self.relate('connect', 'c2', 'e4')
        self.relate('connect', 'c2', 'e5')
