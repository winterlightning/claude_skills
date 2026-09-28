"""Japanese Gyoza Dumpling.

SOLO48 visible bounds: (2, 8, 46, 40). Centerline extremes: (4, 10, 44, 38).

Symbol plan: Half-moon dumpling with three pleat seams sharing its rim.
Reduction: Reduce scallops to a smooth dome and three short folds.
Construction reference: No useful local Lucide subject match; supplied reference governs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '21395538-12e9-5de3-acef-658966ba5bd2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/food/gyoza grill deep fried dumpling_21395538-12e9-5de3-acef-658966ba5bd2.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/gyoza grill deep fried dumpling_21395538-12e9-5de3-acef-658966ba5bd2.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-012/references/gyoza grill deep fried dumpling_21395538-12e9-5de3-acef-658966ba5bd2.svg'
AUTHOR = "gpt-6"
BATCH_AUTHORING_RUN = "20260917-011-015"


class GeneratedSolo(Solo48):
    icon_id = 'gyoza-dumpling-batch-012-03'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    categories = ("primitives", "food")
    aliases = ()
    keywords = ('gyoza', 'dumpling', 'pleat', 'dough', 'food', 'japanese')

    def build(self):
        self.add_bezier('dumpling-1', (4, 30), ((4, 24), (6, 19), (10, 16)))
        self.add_bezier('dumpling-2', (10, 16), ((14, 13), (18, 10), (24, 10)))
        self.add_bezier('dumpling-3', (24, 10), ((30, 10), (34, 13), (38, 16)))
        self.add_bezier('dumpling-4', (38, 16), ((42, 19), (44, 24), (44, 30)))
        self.add_bezier('dumpling-5', (44, 30), ((44, 38), (34, 38), (24, 38)))
        self.add_bezier('dumpling-6', (24, 38), ((14, 38), (4, 38), (4, 30)))
        self.add_contour('dumpling', 'dumpling-1', 'dumpling-2', 'dumpling-3', 'dumpling-4', 'dumpling-5', 'dumpling-6', closed=True)
        self.add_line('pleat-middle', (24, 10), (24, 20))
        self.add_line('pleat-left', (10, 16), (15, 23))
        self.add_line('pleat-right', (38, 16), (33, 23))
        self.relate("connect", 'dumpling', 'pleat-middle')
        self.relate("connect", 'dumpling', 'pleat-left')
        self.relate("connect", 'dumpling', 'pleat-right')
