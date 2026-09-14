"""Crown (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b4b92d69-8105-44cf-b2da-b627898b4365'
SOURCE_PATH = 'icons-json/symbol/crown_b4b92d69-8105-44cf-b2da-b627898b4365.json'
AUTHOR = 'json_to_solo'

class Crown(Solo48):
    icon_id = 'crown'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('crown', 'symbol')

    def build(self):
        self.add_line('e0', (33, 23), (24, 8))
        self.add_line('e1', (24, 8), (15, 23))
        self.add_line('e2', (15, 23), (4, 13))
        self.add_line('e3', (4, 13), (6, 40))
        self.add_line('e4', (6, 40), (42, 40))
        self.add_line('e5', (42, 40), (44, 13))
        self.add_line('e6', (44, 13), (33, 23))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', closed=True)
