"""Flash (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '821a0fbf-70fd-4f18-bc5d-1a46c93ca7e9'
SOURCE_PATH = 'pictographic-primitives/interface-essential/flash_821a0fbf-70fd-4f18-bc5d-1a46c93ca7e9.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class Flash821a0fbf(Solo48):
    icon_id = 'flash-821a0fbf'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('flash', 'interface-essential')

    def build(self):
        self.add_line('e0', (33, 4), (8, 27))
        self.add_line('e1', (8, 27), (40, 21))
        self.add_line('e2', (40, 21), (14, 44))
        self.add_contour('c0', 'e0', 'e1', 'e2')
