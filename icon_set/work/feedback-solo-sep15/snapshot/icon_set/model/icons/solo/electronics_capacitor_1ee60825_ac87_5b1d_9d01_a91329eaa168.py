"""Electronics capacitor (electronics), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '1ee60825-ac87-5b1d-9d01-a91329eaa168'
SOURCE_PATH = 'pictographic-primitives/electronics/electronics capacitor_1ee60825-ac87-5b1d-9d01-a91329eaa168.svg'
AUTHOR = 'gpt-6'

class ElectronicsCapacitor(Solo48):
    icon_id = 'electronics-capacitor'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'electronics'
    aliases = ()
    keywords = ('electronics', 'capacitor')

    def build(self):
        self.add_line('sym-e0', (40, 27), (8, 27))
        self.add_line('sym-e4', (24, 27), (24, 44))
        self.add_line('sym-e5', (35, 4), (35, 27))
        self.add_line('sym-e6', (13, 4), (13, 27))
        self.add_contour('sym-c0', 'sym-e0', closed=False)
        self.add_contour('sym-c1', 'sym-e4', closed=False)
        self.add_contour('sym-c2', 'sym-e5', closed=False)
        self.add_contour('sym-c3', 'sym-e6', closed=False)
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
