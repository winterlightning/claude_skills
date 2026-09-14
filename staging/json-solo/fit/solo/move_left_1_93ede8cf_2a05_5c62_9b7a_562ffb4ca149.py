"""Move left 1 (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '93ede8cf-2a05-5c62-9b7a-562ffb4ca149'
SOURCE_PATH = 'icons-json/interface-essential/move left 1_93ede8cf-2a05-5c62-9b7a-562ffb4ca149.json'
AUTHOR = 'json_to_solo'

class MoveLeft1InterfaceEssential(Solo48):
    icon_id = 'move-left-1-interface-essential'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('move', 'left', 'interface-essential')

    def build(self):
        self.add_line('e0', (4, 40), (4, 8))
        self.add_line('e1', (26, 14), (15, 24))
        self.add_line('e2', (15, 24), (44, 24))
        self.add_line('e3', (15, 24), (26, 34))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2')
        self.add_contour('c2', 'e3')
