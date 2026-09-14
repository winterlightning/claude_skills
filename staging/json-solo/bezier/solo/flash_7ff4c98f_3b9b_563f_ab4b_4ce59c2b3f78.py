"""Flash (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7ff4c98f-3b9b-563f-ab4b-4ce59c2b3f78'
SOURCE_PATH = 'icons-json/interface-essential/flash_7ff4c98f-3b9b-563f-ab4b-4ce59c2b3f78.json'
AUTHOR = 'json_to_solo'

class Flash(Solo48):
    icon_id = 'flash'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('flash', 'interface-essential')

    def build(self):
        self.add_line('e0', (30, 4), (24, 20))
        self.add_line('e1', (24, 20), (40, 20))
        self.add_line('e2', (40, 20), (17, 44))
        self.add_line('e3', (17, 44), (23, 27))
        self.add_line('e4', (23, 27), (8, 27))
        self.add_line('e5', (8, 27), (30, 4))
        self.add_contour('c0', 'e0', 'e1', 'e2')
        self.add_contour('c1', 'e3', 'e4', 'e5')
        self.relate('connect', 'c0', 'c1')
