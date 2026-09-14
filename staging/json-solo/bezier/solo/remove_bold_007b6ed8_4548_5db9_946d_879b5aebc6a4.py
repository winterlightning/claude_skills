"""Remove bold (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '007b6ed8-4548-5db9-946d-879b5aebc6a4'
SOURCE_PATH = 'icons-json/interface-essential/remove bold_007b6ed8-4548-5db9-946d-879b5aebc6a4.json'
AUTHOR = 'json_to_solo'

class RemoveBoldInterfaceEssential(Solo48):
    icon_id = 'remove-bold-interface-essential'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('remove', 'bold', 'interface-essential')

    def build(self):
        self.add_line('e0', (13, 6), (6, 13))
        self.add_line('e1', (6, 13), (17, 24))
        self.add_line('e2', (17, 24), (6, 35))
        self.add_line('e3', (6, 35), (13, 42))
        self.add_line('e4', (13, 42), (24, 31))
        self.add_line('e5', (24, 31), (35, 42))
        self.add_line('e6', (35, 42), (42, 35))
        self.add_line('e7', (42, 35), (31, 24))
        self.add_line('e8', (31, 24), (42, 13))
        self.add_line('e9', (42, 13), (35, 6))
        self.add_line('e10', (35, 6), (24, 17))
        self.add_line('e11', (24, 17), (13, 6))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9', 'e10', 'e11', closed=True)
