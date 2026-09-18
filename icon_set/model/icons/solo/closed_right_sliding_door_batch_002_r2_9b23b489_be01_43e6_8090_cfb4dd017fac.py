"""Closed Right Sliding Door -- batch-002 r2 generation.

Subject: a closed two-panel sliding door whose handle sits on the right panel.

Plan: one rounded-square frame (radius 4) owns a full-height centre divider
that shares split nodes with the top and bottom edges. The handle is a short
vertical pull in the right panel, mirrored from the left-hand variant about
the divider. It keeps 9 from the rounded frame and 9 from the divider.
Keyshape SQUARE; centerline box (6,6)-(42,42).
Reduction: the reference handle hugs the right jamb; the 18-wide panel at 48
centres it in the right panel instead.
Construction reference: Lucide door-closed (straight panel edges and one short
handle mark), re-derived on the SOLO48 grid.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._batch_002_r2_shapes import rounded_rect

SOURCE_ICON_ID = '9b23b489-be01-43e6-8090-cfb4dd017fac'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/building/door sliding right hand closed_9b23b489-be01-43e6-8090-cfb4dd017fac.svg'
EXPORTED_REFERENCE = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-002/references/door sliding right hand closed_9b23b489-be01-43e6-8090-cfb4dd017fac.svg'
AUTHOR = 'claude-opus-5'

LEFT, TOP, RIGHT, BOTTOM, RADIUS = 6, 6, 42, 42, 4
DIVIDER_X = (LEFT + RIGHT) // 2
HANDLE_X, HANDLE_TOP, HANDLE_BOTTOM = RIGHT - 9, 21, 27


class ClosedRightSlidingDoorBatch002R2(Solo48):
    icon_id = 'closed-right-sliding-door-batch-002-r2'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'building/doors'
    aliases = ('sliding-door-right-closed',)
    keywords = ('door', 'sliding', 'closed', 'right', 'panel', 'entrance', 'building')

    def build(self) -> None:
        top_node, bottom_node = (DIVIDER_X, TOP), (DIVIDER_X, BOTTOM)
        rounded_rect(self, 'frame', LEFT, TOP, RIGHT, BOTTOM, RADIUS,
                     nodes=(top_node, bottom_node))
        self.add_line('divider', top_node, bottom_node)
        self.relate('connect', 'frame', 'divider')
        self.add_line('handle', (HANDLE_X, HANDLE_TOP), (HANDLE_X, HANDLE_BOTTOM))
