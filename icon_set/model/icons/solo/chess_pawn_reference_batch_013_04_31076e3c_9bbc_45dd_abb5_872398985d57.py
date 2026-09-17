"""Chess Pawn Game Piece.

SOLO48 visible bounds: (6, 2, 42, 46). Centerline extremes: (8, 4, 40, 44).

Symbol plan: Round pawn head attached to a flared body and single broad base.
Reduction: Merge two pedestal tiers into one clear plinth.
Construction reference: No useful local Lucide subject match; supplied reference governs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '31076e3c-9bbc-45dd-abb5-872398985d57'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/hobbies/chess pawn 1_31076e3c-9bbc-45dd-abb5-872398985d57.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/hobbies/chess pawn 1_31076e3c-9bbc-45dd-abb5-872398985d57.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-013/references/chess pawn 1_31076e3c-9bbc-45dd-abb5-872398985d57.svg'
AUTHOR = "gpt-6"
BATCH_AUTHORING_RUN = "20260917-011-015"


class GeneratedSolo(Solo48):
    icon_id = 'chess-pawn-reference-batch-013-04'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/batch-subjects"
    aliases = ()
    keywords = ('chess', 'pawn', 'piece', 'game', 'board', 'base')

    def build(self):
        self.add_arc('head-1', (24, 4), (32, 12), radius_x=8, radius_y=8, sweep=True)
        self.add_arc('head-2', (32, 12), (24, 20), radius_x=8, radius_y=8, sweep=True)
        self.add_arc('head-3', (24, 20), (16, 12), radius_x=8, radius_y=8, sweep=True)
        self.add_arc('head-4', (16, 12), (24, 4), radius_x=8, radius_y=8, sweep=True)
        self.add_contour('head', 'head-1', 'head-2', 'head-3', 'head-4', closed=True)
        self.add_line('body-1', (24, 20), (20, 20))
        self.add_bezier('body-2', (20, 20), ((20, 30), (16, 36), (8, 44)))
        self.add_line('body-3', (8, 44), (40, 44))
        self.add_bezier('body-4', (40, 44), ((32, 36), (28, 30), (28, 20)))
        self.add_line('body-5', (28, 20), (24, 20))
        self.add_contour('body', 'body-1', 'body-2', 'body-3', 'body-4', 'body-5', closed=False)
        self.relate("connect", 'head', 'body')
