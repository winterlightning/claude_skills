"""Switch on (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
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
        self.add_bezier('sym-e2', (18, 30), ((18, 30.335), (17.959, 30.656), (18, 31)))
        self.add_bezier('sym-e3', (18, 31), ((18.172, 32.276), (19.707, 33), (21, 33)))
        self.add_line('sym-e4', (21, 33), (24, 33))
        self.add_line('sym-e5', (24, 33), (27, 33))
        self.add_bezier('sym-e6', (27, 33), ((28.293, 33), (29.828, 32.276), (30, 31)))
        self.add_bezier('sym-e7', (30, 31), ((30.041, 30.656), (30, 30.335), (30, 30)))
        self.add_line('sym-e8', (30, 30), (30, 21))
        self.add_line('sym-e9', (30, 21), (30, 17))
        self.add_bezier('sym-e10', (30, 17), ((30, 15.658), (28.366, 15), (27, 15)))
        self.add_line('sym-e11', (27, 15), (24, 15))
        self.add_line('sym-e12', (24, 15), (21, 15))
        self.add_bezier('sym-e13', (21, 15), ((19.634, 15), (18, 15.658), (18, 17)))
        self.add_line('sym-e14', (18, 17), (18, 21))
        self.add_line('sym-e15', (24, 42), (39, 42))
        self.add_bezier('sym-e16', (39, 42), ((39.098, 42), (38.902, 42), (39, 42)))
        self.add_bezier('sym-e17', (39, 42), ((40.669, 42), (42, 40.636), (42, 39)))
        self.add_bezier('sym-e18', (42, 39), ((42, 38.845), (42, 39.164), (42, 39)))
        self.add_bezier('sym-e19', (42, 39), ((42, 38.804), (42, 38.196), (42, 38)))
        self.add_line('sym-e20', (42, 38), (42, 9))
        self.add_bezier('sym-e21', (42, 9), ((41.992, 8.894), (42, 9.106), (42, 9)))
        self.add_bezier('sym-e22', (42, 9), ((42, 7.503), (40.563, 6), (39, 6)))
        self.add_bezier('sym-e23', (39, 6), ((38.943, 6), (39.057, 6), (39, 6)))
        self.add_bezier('sym-e24', (39, 6), ((38.877, 6), (39.123, 6), (39, 6)))
        self.add_line('sym-e25', (39, 6), (24, 6))
        self.add_line('sym-e26', (24, 6), (9, 6))
        self.add_bezier('sym-e27', (9, 6), ((8.877, 6), (9.123, 6), (9, 6)))
        self.add_bezier('sym-e28', (9, 6), ((8.943, 6), (9.057, 6), (9, 6)))
        self.add_bezier('sym-e29', (9, 6), ((7.437, 6), (6, 7.503), (6, 9)))
        self.add_bezier('sym-e30', (6, 9), ((6, 9.106), (6.008, 8.894), (6, 9)))
        self.add_line('sym-e31', (6, 9), (6, 38))
        self.add_bezier('sym-e32', (6, 38), ((6, 38.196), (6, 38.804), (6, 39)))
        self.add_bezier('sym-e33', (6, 39), ((6, 39.164), (6, 38.845), (6, 39)))
        self.add_bezier('sym-e34', (6, 39), ((6, 40.636), (7.331, 42), (9, 42)))
        self.add_bezier('sym-e35', (9, 42), ((9.098, 42), (8.902, 42), (9, 42)))
        self.add_line('sym-e36', (9, 42), (24, 42))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14')
        self.add_contour('sym-c1', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e27', 'sym-e28', 'sym-e29', 'sym-e30', 'sym-e31', 'sym-e32', 'sym-e33', 'sym-e34', 'sym-e35', 'sym-e36', closed=True)
