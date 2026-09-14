"""Add (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bd3e56c0-5ba1-4ac1-b0be-84a6491da7ab'
SOURCE_PATH = 'icons-json/interface-essential/add_bd3e56c0-5ba1-4ac1-b0be-84a6491da7ab.json'
AUTHOR = 'json_to_solo'

class Add(Solo48):
    icon_id = 'add'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('add', 'interface-essential')

    def build(self):
        self.add_line('e0', (24, 6), (24, 42))
        self.add_line('e1', (6, 24), (42, 24))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
