"""Puzzle (state), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
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
        self.add_bezier('e13', (10, 44), ((9.731, 43.836), (8, 42.936), (8, 42.673)), ((8.025, 42.627), (8.051, 42.591), (8.067, 42.545)), ((8.051, 42.427), (8.025, 42.118), (8, 42)))
        self.add_bezier('e14', (10, 33), ((11.853, 33.845), (13.684, 33.855), (15.234, 32.255)), ((17.592, 29.818), (17.204, 25.3), (13.827, 24.155)), ((12.985, 23.873), (11.859, 23.909), (11, 24)))
        self.add_bezier('e15', (8, 15), ((8.076, 14.818), (8.059, 14.527), (8.143, 14.355)), ((8.387, 13.855), (9.419, 13), (10, 13)))
        self.add_bezier('e16', (20, 10), ((19.899, 9.673), (19.714, 9.609), (19.697, 9.273)), ((19.579, 6.664), (21.112, 4.009), (23.781, 4.009)), ((23.881, 4.009), (23.988, 4), (24.088, 4)), ((24.089, 4), (24.091, 4), (24.093, 4)), ((24.177, 4), (24.261, 4.018), (24.345, 4.018)), ((27.149, 4.018), (28.202, 6.355), (28, 9)))
        self.add_bezier('e17', (38, 13), ((39.069, 13.509), (39.545, 13.864), (40, 15)))
        self.add_bezier('e18', (40, 42), ((39.739, 42.555), (39.427, 43.573), (38.872, 43.9)), ((38.703, 44), (38.185, 43.9), (38, 44)))
        self.add_bezier('e19', (28, 41), ((29.819, 35.118), (21.693, 32.527), (19.789, 38.664)), ((19.512, 39.564), (19.84, 40.109), (20, 41)))
        self.add_contour('c0', 'e0', 'e13', 'e1', 'e2', 'e14', 'e3', 'e4', 'e15', 'e5', 'e6', 'e16', 'e7', 'e8', 'e17', 'e9', 'e18', 'e10', 'e11', 'e19', 'e12', closed=True)
