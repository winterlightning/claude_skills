"""Hash (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fb5ba9f3-ed34-4ad9-a6c7-13d0b23d03d1'
SOURCE_PATH = 'icons-json/interface-essential/hash_fb5ba9f3-ed34-4ad9-a6c7-13d0b23d03d1.json'
AUTHOR = 'json_to_solo'

class Hash(Solo48):
    icon_id = 'hash'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
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
