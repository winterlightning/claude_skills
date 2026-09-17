"""Mountain with Wine Jar and Bowl.

SOLO48 visible bounds: (4, 4, 44, 44). Centerline extremes: (6, 6, 42, 42).

Symbol plan: Mountain skyline over squat capped wine jar and bowl.
Reduction: Omit cloud and scalloped band; retain both vessels.
Construction reference: No useful local Lucide subject match; supplied reference governs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8c8ea1c5-e571-4e19-84f5-1beeac5c898d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/holidays/double ninth festival drink_8c8ea1c5-e571-4e19-84f5-1beeac5c898d.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/double ninth festival drink_8c8ea1c5-e571-4e19-84f5-1beeac5c898d.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-014/references/double ninth festival drink_8c8ea1c5-e571-4e19-84f5-1beeac5c898d.svg'
AUTHOR = "gpt-6"
BATCH_AUTHORING_RUN = "20260917-011-015"


class GeneratedSolo(Solo48):
    icon_id = 'mountains-with-wine-jar-and-bowl-batch-014-07'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/batch-subjects"
    aliases = ()
    keywords = ('mountains', 'wine', 'jar', 'bowl', 'cloud', 'festival')

    def build(self):
        self.add_polyline('mountains', (6, 20), (16, 6), (23, 14), (30, 6), (42, 20), closed=False)
        self.add_line('jar-1', (32, 28), (38, 28))
        self.add_arc('jar-2', (38, 28), (42, 32), radius_x=4, radius_y=4, sweep=True)
        self.add_line('jar-3', (42, 32), (42, 38))
        self.add_arc('jar-4', (42, 38), (38, 42), radius_x=4, radius_y=4, sweep=True)
        self.add_line('jar-5', (38, 42), (32, 42))
        self.add_arc('jar-6', (32, 42), (28, 38), radius_x=4, radius_y=4, sweep=True)
        self.add_line('jar-7', (28, 38), (28, 32))
        self.add_arc('jar-8', (28, 32), (32, 28), radius_x=4, radius_y=4, sweep=True)
        self.add_contour('jar', 'jar-1', 'jar-2', 'jar-3', 'jar-4', 'jar-5', 'jar-6', 'jar-7', 'jar-8', closed=True)
        self.add_line('bowl-1', (6, 32), (20, 32))
        self.add_bezier('bowl-2', (20, 32), ((20, 42), (6, 42), (6, 32)))
        self.add_contour('bowl', 'bowl-1', 'bowl-2', closed=True)
