"""Flash (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a1503607-5c61-5edd-bfbc-5466fc717ea6'
SOURCE_PATH = 'pictographic-primitives/interface-essential/flash_a1503607-5c61-5edd-bfbc-5466fc717ea6.svg'
AUTHOR = 'gpt-6'

class FlashA1503607(Solo48):
    icon_id = 'flash-a1503607'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('flash', 'interface-essential')

    def build(self):
        self.add_line('e0', (12, 44), (40, 19))
        self.add_line('e1', (40, 19), (25, 19))
        self.add_line('e2', (25, 19), (37, 4))
        self.add_line('e3', (37, 4), (18, 4))
        self.add_line('e4', (18, 4), (8, 24))
        self.add_line('e5', (8, 24), (20, 24))
        self.add_line('e6', (20, 24), (12, 44))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', closed=True)
