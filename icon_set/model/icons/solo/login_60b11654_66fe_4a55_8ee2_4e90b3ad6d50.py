"""Login (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '60b11654-66fe-4a55-8ee2-4e90b3ad6d50'
SOURCE_PATH = 'pictographic-primitives/interface-essential/login_60b11654-66fe-4a55-8ee2-4e90b3ad6d50.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class Login(Solo48):
    icon_id = 'login'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
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
