"""Japanese Bento Box Meal.

SOLO48 visible bounds: (4, 4, 44, 44). Centerline extremes: (6, 6, 42, 42).

Symbol plan: Three-compartment bento box with food marks in each section.
Reduction: Simplify food outlines to one rice arc and two round portions.
Construction reference: No useful local Lucide subject match; supplied reference governs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ba617c30-affd-453a-9840-5a1b6cb3e0ff'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/food/japanese launchbox bento ekiben_ba617c30-affd-453a-9840-5a1b6cb3e0ff.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/japanese launchbox bento ekiben_ba617c30-affd-453a-9840-5a1b6cb3e0ff.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-012/references/japanese launchbox bento ekiben_ba617c30-affd-453a-9840-5a1b6cb3e0ff.svg'
AUTHOR = "gpt-6"
BATCH_AUTHORING_RUN = "20260917-011-015"


class GeneratedSolo(Solo48):
    icon_id = 'compartment-bento-meal-batch-012-01'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/batch-subjects"
    aliases = ()
    keywords = ('bento', 'lunchbox', 'meal', 'food', 'compartment', 'japanese')

    def build(self):
        self.add_line('box-1', (9, 6), (39, 6))
        self.add_arc('box-2', (39, 6), (42, 9), radius_x=3, radius_y=3, sweep=True)
        self.add_line('box-3', (42, 9), (42, 39))
        self.add_arc('box-4', (42, 39), (39, 42), radius_x=3, radius_y=3, sweep=True)
        self.add_line('box-5', (39, 42), (9, 42))
        self.add_arc('box-6', (9, 42), (6, 39), radius_x=3, radius_y=3, sweep=True)
        self.add_line('box-7', (6, 39), (6, 9))
        self.add_arc('box-8', (6, 9), (9, 6), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('box', 'box-1', 'box-2', 'box-3', 'box-4', 'box-5', 'box-6', 'box-7', 'box-8', closed=True)
        self.add_line('vertical', (24, 6), (24, 42))
        self.add_line('horizontal', (24, 24), (42, 24))
        self.relate("connect", 'box', 'vertical')
        self.relate("connect", 'box', 'horizontal')
        self.relate("connect", 'vertical', 'horizontal')
        self.add_line('rice', (15, 27), (15, 32))
        self.add_dot('food-top', (33, 15))
        self.add_dot('food-bottom', (33, 33))
