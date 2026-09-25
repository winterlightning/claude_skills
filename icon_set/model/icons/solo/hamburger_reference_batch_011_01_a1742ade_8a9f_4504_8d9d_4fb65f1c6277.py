"""Classic Fast Food Hamburger.

SOLO48 visible bounds: (2, 6, 46, 42). Centerline extremes: (4, 8, 44, 40).

Symbol plan: Three horizontal bun/filling runs; mirrored dome about x=24.
Reduction: Omit sesame seeds; retain wavy filling and open layer gaps.
Construction reference: No useful local Lucide subject match; supplied reference governs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a1742ade-8a9f-4504-8d9d-4fb65f1c6277'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/food/double burger_a1742ade-8a9f-4504-8d9d-4fb65f1c6277.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/double burger_a1742ade-8a9f-4504-8d9d-4fb65f1c6277.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-011/references/double burger_a1742ade-8a9f-4504-8d9d-4fb65f1c6277.svg'
AUTHOR = "gpt-6"
BATCH_AUTHORING_RUN = "20260917-011-015"


class GeneratedSolo(Solo48):
    icon_id = 'hamburger-reference-batch-011-01'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    aliases = ()
    keywords = ('hamburger', 'burger', 'bun', 'food', 'sandwich', 'fastfood')

    def build(self):
        self.add_bezier('top-bun-1', (4, 20), ((4, 14), (13, 8), (24, 8)))
        self.add_bezier('top-bun-2', (24, 8), ((35, 8), (44, 14), (44, 20)))
        self.add_line('top-bun-close', (44, 20), (4, 20))
        self.add_contour('top-bun', 'top-bun-1', 'top-bun-2', 'top-bun-close', closed=True)
        self.add_bezier('filling-1', (4, 30), ((9, 34), (11, 26), (16, 30)))
        self.add_bezier('filling-2', (16, 30), ((21, 34), (23, 26), (28, 30)))
        self.add_bezier('filling-3', (28, 30), ((33, 34), (35, 26), (40, 30)))
        self.add_line('filling-4', (40, 30), (44, 30))
        self.add_contour('filling', 'filling-1', 'filling-2', 'filling-3', 'filling-4', closed=False)
        self.add_line('lower-bun-1', (4, 40), (44, 40))
        self.add_contour('lower-bun', 'lower-bun-1', closed=False)
