"""Flash (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '482239ce-8075-436a-b065-ac0bc289a949'
SOURCE_PATH = 'icons-json/interface-essential/flash_482239ce-8075-436a-b065-ac0bc289a949.json'
AUTHOR = 'json_to_solo'

class Flash482239ce(Solo48):
    icon_id = 'flash-482239ce'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('flash', 'interface-essential')

    def build(self):
        self.add_line('e0', (14, 44), (20, 39))
        self.add_line('e1', (20, 39), (29, 31))
        self.add_line('e2', (29, 31), (40, 19))
        self.add_line('e3', (40, 19), (24, 19))
        self.add_line('e4', (24, 19), (34, 4))
        self.add_line('e5', (34, 4), (22, 4))
        self.add_line('e6', (22, 4), (8, 26))
        self.add_line('e7', (8, 26), (22, 26))
        self.add_line('e8', (22, 26), (14, 44))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8')
