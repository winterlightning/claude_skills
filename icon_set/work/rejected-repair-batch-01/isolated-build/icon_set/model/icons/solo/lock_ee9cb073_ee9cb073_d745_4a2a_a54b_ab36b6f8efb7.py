"""Lock (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ee9cb073-d745-4a2a-a54b-ab36b6f8efb7'
SOURCE_PATH = 'pictographic-primitives/interface-essential/lock_ee9cb073-d745-4a2a-a54b-ab36b6f8efb7.svg'
AUTHOR = 'gpt-6'

class LockEe9cb073(Solo48):
    icon_id = 'lock-ee9cb073'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('lock', 'interface-essential')

    def build(self):
        self.add_line('sym-e0', (24, 4), (23, 4))
        self.add_arc('sym-e1', (23, 4), (13, 14), radius_x=12, radius_y=12, large_arc=False, sweep=False)
        self.add_line('sym-e2', (13, 14), (13, 20))
        self.add_line('sym-e3', (13, 20), (35, 20))
        self.add_line('sym-e5', (35, 20), (35, 14))
        self.add_arc('sym-e6', (35, 14), (25, 4), radius_x=11, radius_y=11, large_arc=False, sweep=False)
        self.add_line('sym-e7', (25, 4), (24, 4))
        self.add_line('sym-e8', (8, 23), (8, 40))
        self.add_arc('sym-e9', (8, 40), (12, 44), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('sym-e10', (12, 44), (36, 44))
        self.add_arc('sym-e14', (36, 44), (40, 40), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('sym-e15', (40, 40), (40, 23))
        self.add_arc('sym-e17', (40, 23), (38, 20), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('sym-e18', (38, 20), (35, 20))
        self.add_line('sym-e19', (13, 20), (10, 20))
        self.add_arc('sym-e20', (10, 20), (8, 23), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e5', 'sym-e6', 'sym-e7', closed=True)
        self.add_contour('sym-c1', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e14', 'sym-e15', 'sym-e17', 'sym-e18', closed=False)
        self.add_contour('sym-c2', 'sym-e19', 'sym-e20', closed=False)
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2')
