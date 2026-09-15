"""Lock (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '25032f12-63bc-403a-9b53-69083f3313cb'
SOURCE_PATH = 'pictographic-primitives/interface-essential/lock_25032f12-63bc-403a-9b53-69083f3313cb.svg'
AUTHOR = 'gpt-6'

class Lock(Solo48):
    icon_id = 'lock'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('lock', 'interface-essential')

    def build(self):
        self.add_line('sym-e0', (24, 4), (23, 4))
        self.add_arc('sym-e1', (23, 4), (13, 14), radius_x=10, radius_y=10, large_arc=False, sweep=False)
        self.add_line('sym-e2', (13, 14), (13, 20))
        self.add_line('sym-e3', (13, 20), (35, 20))
        self.add_line('sym-e5', (35, 20), (35, 14))
        self.add_arc('sym-e6', (35, 14), (25, 4), radius_x=11, radius_y=11, large_arc=False, sweep=False)
        self.add_line('sym-e7', (25, 4), (24, 4))
        self.add_line('sym-e8', (24, 44), (13, 44))
        self.add_arc('sym-e10', (13, 44), (8, 39), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('sym-e11', (8, 39), (8, 23))
        self.add_arc('sym-e13', (8, 23), (13, 20), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('sym-e16', (24, 44), (35, 44))
        self.add_arc('sym-e18', (35, 44), (40, 39), radius_x=5, radius_y=5, large_arc=False, sweep=False)
        self.add_arc('sym-e19', (40, 39), (40, 38), radius_x=38, radius_y=38, large_arc=False, sweep=True)
        self.add_line('sym-e20', (40, 38), (40, 23))
        self.add_arc('sym-e21', (40, 23), (35, 20), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e5', 'sym-e6', 'sym-e7', closed=True)
        self.add_contour('sym-c1', 'sym-e8', 'sym-e10', 'sym-e11', 'sym-e13', closed=False)
        self.add_contour('sym-c2', 'sym-e16', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', closed=False)
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
