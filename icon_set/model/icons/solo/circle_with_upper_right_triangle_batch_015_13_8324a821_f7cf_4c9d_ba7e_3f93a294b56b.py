"""Male Mars Gender Symbol.

SOLO48 visible bounds: (4, 4, 44, 44). Centerline extremes: (6, 6, 42, 42).

Symbol plan: Empty circle below-left of an outlined upper-right pointer.
Reduction: Keep detached triangle seen in reference; do not invent a Mars shaft.
Construction reference: No useful local Lucide subject match; supplied reference governs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8324a821-f7cf-4c9d-ba7e-3f93a294b56b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/interface-essential/cursor information_8324a821-f7cf-4c9d-ba7e-3f93a294b56b.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/cursor information_8324a821-f7cf-4c9d-ba7e-3f93a294b56b.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-015/references/cursor information_8324a821-f7cf-4c9d-ba7e-3f93a294b56b.svg'
AUTHOR = "gpt-6"
BATCH_AUTHORING_RUN = "20260917-011-015"


class GeneratedSolo(Solo48):
    icon_id = 'circle-with-upper-right-triangle-batch-015-13'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    categories = ("interface-essential", "primitives")
    aliases = ()
    keywords = ('circle', 'triangle', 'pointer', 'direction', 'geometric', 'symbol')

    def build(self):
        self.add_arc('circle-1', (19, 16), (32, 29), radius_x=13, radius_y=13, sweep=True)
        self.add_arc('circle-2', (32, 29), (19, 42), radius_x=13, radius_y=13, sweep=True)
        self.add_arc('circle-3', (19, 42), (6, 29), radius_x=13, radius_y=13, sweep=True)
        self.add_arc('circle-4', (6, 29), (19, 16), radius_x=13, radius_y=13, sweep=True)
        self.add_contour('circle', 'circle-1', 'circle-2', 'circle-3', 'circle-4', closed=True)
        self.add_polyline('pointer', (30, 6), (42, 6), (42, 18), closed=True)
