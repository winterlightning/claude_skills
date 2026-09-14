"""75 (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '96923c04-af2b-4baa-b0f7-7fb4d30662f9'
SOURCE_PATH = 'icons-json/symbol/75_96923c04-af2b-4baa-b0f7-7fb4d30662f9.json'
AUTHOR = 'json_to_solo'

class Icon75Symbol(Solo48):
    icon_id = 'icon-75-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('symbol',)

    def build(self):
        self.add_line('e0', (43, 8), (31, 8))
        self.add_line('e1', (31, 8), (30, 22))
        self.add_line('e2', (4, 8), (20, 8))
        self.add_line('e3', (20, 8), (9, 40))
        self.add_arc('e4-1', (30, 22), (39, 20), radius_x=8)
        self.add_arc('e4-2', (39, 20), (43, 24), radius_x=9)
        self.add_line('e4-3', (43, 24), (44, 29))
        self.add_line('e4-4', (44, 29), (42, 37))
        self.add_arc('e4-5', (42, 37), (40, 39), radius_x=8)
        self.add_line('e4-6', (40, 39), (36, 40))
        self.add_line('e4-7', (36, 40), (31, 38))
        self.add_arc('e4-8', (31, 38), (29, 35), radius_x=8)
        self.add_contour('c0', 'e0', 'e1', 'e4-1', 'e4-2', 'e4-3', 'e4-4', 'e4-5', 'e4-6', 'e4-7', 'e4-8')
        self.add_contour('c1', 'e2', 'e3')
