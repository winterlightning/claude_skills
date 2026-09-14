"""R (typeface), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd0effb3a-dd71-5368-9650-1678a3b7798b'
SOURCE_PATH = 'icons-json/typeface/R_d0effb3a-dd71-5368-9650-1678a3b7798b.json'
AUTHOR = 'json_to_solo'

class RD0effb3a(Solo48):
    icon_id = 'r-d0effb3a'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'typeface'
    aliases = ()
    keywords = ('r', 'typeface')

    def build(self):
        self.add_line('e0', (8, 25), (26, 25))
        self.add_line('e1', (26, 4), (9, 4))
        self.add_line('e2', (8, 5), (8, 44))
        self.add_line('e3', (40, 44), (26, 25))
        self.add_arc('e4-1', (26, 25), (40, 14), radius_x=12, sweep=False)
        self.add_arc('e4-2', (40, 14), (35, 6), radius_x=10, sweep=False)
        self.add_line('e4-3', (35, 6), (27, 4))
        self.add_line('e4-4', (27, 4), (26, 4))
        self.add_arc('e5', (9, 4), (8, 5), radius_x=1, sweep=False)
        self.add_contour('c0', 'e0', 'e4-1', 'e4-2', 'e4-3', 'e4-4', 'e1', 'e5', 'e2')
        self.add_contour('c1', 'e3')
