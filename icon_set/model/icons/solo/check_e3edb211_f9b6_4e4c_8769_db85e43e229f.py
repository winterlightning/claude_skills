"""Check (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e3edb211-f9b6-4e4c-8769-db85e43e229f'
SOURCE_PATH = 'pictographic-primitives/interface-essential/check_e3edb211-f9b6-4e4c-8769-db85e43e229f.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class CheckInterfaceEssential(Solo48):
    icon_id = 'check-interface-essential'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'state', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('check', 'interface-essential')

    def build(self):
        self.add_line('e0', (44, 8), (19, 40))
        self.add_line('e1', (19, 40), (4, 24))
        self.add_contour('c0', 'e0', 'e1')
