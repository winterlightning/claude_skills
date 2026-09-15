"""House (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '50aedd0f-a5ea-4128-8144-82d4f6ce9abc'
SOURCE_PATH = 'pictographic-primitives/interface-essential/house_50aedd0f-a5ea-4128-8144-82d4f6ce9abc.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class HouseInterfaceEssential(Solo48):
    icon_id = 'house-interface-essential'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('house', 'interface-essential')

    def build(self):
        self.add_line('e0', (24, 44), (24, 29))
        self.add_line('e1', (40, 44), (8, 44))
        self.add_line('e2', (8, 44), (8, 19))
        self.add_line('e3', (8, 19), (24, 4))
        self.add_line('e4', (24, 4), (40, 19))
        self.add_line('e5', (40, 19), (40, 44))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2', 'e3', 'e4', 'e5', closed=True)
        self.relate('connect', 'c0', 'c1')
