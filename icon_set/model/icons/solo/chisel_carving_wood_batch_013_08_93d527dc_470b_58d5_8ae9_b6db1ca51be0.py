"""Chisel Carving Wood Surface.

SOLO48 visible bounds: (4, 4, 44, 44). Centerline extremes: (6, 6, 42, 42).

Symbol plan: Diagonal chisel above a carved wood surface with one grain contour.
Reduction: Single tool outline and broad carved dip replace tiny shaft steps.
Construction reference: No useful local Lucide subject match; supplied reference governs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '93d527dc-470b-58d5-8ae9-b6db1ca51be0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/hobbies/wood carving_93d527dc-470b-58d5-8ae9-b6db1ca51be0.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/hobbies/wood carving_93d527dc-470b-58d5-8ae9-b6db1ca51be0.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-013/references/wood carving_93d527dc-470b-58d5-8ae9-b6db1ca51be0.svg'
AUTHOR = "gpt-6"
BATCH_AUTHORING_RUN = "20260917-011-015"


class GeneratedSolo(Solo48):
    icon_id = 'chisel-carving-wood-batch-013-08'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/batch-subjects"
    aliases = ()
    keywords = ('chisel', 'wood', 'carving', 'blade', 'craft', 'tool')

    def build(self):
        self.add_polyline('tool', (24, 8), (34, 6), (42, 14), (22, 32), (14, 26), closed=True)
        self.add_line('wood-1', (6, 38), (12, 38))
        self.add_bezier('wood-2', (12, 38), ((18, 38), (18, 42), (26, 42)))
        self.add_bezier('wood-3', (26, 42), ((32, 42), (32, 38), (42, 38)))
        self.add_contour('wood', 'wood-1', 'wood-2', 'wood-3', closed=False)
