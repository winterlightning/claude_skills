"""Equal (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '07c0b4b6-b72a-4a5f-af8f-985bd7230cc2'
SOURCE_PATH = 'pictographic-primitives/interface-essential/equal_07c0b4b6-b72a-4a5f-af8f-985bd7230cc2.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class Equal(Solo48):
    icon_id = 'equal'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('equal', 'interface-essential')

    def build(self):
        self.add_line('e0', (4, 8), (44, 8))
        self.add_line('e1', (4, 40), (44, 40))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
