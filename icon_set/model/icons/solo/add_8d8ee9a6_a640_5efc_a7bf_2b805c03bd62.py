"""Add (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8d8ee9a6-a640-5efc-a7bf-2b805c03bd62'
SOURCE_PATH = 'icons-json/interface-essential/add_8d8ee9a6-a640-5efc-a7bf-2b805c03bd62.json'
AUTHOR = 'json_to_solo'

class AddInterfaceEssential(Solo48):
    icon_id = 'add-interface-essential'
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
