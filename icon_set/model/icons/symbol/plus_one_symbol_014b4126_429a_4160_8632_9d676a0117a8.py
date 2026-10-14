"""Plus one: a plus sign beside a full-height digit 1.

SYMBOL32 content symbol for a container combination; letters and digits are the official letter set
(Letters/official) grid-hinted to an even height with typeface_hinting, knots on whole units.
"""

from ...keyshapes import Keyshape
from ._base import Symbol32

SOURCE_ICON_ID = '014b4126-429a-4160-8632-9d676a0117a8'
SOURCE_PATH = 'published/gallery/combination-originals/014b4126-429a-4160-8632-9d676a0117a8.svg'
AUTHOR = 'claude-opus-5-5'


class PlusOneSymbol(Symbol32):
    icon_id = 'plus-one-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ('+1',)
    keywords = ('plus', 'one', 'add')

    def build(self) -> None:
        self.add_line('plus-h', (2, 16), (16, 16))
        self.add_line('plus-v', (9, 9), (9, 23))
        self.relate('connect', 'plus-h', 'plus-v')
        self.add_line('one-0-0-0', (30, 30), (30, 2))
        self.add_line('one-0-0-1', (30, 2), (22, 8))
        self.add_contour('one-0-0', 'one-0-0-0', 'one-0-0-1')
