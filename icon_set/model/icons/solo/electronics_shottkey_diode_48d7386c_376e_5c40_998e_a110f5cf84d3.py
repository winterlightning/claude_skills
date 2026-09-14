"""Electronics shottkey diode (electronics), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '48d7386c-376e-5c40-998e-a110f5cf84d3'
SOURCE_PATH = 'icons-json/electronics/electronics shottkey diode_48d7386c-376e-5c40-998e-a110f5cf84d3.json'
AUTHOR = 'json_to_solo'

class ElectronicsShottkeyDiode(Solo48):
    icon_id = 'electronics-shottkey-diode'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'electronics'
    aliases = ()
    keywords = ('electronics', 'shottkey', 'diode')

    def build(self):
        self.add_line('e0', (32, 8), (32, 40))
        self.add_line('e1', (4, 24), (17, 24))
        self.add_line('e2', (32, 24), (44, 24))
        self.add_line('e3', (31, 24), (17, 10))
        self.add_line('e4', (17, 10), (17, 38))
        self.add_line('e5', (17, 38), (31, 24))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3', 'e4', 'e5', closed=True)
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c0')
