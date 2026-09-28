"""House with crossed knitting needles.

SOLO48 visible bounds: (4, 4, 44, 44). Centerline extremes: (6, 6, 42, 42).

Symbol plan: Crossed knitting needles above a rectangular fabric panel.
Reduction: Knobs use round caps; no invented house door or windows.
Construction reference: No useful local Lucide subject match; supplied reference governs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '42e0445b-86b9-4a5a-b1c7-898db65d5c28'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/hobbies/sewing_42e0445b-86b9-4a5a-b1c7-898db65d5c28.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/hobbies/sewing_42e0445b-86b9-4a5a-b1c7-898db65d5c28.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-013/references/sewing_42e0445b-86b9-4a5a-b1c7-898db65d5c28.svg'
AUTHOR = "gpt-6"
BATCH_AUTHORING_RUN = "20260917-011-015"


class GeneratedSolo(Solo48):
    icon_id = 'crossed-knitting-needles-with-fabric-batch-013-12'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "hobbies"
    categories = ("primitives", "hobbies")
    aliases = ()
    keywords = ('knitting', 'needles', 'fabric', 'craft', 'textile', 'sewing')

    def build(self):
        self.add_line('needle-left', (6, 6), (42, 34))
        self.add_line('needle-right', (42, 6), (6, 34))
        self.relate("connect", 'needle-left', 'needle-right')
        self.add_polyline('fabric', (15, 27), (15, 42), (33, 42), (33, 27), closed=False)
        self.relate("connect", 'fabric', 'needle-left')
        self.relate("connect", 'fabric', 'needle-right')
