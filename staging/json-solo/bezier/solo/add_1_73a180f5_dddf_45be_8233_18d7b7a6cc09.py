"""Add 1 (state), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '73a180f5-dddf-45be-8233-18d7b7a6cc09'
SOURCE_PATH = 'icons-json/state/add 1_73a180f5-dddf-45be-8233-18d7b7a6cc09.json'
AUTHOR = 'json_to_solo'

class Add1State(Solo48):
    icon_id = 'add-1-state'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('add', 'state')

    def build(self):
        self.add_line('e0', (24, 6), (24, 42))
        self.add_line('e1', (6, 24), (42, 24))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
