"""Puzzle piece (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'daa95c47-3220-4ba6-8dc5-aca5e1866078'
SOURCE_PATH = 'pictographic-primitives/symbol/puzzle piece_daa95c47-3220-4ba6-8dc5-aca5e1866078.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class PuzzlePiece(Solo48):
    icon_id = 'puzzle-piece'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    categories = ('symbol', 'state')
    aliases = ()
    keywords = ('puzzle', 'piece', 'symbol')

    def build(self):
        # Plan: remove subpixel cubic detours while preserving real contour nodes.
        # Reference: supplied subject and its existing stroke graph.
        self.add_line('e0', (8, 24), (8, 14))
        self.add_line('e1', (8, 14), (18, 14))
        self.add_line('e2', (31, 14), (40, 14))
        self.add_line('e3', (40, 14), (40, 24))
        self.add_line('e4', (40, 35), (40, 44))
        self.add_line('e5', (40, 44), (8, 44))
        self.add_line('e6', (8, 44), (8, 34))
        self.add_bezier('e7', (18, 14), ((17.18, 10.673), (16.79, 7.255), (20.35, 5.036)), ((21.27, 4.464), (22.51, 4.009), (23.64, 4.009)), ((23.709, 4.009), (23.788, 4), (23.857, 4)), ((24.08, 4), (24.31, 4.009), (24.53, 4.009)), ((27.96, 4.009), (30.81, 7.064), (31.27, 9.964)), ((31.48, 11.327), (31.2, 12.655), (31, 14)))
        self.add_bezier('e8', (40, 24), ((38.3, 23.627), (36.97, 23.382), (35.37, 24.182)), ((30.67, 26.536), (31.09, 33.709), (36.47, 35.1)), ((37.72, 35.427), (38.73, 35.255), (40, 35)))
        self.add_bezier('e9', (8, 34), ((9.17, 34.345), (10.18, 34.736), (11.42, 34.555)), ((18.74, 33.473), (17.84, 23.227), (10.98, 23.1)), ((9.73, 23.073), (9.21, 23.436), (8, 24)))
        self.add_contour('c0', 'e0', 'e1', 'e7', 'e2', 'e3', 'e8', 'e4', 'e5', 'e6', 'e9', closed=True)
