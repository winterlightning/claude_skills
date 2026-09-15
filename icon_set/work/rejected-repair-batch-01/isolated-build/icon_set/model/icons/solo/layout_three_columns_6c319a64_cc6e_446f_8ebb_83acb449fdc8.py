"""Layout three columns (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6c319a64-cc6e-446f-8ebb-83acb449fdc8'
SOURCE_PATH = 'pictographic-primitives/interface-essential/layout three columns_6c319a64-cc6e-446f-8ebb-83acb449fdc8.svg'
AUTHOR = 'gpt-6'

class LayoutThreeColumns(Solo48):
    icon_id = 'layout-three-columns'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('layout', 'three', 'columns', 'interface-essential')

    def build(self):
        self.add_line('sym-e0', (18, 8), (18, 40))
        self.add_line('sym-e1', (18, 40), (30, 40))
        self.add_line('sym-e2', (30, 40), (30, 8))
        self.add_line('sym-e3', (30, 8), (8, 8))
        self.add_arc('sym-e5', (8, 8), (4, 11), radius_x=5, radius_y=5, large_arc=False, sweep=False)
        self.add_line('sym-e7', (4, 11), (4, 37))
        self.add_arc('sym-e10', (4, 37), (8, 40), radius_x=5, radius_y=5, large_arc=False, sweep=False)
        self.add_line('sym-e11', (8, 40), (18, 40))
        self.add_line('sym-e12', (30, 8), (40, 8))
        self.add_arc('sym-e13', (40, 8), (44, 11), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('sym-e15', (44, 11), (44, 37))
        self.add_arc('sym-e18', (44, 37), (40, 40), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('sym-e19', (40, 40), (30, 40))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e5', 'sym-e7', 'sym-e10', 'sym-e11', closed=False)
        self.add_contour('sym-c1', 'sym-e12', 'sym-e13', 'sym-e15', 'sym-e18', 'sym-e19', closed=False)
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
