"""Traditional Japanese Harvest Festival Sculpture.

SOLO48 visible bounds: (4, 4, 44, 44). Centerline extremes: (6, 6, 42, 42).

Symbol plan: Roofed upright ceremonial sculpture with lateral projections and base.
Reduction: Remove tiny central curve; preserve asymmetrical projecting form.
Construction reference: No useful local Lucide subject match; supplied reference governs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5ae5723c-3e4b-4cec-9859-179ce6bc8ccd'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/holidays/honensai_5ae5723c-3e4b-4cec-9859-179ce6bc8ccd.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/honensai_5ae5723c-3e4b-4cec-9859-179ce6bc8ccd.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-014/references/honensai_5ae5723c-3e4b-4cec-9859-179ce6bc8ccd.svg'
AUTHOR = "gpt-6"
BATCH_AUTHORING_RUN = "20260917-011-015"


class GeneratedSolo(Solo48):
    icon_id = 'roofed-honensai-festival-sculpture-batch-014-12'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/batch-subjects"
    aliases = ()
    keywords = ('honensai', 'festival', 'sculpture', 'roof', 'base', 'ceremony')

    def build(self):
        self.add_polyline('roof', (10, 16), (24, 6), (38, 16), closed=True)
        self.add_polyline('stand', (16, 16), (16, 42), (32, 42), (32, 16), closed=False)
        self.relate("connect", 'roof', 'stand')
        self.add_line('base-left', (6, 42), (16, 42))
        self.add_line('base-right', (32, 42), (42, 42))
        self.relate("connect", 'stand', 'base-left')
        self.relate("connect", 'stand', 'base-right')
        self.add_line('left-projection-1', (16, 24), (10, 24))
        self.add_arc('left-projection-2', (10, 24), (10, 32), radius_x=4, radius_y=4, sweep=False)
        self.add_line('left-projection-3', (10, 32), (16, 32))
        self.add_contour('left-projection', 'left-projection-1', 'left-projection-2', 'left-projection-3', closed=False)
        self.add_polyline('right-projection', (32, 24), (42, 24), (42, 32), (32, 32), closed=False)
        self.relate("connect", 'stand', 'left-projection')
        self.relate("connect", 'stand', 'right-projection')
