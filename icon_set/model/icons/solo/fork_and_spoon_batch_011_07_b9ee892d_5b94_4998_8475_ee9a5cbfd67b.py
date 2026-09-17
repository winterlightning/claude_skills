"""Fork and Spoon Utensils.

SOLO48 visible bounds: (4, 4, 44, 44). Centerline extremes: (6, 6, 42, 42).

Symbol plan: Fork on left; second utensil on right; fixed 8-unit tine spacing.
Reduction: Retain three tines; simplify handles to single strokes.
Construction reference: utensils: U-shaped fork bowl and continuous handle
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b9ee892d-5b94-4998-8475-ee9a5cbfd67b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/food/restaurant fork spoon_b9ee892d-5b94-4998-8475-ee9a5cbfd67b.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/restaurant fork spoon_b9ee892d-5b94-4998-8475-ee9a5cbfd67b.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-011/references/restaurant fork spoon_b9ee892d-5b94-4998-8475-ee9a5cbfd67b.svg'
AUTHOR = "gpt-6"
BATCH_AUTHORING_RUN = "20260917-011-015"


class GeneratedSolo(Solo48):
    icon_id = 'fork-and-spoon-batch-011-07'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/batch-subjects"
    aliases = ()
    keywords = ('fork', 'spoon', 'cutlery', 'utensils', 'meal', 'dining')

    def build(self):
        self.add_polyline('fork', (6, 6), (6, 24), (14, 24), (22, 24), (22, 6), closed=False)
        self.add_line('middle-tine', (14, 6), (14, 16))
        self.add_line('handle', (14, 24), (14, 42))
        self.relate("connect", 'fork', 'handle')
        self.add_arc('spoon-1', (36, 6), (42, 16), radius_x=6, radius_y=10, sweep=True)
        self.add_arc('spoon-2', (42, 16), (36, 26), radius_x=6, radius_y=10, sweep=True)
        self.add_arc('spoon-3', (36, 26), (30, 16), radius_x=6, radius_y=10, sweep=True)
        self.add_arc('spoon-4', (30, 16), (36, 6), radius_x=6, radius_y=10, sweep=True)
        self.add_contour('spoon', 'spoon-1', 'spoon-2', 'spoon-3', 'spoon-4', closed=True)
        self.add_line('spoon-handle', (36, 26), (36, 42))
        self.relate("connect", 'spoon', 'spoon-handle')
