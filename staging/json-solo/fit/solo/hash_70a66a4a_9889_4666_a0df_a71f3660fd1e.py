"""Hash (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '70a66a4a-9889-4666-a0df-a71f3660fd1e'
SOURCE_PATH = 'icons-json/interface-essential/hash_70a66a4a-9889-4666-a0df-a71f3660fd1e.json'
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
        self.add_line('e0', (42, 17), (6, 17))
        self.add_line('e1', (31, 42), (31, 6))
        self.add_line('e2', (42, 30), (6, 30))
        self.add_line('e3', (18, 6), (18, 42))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
