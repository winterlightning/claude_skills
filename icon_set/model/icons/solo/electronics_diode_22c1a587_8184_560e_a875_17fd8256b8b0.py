"""Electronics diode (electronics), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '22c1a587-8184-560e-a875-17fd8256b8b0'
SOURCE_PATH = 'icons-json/electronics/electronics diode_22c1a587-8184-560e-a875-17fd8256b8b0.json'
AUTHOR = 'json_to_solo'

class ElectronicsDiode(Solo48):
    icon_id = 'electronics-diode'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'electronics'
    aliases = ()
    keywords = ('electronics', 'diode')

    def build(self):
        self.add_line('e0', (35, 8), (35, 40))
        self.add_line('e1', (4, 24), (14, 24))
        self.add_line('e2', (44, 24), (35, 24))
        self.add_line('e3', (34, 24), (14, 8))
        self.add_line('e4', (14, 8), (14, 40))
        self.add_line('e5', (14, 40), (34, 24))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3', 'e4', 'e5', closed=True)
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c0')
