"""Lock (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ae80ad8e-78ff-4d1d-a60a-d6c106563f5d'
SOURCE_PATH = 'icons-json/interface-essential/lock_ae80ad8e-78ff-4d1d-a60a-d6c106563f5d.json'
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
        self.add_arc('sym-e0', (21, 32), (27, 32), radius_x=3, radius_y=4)
        self.add_arc('sym-e1', (27, 32), (21, 32), radius_x=3, radius_y=4)
        self.add_arc('sym-e3', (24, 4), (14, 15), radius_x=11, sweep=False)
        self.add_line('sym-e4', (14, 15), (14, 20))
        self.add_line('sym-e5', (14, 20), (12, 20))
        self.add_arc('sym-e6', (12, 20), (8, 24), radius_x=5, sweep=False)
        self.add_line('sym-e7', (8, 24), (8, 39))
        self.add_line('sym-e10', (8, 39), (8, 41))
        self.add_arc('sym-e11', (8, 41), (12, 44), radius_x=5, sweep=False)
        self.add_line('sym-e13', (12, 44), (24, 44))
        self.add_line('sym-e14', (24, 44), (36, 44))
        self.add_arc('sym-e16', (36, 44), (40, 41), radius_x=5, sweep=False)
        self.add_line('sym-e17', (40, 41), (40, 39))
        self.add_line('sym-e20', (40, 39), (40, 24))
        self.add_arc('sym-e21', (40, 24), (36, 20), radius_x=5, sweep=False)
        self.add_line('sym-e22', (36, 20), (34, 20))
        self.add_line('sym-e23', (34, 20), (34, 15))
        self.add_arc('sym-e24', (34, 15), (24, 4), radius_x=11, sweep=False)
        self.add_line('sym-e26', (14, 20), (24, 20))
        self.add_line('sym-e27', (24, 20), (34, 20))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e10', 'sym-e11', 'sym-e13', 'sym-e14', 'sym-e16', 'sym-e17', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', closed=True)
        self.add_contour('sym-c2', 'sym-e26', 'sym-e27')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
