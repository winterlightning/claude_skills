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
        self.add_bezier('size-0-0-0', (5, 6), ((5, 3.79), (6.79, 2), (9, 2)), ((11.21, 2), (13, 3.79), (13, 6)), ((13, 7), (12.55, 7.91), (12, 9)))
        self.add_line('size-0-0-1', (12, 9), (5, 16))
        self.add_line('size-0-0-2', (5, 16), (13, 16))
        self.add_contour('size-0-0', 'size-0-0-0', 'size-0-0-1', 'size-0-0-2')
        self.add_line('size-1-0-0', (27, 2), (27, 16))
        self.add_line('size-1-0-1', (27, 11), (19, 11))
        self.add_line('size-1-0-3', (19, 11), (19, 2))
        self.add_contour('size-1-0', 'size-1-0-1', 'size-1-0-3')
        self.add_arc('jaw-left', (2, 22), (2, 30), radius_x=4)
        self.add_line('handle', (6, 26), (26, 26))
        self.add_arc('jaw-right', (30, 30), (30, 22), radius_x=4)
        self.relate('connect', 'jaw-left', 'handle')
        self.relate('connect', 'jaw-right', 'handle')
