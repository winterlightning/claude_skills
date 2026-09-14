"""Eye 1 (state), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4fe0ffe1-6a10-4f5e-96f8-3d6033f13623'
SOURCE_PATH = 'icons-json/state/eye 1_4fe0ffe1-6a10-4f5e-96f8-3d6033f13623.json'
AUTHOR = 'json_to_solo'

class Eye14fe0ffe1(Solo48):
    icon_id = 'eye-1-4fe0ffe1'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('eye', 'state')

    def build(self):
        self.add_line('sym-e0', (24, 24), (24, 24))
        self.add_bezier('sym-e1', (44, 24), ((44, 24.012), (43.995, 23.988), (44, 24)))
        self.add_bezier('sym-e2', (44, 24), ((44, 24.505), (41.382, 29.446), (41, 30)))
        self.add_bezier('sym-e3', (41, 30), ((36.909, 35.92), (30.091, 40), (24, 40)))
        self.add_bezier('sym-e4', (24, 40), ((23.836, 40), (24.164, 40), (24, 40)))
        self.add_bezier('sym-e5', (24, 40), ((23.836, 40), (23.164, 40), (23, 40)))
        self.add_bezier('sym-e6', (23, 40), ((17.164, 40), (12.009, 35.477), (8, 30)))
        self.add_bezier('sym-e7', (8, 30), ((6.618, 28.117), (5.173, 26.129), (4, 24)))
        self.add_bezier('sym-e8', (4, 24), ((5.173, 21.871), (6.618, 19.883), (8, 18)))
        self.add_bezier('sym-e9', (8, 18), ((12.009, 12.523), (17.164, 8), (23, 8)))
        self.add_bezier('sym-e10', (23, 8), ((23.164, 8), (23.836, 8), (24, 8)))
        self.add_bezier('sym-e11', (24, 8), ((24.164, 8), (23.836, 8), (24, 8)))
        self.add_bezier('sym-e12', (24, 8), ((30.091, 8), (36.909, 12.08), (41, 18)))
        self.add_bezier('sym-e13', (41, 18), ((41.382, 18.554), (44, 23.495), (44, 24)))
        self.add_bezier('sym-e14', (44, 24), ((43.995, 24.012), (44, 23.988), (44, 24)))
        self.add_contour('sym-c0', 'sym-e0', closed=True)
        self.add_contour('sym-c1', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', closed=True)
