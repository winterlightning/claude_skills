"""Arrow down right (other), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1888dd76-ccb6-47f9-8b09-93820a0e4fb5'
SOURCE_PATH = 'icons-json/other/arrow down right_1888dd76-ccb6-47f9-8b09-93820a0e4fb5.json'
AUTHOR = 'json_to_solo'

class ArrowDownRight(Solo48):
    icon_id = 'arrow-down-right'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'other'
    aliases = ()
    keywords = ('arrow', 'down', 'right', 'other')

    def build(self):
        self.add_line('e0', (6, 6), (42, 42))
        self.add_line('e1', (6, 42), (42, 42))
        self.add_line('e2', (42, 6), (42, 42))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
