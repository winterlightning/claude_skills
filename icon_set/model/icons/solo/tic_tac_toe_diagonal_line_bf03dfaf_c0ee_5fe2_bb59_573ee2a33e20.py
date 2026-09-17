"""Tic Tac Toe Winning Game.
Plan: Grid intersections and winning diagonal share exact nodes. Two corner crosses repeat about the center. Centerline extremes (6,6)-(42,42).
Reference: Lucide grid-3x3: shared grid divisions.
Reduction: Rings omitted to keep the winning diagonal open and readable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bf03dfaf-c0ee-5fe2-bb59-573ee2a33e20'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/entertainment/board game tic tac toe_bf03dfaf-c0ee-5fe2-bb59-573ee2a33e20.svg'
AUTHOR = 'gpt-6'


class Batch25Icon(Solo48):
    icon_id = 'tic-tac-toe-diagonal-line'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/entertainment"
    aliases = ()
    keywords = ('tic', 'tac', 'toe', 'winning', 'game')

    def build(self):

        for i,y in enumerate((18,30)):
            self.add_polyline(f'row-{i}',(6,y),(18,y),(30,y),(42,y))
        for i,x in enumerate((18,30)):
            self.add_polyline(f'column-{i}',(x,6),(x,18),(x,30),(x,42))
            for j in range(2): self.relate('connect',f'column-{i}',f'row-{j}')
        self.add_polyline('win',(6,42),(18,30),(30,18),(42,6))
        for i in range(2):
            self.relate('connect','win',f'row-{i}')
            self.relate('connect','win',f'column-{i}')
        for i,c in enumerate((8,40)):
            self.add_polyline(f'cross-{i}-a',(c-2,c-2),(c,c),(c+2,c+2))
            self.add_polyline(f'cross-{i}-b',(c-2,c+2),(c,c),(c+2,c-2))
            self.relate('connect',f'cross-{i}-a',f'cross-{i}-b')
