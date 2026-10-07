"""The expression 2 - 1: digits at height 16 around a minus sign.

SYMBOL32 content symbol for a container combination; letters and digits are the official letter set
(Letters/official) grid-hinted to an even height with typeface_hinting, knots on whole units.
"""

from ...keyshapes import Keyshape
from ._base import Symbol32

SOURCE_ICON_ID = '17d5ec75-09d3-4664-bd59-09488d4395a3'
SOURCE_PATH = 'published/gallery/combination-originals/17d5ec75-09d3-4664-bd59-09488d4395a3.svg'
AUTHOR = 'claude-opus-5-5'


class TwoMinusOneSymbol(Symbol32):
    icon_id = 'two-minus-one-symbol'
    keyshape = Keyshape.HRECT_S
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ('2-1',)
    keywords = ('math', 'subtract', 'expression')

    def build(self) -> None:
        self.add_bezier('two-0-0-0', (2, 13), ((2, 11.34), (3.34, 10), (5, 10)), ((6.66, 10), (8, 11.34), (8, 13)), ((8, 13.9), (7.66, 14.72), (7, 15)))
        self.add_line('two-0-0-1', (7, 15), (2, 22))
        self.add_line('two-0-0-2', (2, 22), (8, 22))
        self.add_contour('two-0-0', 'two-0-0-0', 'two-0-0-1', 'two-0-0-2')
        self.add_line('minus', (14, 16), (20, 16))
        self.add_line('one-0-0-0', (30, 22), (30, 10))
        self.add_line('one-0-0-1', (30, 10), (26, 12))
        self.add_contour('one-0-0', 'one-0-0-0', 'one-0-0-1')
