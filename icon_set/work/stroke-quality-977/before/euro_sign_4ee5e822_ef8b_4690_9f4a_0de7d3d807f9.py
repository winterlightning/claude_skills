"""Euro sign (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4ee5e822-ef8b-4690-9f4a-0de7d3d807f9'
SOURCE_PATH = 'pictographic-primitives/symbol/euro sign_4ee5e822-ef8b-4690-9f4a-0de7d3d807f9.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class EuroSign(Solo48):
    icon_id = 'euro-sign'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('euro', 'sign', 'symbol')

    def build(self):
        self.add_line('e0', (14, 32), (12, 25))
        self.add_line('e1', (8, 25), (18, 25))
        self.add_arc('e2-1', (40, 8), (30, 4), radius_x=16, sweep=False)
        self.add_arc('e2-2', (30, 4), (13, 25), radius_x=18, sweep=False)
        self.add_arc('e3-1', (40, 40), (30, 44), radius_x=15)
        self.add_arc('e3-2', (30, 44), (14, 32), radius_x=17)
        self.add_contour('c0', 'e2-1', 'e2-2')
        self.add_contour('c1', 'e3-1', 'e3-2', 'e0')
        self.add_contour('c2', 'e1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
