"""Flash (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7ff4c98f-3b9b-563f-ab4b-4ce59c2b3f78'
SOURCE_PATH = 'pictographic-primitives/interface-essential/flash_7ff4c98f-3b9b-563f-ab4b-4ce59c2b3f78.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class Flash7ff4c98f(Solo48):
    icon_id = 'flash-7ff4c98f'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('flash', 'interface-essential')

    def build(self):
        self.add_line('e0', (30, 4), (24, 20))
        self.add_line('e1', (24, 20), (40, 20))
        self.add_line('e2', (40, 20), (17, 44))
        self.add_line('e3', (17, 44), (23, 27))
        self.add_line('e4', (23, 27), (8, 27))
        self.add_line('e5', (8, 27), (30, 4))
        self.add_contour('c0', 'e0', 'e1', 'e2')
        self.add_contour('c1', 'e3', 'e4', 'e5')
        self.relate('connect', 'c0', 'c1')
