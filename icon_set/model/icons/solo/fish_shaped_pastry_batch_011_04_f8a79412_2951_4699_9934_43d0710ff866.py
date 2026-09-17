"""Fish Shaped Pastry Taiyaki.

SOLO48 visible bounds: (2, 8, 46, 40). Centerline extremes: (4, 10, 44, 38).

Symbol plan: Plump left-facing fish with concave tail junction and one eye.
Reduction: Remove paired crust marks to preserve the plump pastry body.
Construction reference: fish: pointed tail contrasted with round body
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f8a79412-2951-4699-9934-43d0710ff866'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/food/desert fish shaped grilled bun taiyaki_f8a79412-2951-4699-9934-43d0710ff866.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/desert fish shaped grilled bun taiyaki_f8a79412-2951-4699-9934-43d0710ff866.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-011/references/desert fish shaped grilled bun taiyaki_f8a79412-2951-4699-9934-43d0710ff866.svg'
AUTHOR = "gpt-6"
BATCH_AUTHORING_RUN = "20260917-011-015"


class GeneratedSolo(Solo48):
    icon_id = 'fish-shaped-pastry-batch-011-04'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/batch-subjects"
    aliases = ()
    keywords = ('fish', 'pastry', 'taiyaki', 'dessert', 'food', 'bun')

    def build(self):
        self.add_bezier('fish-1', (32, 18), ((28, 12), (24, 10), (20, 10)))
        self.add_bezier('fish-2', (20, 10), ((11, 10), (4, 16), (4, 24)))
        self.add_bezier('fish-3', (4, 24), ((4, 32), (11, 38), (20, 38)))
        self.add_bezier('fish-4', (20, 38), ((24, 38), (28, 36), (32, 30)))
        self.add_line('fish-5', (32, 30), (44, 38))
        self.add_line('fish-6', (44, 38), (44, 10))
        self.add_line('fish-7', (44, 10), (32, 18))
        self.add_contour('fish', 'fish-1', 'fish-2', 'fish-3', 'fish-4', 'fish-5', 'fish-6', 'fish-7', closed=True)
        self.add_dot('eye', (15, 24))
