"""Diamond (money), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5d9db826-3f1d-489d-b7b6-bf5b50bbe949'
SOURCE_PATH = 'icons-json/money/diamond_5d9db826-3f1d-489d-b7b6-bf5b50bbe949.json'
AUTHOR = 'json_to_solo'

class Diamond(Solo48):
    icon_id = 'diamond'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    aliases = ()
    keywords = ('diamond', 'money')

    def build(self):
        self.add_line('e0', (24, 40), (17, 32))
        self.add_line('e1', (17, 32), (4, 18))
        self.add_line('e2', (4, 18), (44, 18))
        self.add_line('e3', (44, 18), (29, 34))
        self.add_line('e4', (29, 34), (24, 40))
        self.add_line('e5', (44, 18), (37, 8))
        self.add_line('e6', (37, 8), (11, 8))
        self.add_line('e7', (11, 8), (4, 18))
        self.add_line('e8', (24, 8), (24, 40))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', 'e4')
        self.add_contour('c1', 'e5', 'e6', 'e7')
        self.add_contour('c2', 'e8')
        self.relate('connect', 'c2', 'c1')
