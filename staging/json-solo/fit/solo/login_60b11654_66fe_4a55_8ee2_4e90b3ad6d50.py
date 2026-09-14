"""Login (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '60b11654-66fe-4a55-8ee2-4e90b3ad6d50'
SOURCE_PATH = 'icons-json/interface-essential/login_60b11654-66fe-4a55-8ee2-4e90b3ad6d50.json'
AUTHOR = 'json_to_solo'

class LoginInterfaceEssential(Solo48):
    icon_id = 'login-interface-essential'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('login', 'interface-essential')

    def build(self):
        self.add_line('e0', (29, 8), (44, 24))
        self.add_line('e1', (44, 24), (4, 24))
        self.add_line('e2', (44, 24), (29, 40))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
