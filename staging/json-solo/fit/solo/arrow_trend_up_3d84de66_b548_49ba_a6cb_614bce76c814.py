"""Arrow trend up (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3d84de66-b548-49ba-a6cb-614bce76c814'
SOURCE_PATH = 'icons-json/symbol/arrow trend up_3d84de66-b548-49ba-a6cb-614bce76c814.json'
AUTHOR = 'json_to_solo'

class ArrowTrendUpSymbol(Solo48):
    icon_id = 'arrow-trend-up-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('arrow', 'trend', 'up', 'symbol')

    def build(self):
        self.add_line('e0', (34, 8), (44, 8))
        self.add_line('e1', (4, 40), (19, 19))
        self.add_line('e2', (19, 19), (28, 33))
        self.add_line('e3', (28, 33), (44, 8))
        self.add_line('e4', (44, 24), (44, 8))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2', 'e3')
        self.add_contour('c2', 'e4')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
