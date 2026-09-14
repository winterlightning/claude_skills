"""Pin (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a0e2619f-eb92-5a87-a26b-6e67a05f7d66'
SOURCE_PATH = 'icons-json/interface-essential/pin_a0e2619f-eb92-5a87-a26b-6e67a05f7d66.json'
AUTHOR = 'json_to_solo'

class PinA0e2619f(Solo48):
    icon_id = 'pin-a0e2619f'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('pin', 'interface-essential')

    def build(self):
        self.add_arc('sym-e0', (18, 19), (30, 19), radius_x=6, radius_y=5)
        self.add_arc('sym-e1', (30, 19), (18, 19), radius_x=6, radius_y=5)
        self.add_line('sym-e2-1', (24, 44), (14, 32))
        self.add_arc('sym-e2-2', (14, 32), (12, 28), radius_x=61)
        self.add_arc('sym-e3', (12, 28), (8, 19), radius_x=18)
        self.add_line('sym-e4', (8, 19), (8, 18))
        self.add_line('sym-e5', (8, 18), (8, 17))
        self.add_arc('sym-e6', (8, 17), (23, 4), radius_x=16)
        self.add_line('sym-e7', (23, 4), (24, 4))
        self.add_line('sym-e10', (24, 4), (25, 4))
        self.add_arc('sym-e11', (25, 4), (40, 17), radius_x=16)
        self.add_arc('sym-e12', (40, 17), (40, 18), radius_x=23, sweep=False)
        self.add_arc('sym-e13', (40, 18), (40, 19), radius_x=24, sweep=False)
        self.add_arc('sym-e14', (40, 19), (36, 28), radius_x=18)
        self.add_line('sym-e15-1', (36, 28), (34, 32))
        self.add_line('sym-e15-2', (34, 32), (24, 44))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e2-1', 'sym-e2-2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15-1', 'sym-e15-2', closed=True)
