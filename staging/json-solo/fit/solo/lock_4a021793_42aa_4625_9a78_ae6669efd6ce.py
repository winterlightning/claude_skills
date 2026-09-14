"""Lock (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4a021793-42aa-4625-9a78-ae6669efd6ce'
SOURCE_PATH = 'icons-json/interface-essential/lock_4a021793-42aa-4625-9a78-ae6669efd6ce.json'
AUTHOR = 'json_to_solo'

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
        self.add_arc('sym-e1', (23, 4), (13, 14), radius_x=12, sweep=False)
        self.add_line('sym-e2', (13, 14), (13, 20))
        self.add_line('sym-e3', (13, 20), (24, 20))
        self.add_line('sym-e4', (24, 20), (35, 20))
        self.add_line('sym-e5', (35, 20), (35, 14))
        self.add_arc('sym-e6', (35, 14), (25, 4), radius_x=11, sweep=False)
        self.add_line('sym-e7', (25, 4), (24, 4))
        self.add_line('sym-e8', (8, 23), (8, 40))
        self.add_arc('sym-e9', (8, 40), (12, 44), radius_x=4, sweep=False)
        self.add_line('sym-e10', (12, 44), (13, 44))
        self.add_line('sym-e11', (13, 44), (24, 44))
        self.add_line('sym-e12', (24, 44), (35, 44))
        self.add_line('sym-e13', (35, 44), (36, 44))
        self.add_arc('sym-e14', (36, 44), (40, 40), radius_x=4, sweep=False)
        self.add_line('sym-e15', (40, 40), (40, 23))
        self.add_arc('sym-e17', (40, 23), (38, 20), radius_x=4, sweep=False)
        self.add_line('sym-e18', (38, 20), (35, 20))
        self.add_line('sym-e19', (13, 20), (10, 20))
        self.add_arc('sym-e20', (10, 20), (8, 23), radius_x=4, sweep=False)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', closed=True)
        self.add_contour('sym-c1', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e17', 'sym-e18')
        self.add_contour('sym-c2', 'sym-e19', 'sym-e20')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2')
