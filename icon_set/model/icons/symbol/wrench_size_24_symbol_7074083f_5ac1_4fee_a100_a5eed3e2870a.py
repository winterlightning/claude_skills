"""Wrench size 24: the number 24 (height 18) over a double open-end wrench.

SYMBOL32 content symbol for a container combination; letters and digits are the official letter set
(Letters/official) grid-hinted to an even height with typeface_hinting, knots on whole units.
"""

from ...keyshapes import Keyshape
from ._base import Symbol32

SOURCE_ICON_ID = '7074083f-5ac1-4fee-a100-a5eed3e2870a'
SOURCE_PATH = 'published/gallery/combination-originals/7074083f-5ac1-4fee-a100-a5eed3e2870a.svg'
AUTHOR = 'claude-opus-5-5'


class WrenchSize24Symbol(Symbol32):
    icon_id = 'wrench-size-24-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ('24 wrench',)
    keywords = ('wrench', 'size', 'service')

    def build(self) -> None:
        # Size 24 from the official typeface (grid-hinted v2) above an open-ended wrench.
        self.add_bezier('size-0-0-0', (4, 6), ((4, 3.79), (5.79, 2), (8, 2)), ((10.21, 2), (12, 3.79), (12, 6)), ((12, 7), (11.55, 7.91), (11, 9)))
        self.add_line('size-0-0-1', (11, 9), (4, 16))
        self.add_line('size-0-0-2', (4, 16), (12, 16))
        self.add_contour('size-0-0', 'size-0-0-0', 'size-0-0-1', 'size-0-0-2')
        self.add_line('size-1-0-0', (28, 2), (28, 16))
        self.add_line('size-1-0-1', (28, 11), (20, 11))
        self.add_line('size-1-0-3', (20, 11), (20, 2))
        self.add_contour('size-1-0', 'size-1-0-1', 'size-1-0-3')
        self.add_arc('jaw-left', (2, 24), (2, 30), radius_x=3)
        self.add_line('handle', (5, 27), (27, 27))
        self.add_arc('jaw-right', (30, 30), (30, 24), radius_x=3)
        self.relate('connect', 'jaw-left', 'handle')
        self.relate('connect', 'jaw-right', 'handle')
