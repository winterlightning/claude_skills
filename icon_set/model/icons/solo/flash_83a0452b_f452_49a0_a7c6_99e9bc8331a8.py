"""Flash (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '83a0452b-f452-49a0-a7c6-99e9bc8331a8'
SOURCE_PATH = 'icons-json/interface-essential/flash_83a0452b-f452-49a0-a7c6-99e9bc8331a8.json'
AUTHOR = 'json_to_solo'

class Flash83a0452b(Solo48):
    icon_id = 'flash-83a0452b'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('flash', 'interface-essential')

    def build(self):
        self.add_line('e0', (32, 4), (10, 23))
        self.add_line('e1', (10, 23), (40, 23))
        self.add_line('e2', (40, 23), (8, 44))
        self.add_contour('c0', 'e0', 'e1', 'e2')
