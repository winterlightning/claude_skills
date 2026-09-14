"""Workflow data table 1 (business), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c8dfe4cb-2c1f-4086-8985-b294567074d5'
SOURCE_PATH = 'icons-json/business/workflow data table 1_c8dfe4cb-2c1f-4086-8985-b294567074d5.json'
AUTHOR = 'json_to_solo'

class WorkflowDataTable1C8dfe4cb(Solo48):
    icon_id = 'workflow-data-table-1-c8dfe4cb'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'business'
    aliases = ()
    keywords = ('workflow', 'data', 'table', 'business')

    def build(self):
        self.add_line('sym-e0', (42, 27), (6, 27))
        self.add_line('sym-e1', (6, 27), (6, 39))
        self.add_bezier('sym-e2', (6, 39), ((6, 40.047), (6.781, 42), (8, 42)))
        self.add_bezier('sym-e3', (8, 42), ((8.033, 42), (7.967, 42), (8, 42)))
        self.add_line('sym-e4', (8, 42), (18, 42))
        self.add_line('sym-e5', (18, 42), (18, 14))
        self.add_line('sym-e6', (18, 14), (30, 14))
        self.add_line('sym-e7', (30, 14), (42, 14))
        self.add_line('sym-e8', (42, 14), (42, 27))
        self.add_line('sym-e9', (42, 27), (42, 39))
        self.add_bezier('sym-e10', (42, 39), ((42, 40.047), (41.219, 42), (40, 42)))
        self.add_bezier('sym-e11', (40, 42), ((39.967, 42), (40.033, 42), (40, 42)))
        self.add_line('sym-e12', (40, 42), (30, 42))
        self.add_line('sym-e13', (30, 42), (30, 14))
        self.add_line('sym-e14', (18, 14), (6, 14))
        self.add_line('sym-e15', (6, 14), (6, 27))
        self.add_line('sym-e16', (24, 42), (18, 42))
        self.add_line('sym-e17', (24, 6), (9, 6))
        self.add_bezier('sym-e18', (9, 6), ((7.797, 6), (6, 7.789), (6, 9)))
        self.add_line('sym-e19', (6, 9), (6, 14))
        self.add_line('sym-e20', (24, 42), (30, 42))
        self.add_line('sym-e21', (24, 6), (39, 6))
        self.add_bezier('sym-e22', (39, 6), ((40.203, 6), (42, 7.789), (42, 9)))
        self.add_line('sym-e23', (42, 9), (42, 14))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13')
        self.add_contour('sym-c1', 'sym-e14', 'sym-e15')
        self.add_contour('sym-c2', 'sym-e16')
        self.add_contour('sym-c3', 'sym-e17', 'sym-e18', 'sym-e19')
        self.add_contour('sym-c4', 'sym-e20')
        self.add_contour('sym-c5', 'sym-e21', 'sym-e22', 'sym-e23')
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
