"""A diagonal skeleton key with a round bow at lower left and a thin shaft rising to upper right, ending in short teeth. Exclude the smartphone and avoid a solid key-tag blade.

Plan: Round bow with a rising diagonal shaft and two teeth; source orientation preserved. Bounds (2,2)-(30,30).
Construction reference: Lucide key-round: round bow and connected shaft; source owns orientation and teeth."""
from ...keyshapes import Keyshape
from ._base import Symbol32

SOURCE_ICON_ID = '45efdc96-5aab-49eb-ac68-b0e1ceb428c9'
SOURCE_PATH = 'pictographic-primitives/other/mobile phone key_45efdc96-5aab-49eb-ac68-b0e1ceb428c9.svg'
SOURCE_ICON_IDS = ('45efdc96-5aab-49eb-ac68-b0e1ceb428c9',)
AUTHOR = 'gpt-6'

class DiagonalRoundBowKeySymbol(Symbol32):
    icon_id = 'diagonal-round-bow-key-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives-generate'
    categories = ('other', 'primitives-generate')
    aliases = ()
    keywords = ('diagonal', 'round', 'bow', 'key', 'symbol')

    def build(self) -> None:
        self.add_arc('p1-r1-1', (2, 20), (22, 20), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (22, 20), (2, 20), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=True)
        self.add_line('p2-r1-1', (18, 12), (28, 2))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (25, 5), (30, 10))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'path-1-1', 'path-2-1')
