"""Fresh Broccoli Vegetable.

SOLO48 visible bounds: (4, 4, 44, 44). Centerline extremes: (6, 6, 42, 42).

Symbol plan: Three-lobed broccoli crown with attached broad stalk.
Reduction: Remove small central vein to open negative space.
Construction reference: No useful local Lucide subject match; supplied reference governs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '57d07ae0-a586-52f2-b0d1-5f36b6fe1c7b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/food/broccoli_57d07ae0-a586-52f2-b0d1-5f36b6fe1c7b.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/broccoli_57d07ae0-a586-52f2-b0d1-5f36b6fe1c7b.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-011/references/broccoli_57d07ae0-a586-52f2-b0d1-5f36b6fe1c7b.svg'
AUTHOR = "gpt-6"
BATCH_AUTHORING_RUN = "20260917-011-015"


class GeneratedSolo(Solo48):
    icon_id = 'broccoli-floret-batch-011-11'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    aliases = ()
    keywords = ('broccoli', 'floret', 'vegetable', 'stem', 'greens', 'food')

    def build(self):
        self.add_bezier('crown-1', (16, 30), ((10, 34), (6, 30), (6, 24)))
        self.add_bezier('crown-2', (6, 24), ((6, 18), (8, 14), (14, 14)))
        self.add_bezier('crown-3', (14, 14), ((14, 9), (18, 6), (24, 6)))
        self.add_bezier('crown-4', (24, 6), ((30, 6), (34, 9), (34, 14)))
        self.add_bezier('crown-5', (34, 14), ((40, 14), (42, 18), (42, 24)))
        self.add_bezier('crown-6', (42, 24), ((42, 30), (38, 34), (32, 30)))
        self.add_bezier('crown-7', (32, 30), ((28, 34), (20, 34), (16, 30)))
        self.add_contour('crown', 'crown-1', 'crown-2', 'crown-3', 'crown-4', 'crown-5', 'crown-6', 'crown-7', closed=True)
        self.add_polyline('stem', (16, 30), (18, 42), (30, 42), (32, 30), closed=False)
        self.relate("connect", 'crown', 'stem')
