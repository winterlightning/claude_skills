"""Switch on (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '69a3714e-47a4-5c41-9c78-1b1b26a4a41c'
SOURCE_PATH = 'icons-json/interface-essential/switch on_69a3714e-47a4-5c41-9c78-1b1b26a4a41c.json'
AUTHOR = 'json_to_solo'

class SwitchOnInterfaceEssential(Solo48):
    icon_id = 'switch-on-interface-essential'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('switch', 'on', 'interface-essential')

    def build(self):
        self.add_line('sym-e0', (30, 21), (18, 21))
        self.add_line('sym-e1', (18, 21), (18, 30))
        self.add_line('sym-e2', (18, 30), (18, 31))
        self.add_arc('sym-e3', (18, 31), (21, 33), radius_x=3, sweep=False)
        self.add_line('sym-e4', (21, 33), (24, 33))
        self.add_line('sym-e5', (24, 33), (27, 33))
        self.add_arc('sym-e6', (27, 33), (30, 31), radius_x=3, sweep=False)
        self.add_line('sym-e7', (30, 31), (30, 30))
        self.add_line('sym-e8', (30, 30), (30, 21))
        self.add_line('sym-e9', (30, 21), (30, 17))
        self.add_arc('sym-e10', (30, 17), (27, 15), radius_x=3, sweep=False)
        self.add_line('sym-e11', (27, 15), (24, 15))
        self.add_line('sym-e12', (24, 15), (21, 15))
        self.add_arc('sym-e13', (21, 15), (18, 17), radius_x=3, sweep=False)
        self.add_line('sym-e14', (18, 17), (18, 21))
        self.add_line('sym-e15', (24, 42), (39, 42))
        self.add_arc('sym-e17', (39, 42), (42, 39), radius_x=3, sweep=False)
        self.add_arc('sym-e19', (42, 39), (42, 38), radius_x=38)
        self.add_line('sym-e20', (42, 38), (42, 9))
        self.add_arc('sym-e22', (42, 9), (39, 6), radius_x=3, sweep=False)
        self.add_line('sym-e25', (39, 6), (24, 6))
        self.add_line('sym-e26', (24, 6), (9, 6))
        self.add_arc('sym-e29', (9, 6), (6, 9), radius_x=3, sweep=False)
        self.add_line('sym-e31', (6, 9), (6, 38))
        self.add_line('sym-e32', (6, 38), (6, 39))
        self.add_arc('sym-e34', (6, 39), (9, 42), radius_x=3, sweep=False)
        self.add_line('sym-e36', (9, 42), (24, 42))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14')
        self.add_contour('sym-c1', 'sym-e15', 'sym-e17', 'sym-e19', 'sym-e20', 'sym-e22', 'sym-e25', 'sym-e26', 'sym-e29', 'sym-e31', 'sym-e32', 'sym-e34', 'sym-e36', closed=True)
