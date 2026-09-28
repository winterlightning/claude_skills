"""Outlined Minus: A long horizontal bar has broad rounded corners and an empty interior. Its squat proportions form a single outlined minus without surrounding marks or an enclosing badge.

Construction: Horizontal capsule with semicircular radius6 ends and two tangent rails.
Keyshape: HRECT_S; extremes follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'a6b4ed56-3a81-4fe8-ab46-c2e8af425eff'
SOURCE_PATH = 'pictographic-primitives/state/minus bold_a6b4ed56-3a81-4fe8-ab46-c2e8af425eff.svg'
AUTHOR = 'gpt-6'


class OutlinedMinus(Sub32):
    icon_id = 'outlined-minus'
    keyshape = Keyshape.HRECT_S
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = "state"
    categories = ("state",)
    aliases = ()
    keywords = ('outlined', 'minus', 'long', 'horizontal', 'bar', 'broad', 'rounded', 'corners')

    def build(self):
        self.add_line("top",(8,10),(24,10))
        self.add_arc("right",(24,10),(24,22),radius_x=6)
        self.add_line("bottom",(24,22),(8,22))
        self.add_arc("left",(8,22),(8,10),radius_x=6)
        self.add_contour("outline","top","right","bottom","left",closed=True)
