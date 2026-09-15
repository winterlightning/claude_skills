"""Workflow data table 1 (business), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '85a99e1a-5536-45d4-b09e-abc39d640a88'
SOURCE_PATH = 'pictographic-primitives/business/workflow data table 1_85a99e1a-5536-45d4-b09e-abc39d640a88.svg'
AUTHOR = 'gpt-6'

class WorkflowDataTable1(Solo48):
    icon_id = 'workflow-data-table-1'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'business'
    aliases = ()
    keywords = ('workflow', 'data', 'table', 'business')

    def build(self):
        self.add_line('sym-e0', (42, 27), (6, 27))
        self.add_line('sym-e1', (6, 27), (6, 39))
        self.add_arc('sym-e2', (6, 39), (8, 42), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('sym-e4', (8, 42), (18, 42))
        self.add_line('sym-e5', (18, 42), (18, 14))
        self.add_line('sym-e6', (18, 14), (42, 14))
        self.add_line('sym-e8', (42, 14), (42, 39))
        self.add_arc('sym-e10', (42, 39), (40, 42), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('sym-e12', (40, 42), (30, 42))
        self.add_line('sym-e13', (30, 42), (30, 14))
        self.add_line('sym-e14', (18, 14), (6, 14))
        self.add_line('sym-e15', (6, 14), (6, 27))
        self.add_line('sym-e16', (24, 42), (18, 42))
        self.add_line('sym-e17', (24, 6), (9, 6))
        self.add_arc('sym-e18', (9, 6), (6, 9), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('sym-e19', (6, 9), (6, 14))
        self.add_line('sym-e20', (24, 42), (30, 42))
        self.add_line('sym-e21', (24, 6), (39, 6))
        self.add_arc('sym-e22', (39, 6), (42, 9), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('sym-e23', (42, 9), (42, 14))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e8', 'sym-e10', 'sym-e12', 'sym-e13', closed=False)
        self.add_contour('sym-c1', 'sym-e14', 'sym-e15', closed=False)
        self.add_contour('sym-c2', 'sym-e16', closed=False)
        self.add_contour('sym-c3', 'sym-e17', 'sym-e18', 'sym-e19', closed=False)
        self.add_contour('sym-c4', 'sym-e20', closed=False)
        self.add_contour('sym-c5', 'sym-e21', 'sym-e22', 'sym-e23', closed=False)
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c5')
        self.relate('connect', 'sym-c0', 'sym-c4')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c2', 'sym-c4')
        self.relate('connect', 'sym-c3', 'sym-c5')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c4')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c5')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c4', 'sym-c5')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c4')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c5')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c4', 'sym-c5')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c4')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c4')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c4')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c4')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
