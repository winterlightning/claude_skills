"""Chess King Piece.

SOLO48 visible bounds: (6, 2, 42, 46). Centerline extremes: (8, 4, 40, 44).

Symbol plan: Crown, waist and broad base beneath a cross finial.
Reduction: Single pedestal tier and open cross retain king silhouette.
Construction reference: No useful local Lucide subject match; supplied reference governs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '68a6d25b-eff8-528a-a8e2-082a52565f0f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/hobbies/chess king_68a6d25b-eff8-528a-a8e2-082a52565f0f.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/hobbies/chess king_68a6d25b-eff8-528a-a8e2-082a52565f0f.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-013/references/chess king_68a6d25b-eff8-528a-a8e2-082a52565f0f.svg'
AUTHOR = "gpt-6"
BATCH_AUTHORING_RUN = "20260917-011-015"


class GeneratedSolo(Solo48):
    icon_id = 'chess-king-batch-013-02'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "hobbies"
    aliases = ()
    keywords = ('chess', 'king', 'piece', 'cross', 'game', 'board')

    def build(self):
        self.add_polyline('piece', (12, 20), (36, 20), (30, 34), (40, 44), (8, 44), (18, 34), closed=True)
        self.add_line('cross-stem', (24, 4), (24, 20))
        self.add_line('cross-bar', (16, 10), (32, 10))
        self.relate("connect", 'piece', 'cross-stem')
        self.relate("connect", 'cross-stem', 'cross-bar')
