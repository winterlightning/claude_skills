"""Wave forward (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e127ddf8-ee9b-5545-b197-daeac78ecea8'
SOURCE_PATH = 'icons-json/interface-essential/wave forward_e127ddf8-ee9b-5545-b197-daeac78ecea8.json'
AUTHOR = 'json_to_solo'

class WaveForwardInterfaceEssential(Solo48):
    icon_id = 'wave-forward-interface-essential'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('wave', 'forward', 'interface-essential')

    def build(self):
        self.add_arc('sym-e0', (40, 24), (40, 23), radius_x=1)
        self.add_arc('sym-e1', (40, 23), (33, 10), radius_x=19, sweep=False)
        self.add_line('sym-e2', (33, 10), (26, 4))
        self.add_arc('sym-e4', (8, 11), (11, 13), radius_x=35, sweep=False)
        self.add_arc('sym-e5', (11, 13), (17, 24), radius_x=15)
        self.add_arc('sym-e6', (17, 24), (11, 35), radius_x=15)
        self.add_arc('sym-e7', (11, 35), (8, 37), radius_x=35, sweep=False)
        self.add_arc('sym-e8', (40, 24), (40, 25), radius_x=1, sweep=False)
        self.add_arc('sym-e9', (40, 25), (33, 38), radius_x=19)
        self.add_line('sym-e10', (33, 38), (26, 44))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2')
        self.add_contour('sym-c1', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7')
        self.add_contour('sym-c2', 'sym-e8', 'sym-e9', 'sym-e10')
        self.relate('connect', 'sym-c0', 'sym-c2')
