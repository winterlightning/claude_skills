"""Workflow data table (business), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7c72f658-38f6-58e9-8aab-d02ad6a2b36f'
SOURCE_PATH = 'icons-json/business/workflow data table_7c72f658-38f6-58e9-8aab-d02ad6a2b36f.json'
AUTHOR = 'json_to_solo'

class WorkflowDataTableBusiness(Solo48):
    icon_id = 'workflow-data-table-business'
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
        self.add_bezier('sym-e8', (6, 9), ((6.687, 7.2), (7.914, 6), (10, 6)))
        self.add_line('sym-e9', (10, 6), (24, 6))
        self.add_line('sym-e10', (24, 6), (38, 6))
        self.add_bezier('sym-e11', (38, 6), ((40.086, 6), (41.313, 7.2), (42, 9)))
        self.add_line('sym-e12', (42, 9), (42, 14))
        self.add_line('sym-e13', (18, 42), (18, 14))
        self.add_line('sym-e14', (6, 14), (6, 24))
        self.add_line('sym-e15', (6, 33), (6, 39))
        self.add_bezier('sym-e16', (6, 39), ((6, 39.131), (6, 38.877), (6, 39)))
        self.add_bezier('sym-e17', (6, 39), ((6, 40.293), (7.658, 42), (9, 42)))
        self.add_bezier('sym-e18', (9, 42), ((9.065, 42), (8.935, 42), (9, 42)))
        self.add_bezier('sym-e19', (9, 42), ((9.385, 42), (9.615, 42), (10, 42)))
        self.add_line('sym-e20', (10, 42), (18, 42))
        self.add_line('sym-e21', (18, 42), (24, 42))
        self.add_line('sym-e22', (24, 42), (30, 42))
        self.add_line('sym-e23', (30, 42), (30, 14))
        self.add_line('sym-e24', (42, 24), (42, 33))
        self.add_line('sym-e25', (42, 33), (42, 39))
        self.add_bezier('sym-e26', (42, 39), ((42, 39.131), (42, 38.877), (42, 39)))
        self.add_bezier('sym-e27', (42, 39), ((42, 40.293), (40.342, 42), (39, 42)))
        self.add_bezier('sym-e28', (39, 42), ((38.935, 42), (39.065, 42), (39, 42)))
        self.add_bezier('sym-e29', (39, 42), ((38.615, 42), (38.385, 42), (38, 42)))
        self.add_line('sym-e30', (38, 42), (30, 42))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12')
        self.add_contour('sym-c1', 'sym-e13')
        self.add_contour('sym-c2', 'sym-e14')
        self.add_contour('sym-c3', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23')
        self.add_contour('sym-c4', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e27', 'sym-e28', 'sym-e29', 'sym-e30')
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
