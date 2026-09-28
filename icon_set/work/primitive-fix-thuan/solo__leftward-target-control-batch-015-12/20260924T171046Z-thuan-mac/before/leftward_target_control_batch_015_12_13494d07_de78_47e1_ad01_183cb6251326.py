"""Left Target Direction Arrow.

SOLO48 visible bounds: (2, 6, 46, 42). Centerline extremes: (4, 8, 44, 40).

Symbol plan: Large target circle with left node and central left arrow.
Reduction: Open larger circle at node; keep intrinsic control diagram.
Construction reference: No useful local Lucide subject match; supplied reference governs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '13494d07-de78-47e1-ad01-183cb6251326'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/interface-essential/cursor move target left_13494d07-de78-47e1-ad01-183cb6251326.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/cursor move target left_13494d07-de78-47e1-ad01-183cb6251326.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-015/references/cursor move target left_13494d07-de78-47e1-ad01-183cb6251326.svg'
AUTHOR = "gpt-6"
BATCH_AUTHORING_RUN = "20260917-011-015"


class GeneratedSolo(Solo48):
    icon_id = 'leftward-target-control-batch-015-12'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/batch-subjects"
    aliases = ()
    keywords = ('target', 'left', 'arrow', 'circles', 'control', 'direction')

    def build(self):
        self.add_bezier('target-1', (10, 18), ((16, 8), (23, 8), (28, 8)))
        self.add_arc('target-2', (28, 8), (44, 24), radius_x=16, radius_y=16, sweep=True)
        self.add_arc('target-3', (44, 24), (28, 40), radius_x=16, radius_y=16, sweep=True)
        self.add_bezier('target-4', (28, 40), ((23, 40), (16, 40), (10, 30)))
        self.add_contour('target', 'target-1', 'target-2', 'target-3', 'target-4', closed=False)
        self.add_arc('node-1', (10, 18), (16, 24), radius_x=6, radius_y=6, sweep=True)
        self.add_arc('node-2', (16, 24), (10, 30), radius_x=6, radius_y=6, sweep=True)
        self.add_arc('node-3', (10, 30), (4, 24), radius_x=6, radius_y=6, sweep=True)
        self.add_arc('node-4', (4, 24), (10, 18), radius_x=6, radius_y=6, sweep=True)
        self.add_contour('node', 'node-1', 'node-2', 'node-3', 'node-4', closed=True)
        self.relate("connect", 'target', 'node')
        self.add_polyline('arrow', (30, 18), (24, 24), (30, 30), closed=False)
        self.add_line('shaft', (24, 24), (34, 24))
        self.relate("connect", 'arrow', 'shaft')
