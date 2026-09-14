"""Arrow thin bottom (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b6a9ec80-0591-424e-824e-f6719ae172f4'
SOURCE_PATH = 'icons-json/symbol/arrow thin bottom_b6a9ec80-0591-424e-824e-f6719ae172f4.json'
AUTHOR = 'json_to_solo'

class ArrowThinBottomB6a9ec80(Solo48):
    icon_id = 'arrow-thin-bottom-b6a9ec80'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('arrow', 'thin', 'bottom', 'symbol')

    def build(self):
        self.add_line('e0', (8, 32), (24, 44))
        self.add_line('e1', (40, 32), (24, 44))
        self.add_line('e2', (24, 4), (24, 44))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
