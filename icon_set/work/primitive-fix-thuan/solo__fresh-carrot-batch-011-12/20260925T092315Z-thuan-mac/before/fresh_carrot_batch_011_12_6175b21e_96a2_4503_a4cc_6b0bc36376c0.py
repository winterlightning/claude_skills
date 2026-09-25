"""Fresh Carrot Vegetable.

SOLO48 visible bounds: (6, 2, 42, 46). Centerline extremes: (8, 4, 40, 44).

Symbol plan: Long tapered carrot below two spreading leaf strokes.
Reduction: Use open leaf strokes; omit root notches.
Construction reference: carrot: tapering root and sparse shoulder detail
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6175b21e-96a2-4503-a4cc-6b0bc36376c0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/food/carrot_6175b21e-96a2-4503-a4cc-6b0bc36376c0.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/carrot_6175b21e-96a2-4503-a4cc-6b0bc36376c0.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-011/references/carrot_6175b21e-96a2-4503-a4cc-6b0bc36376c0.svg'
AUTHOR = "gpt-6"
BATCH_AUTHORING_RUN = "20260917-011-015"


class GeneratedSolo(Solo48):
    icon_id = 'fresh-carrot-batch-011-12'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    categories = ("food", "state")
    aliases = ()
    keywords = ('carrot', 'vegetable', 'root', 'leaves', 'food', 'produce')

    def build(self):
        self.add_bezier('root-1', (24, 16), ((8, 16), (14, 32), (22, 42)))
        self.add_bezier('root-2', (22, 42), ((23, 44), (23, 44), (24, 44)))
        self.add_bezier('root-3', (24, 44), ((25, 44), (25, 44), (26, 42)))
        self.add_bezier('root-4', (26, 42), ((34, 32), (40, 16), (24, 16)))
        self.add_contour('root', 'root-1', 'root-2', 'root-3', 'root-4', closed=True)
        self.add_polyline('leaves', (8, 4), (24, 16), (40, 4), closed=False)
        self.relate("connect", 'root', 'leaves')
