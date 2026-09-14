"""Arrow down left (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bc7210f9-98c5-477d-a124-bfde36e44a35'
SOURCE_PATH = 'icons-json/symbol/arrow down left_bc7210f9-98c5-477d-a124-bfde36e44a35.json'
AUTHOR = 'json_to_solo'

class ArrowDownLeft(Solo48):
    icon_id = 'arrow-down-left'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('arrow', 'down', 'left', 'symbol')

    def build(self):
        self.add_line('e0', (42, 6), (6, 42))
        self.add_line('e1', (6, 25), (6, 42))
        self.add_line('e2', (23, 42), (6, 42))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
