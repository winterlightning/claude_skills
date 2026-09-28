"""French Door Refrigerator.

SOLO48 visible bounds: (6, 2, 42, 46). Centerline extremes: (8, 4, 40, 44).

Symbol plan: Two upper doors and one freezer drawer; mirrored cabinet.
Reduction: Remove narrow handles and feet; door divisions retain French-door identity.
Construction reference: No useful local Lucide subject match; supplied reference governs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '662158d5-3fa3-4e39-af73-91291a6d8e84'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/food/fridge double door_662158d5-3fa3-4e39-af73-91291a6d8e84.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/fridge double door_662158d5-3fa3-4e39-af73-91291a6d8e84.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-011/references/fridge double door_662158d5-3fa3-4e39-af73-91291a6d8e84.svg'
AUTHOR = "gpt-6"
BATCH_AUTHORING_RUN = "20260917-011-015"


class GeneratedSolo(Solo48):
    icon_id = 'french-door-refrigerator-batch-011-09'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    categories = ("primitives", "food")
    aliases = ()
    keywords = ('refrigerator', 'fridge', 'freezer', 'doors', 'kitchen', 'appliance')

    def build(self):
        self.add_line('cabinet-1', (12, 4), (36, 4))
        self.add_arc('cabinet-2', (36, 4), (40, 8), radius_x=4, radius_y=4, sweep=True)
        self.add_line('cabinet-3', (40, 8), (40, 40))
        self.add_arc('cabinet-4', (40, 40), (36, 44), radius_x=4, radius_y=4, sweep=True)
        self.add_line('cabinet-5', (36, 44), (12, 44))
        self.add_arc('cabinet-6', (12, 44), (8, 40), radius_x=4, radius_y=4, sweep=True)
        self.add_line('cabinet-7', (8, 40), (8, 8))
        self.add_arc('cabinet-8', (8, 8), (12, 4), radius_x=4, radius_y=4, sweep=True)
        self.add_contour('cabinet', 'cabinet-1', 'cabinet-2', 'cabinet-3', 'cabinet-4', 'cabinet-5', 'cabinet-6', 'cabinet-7', 'cabinet-8', closed=True)
        self.add_line('door-divider', (24, 4), (24, 28))
        self.add_line('freezer-top', (8, 28), (40, 28))
        self.relate("connect", 'cabinet', 'door-divider')
        self.relate("connect", 'cabinet', 'freezer-top')
        self.relate("connect", 'door-divider', 'freezer-top')
