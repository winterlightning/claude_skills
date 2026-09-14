"""Electronics tunnel diode (electronics), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '02aa6b76-7a76-5e61-97f5-c6663e07367b'
SOURCE_PATH = 'icons-json/electronics/electronics tunnel diode_02aa6b76-7a76-5e61-97f5-c6663e07367b.json'
AUTHOR = 'json_to_solo'

class ElectronicsTunnelDiode(Solo48):
    icon_id = 'electronics-tunnel-diode'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'electronics'
    aliases = ()
    keywords = ('electronics', 'tunnel', 'diode')

    def build(self):
        self.add_line('sym-e0', (30, 24), (44, 24))
        self.add_line('sym-e1', (35, 8), (35, 40))
        self.add_line('sym-e2', (4, 24), (14, 24))
        self.add_line('sym-e3', (14, 24), (14, 40))
        self.add_line('sym-e4', (14, 40), (30, 24))
        self.add_line('sym-e5', (30, 24), (14, 8))
        self.add_line('sym-e6', (14, 8), (14, 24))
        self.add_contour('sym-c0', 'sym-e0')
        self.add_contour('sym-c1', 'sym-e1')
        self.add_contour('sym-c2', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
