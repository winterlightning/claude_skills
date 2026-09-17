"""Chess Knight and Pawn.

SOLO48 visible bounds: (4, 4, 44, 44). Centerline extremes: (6, 6, 42, 42).

Symbol plan: Left-facing knight and smaller pawn share baseline.
Reduction: Simplify pedestal layers and omit horse eye to fit paired pieces.
Construction reference: No useful local Lucide subject match; supplied reference governs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e8184764-3245-40c1-a10d-883944a9fe13'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/hobbies/chess_e8184764-3245-40c1-a10d-883944a9fe13.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/hobbies/chess_e8184764-3245-40c1-a10d-883944a9fe13.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-013/references/chess_e8184764-3245-40c1-a10d-883944a9fe13.svg'
AUTHOR = "gpt-6"
BATCH_AUTHORING_RUN = "20260917-011-015"


class GeneratedSolo(Solo48):
    icon_id = 'chess-knight-and-pawn-batch-013-03'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/batch-subjects"
    aliases = ()
    keywords = ('chess', 'knight', 'pawn', 'pieces', 'game', 'board')

    def build(self):
        self.add_polyline('knight', (6, 42), (10, 28), (14, 20), (6, 20), (6, 14), (16, 6), (22, 12), (22, 42), closed=True)
        self.add_arc('pawn-head-1', (36, 17), (42, 23), radius_x=6, radius_y=6, sweep=True)
        self.add_arc('pawn-head-2', (42, 23), (36, 29), radius_x=6, radius_y=6, sweep=True)
        self.add_arc('pawn-head-3', (36, 29), (30, 23), radius_x=6, radius_y=6, sweep=True)
        self.add_arc('pawn-head-4', (30, 23), (36, 17), radius_x=6, radius_y=6, sweep=True)
        self.add_contour('pawn-head', 'pawn-head-1', 'pawn-head-2', 'pawn-head-3', 'pawn-head-4', closed=True)
        self.add_polyline('pawn-base', (36, 29), (30, 42), (42, 42), closed=True)
        self.relate("connect", 'pawn-head', 'pawn-base')
