"""Fish rod (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '03dbc4e5-5755-4b95-a62e-3b755dafdffb'
SOURCE_PATH = 'icons-json/symbol/fish rod_03dbc4e5-5755-4b95-a62e-3b755dafdffb.json'
AUTHOR = 'json_to_solo'

class FishRodSymbol(Solo48):
    icon_id = 'fish-rod-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('fish', 'rod', 'symbol')

    def build(self):
        self.add_line('e0', (28, 23), (28, 37))
        self.add_line('e1', (8, 33), (9, 29))
        self.add_line('e2', (9, 29), (13, 33))
        self.add_arc('e3-1', (38, 16), (40, 11), radius_x=8, sweep=False)
        self.add_arc('e3-2', (40, 11), (37, 6), radius_x=7, sweep=False)
        self.add_arc('e3-3', (37, 6), (31, 4), radius_x=10, sweep=False)
        self.add_arc('e3-4', (31, 4), (22, 10), radius_x=10, sweep=False)
        self.add_arc('e3-5', (22, 10), (22, 15), radius_x=7, sweep=False)
        self.add_arc('e3-6', (22, 15), (28, 23), radius_x=13)
        self.add_arc('e4-1', (28, 37), (23, 43), radius_x=8)
        self.add_line('e4-2', (23, 43), (17, 44))
        self.add_arc('e4-3', (17, 44), (8, 35), radius_x=9)
        self.add_line('e4-4', (8, 35), (8, 33))
        self.add_contour('c0', 'e3-1', 'e3-2', 'e3-3', 'e3-4', 'e3-5', 'e3-6', 'e0', 'e4-1', 'e4-2', 'e4-3', 'e4-4', 'e1', 'e2')
