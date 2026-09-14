"""Add (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1f3bf2aa-954f-457a-bf9a-49c4b3cb9cd3'
SOURCE_PATH = 'icons-json/interface-essential/add_1f3bf2aa-954f-457a-bf9a-49c4b3cb9cd3.json'
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
