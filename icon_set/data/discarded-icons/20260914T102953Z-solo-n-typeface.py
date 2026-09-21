"""N (typeface), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5cb4a735-46c6-4f73-a139-ef91464aaa08'
SOURCE_PATH = 'icons-json/typeface/n_5cb4a735-46c6-4f73-a139-ef91464aaa08.json'
AUTHOR = 'json_to_solo'

class NTypeface(Solo48):
    icon_id = 'n-typeface'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'typeface'
    aliases = ()
    keywords = ('n', 'typeface')

    def build(self):
        self.add_line('e0', (8, 5), (8, 44))
        self.add_line('e1', (40, 16), (40, 44))
        self.add_arc('e2-1', (8, 14), (15, 6), radius_x=15)
        self.add_line('e2-2', (15, 6), (24, 4))
        self.add_line('e2-3', (24, 4), (31, 5))
        self.add_arc('e2-4', (31, 5), (35, 7), radius_x=16)
        self.add_arc('e2-5', (35, 7), (40, 16), radius_x=11)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e2-1', 'e2-2', 'e2-3', 'e2-4', 'e2-5', 'e1')
        self.relate('connect', 'c1', 'c0')
