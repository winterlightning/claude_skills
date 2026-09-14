"""Power outlet type g (electronics), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c0411cd9-5038-475a-aa2f-c63811150a34'
SOURCE_PATH = 'icons-json/electronics/power outlet type g_c0411cd9-5038-475a-aa2f-c63811150a34.json'
AUTHOR = 'json_to_solo'

class PowerOutletTypeGElectronics(Solo48):
    icon_id = 'power-outlet-type-g-electronics'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'electronics'
    aliases = ()
    keywords = ('power', 'outlet', 'type', 'g', 'electronics')

    def build(self):
        self.add_line('sym-e0', (24, 22), (24, 13))
        self.add_line('sym-e1', (13, 31), (19, 31))
        self.add_line('sym-e2', (24, 42), (10, 42))
        self.add_arc('sym-e3', (10, 42), (6, 38), radius_x=5)
        self.add_line('sym-e5', (6, 38), (6, 11))
        self.add_arc('sym-e7', (6, 11), (10, 6), radius_x=6)
        self.add_line('sym-e8', (10, 6), (24, 6))
        self.add_line('sym-e9', (24, 6), (38, 6))
        self.add_arc('sym-e10', (38, 6), (42, 11), radius_x=6)
        self.add_line('sym-e12', (42, 11), (42, 38))
        self.add_arc('sym-e14', (42, 38), (38, 42), radius_x=5)
        self.add_line('sym-e15', (38, 42), (24, 42))
        self.add_line('sym-e16', (35, 31), (29, 31))
        self.add_contour('sym-c0', 'sym-e0')
        self.add_contour('sym-c1', 'sym-e1')
        self.add_contour('sym-c2', 'sym-e2', 'sym-e3', 'sym-e5', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e12', 'sym-e14', 'sym-e15', closed=True)
        self.add_contour('sym-c3', 'sym-e16')
