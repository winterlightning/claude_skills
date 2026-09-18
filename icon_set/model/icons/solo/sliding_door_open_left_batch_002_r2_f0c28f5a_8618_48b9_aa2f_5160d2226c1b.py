"""Sliding Door Open Left -- batch-002 r2 generation.

Subject: a sliding door whose panel has slid right, leaving an open passage
on the left of the frame.

Plan: one open frame run starts at the free foot of the left jamb, climbs to a
square top-left corner, crosses the top, turns the rounded right corners and
returns along the floor only as far as the panel's left edge, leaving the
passage open at the bottom left. The slid panel is bounded by two
full-height edges sharing split nodes with the top and floor. The fixed strip
to its right is exactly 8 wide (straight edges). The handle sits near the
panel's leading edge, exactly 8 from it.
Keyshape SQUARE; centerline box (6,6)-(42,42).
Reduction: none; open passage, slid panel, fixed strip and handle are kept.
Construction reference: Lucide door-open (an open frame run beside the moved
leaf), re-derived on the SOLO48 grid.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._batch_002_r2_shapes import path

SOURCE_ICON_ID = 'f0c28f5a-8618-48b9-aa2f-5160d2226c1b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/building/door sliding left hand open_f0c28f5a-8618-48b9-aa2f-5160d2226c1b.svg'
EXPORTED_REFERENCE = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-002/references/door sliding left hand open_f0c28f5a-8618-48b9-aa2f-5160d2226c1b.svg'
AUTHOR = 'claude-opus-5'

LEFT, TOP, RIGHT, FLOOR, RADIUS = 6, 6, 42, 42, 4
PANEL_LEFT, PANEL_RIGHT = 16, RIGHT - 8
HANDLE_X, HANDLE_TOP, HANDLE_BOTTOM = PANEL_LEFT + 8, 21, 27


class SlidingDoorOpenLeftBatch002R2(Solo48):
    icon_id = 'sliding-door-open-left-batch-002-r2'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'building/doors'
    aliases = ('sliding-door-left-open',)
    keywords = ('door', 'sliding', 'open', 'left', 'passage', 'entrance', 'building')

    def build(self) -> None:
        path(self, 'frame', (LEFT, FLOOR),
             ('L', (LEFT, TOP)),
             ('L', (PANEL_LEFT, TOP)),
             ('L', (PANEL_RIGHT, TOP)),
             ('L', (RIGHT - RADIUS, TOP)),
             ('A', (RIGHT, TOP + RADIUS), RADIUS, RADIUS, True),
             ('L', (RIGHT, FLOOR - RADIUS)),
             ('A', (RIGHT - RADIUS, FLOOR), RADIUS, RADIUS, True),
             ('L', (PANEL_RIGHT, FLOOR)),
             ('L', (PANEL_LEFT, FLOOR)))
        self.add_line('panel-left-edge', (PANEL_LEFT, TOP), (PANEL_LEFT, FLOOR))
        self.add_line('panel-right-edge', (PANEL_RIGHT, TOP), (PANEL_RIGHT, FLOOR))
        self.relate('connect', 'frame', 'panel-left-edge')
        self.relate('connect', 'frame', 'panel-right-edge')
        self.add_line('handle', (HANDLE_X, HANDLE_TOP), (HANDLE_X, HANDLE_BOTTOM))
