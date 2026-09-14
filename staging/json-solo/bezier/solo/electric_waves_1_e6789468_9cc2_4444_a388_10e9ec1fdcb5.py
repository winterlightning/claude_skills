"""Electric waves 1 (state), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
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
        self.add_bezier('sym-e1', (24, 8), ((23.945, 8), (24.054, 8), (24, 8)))
        self.add_bezier('sym-e2', (24, 8), ((23.627, 8), (23.373, 8), (23, 8)))
        self.add_bezier('sym-e3', (23, 8), ((16.518, 8), (9.409, 11.409), (4, 16)))
        self.add_bezier('sym-e4', (4, 16), ((4, 16.148), (4.155, 16.84), (4, 17)))
        self.add_bezier('sym-e5', (24, 21), ((19.48, 21), (14.716, 22.358), (11, 26)))
        self.add_bezier('sym-e6', (24, 8), ((24.055, 8), (23.946, 8), (24, 8)))
        self.add_bezier('sym-e7', (24, 8), ((24.373, 8), (24.627, 8), (25, 8)))
        self.add_bezier('sym-e8', (25, 8), ((31.482, 8), (38.591, 11.409), (44, 16)))
        self.add_bezier('sym-e9', (44, 16), ((44, 16.148), (43.845, 16.84), (44, 17)))
        self.add_bezier('sym-e10', (24, 21), ((28.52, 21), (33.284, 22.358), (37, 26)))
        self.add_contour('sym-c0', 'sym-e0', closed=True)
        self.add_contour('sym-c1', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4')
        self.add_contour('sym-c2', 'sym-e5')
        self.add_contour('sym-c3', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9')
        self.add_contour('sym-c4', 'sym-e10')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c2', 'sym-c4')
