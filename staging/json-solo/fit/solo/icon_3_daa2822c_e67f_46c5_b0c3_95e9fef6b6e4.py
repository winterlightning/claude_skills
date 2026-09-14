"""3 (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'daa2822c-e67f-46c5-b0c3-95e9fef6b6e4'
SOURCE_PATH = 'icons-json/symbol/3_daa2822c-e67f-46c5-b0c3-95e9fef6b6e4.json'
AUTHOR = 'json_to_solo'

class Icon3Symbol(Solo48):
    icon_id = 'icon-3-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('symbol',)

    def build(self):
        self.add_arc('e0-1', (9, 10), (17, 5), radius_x=13)
        self.add_line('e0-2', (17, 5), (24, 4))
        self.add_line('e0-3', (24, 4), (31, 5))
        self.add_arc('e0-4', (31, 5), (35, 7), radius_x=13)
        self.add_arc('e0-5', (35, 7), (39, 14), radius_x=9)
        self.add_arc('e0-6', (39, 14), (38, 18), radius_x=7)
        self.add_arc('e0-7', (38, 18), (33, 22), radius_x=11)
        self.add_line('e0-8', (33, 22), (23, 24))
        self.add_arc('e0-9', (23, 24), (25, 24), radius_x=32)
        self.add_arc('e0-10', (25, 24), (36, 27), radius_x=27)
        self.add_arc('e0-11', (36, 27), (40, 33), radius_x=7)
        self.add_arc('e0-12', (40, 33), (31, 43), radius_x=11)
        self.add_line('e0-13', (31, 43), (24, 44))
        self.add_arc('e0-14', (24, 44), (14, 42), radius_x=26)
        self.add_arc('e0-15', (14, 42), (8, 37), radius_x=8)
        self.add_contour('c0', 'e0-1', 'e0-2', 'e0-3', 'e0-4', 'e0-5', 'e0-6', 'e0-7', 'e0-8', 'e0-9', 'e0-10', 'e0-11', 'e0-12', 'e0-13', 'e0-14', 'e0-15')
