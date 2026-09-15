"""Table tools (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'adb0d6e1-411d-459c-b0d6-73e65e4e8c15'
SOURCE_PATH = 'pictographic-primitives/interface-essential/table tools_adb0d6e1-411d-459c-b0d6-73e65e4e8c15.svg'
AUTHOR = 'gpt-6'

class TableTools(Solo48):
    icon_id = 'table-tools'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('table', 'tools', 'interface-essential')

    def build(self):
        self.add_line('sym-e0', (31, 40), (7, 40))
        self.add_arc('sym-e2', (7, 40), (4, 37), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('sym-e3', (4, 37), (4, 29))
        self.add_line('sym-e4', (4, 29), (44, 29))
        self.add_line('sym-e7', (44, 29), (44, 37))
        self.add_arc('sym-e8', (44, 37), (41, 40), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('sym-e9', (41, 40), (31, 40))
        self.add_line('sym-e10', (31, 40), (31, 18))
        self.add_line('sym-e12', (31, 18), (17, 18))
        self.add_line('sym-e13', (17, 18), (17, 40))
        self.add_line('sym-e15', (44, 29), (44, 18))
        self.add_line('sym-e16', (44, 18), (31, 18))
        self.add_line('sym-e17', (44, 18), (44, 11))
        self.add_arc('sym-e18', (44, 11), (44, 10), radius_x=1, radius_y=1, large_arc=False, sweep=True)
        self.add_arc('sym-e19', (44, 10), (41, 8), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('sym-e20', (41, 8), (7, 8))
        self.add_arc('sym-e22', (7, 8), (4, 10), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('sym-e23', (4, 10), (4, 29))
        self.add_line('sym-e26', (17, 18), (4, 18))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e12', 'sym-e13', closed=False)
        self.add_contour('sym-c1', 'sym-e15', 'sym-e16', closed=False)
        self.add_contour('sym-c2', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e22', 'sym-e23', closed=False)
        self.add_contour('sym-c3', 'sym-e26', closed=False)
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
