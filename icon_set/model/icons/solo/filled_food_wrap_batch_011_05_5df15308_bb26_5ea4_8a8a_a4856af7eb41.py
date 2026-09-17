"""Food Wrap Burrito.

SOLO48 visible bounds: (6, 2, 42, 46). Centerline extremes: (8, 4, 40, 44).

Symbol plan: Upright wrapped tortilla with scalloped filling top and diagonal fold.
Reduction: Reorient upright; omit filling hatch marks.
Construction reference: No useful local Lucide subject match; supplied reference governs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5df15308-bb26-5ea4-8a8a-a4856af7eb41'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/food/wrap_5df15308-bb26-5ea4-8a8a-a4856af7eb41.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/wrap_5df15308-bb26-5ea4-8a8a-a4856af7eb41.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-011/references/wrap_5df15308-bb26-5ea4-8a8a-a4856af7eb41.svg'
AUTHOR = "gpt-6"
BATCH_AUTHORING_RUN = "20260917-011-015"


class GeneratedSolo(Solo48):
    icon_id = 'filled-food-wrap-batch-011-05'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/batch-subjects"
    aliases = ()
    keywords = ('wrap', 'burrito', 'tortilla', 'food', 'meal', 'filling')

    def build(self):
        self.add_line('wrap-1', (8, 16), (14, 39))
        self.add_bezier('wrap-2', (14, 39), ((15, 44), (19, 44), (23, 44)))
        self.add_bezier('wrap-3', (23, 44), ((27, 44), (31, 42), (33, 37)))
        self.add_line('wrap-4', (33, 37), (40, 16))
        self.add_line('wrap-5', (40, 16), (8, 16))
        self.add_contour('wrap', 'wrap-1', 'wrap-2', 'wrap-3', 'wrap-4', 'wrap-5', closed=True)
        self.add_bezier('filling-1', (8, 16), ((8, 6), (12, 4), (16, 8)))
        self.add_bezier('filling-2', (16, 8), ((18, 6), (20, 4), (24, 4)))
        self.add_bezier('filling-3', (24, 4), ((28, 4), (28, 6), (28, 8)))
        self.add_bezier('filling-4', (28, 8), ((34, 4), (40, 6), (40, 16)))
        self.add_contour('filling', 'filling-1', 'filling-2', 'filling-3', 'filling-4', closed=False)
        self.relate("connect", 'wrap', 'filling')
        self.add_line('fold', (8, 16), (33, 37))
        self.relate("connect", 'wrap', 'fold')
