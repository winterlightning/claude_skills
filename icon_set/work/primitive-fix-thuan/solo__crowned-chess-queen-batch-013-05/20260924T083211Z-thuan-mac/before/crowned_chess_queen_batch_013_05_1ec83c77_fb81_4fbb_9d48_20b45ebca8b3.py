"""Chess Queen Piece.

SOLO48 visible bounds: (6, 2, 42, 46). Centerline extremes: (8, 4, 40, 44).

Symbol plan: Three-point queen crown above tapered waist and pedestal.
Reduction: Integrate central finial into high crown point; omit narrow collar.
Construction reference: crown: open valleys between three high points
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1ec83c77-fb81-4fbb-9d48-20b45ebca8b3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/hobbies/chess king_1ec83c77-fb81-4fbb-9d48-20b45ebca8b3.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/hobbies/chess king_1ec83c77-fb81-4fbb-9d48-20b45ebca8b3.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-013/references/chess king_1ec83c77-fb81-4fbb-9d48-20b45ebca8b3.svg'
AUTHOR = "gpt-6"
BATCH_AUTHORING_RUN = "20260917-011-015"


class GeneratedSolo(Solo48):
    icon_id = 'crowned-chess-queen-batch-013-05'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/batch-subjects"
    aliases = ()
    keywords = ('chess', 'queen', 'crown', 'piece', 'game', 'board')

    def build(self):
        self.add_polyline('piece', (8, 12), (16, 20), (24, 4), (32, 20), (40, 12), (34, 28), (30, 28), (30, 34), (40, 44), (8, 44), (18, 34), (18, 28), (14, 28), closed=True)
