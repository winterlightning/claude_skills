"""Double Pane Window -- batch-002 r2 generation.

Subject: a square window of two panes split by a central mullion, with a
latch on the left pane beside the mullion.

Plan: one square-cornered frame (the reference has sharp corners) owns the
full-height mullion through split nodes on the top and bottom edges. The latch
is a short vertical mark exactly 8 from the straight mullion, so it reads as
sitting against the meeting rail rather than floating mid-pane.
Keyshape SQUARE; centerline box (6,6)-(42,42).
Reduction: none; frame, mullion and latch are all kept.
Construction reference: Lucide app-window (outer frame with one internal
divider), re-derived on the SOLO48 grid with square corners.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._batch_002_r2_shapes import rounded_rect

SOURCE_ICON_ID = '4ffa6c0d-9134-5a35-a135-73fe4d06cbe2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/building/window open_4ffa6c0d-9134-5a35-a135-73fe4d06cbe2.svg'
EXPORTED_REFERENCE = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-002/references/window open_4ffa6c0d-9134-5a35-a135-73fe4d06cbe2.svg'
AUTHOR = 'claude-opus-5'

LEFT, TOP, RIGHT, BOTTOM = 6, 6, 42, 42
MULLION_X = (LEFT + RIGHT) // 2
LATCH_X, LATCH_TOP, LATCH_BOTTOM = MULLION_X - 8, 21, 27


class DoublePaneWindowBatch002R2(Solo48):
    icon_id = 'double-pane-window-batch-002-r2'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'building/windows'
    aliases = ('window', 'casement-window', 'two-pane-window')
    keywords = ('window', 'pane', 'glass', 'mullion', 'latch', 'building', 'open')

    def build(self) -> None:
        top_node, bottom_node = (MULLION_X, TOP), (MULLION_X, BOTTOM)
        rounded_rect(self, 'frame', LEFT, TOP, RIGHT, BOTTOM, 0,
                     nodes=(top_node, bottom_node))
        self.add_line('mullion', top_node, bottom_node)
        self.relate('connect', 'frame', 'mullion')
        self.add_line('latch', (LATCH_X, LATCH_TOP), (LATCH_X, LATCH_BOTTOM))
