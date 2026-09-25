"""Outlined Arrow Down: A broad downward arrow has a tall rectangular shaft and a wide triangular head. The outline encloses an empty interior, with matching horizontal shoulders on both sides.

Construction: Closed down arrow, mirrored about x16; broad shaft and shoulders share exact corners.
Keyshape: VRECT_XL; extremes follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '58727bf7-a897-4f91-b5c6-d02dbeb80019'
SOURCE_PATH = 'pictographic-primitives/state/down arrow_58727bf7-a897-4f91-b5c6-d02dbeb80019.svg'
AUTHOR = 'gpt-6'


class OutlinedArrowDown(Sub32):
    icon_id = 'outlined-arrow-down'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = "state"
    aliases = ()
    keywords = ('outlined', 'arrow', 'down', 'broad', 'downward', 'tall', 'rectangular', 'shaft')

    def build(self):
        self.add_polyline("outline", (10,2),(22,2),(22,18),(28,18),(16,30),(4,18),(10,18),closed=True)
