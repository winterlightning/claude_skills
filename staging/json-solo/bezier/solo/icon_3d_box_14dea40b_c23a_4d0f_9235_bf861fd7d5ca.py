"""3d box (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '14dea40b-c23a-4d0f-9235-bf861fd7d5ca'
SOURCE_PATH = 'icons-json/symbol/3d box_14dea40b-c23a-4d0f-9235-bf861fd7d5ca.json'
AUTHOR = 'json_to_solo'

class Icon3dBoxSymbol(Solo48):
    icon_id = 'icon-3d-box-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('3d', 'box', 'symbol')

    def build(self):
        self.add_line('e0', (24, 44), (40, 34))
        self.add_line('e1', (40, 34), (40, 14))
        self.add_line('e2', (40, 14), (24, 24))
        self.add_line('e3', (40, 14), (24, 4))
        self.add_line('e4', (24, 4), (8, 14))
        self.add_line('e5', (24, 24), (24, 44))
        self.add_line('e6', (24, 44), (8, 34))
        self.add_line('e7', (8, 34), (8, 14))
        self.add_line('e8', (24, 24), (8, 14))
        self.add_contour('c0', 'e0', 'e1', 'e2')
        self.add_contour('c1', 'e3', 'e4')
        self.add_contour('c2', 'e5', 'e6', 'e7')
        self.add_contour('c3', 'e8')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
