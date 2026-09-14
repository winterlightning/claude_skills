"""Branch line (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4a90db8b-9f2a-5f07-9c86-67dfb7581fee'
SOURCE_PATH = 'icons-json/interface-essential/branch line_4a90db8b-9f2a-5f07-9c86-67dfb7581fee.json'
AUTHOR = 'json_to_solo'

class BranchLineInterfaceEssential(Solo48):
    icon_id = 'branch-line-interface-essential'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('branch', 'line', 'interface-essential')

    def build(self):
        self.add_line('e0', (44, 8), (27, 8))
        self.add_line('e1', (27, 8), (27, 40))
        self.add_line('e2', (27, 40), (44, 40))
        self.add_line('e3', (4, 24), (27, 24))
        self.add_contour('c0', 'e0', 'e1', 'e2')
        self.add_contour('c1', 'e3')
        self.relate('connect', 'c1', 'c0')
