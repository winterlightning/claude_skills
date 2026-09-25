"""Hot Dog with Mustard.

SOLO48 visible bounds: (4, 4, 44, 44). Centerline extremes: (6, 6, 42, 42).

Symbol plan: Diagonal rounded bun enclosing a single continuous mustard wave.
Reduction: Recompose diagonally for a visibly elongated hot dog; omit projecting sausage ends.
Construction reference: No useful local Lucide subject match; supplied reference governs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2b81b158-1000-5c01-96ea-05c64a806041'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/food/hot dog grilled_2b81b158-1000-5c01-96ea-05c64a806041.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/hot dog grilled_2b81b158-1000-5c01-96ea-05c64a806041.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-011/references/hot dog grilled_2b81b158-1000-5c01-96ea-05c64a806041.svg'
AUTHOR = "gpt-6"
BATCH_AUTHORING_RUN = "20260917-011-015"


class GeneratedSolo(Solo48):
    icon_id = 'diagonal-hot-dog-batch-011-15'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    aliases = ()
    keywords = ('hotdog', 'sausage', 'bun', 'food', 'snack', 'mustard')

    def build(self):
        self.add_bezier('bun-1', (6, 32), ((6, 28), (8, 26), (10, 24)))
        self.add_line('bun-2', (10, 24), (24, 10))
        self.add_bezier('bun-3', (24, 10), ((26, 8), (28, 6), (32, 6)))
        self.add_bezier('bun-4', (32, 6), ((38, 6), (42, 10), (42, 16)))
        self.add_bezier('bun-5', (42, 16), ((42, 20), (40, 22), (38, 24)))
        self.add_line('bun-6', (38, 24), (24, 38))
        self.add_bezier('bun-7', (24, 38), ((22, 40), (20, 42), (16, 42)))
        self.add_bezier('bun-8', (16, 42), ((10, 42), (6, 38), (6, 32)))
        self.add_contour('bun', 'bun-1', 'bun-2', 'bun-3', 'bun-4', 'bun-5', 'bun-6', 'bun-7', 'bun-8', closed=True)
        self.add_bezier('mustard-1', (16, 32), ((16, 28), (24, 28), (24, 24)))
        self.add_bezier('mustard-2', (24, 24), ((24, 20), (32, 20), (32, 16)))
        self.add_contour('mustard', 'mustard-1', 'mustard-2', closed=False)
