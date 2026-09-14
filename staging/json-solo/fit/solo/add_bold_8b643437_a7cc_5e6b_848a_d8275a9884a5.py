"""Add bold (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8b643437-a7cc-5e6b-848a-d8275a9884a5'
SOURCE_PATH = 'icons-json/interface-essential/add bold_8b643437-a7cc-5e6b-848a-d8275a9884a5.json'
AUTHOR = 'json_to_solo'

class AddBoldInterfaceEssential(Solo48):
    icon_id = 'add-bold-interface-essential'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('add', 'bold', 'interface-essential')

    def build(self):
        self.add_line('e0', (29, 6), (19, 6))
        self.add_line('e1', (19, 6), (19, 19))
        self.add_line('e2', (19, 19), (6, 19))
        self.add_line('e3', (6, 19), (6, 29))
        self.add_line('e4', (6, 29), (19, 29))
        self.add_line('e5', (19, 29), (19, 42))
        self.add_line('e6', (19, 42), (29, 42))
        self.add_line('e7', (29, 42), (29, 29))
        self.add_line('e8', (29, 29), (42, 29))
        self.add_line('e9', (42, 29), (42, 19))
        self.add_line('e10', (42, 19), (29, 19))
        self.add_line('e11', (29, 19), (29, 6))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9', 'e10', 'e11', closed=True)
