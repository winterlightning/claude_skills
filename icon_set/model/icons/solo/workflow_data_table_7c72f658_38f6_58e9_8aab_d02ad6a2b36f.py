"""Workflow data table (business), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7c72f658-38f6-58e9-8aab-d02ad6a2b36f'
SOURCE_PATH = 'icons-json/business/workflow data table_7c72f658-38f6-58e9-8aab-d02ad6a2b36f.json'
AUTHOR = 'json_to_solo'

class WorkflowDataTable(Solo48):
    icon_id = 'workflow-data-table'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'business'
    aliases = ()
    keywords = ('workflow', 'data', 'table', 'business')

    def build(self):
        self.add_line('sym-e0', (42, 33), (6, 33))
        self.add_line('sym-e1', (6, 33), (6, 24))
        self.add_line('sym-e2', (6, 24), (42, 24))
        self.add_line('sym-e3', (42, 24), (42, 14))
        self.add_line('sym-e4', (42, 14), (30, 14))
        self.add_line('sym-e5', (30, 14), (18, 14))
        self.add_line('sym-e6', (18, 14), (6, 14))
        self.add_line('sym-e7', (6, 14), (6, 9))
        self.add_arc('sym-e8', (6, 9), (10, 6), radius_x=5)
        self.add_line('sym-e9', (10, 6), (24, 6))
        self.add_line('sym-e10', (24, 6), (38, 6))
        self.add_arc('sym-e11', (38, 6), (42, 9), radius_x=5)
        self.add_line('sym-e12', (42, 9), (42, 14))
        self.add_line('sym-e13', (18, 42), (18, 14))
        self.add_line('sym-e14', (6, 14), (6, 24))
        self.add_line('sym-e15', (6, 33), (6, 39))
        self.add_arc('sym-e17', (6, 39), (9, 42), radius_x=3, sweep=False)
        self.add_arc('sym-e19', (9, 42), (10, 42), radius_x=22)
        self.add_line('sym-e20', (10, 42), (18, 42))
        self.add_line('sym-e21', (18, 42), (24, 42))
        self.add_line('sym-e22', (24, 42), (30, 42))
        self.add_line('sym-e23', (30, 42), (30, 14))
        self.add_line('sym-e24', (42, 24), (42, 33))
        self.add_line('sym-e25', (42, 33), (42, 39))
        self.add_arc('sym-e27', (42, 39), (39, 42), radius_x=3)
        self.add_arc('sym-e29', (39, 42), (38, 42), radius_x=38, sweep=False)
        self.add_line('sym-e30', (38, 42), (30, 42))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12')
        self.add_contour('sym-c1', 'sym-e13')
        self.add_contour('sym-c2', 'sym-e14')
        self.add_contour('sym-c3', 'sym-e15', 'sym-e17', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23')
        self.add_contour('sym-c4', 'sym-e24', 'sym-e25', 'sym-e27', 'sym-e29', 'sym-e30')
        self.relate('connect', 'sym-c0', 'sym-c4')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c4')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c3', 'sym-c4')
        self.relate('connect', 'sym-c0', 'sym-c3', 'sym-c4')
        self.relate('connect', 'sym-c0', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c3', 'sym-c4')
        self.relate('connect', 'sym-c0', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c3', 'sym-c4')
        self.relate('connect', 'sym-c0', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c3', 'sym-c4')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c3', 'sym-c4')
        self.relate('connect', 'sym-c0', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c3', 'sym-c4')
        self.relate('connect', 'sym-c0', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c3', 'sym-c4')
        self.relate('connect', 'sym-c0', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c3', 'sym-c4')
        self.relate('connect', 'sym-c0', 'sym-c2', 'sym-c3')
