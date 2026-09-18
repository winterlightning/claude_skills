"""Simple Entrance Door -- batch-002 r2 generation.

Subject: a door leaf set inside its jamb, standing on a floor line, with a
short pull handle near the leaf's right edge.

Plan: the floor line is the base. The jamb is an open three-sided run whose
feet share the floor's ends. The leaf is an inset open three-sided run whose
feet split the floor. The leaf keeps exactly 8 from the jamb on its sides and
top; all of these are straight, so 8 is certifiable. The handle is a short
vertical pull 8 from the leaf's right edge; a 2-unit horizontal dash sat so
close to the axis that the drawing measured 98.2% mirrored and failed the
symmetry diagnostic, whereas the door is deliberately handed.
Keyshape SQUARE; centerline box (6,6)-(42,42).
Reduction: the reference floor line overhangs the jamb slightly. At 48 the
leaf needs the jamb's full width to seat an off-centre handle, so the floor
ends at the jamb feet.
Construction reference: Lucide door-closed (open-bottom leaf on a floor line
with a single handle mark), re-derived on the SOLO48 grid.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._batch_002_r2_shapes import polyline

SOURCE_ICON_ID = '3e6dc1a6-3374-5410-8e37-9141b717983b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/building/architecture door_3e6dc1a6-3374-5410-8e37-9141b717983b.svg'
EXPORTED_REFERENCE = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-002/references/architecture door_3e6dc1a6-3374-5410-8e37-9141b717983b.svg'
AUTHOR = 'claude-opus-5'

LEFT, TOP, RIGHT, FLOOR = 6, 6, 42, 42
INSET = 8
LEAF_LEFT, LEAF_TOP, LEAF_RIGHT = LEFT + INSET, TOP + INSET, RIGHT - INSET
HANDLE_X, HANDLE_TOP, HANDLE_BOTTOM = LEAF_RIGHT - 8, 25, 31


class SimpleEntranceDoorBatch002R2(Solo48):
    icon_id = 'simple-entrance-door-batch-002-r2'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'building/doors'
    aliases = ('door', 'entrance', 'doorway')
    keywords = ('door', 'entrance', 'entry', 'jamb', 'architecture', 'building', 'exit')

    def build(self) -> None:
        leaf_feet = ((LEAF_LEFT, FLOOR), (LEAF_RIGHT, FLOOR))
        polyline(self, 'floor', (LEFT, FLOOR), (RIGHT, FLOOR), nodes=leaf_feet)
        polyline(self, 'jamb', (LEFT, FLOOR), (LEFT, TOP), (RIGHT, TOP), (RIGHT, FLOOR))
        polyline(self, 'leaf', leaf_feet[0], (LEAF_LEFT, LEAF_TOP),
                 (LEAF_RIGHT, LEAF_TOP), leaf_feet[1])
        self.relate('connect', 'floor', 'jamb')
        self.relate('connect', 'floor', 'leaf')
        self.add_line('handle', (HANDLE_X, HANDLE_TOP), (HANDLE_X, HANDLE_BOTTOM))
