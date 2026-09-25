"""French Pastry Croissant.

SOLO48 visible bounds: (2, 6, 46, 42). Centerline extremes: (4, 8, 44, 40).

Symbol plan: Symmetric curved crescent pastry with two attached fold seams.
Reduction: Use horizontal crescent for broad open center; omit tiny rolled tips.
Construction reference: croissant: large central mass and tapering end rolls
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f9e55377-8da9-5927-845b-403bea7db251'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/food/breakfast croissant_f9e55377-8da9-5927-845b-403bea7db251.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/breakfast croissant_f9e55377-8da9-5927-845b-403bea7db251.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-011/references/breakfast croissant_f9e55377-8da9-5927-845b-403bea7db251.svg'
AUTHOR = "gpt-6"
BATCH_AUTHORING_RUN = "20260917-011-015"


class GeneratedSolo(Solo48):
    icon_id = 'croissant-batch-011-10'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    aliases = ()
    keywords = ('croissant', 'pastry', 'bread', 'breakfast', 'food', 'bakery')

    def build(self):
        self.add_bezier('pastry-1', (4, 32), ((4, 18), (12, 8), (24, 8)))
        self.add_bezier('pastry-2', (24, 8), ((36, 8), (44, 18), (44, 32)))
        self.add_bezier('pastry-3', (44, 32), ((44, 40), (40, 40), (38, 40)))
        self.add_bezier('pastry-4', (38, 40), ((36, 40), (34, 37), (32, 32)))
        self.add_bezier('pastry-5', (32, 32), ((28, 24), (20, 24), (16, 32)))
        self.add_bezier('pastry-6', (16, 32), ((14, 37), (12, 40), (10, 40)))
        self.add_bezier('pastry-7', (10, 40), ((8, 40), (4, 40), (4, 32)))
        self.add_contour('pastry', 'pastry-1', 'pastry-2', 'pastry-3', 'pastry-4', 'pastry-5', 'pastry-6', 'pastry-7', closed=True)
        self.add_bezier('fold-left-1', (14, 12), ((16, 18), (16, 23), (16, 32)))
        self.add_contour('fold-left', 'fold-left-1', closed=False)
        self.add_bezier('fold-right-1', (34, 12), ((32, 18), (32, 23), (32, 32)))
        self.add_contour('fold-right', 'fold-right-1', closed=False)
        self.relate("connect", 'pastry', 'fold-left')
        self.relate("connect", 'pastry', 'fold-right')
