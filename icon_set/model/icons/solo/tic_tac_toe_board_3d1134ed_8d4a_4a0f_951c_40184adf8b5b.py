"""Tic Tac Toe Game Board.
Plan: Open orthogonal nine-cell grid; corner noughts have shared radius. Centerline extremes (6,6)-(42,42).
Reference: Lucide grid-3x3: shared grid divisions.
Reduction: Outer border and central cross omitted; nine-cell grid and opposing noughts retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3d1134ed-8d4a-4a0f-951c-40184adf8b5b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/entertainment/tic tac toe_3d1134ed-8d4a-4a0f-951c-40184adf8b5b.svg'
AUTHOR = 'gpt-6'


class Batch25Icon(Solo48):
    icon_id = 'tic-tac-toe-board'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "entertainment"
    categories = ("entertainment", "primitives")
    aliases = ()
    keywords = ('tic', 'tac', 'toe', 'game', 'board')

    def build(self):

        for i,y in enumerate((20,28)):
            self.add_polyline(f'row-{i}',(6,y),(20,y),(28,y),(42,y))
        for i,x in enumerate((20,28)):
            self.add_polyline(f'column-{i}',(x,6),(x,20),(x,28),(x,42))
            for j in range(2): self.relate('connect',f'column-{i}',f'row-{j}')
        for i,c in enumerate((9,39)):
            self.add_arc(f'nought-{i}-a',(c-3,c),(c+3,c),radius_x=3)
            self.add_arc(f'nought-{i}-b',(c+3,c),(c-3,c),radius_x=3)
            self.add_contour(f'nought-{i}',f'nought-{i}-a',f'nought-{i}-b',closed=True)
