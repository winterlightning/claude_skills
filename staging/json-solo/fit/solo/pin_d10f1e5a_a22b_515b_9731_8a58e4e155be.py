"""Pin (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd10f1e5a-a22b-515b-9731-8a58e4e155be'
SOURCE_PATH = 'icons-json/interface-essential/pin_d10f1e5a-a22b-515b-9731-8a58e4e155be.json'
AUTHOR = 'json_to_solo'

class Pin(Solo48):
    icon_id = 'pin'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('pin', 'interface-essential')

    def build(self):
        self.add_line('sym-e0', (9, 42), (14, 42))
        self.add_line('sym-e1', (14, 42), (24, 44))
        self.add_line('sym-e2', (24, 44), (34, 42))
        self.add_line('sym-e3', (34, 42), (39, 42))
        self.add_line('sym-e4', (24, 39), (19, 33))
        self.add_line('sym-e5', (19, 33), (12, 25))
        self.add_arc('sym-e6', (12, 25), (8, 17), radius_x=14)
        self.add_line('sym-e7', (8, 17), (8, 16))
        self.add_arc('sym-e9-1', (8, 16), (12, 8), radius_x=11)
        self.add_arc('sym-e9-2', (12, 8), (23, 4), radius_x=18)
        self.add_arc('sym-e10', (23, 4), (24, 4), radius_x=70, sweep=False)
        self.add_line('sym-e13', (24, 4), (25, 4))
        self.add_arc('sym-e14-1', (25, 4), (36, 8), radius_x=18)
        self.add_arc('sym-e14-2', (36, 8), (40, 16), radius_x=11)
        self.add_arc('sym-e16', (40, 16), (40, 17), radius_x=23, sweep=False)
        self.add_arc('sym-e17', (40, 17), (36, 25), radius_x=14)
        self.add_line('sym-e18', (36, 25), (29, 33))
        self.add_line('sym-e19', (29, 33), (24, 39))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3')
        self.add_contour('sym-c1', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e9-1', 'sym-e9-2', 'sym-e10', 'sym-e13', 'sym-e14-1', 'sym-e14-2', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', closed=True)
