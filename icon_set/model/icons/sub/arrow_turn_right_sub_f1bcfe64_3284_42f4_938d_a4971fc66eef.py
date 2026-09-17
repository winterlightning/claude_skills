"""Arrow Turn Right: An arrow rises vertically from the lower left, turns through a rounded corner, and continues horizontally right. Its tip ends in an open, symmetrical right-facing arrowhead.

Construction: One tangent quarter-circle elbow connects upright and horizontal runs; right head shares tip.
Keyshape: SQUARE; extremes follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'f1bcfe64-3284-42f4-938d-a4971fc66eef'
SOURCE_PATH = 'pictographic-primitives/state/arrow turn right_f1bcfe64-3284-42f4-938d-a4971fc66eef.svg'
AUTHOR = 'gpt-6'


class ArrowTurnRightSub(Sub32):
    icon_id = 'arrow-turn-right-sub'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = "primitives/mark"
    aliases = ()
    keywords = ('arrow', 'turn', 'right', 'rises', 'vertically', 'lower', 'left', 'turns')

    def build(self):
        self.add_line("upright", (2,30), (2,18))
        self.add_arc("elbow", (2,18), (10,10), radius_x=8)
        self.add_line("run", (10,10), (30,10))
        self.add_contour("shaft", "upright", "elbow", "run")
        self.add_polyline("head", (22,2), (30,10), (22,18))
        self.relate("connect", "shaft", "head")
