"""Hand Carving Wooden Bowl.

SOLO48 visible bounds: (4, 4, 44, 44). Centerline extremes: (6, 6, 42, 42).

Symbol plan: Gouge touches bowl rim and curled shaving rises to its right.
Reduction: One cutting stroke, broad bowl and single curl retain carving action.
Construction reference: No useful local Lucide subject match; supplied reference governs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f746fcda-f75b-56bc-8b21-d20b11cd104f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/hobbies/wood carving bowl_f746fcda-f75b-56bc-8b21-d20b11cd104f.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/hobbies/wood carving bowl_f746fcda-f75b-56bc-8b21-d20b11cd104f.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-013/references/wood carving bowl_f746fcda-f75b-56bc-8b21-d20b11cd104f.svg'
AUTHOR = "gpt-6"
BATCH_AUTHORING_RUN = "20260917-011-015"


class GeneratedSolo(Solo48):
    icon_id = 'carving-a-wooden-bowl-batch-013-10'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "hobbies"
    aliases = ()
    keywords = ('carving', 'bowl', 'wood', 'gouge', 'shaving', 'craft')

    def build(self):
        self.add_bezier('bowl-1', (6, 26), ((8, 38), (16, 42), (24, 42)))
        self.add_bezier('bowl-2', (24, 42), ((32, 42), (40, 38), (42, 26)))
        self.add_line('bowl-close', (42, 26), (6, 26))
        self.add_contour('bowl', 'bowl-1', 'bowl-2', 'bowl-close', closed=True)
        self.add_line('gouge', (6, 6), (26, 26))
        self.relate("connect", 'gouge', 'bowl')
        self.add_line('shaving-1', (32, 26), (32, 18))
        self.add_arc('shaving-2', (32, 18), (42, 18), radius_x=5, radius_y=5, sweep=True)
        self.add_contour('shaving', 'shaving-1', 'shaving-2', closed=False)
        self.relate("connect", 'shaving', 'bowl')
