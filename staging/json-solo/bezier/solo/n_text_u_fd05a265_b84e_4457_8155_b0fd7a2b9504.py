"""N (text u) (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fd05a265-b84e-4457-8155-b0fd7a2b9504'
SOURCE_PATH = 'icons-json/symbol/n (text u)_fd05a265-b84e-4457-8155-b0fd7a2b9504.json'
AUTHOR = 'json_to_solo'

class NTextUSymbol(Solo48):
    icon_id = 'n-text-u-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('n', 'text', 'u', 'symbol')

    def build(self):
        self.add_line('e0', (8, 33), (8, 5))
        self.add_line('e1', (10, 4), (38, 32))
        self.add_line('e2', (40, 32), (40, 4))
        self.add_line('e3', (8, 44), (40, 44))
        self.add_bezier('e4', (8, 5), ((8, 4.845), (8, 4.6), (8, 4.436)), ((8, 4.255), (8.512, 4), (8.832, 4)), ((9.088, 4), (9.744, 4), (10, 4)))
        self.add_bezier('e5', (38, 32), ((38.08, 32.018), (38.656, 32.455), (38.864, 32.509)), ((39.824, 32.727), (39.648, 32.064), (40, 32)))
        self.add_contour('c0', 'e0', 'e4', 'e1', 'e5', 'e2')
        self.add_contour('c1', 'e3')
