"""House (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '51e8bb01-0f35-5ff5-85f3-672839327e85'
SOURCE_PATH = 'icons-json/interface-essential/house_51e8bb01-0f35-5ff5-85f3-672839327e85.json'
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
        self.add_line('sym-e0', (29, 42), (29, 30))
        self.add_line('sym-e1', (29, 30), (19, 30))
        self.add_line('sym-e2', (19, 30), (19, 42))
        self.add_line('sym-e3', (19, 42), (6, 42))
        self.add_line('sym-e4', (6, 42), (6, 23))
        self.add_line('sym-e5', (6, 23), (24, 6))
        self.add_line('sym-e6', (24, 6), (42, 23))
        self.add_line('sym-e7', (42, 23), (42, 42))
        self.add_line('sym-e8', (42, 42), (29, 42))
        self.add_line('sym-e9', (29, 42), (24, 42))
        self.add_line('sym-e10', (24, 42), (19, 42))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10')
