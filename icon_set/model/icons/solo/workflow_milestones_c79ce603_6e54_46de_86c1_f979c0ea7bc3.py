"""Workflow milestones (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c79ce603-6e54-46de-86c1-f979c0ea7bc3'
SOURCE_PATH = 'icons-json/interface-essential/workflow milestones_c79ce603-6e54-46de-86c1-f979c0ea7bc3.json'
AUTHOR = 'json_to_solo'

class WorkflowMilestones(Solo48):
    icon_id = 'workflow-milestones'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('workflow', 'milestones', 'interface-essential')

    def build(self):
        self.add_line('e0', (4, 40), (44, 40))
        self.add_line('e1', (30, 23), (40, 15))
        self.add_line('e2', (40, 15), (30, 8))
        self.add_line('e3', (30, 8), (30, 40))
        self.add_line('e4', (10, 40), (10, 23))
        self.add_line('e5', (20, 15), (10, 8))
        self.add_line('e6', (10, 8), (10, 23))
        self.add_line('e7', (10, 23), (20, 15))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2', 'e3')
        self.add_contour('c2', 'e4')
        self.add_contour('c3', 'e5', 'e6', 'e7', closed=True)
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c2', 'c0')
