"""Chess Bishop Game Piece.

SOLO48 visible bounds: (8, 2, 40, 46). Centerline extremes: (10, 4, 38, 44).

Symbol plan: Bishop mitre, narrow neck and flared pedestal share vertical axis.
Reduction: Omit separate finial; preserve pointed bishop head with diagonal slit.
Construction reference: No useful local Lucide subject match; supplied reference governs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4020213e-b2a5-5ea0-a2b2-78847651ebd5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/hobbies/chess bishop_4020213e-b2a5-5ea0-a2b2-78847651ebd5.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/hobbies/chess bishop_4020213e-b2a5-5ea0-a2b2-78847651ebd5.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-013/references/chess bishop_4020213e-b2a5-5ea0-a2b2-78847651ebd5.svg'
AUTHOR = "gpt-6"
BATCH_AUTHORING_RUN = "20260917-011-015"


class GeneratedSolo(Solo48):
    icon_id = 'chess-bishop-batch-013-01'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/batch-subjects"
    aliases = ()
    keywords = ('chess', 'bishop', 'piece', 'game', 'board', 'pedestal')

    def build(self):
        self.add_bezier('piece-1', (24, 4), ((16, 12), (10, 18), (18, 24)))
        self.add_line('piece-2', (18, 24), (18, 30))
        self.add_bezier('piece-3', (18, 30), ((18, 37), (10, 38), (10, 44)))
        self.add_line('piece-4', (10, 44), (38, 44))
        self.add_bezier('piece-5', (38, 44), ((38, 38), (30, 37), (30, 30)))
        self.add_line('piece-6', (30, 30), (30, 24))
        self.add_bezier('piece-7', (30, 24), ((38, 18), (32, 12), (24, 4)))
        self.add_contour('piece', 'piece-1', 'piece-2', 'piece-3', 'piece-4', 'piece-5', 'piece-6', 'piece-7', closed=True)
        self.add_line('mitre-cut', (24, 4), (24, 15))
        self.relate("connect", 'piece', 'mitre-cut')
