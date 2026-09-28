"""Square root (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1779227e-43ac-5789-87f5-dd737bf06f33'
SOURCE_PATH = 'pictographic-primitives/interface-essential/square root_1779227e-43ac-5789-87f5-dd737bf06f33.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class SquareRoot(Solo48):
    icon_id = 'square-root'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('square', 'root', 'interface-essential')

    def build(self):
        self.add_line('e0', (44, 8), (20, 8))
        self.add_line('e1', (20, 8), (10, 40))
        self.add_line('e2', (10, 40), (4, 26))
        self.add_contour('c0', 'e0', 'e1', 'e2')
