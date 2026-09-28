"""Flash (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '661caf54-eac9-4e44-897e-de17aaf87c39'
SOURCE_PATH = 'pictographic-primitives/interface-essential/flash_661caf54-eac9-4e44-897e-de17aaf87c39.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class FlashInterfaceEssential(Solo48):
    icon_id = 'flash-interface-essential'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'state', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('flash', 'interface-essential')

    def build(self):
        self.add_line('e0', (30, 4), (8, 27))
        self.add_line('e1', (8, 27), (20, 27))
        self.add_line('e2', (20, 27), (18, 44))
        self.add_line('e3', (18, 44), (40, 21))
        self.add_line('e4', (40, 21), (28, 21))
        self.add_line('e5', (28, 21), (30, 4))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', 'e4', 'e5', closed=True)
