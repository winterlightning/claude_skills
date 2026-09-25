"""Kitchen Electric Food Blender.

SOLO48 visible bounds: (6, 2, 42, 46). Centerline extremes: (8, 4, 40, 44).

Symbol plan: Tapered pitcher and flared motor base with central control.
Reduction: Keep lid, pitcher, base; omit fine controls.
Construction reference: No useful local Lucide subject match; supplied reference governs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fb951df2-e59c-4e70-b69e-b608b6dc62a0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/food/blender_fb951df2-e59c-4e70-b69e-b608b6dc62a0.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/blender_fb951df2-e59c-4e70-b69e-b608b6dc62a0.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-012/references/blender_fb951df2-e59c-4e70-b69e-b608b6dc62a0.svg'
AUTHOR = "gpt-6"
BATCH_AUTHORING_RUN = "20260917-011-015"


class GeneratedSolo(Solo48):
    icon_id = 'countertop-blender-batch-012-05'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    aliases = ()
    keywords = ('blender', 'jug', 'appliance', 'kitchen', 'motor', 'mixer')

    def build(self):
        self.add_polyline('pitcher', (8, 4), (40, 4), (34, 28), (14, 28), closed=True)
        self.add_polyline('base', (14, 28), (8, 44), (40, 44), (34, 28), closed=False)
        self.relate("connect", 'pitcher', 'base')
        self.add_dot('control', (24, 36))
