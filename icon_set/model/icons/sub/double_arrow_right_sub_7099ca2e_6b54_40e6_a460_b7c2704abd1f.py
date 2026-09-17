"""Double Arrow Right: A horizontal shaft ends in a right-pointing open arrowhead, followed by a second detached right chevron. The two heads are aligned across the same horizontal centre.

Construction: Two equal right chevrons share height, separated horizontally; shaft joins only first tip.
Keyshape: HRECT_XL; extremes follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '7099ca2e-6b54-40e6-a460-b7c2704abd1f'
SOURCE_PATH = 'pictographic-primitives/state/double arrow right_7099ca2e-6b54-40e6-a460-b7c2704abd1f.svg'
AUTHOR = 'gpt-6'


class DoubleArrowRightSub(Sub32):
    icon_id = 'double-arrow-right-sub'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = "primitives/mark"
    aliases = ()
    keywords = ('double', 'arrow', 'right', 'horizontal', 'shaft', 'ends', 'pointing', 'open')

    def build(self):
        self.add_polyline("head-inner", (6,4), (18,16), (6,28))
        self.add_polyline("head-outer", (18,4), (30,16), (18,28))
        self.add_line("shaft", (2,16), (18,16))
        self.relate("connect", "shaft", "head-inner")
