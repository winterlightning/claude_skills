"""Two equal rounded squares, the front one upper-left, the one behind showing only its visible L.

Symbol plan: one square definition (side 24, radius 4) repeated at offset (12, 12); the back
square's hidden part is omitted and its visible run starts and ends on the front square's walls.
Keyshape: SQUARE.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1717ecdd-379e-4519-aa6b-956d4d7ebc04'
SOURCE_PATH = 'pictographic-primitives/interface-essential/duplicate_1717ecdd-379e-4519-aa6b-956d4d7ebc04.svg'
AUTHOR = 'claude-opus-5-5'

SIDE, RAD, STEP = 24, 4, 12
FL, FT = 6, 6
FR, FB = FL + SIDE, FT + SIDE
BL, BT = FL + STEP, FT + STEP
BR, BB = BL + SIDE, BT + SIDE


class Drawing(Solo48):
    icon_id = 'overlapping-rounded-squares'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives-generate')
    aliases = ('duplicate', 'copy')
    keywords = ('duplicate', 'copy', 'overlap', 'squares', 'layers')

    def build(self):
        # Front square; its right and bottom walls are split where the back square meets them.
        self.add_line('front-top', (FL + RAD, FT), (FR - RAD, FT))
        self.add_arc('front-tr', (FR - RAD, FT), (FR, FT + RAD), radius_x=RAD)
        self.add_line('front-right-a', (FR, FT + RAD), (FR, BT))
        self.add_line('front-right-b', (FR, BT), (FR, FB - RAD))
        self.add_arc('front-br', (FR, FB - RAD), (FR - RAD, FB), radius_x=RAD)
        self.add_line('front-bottom-a', (FR - RAD, FB), (BL, FB))
        self.add_line('front-bottom-b', (BL, FB), (FL + RAD, FB))
        self.add_arc('front-bl', (FL + RAD, FB), (FL, FB - RAD), radius_x=RAD)
        self.add_line('front-left', (FL, FB - RAD), (FL, FT + RAD))
        self.add_arc('front-tl', (FL, FT + RAD), (FL + RAD, FT), radius_x=RAD)
        self.add_contour('front', 'front-top', 'front-tr', 'front-right-a', 'front-right-b', 'front-br',
                         'front-bottom-a', 'front-bottom-b', 'front-bl', 'front-left', 'front-tl', closed=True)
        # Back square: only the part not covered by the front square.
        self.add_line('back-top', (FR, BT), (BR - RAD, BT))
        self.add_arc('back-tr', (BR - RAD, BT), (BR, BT + RAD), radius_x=RAD)
        self.add_line('back-right', (BR, BT + RAD), (BR, BB - RAD))
        self.add_arc('back-br', (BR, BB - RAD), (BR - RAD, BB), radius_x=RAD)
        self.add_line('back-bottom', (BR - RAD, BB), (BL + RAD, BB))
        self.add_arc('back-bl', (BL + RAD, BB), (BL, BB - RAD), radius_x=RAD)
        self.add_line('back-left', (BL, BB - RAD), (BL, FB))
        self.add_contour('back', 'back-top', 'back-tr', 'back-right', 'back-br', 'back-bottom', 'back-bl', 'back-left')
        self.relate('connect', 'back-top', 'front-right-a', 'front-right-b')
        self.relate('connect', 'back-left', 'front-bottom-a', 'front-bottom-b')
