"""Left and Right Navigation Chevrons.

SOLO48 visible bounds: (2, 8, 46, 40). Centerline extremes: (4, 10, 44, 38).

Symbol plan: Mirrored outward navigation pair with broad central gap.
Reduction: Retain closed triangles or open chevrons as specified.
Construction reference: No useful local Lucide subject match; supplied reference governs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '00b256b7-e63b-5369-b095-0026b11745de'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/interface-essential/scroll horizontal_00b256b7-e63b-5369-b095-0026b11745de.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/scroll horizontal_00b256b7-e63b-5369-b095-0026b11745de.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-015/references/scroll horizontal_00b256b7-e63b-5369-b095-0026b11745de.svg'
AUTHOR = "gpt-6"
BATCH_AUTHORING_RUN = "20260917-011-015"


class GeneratedSolo(Solo48):
    icon_id = 'opposing-navigation-chevrons-batch-015-10'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/batch-subjects"
    aliases = ()
    keywords = ('chevrons', 'left', 'right', 'navigation', 'arrows', 'scroll')

    def build(self):
        self.add_polyline('left', (16, 10), (4, 24), (16, 38), closed=False)
        self.add_polyline('right', (32, 10), (44, 24), (32, 38), closed=False)
