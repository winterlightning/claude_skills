"""Arrow up right (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fe80ad75-1c8b-4c69-bcf8-7de600687de0'
SOURCE_PATH = 'icons-json/symbol/arrow up right_fe80ad75-1c8b-4c69-bcf8-7de600687de0.json'
AUTHOR = 'json_to_solo'

class ArrowUpRightSymbol(Solo48):
    icon_id = 'arrow-up-right-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('arrow', 'up', 'right', 'symbol')

    def build(self):
        self.add_line('e0', (6, 42), (42, 6))
        self.add_line('e1', (42, 6), (42, 23))
        self.add_line('e2', (42, 6), (25, 6))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
