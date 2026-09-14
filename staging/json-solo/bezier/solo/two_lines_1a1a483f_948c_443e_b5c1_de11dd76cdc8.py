"""Two lines (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1a1a483f-948c-443e-b5c1-de11dd76cdc8'
SOURCE_PATH = 'icons-json/symbol/two lines_1a1a483f-948c-443e-b5c1-de11dd76cdc8.json'
AUTHOR = 'json_to_solo'

class TwoLinesSymbol(Solo48):
    icon_id = 'two-lines-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('two', 'lines', 'symbol')

    def build(self):
        self.add_line('e0', (40, 4), (40, 43))
        self.add_line('e1', (39, 44), (8, 44))
        self.add_bezier('e2', (40, 43), ((39.73, 43.391), (40, 43.791), (39.4, 43.973)), ((39.27, 43.982), (39.13, 43.991), (39, 44)))
        self.add_contour('c0', 'e0', 'e2', 'e1')
