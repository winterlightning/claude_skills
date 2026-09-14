"""Puzzle piece (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'daa95c47-3220-4ba6-8dc5-aca5e1866078'
SOURCE_PATH = 'icons-json/symbol/puzzle piece_daa95c47-3220-4ba6-8dc5-aca5e1866078.json'
AUTHOR = 'json_to_solo'

class PuzzlePieceSymbol(Solo48):
    icon_id = 'puzzle-piece-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('puzzle', 'piece', 'symbol')

    def build(self):
        self.add_line('e0', (8, 24), (8, 14))
        self.add_line('e1', (8, 14), (18, 14))
        self.add_line('e2', (31, 14), (40, 14))
        self.add_line('e3', (40, 14), (40, 24))
        self.add_line('e4', (40, 35), (40, 44))
        self.add_line('e5', (40, 44), (8, 44))
        self.add_line('e6', (8, 44), (8, 34))
        self.add_arc('e7-1', (18, 14), (24, 4), radius_x=7)
        self.add_arc('e7-2', (24, 4), (31, 14), radius_x=8)
        self.add_arc('e8', (40, 24), (40, 35), radius_x=6, large_arc=True, sweep=False)
        self.add_arc('e9-1', (8, 34), (15, 33), radius_x=7, sweep=False)
        self.add_arc('e9-2', (15, 33), (14, 24), radius_x=6, sweep=False)
        self.add_arc('e9-3', (14, 24), (8, 24), radius_x=5, sweep=False)
        self.add_contour('c0', 'e0', 'e1', 'e7-1', 'e7-2', 'e2', 'e3', 'e8', 'e4', 'e5', 'e6', 'e9-1', 'e9-2', 'e9-3', closed=True)
