"""N (typeface), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c93adf0c-a051-45cd-bf10-f241e47b2183'
SOURCE_PATH = 'icons-json/typeface/N_c93adf0c-a051-45cd-bf10-f241e47b2183.json'
AUTHOR = 'json_to_solo'

class NC93adf0c(Solo48):
    icon_id = 'n-c93adf0c'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'typeface'
    aliases = ()
    keywords = ('n', 'typeface')

    def build(self):
        self.add_line('e0', (8, 44), (8, 5))
        self.add_line('e1', (10, 4), (38, 44))
        self.add_line('e2', (40, 43), (40, 4))
        self.add_arc('e3-1', (8, 5), (8, 4), radius_x=1, sweep=False)
        self.add_line('e3-2', (8, 4), (10, 4))
        self.add_line('e4-1', (38, 44), (40, 44))
        self.add_arc('e4-2', (40, 44), (40, 43), radius_x=1)
        self.add_contour('c0', 'e0', 'e3-1', 'e3-2', 'e1', 'e4-1', 'e4-2', 'e2')
