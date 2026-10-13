"""The subset-of-or-equal-to sign: an open C (radius 10) with a bar 8 below it.

SYMBOL32 content symbol for a container combination; letters and digits are the official letter set
(Letters/official) grid-hinted to an even height with typeface_hinting, knots on whole units.
"""

from ...keyshapes import Keyshape
from ._base import Symbol32

SOURCE_ICON_ID = 'a83c7456-ab64-437d-9647-fc11cd8bf5f0'
SOURCE_PATH = 'published/gallery/combination-originals/a83c7456-ab64-437d-9647-fc11cd8bf5f0.svg'
AUTHOR = 'claude-opus-5-5'


class SubsetOrEqualSymbol(Symbol32):
    icon_id = 'subset-or-equal-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ('subset or equal',)
    keywords = ('subset', 'math', 'set')

    def build(self) -> None:
        self.add_line('top', (26, 2), (16, 2))
        self.add_arc('bow', (16, 2), (16, 22), radius_x=10, sweep=False)
        self.add_line('bottom', (16, 22), (26, 22))
        self.add_contour('subset', 'top', 'bow', 'bottom')
        self.add_line('equal', (6, 30), (26, 30))
