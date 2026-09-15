"""Pin (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '85a2d016-7773-52ae-a800-9fa66b8f9b53'
SOURCE_PATH = 'icons-json/interface-essential/pin_85a2d016-7773-52ae-a800-9fa66b8f9b53.json'
AUTHOR = 'gpt-6'

class PinInterfaceEssential(Solo48):
    icon_id = 'pin-interface-essential'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('pin', 'interface-essential')

    def build(self):
        self.add_arc('sym-e0', (18, 18), (30, 18), radius_x=6, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('sym-e1', (30, 18), (18, 18), radius_x=6, radius_y=5, large_arc=False, sweep=True)
        self.add_line('sym-e2', (24, 44), (12, 28))
        self.add_arc('sym-e3', (12, 28), (8, 18), radius_x=18, radius_y=18, large_arc=False, sweep=True)
        self.add_line('sym-e5', (8, 18), (8, 17))
        self.add_arc('sym-e6', (8, 17), (9, 14), radius_x=9, radius_y=9, large_arc=False, sweep=True)
        self.add_arc('sym-e7', (9, 14), (23, 4), radius_x=15, radius_y=15, large_arc=False, sweep=True)
        self.add_line('sym-e8', (23, 4), (25, 4))
        self.add_arc('sym-e10', (25, 4), (39, 14), radius_x=15, radius_y=15, large_arc=False, sweep=True)
        self.add_line('sym-e11', (39, 14), (40, 17))
        self.add_line('sym-e12', (40, 17), (40, 18))
        self.add_arc('sym-e14', (40, 18), (36, 28), radius_x=18, radius_y=18, large_arc=False, sweep=True)
        self.add_line('sym-e15', (36, 28), (24, 44))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e14', 'sym-e15', closed=True)
