"""Lock (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a48f8360-8910-49af-84ed-897f79bb4330'
SOURCE_PATH = 'icons-json/interface-essential/lock_a48f8360-8910-49af-84ed-897f79bb4330.json'
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
        self.add_arc('sym-e1', (23, 4), (13, 14), radius_x=10, sweep=False)
        self.add_line('sym-e2', (13, 14), (13, 20))
        self.add_line('sym-e3', (13, 20), (24, 20))
        self.add_line('sym-e4', (24, 20), (35, 20))
        self.add_line('sym-e5', (35, 20), (35, 14))
        self.add_arc('sym-e6', (35, 14), (25, 4), radius_x=11, sweep=False)
        self.add_line('sym-e7', (25, 4), (24, 4))
        self.add_line('sym-e8', (24, 44), (13, 44))
        self.add_arc('sym-e10', (13, 44), (8, 39), radius_x=5)
        self.add_line('sym-e11', (8, 39), (8, 38))
        self.add_line('sym-e12', (8, 38), (8, 23))
        self.add_arc('sym-e13', (8, 23), (13, 20), radius_x=4)
        self.add_line('sym-e16', (24, 44), (35, 44))
        self.add_arc('sym-e18', (35, 44), (40, 39), radius_x=5, sweep=False)
        self.add_arc('sym-e19', (40, 39), (40, 38), radius_x=38)
        self.add_line('sym-e20', (40, 38), (40, 23))
        self.add_arc('sym-e21', (40, 23), (35, 20), radius_x=4, sweep=False)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', closed=True)
        self.add_contour('sym-c1', 'sym-e8', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13')
        self.add_contour('sym-c2', 'sym-e16', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
