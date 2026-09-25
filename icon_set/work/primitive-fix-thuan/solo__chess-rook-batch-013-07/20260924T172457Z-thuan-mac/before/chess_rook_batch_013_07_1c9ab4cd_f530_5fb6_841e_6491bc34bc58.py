"""Chess Rook Game Piece.

SOLO48 visible bounds: (6, 2, 42, 46). Centerline extremes: (8, 4, 40, 44).

Symbol plan: Three battlements on a tower, broad straight pedestal.
Reduction: Use one deep central crenel pair and a single pedestal tier.
Construction reference: No useful local Lucide subject match; supplied reference governs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1c9ab4cd-f530-5fb6-841e-6491bc34bc58'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/hobbies/chess rook_1c9ab4cd-f530-5fb6-841e-6491bc34bc58.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/hobbies/chess rook_1c9ab4cd-f530-5fb6-841e-6491bc34bc58.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-013/references/chess rook_1c9ab4cd-f530-5fb6-841e-6491bc34bc58.svg'
AUTHOR = "gpt-6"
BATCH_AUTHORING_RUN = "20260917-011-015"


class GeneratedSolo(Solo48):
    icon_id = 'chess-rook-batch-013-07'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/batch-subjects"
    aliases = ()
    keywords = ('chess', 'rook', 'tower', 'battlement', 'piece', 'game')

    def build(self):
        self.add_polyline('rook', (8, 4), (8, 20), (16, 20), (14, 36), (8, 44), (40, 44), (34, 36), (32, 20), (40, 20), (40, 4), (32, 4), (32, 12), (24, 12), (24, 4), (16, 4), (16, 12), (8, 12), closed=False)
