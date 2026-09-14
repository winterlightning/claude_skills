"""Electric waves 1 (state), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e6789468-9cc2-4444-a388-10e9ec1fdcb5'
SOURCE_PATH = 'icons-json/state/electric waves 1_e6789468-9cc2-4444-a388-10e9ec1fdcb5.json'
AUTHOR = 'json_to_solo'

class ElectricWaves1State(Solo48):
    icon_id = 'electric-waves-1-state'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('electric', 'waves', 'state')

    def build(self):
        self.add_line('sym-e0', (24, 40), (24, 40))
        self.add_line('sym-e2', (24, 8), (23, 8))
        self.add_arc('sym-e3', (23, 8), (4, 16), radius_x=30, sweep=False)
        self.add_arc('sym-e4', (4, 16), (4, 17), radius_x=1)
        self.add_arc('sym-e5', (24, 21), (11, 26), radius_x=19, sweep=False)
        self.add_line('sym-e7', (24, 8), (25, 8))
        self.add_arc('sym-e8', (25, 8), (44, 16), radius_x=30)
        self.add_arc('sym-e9', (44, 16), (44, 17), radius_x=1, sweep=False)
        self.add_arc('sym-e10', (24, 21), (37, 26), radius_x=18)
        self.add_contour('sym-c0', 'sym-e0', closed=True)
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e4')
        self.add_contour('sym-c2', 'sym-e5')
        self.add_contour('sym-c3', 'sym-e7', 'sym-e8', 'sym-e9')
        self.add_contour('sym-c4', 'sym-e10')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c2', 'sym-c4')
