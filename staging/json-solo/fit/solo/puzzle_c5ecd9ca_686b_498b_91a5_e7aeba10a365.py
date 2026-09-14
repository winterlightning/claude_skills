"""Puzzle (state), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c5ecd9ca-686b-498b-91a5-e7aeba10a365'
SOURCE_PATH = 'icons-json/state/puzzle_c5ecd9ca-686b-498b-91a5-e7aeba10a365.json'
AUTHOR = 'json_to_solo'

class PuzzleState(Solo48):
    icon_id = 'puzzle-state'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('puzzle', 'state')

    def build(self):
        self.add_line('e0', (21, 44), (10, 44))
        self.add_line('e1', (8, 42), (8, 31))
        self.add_line('e2', (8, 31), (10, 33))
        self.add_line('e3', (11, 24), (8, 25))
        self.add_line('e4', (8, 25), (8, 15))
        self.add_line('e5', (10, 13), (21, 13))
        self.add_line('e6', (21, 13), (20, 10))
        self.add_line('e7', (28, 9), (27, 13))
        self.add_line('e8', (27, 13), (38, 13))
        self.add_line('e9', (40, 15), (40, 42))
        self.add_line('e10', (38, 44), (27, 44))
        self.add_line('e11', (27, 44), (28, 41))
        self.add_line('e12', (20, 41), (21, 44))
        self.add_line('e13-1', (10, 44), (8, 43))
        self.add_line('e13-2', (8, 43), (8, 42))
        self.add_arc('e14-1', (10, 33), (16, 31), radius_x=4, sweep=False)
        self.add_arc('e14-2', (16, 31), (11, 24), radius_x=5, sweep=False)
        self.add_arc('e15', (8, 15), (10, 13), radius_x=2)
        self.add_arc('e16-1', (20, 10), (24, 4), radius_x=5)
        self.add_arc('e16-2', (24, 4), (28, 9), radius_x=5)
        self.add_arc('e17', (38, 13), (40, 15), radius_x=2)
        self.add_arc('e18', (40, 42), (38, 44), radius_x=2)
        self.add_arc('e19-1', (28, 41), (24, 35), radius_x=5, sweep=False)
        self.add_arc('e19-2', (24, 35), (20, 41), radius_x=5, sweep=False)
        self.add_contour('c0', 'e0', 'e13-1', 'e13-2', 'e1', 'e2', 'e14-1', 'e14-2', 'e3', 'e4', 'e15', 'e5', 'e6', 'e16-1', 'e16-2', 'e7', 'e8', 'e17', 'e9', 'e18', 'e10', 'e11', 'e19-1', 'e19-2', 'e12', closed=True)
