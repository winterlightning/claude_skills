"""N (text u) (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
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
        self.add_arc('e4-1', (8, 5), (9, 4), radius_x=1)
        self.add_line('e4-2', (9, 4), (10, 4))
        self.add_arc('e5', (38, 32), (40, 32), radius_x=1, sweep=False)
        self.add_contour('c0', 'e0', 'e4-1', 'e4-2', 'e1', 'e5', 'e2')
        self.add_contour('c1', 'e3')
