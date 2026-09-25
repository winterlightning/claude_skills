"""Flash (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '83a0452b-f452-49a0-a7c6-99e9bc8331a8'
SOURCE_PATH = 'pictographic-primitives/interface-essential/flash_83a0452b-f452-49a0-a7c6-99e9bc8331a8.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class Flash83a0452b(Solo48):
    icon_id = 'flash-83a0452b'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('flash', 'interface-essential')

    def build(self):
        self.add_line('e0', (32, 4), (10, 23))
        self.add_line('e1', (10, 23), (40, 23))
        self.add_line('e2', (40, 23), (8, 44))
        self.add_contour('c0', 'e0', 'e1', 'e2')
