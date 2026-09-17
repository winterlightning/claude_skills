"""Fork and Knife Utensils.

SOLO48 visible bounds: (4, 4, 44, 44). Centerline extremes: (6, 6, 42, 42).

Symbol plan: Fork on left; second utensil on right; fixed 8-unit tine spacing.
Reduction: Retain three tines; simplify handles to single strokes.
Construction reference: utensils: U-shaped fork bowl and continuous handle
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '56745c4d-820e-4bdb-9aa5-f3fbd6b451ab'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/food/fork and spoon_56745c4d-820e-4bdb-9aa5-f3fbd6b451ab.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/fork and spoon_56745c4d-820e-4bdb-9aa5-f3fbd6b451ab.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-011/references/fork and spoon_56745c4d-820e-4bdb-9aa5-f3fbd6b451ab.svg'
AUTHOR = "gpt-6"
BATCH_AUTHORING_RUN = "20260917-011-015"


class GeneratedSolo(Solo48):
    icon_id = 'fork-and-knife-reference-batch-011-06'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/batch-subjects"
    aliases = ()
    keywords = ('fork', 'knife', 'cutlery', 'utensils', 'meal', 'dining')

    def build(self):
        self.add_polyline('fork', (6, 6), (6, 24), (14, 24), (22, 24), (22, 6), closed=False)
        self.add_line('middle-tine', (14, 6), (14, 16))
        self.add_line('handle', (14, 24), (14, 42))
        self.relate("connect", 'fork', 'handle')
        self.add_line('knife-1', (32, 6), (42, 24))
        self.add_line('knife-2', (42, 24), (32, 24))
        self.add_line('knife-3', (32, 24), (32, 6))
        self.add_contour('knife', 'knife-1', 'knife-2', 'knife-3', closed=True)
        self.add_line('knife-handle', (32, 24), (32, 42))
        self.relate("connect", 'knife', 'knife-handle')
