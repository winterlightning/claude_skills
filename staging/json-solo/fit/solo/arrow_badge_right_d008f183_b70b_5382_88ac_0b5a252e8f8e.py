"""Arrow badge right (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd008f183-b70b-5382-88ac-0b5a252e8f8e'
SOURCE_PATH = 'icons-json/arrows/arrow badge right_d008f183-b70b-5382-88ac-0b5a252e8f8e.json'
AUTHOR = 'json_to_solo'

class ArrowBadgeRightD008f183(Solo48):
    icon_id = 'arrow-badge-right-d008f183'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'badge', 'right', 'arrows')

    def build(self):
        self.add_line('e0', (31, 40), (7, 40))
        self.add_line('e1', (32, 9), (44, 24))
        self.add_line('e2', (44, 24), (31, 40))
        self.add_line('e3-1', (7, 40), (6, 40))
        self.add_line('e3-2', (6, 40), (4, 37))
        self.add_line('e3-3', (4, 37), (4, 15))
        self.add_line('e3-4', (4, 15), (4, 10))
        self.add_line('e3-5', (4, 10), (7, 8))
        self.add_line('e3-6', (7, 8), (29, 8))
        self.add_line('e3-7', (29, 8), (32, 9))
        self.add_contour('c0', 'e2', 'e0', 'e3-1', 'e3-2', 'e3-3', 'e3-4', 'e3-5', 'e3-6', 'e3-7', 'e1', closed=True)
