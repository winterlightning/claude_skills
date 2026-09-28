"""Hash (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fb5ba9f3-ed34-4ad9-a6c7-13d0b23d03d1'
SOURCE_PATH = 'pictographic-primitives/interface-essential/hash_fb5ba9f3-ed34-4ad9-a6c7-13d0b23d03d1.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class HashFb5ba9f3(Solo48):
    icon_id = 'hash-fb5ba9f3'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('hash', 'interface-essential')

    def build(self):
        self.add_line('e0', (22, 6), (13, 42))
        self.add_line('e1', (8, 17), (42, 17))
        self.add_line('e2', (6, 31), (40, 31))
        self.add_line('e3', (26, 42), (35, 6))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
