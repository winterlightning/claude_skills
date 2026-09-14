"""House (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b3b4c5ab-639d-427c-b354-1b822229a999'
SOURCE_PATH = 'icons-json/interface-essential/house_b3b4c5ab-639d-427c-b354-1b822229a999.json'
AUTHOR = 'json_to_solo'

class House(Solo48):
    icon_id = 'house'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('house', 'interface-essential')

    def build(self):
        self.add_line('sym-e0', (42, 24), (38, 20))
        self.add_line('sym-e1', (38, 20), (24, 6))
        self.add_line('sym-e2', (24, 6), (10, 20))
        self.add_line('sym-e3', (10, 20), (6, 24))
        self.add_line('sym-e4', (38, 20), (38, 42))
        self.add_line('sym-e5', (38, 42), (24, 42))
        self.add_line('sym-e6', (24, 42), (10, 42))
        self.add_line('sym-e7', (10, 42), (10, 20))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3')
        self.add_contour('sym-c1', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
