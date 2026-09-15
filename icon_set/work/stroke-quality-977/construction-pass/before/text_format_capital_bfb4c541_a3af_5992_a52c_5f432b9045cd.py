"""Text format capital (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bfb4c541-a3af-5992-a52c-5f432b9045cd'
SOURCE_PATH = 'pictographic-primitives/interface-essential/text format capital_bfb4c541-a3af-5992-a52c-5f432b9045cd.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class TextFormatCapital(Solo48):
    icon_id = 'text-format-capital'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('text', 'format', 'capital', 'interface-essential')

    def build(self):
        self.add_line('sym-e0', (35, 30), (13, 30))
        self.add_arc('sym-e3', (24, 4), (23, 4), radius_x=69)
        self.add_arc('sym-e4', (23, 4), (21, 8), radius_x=4, sweep=False)
        self.add_line('sym-e5', (21, 8), (8, 44))
        self.add_arc('sym-e8', (24, 4), (25, 4), radius_x=76, sweep=False)
        self.add_arc('sym-e9', (25, 4), (27, 8), radius_x=3)
        self.add_line('sym-e10', (27, 8), (40, 44))
        self.add_contour('sym-c0', 'sym-e0')
        self.add_contour('sym-c1', 'sym-e3', 'sym-e4', 'sym-e5')
        self.add_contour('sym-c2', 'sym-e8', 'sym-e9', 'sym-e10')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
