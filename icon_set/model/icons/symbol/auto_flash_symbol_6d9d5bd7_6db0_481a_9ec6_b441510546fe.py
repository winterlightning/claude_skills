"""Automatic camera flash: an open zigzag lightning bolt with the letter A.

SYMBOL32 content symbol for a container combination; letters and digits are the official letter set
(Letters/official) grid-hinted to an even height with typeface_hinting, knots on whole units.
"""

from ...keyshapes import Keyshape
from ._base import Symbol32

SOURCE_ICON_ID = '6d9d5bd7-6db0-481a-9ec6-b441510546fe'
SOURCE_PATH = 'published/gallery/combination-originals/6d9d5bd7-6db0-481a-9ec6-b441510546fe.svg'
AUTHOR = 'claude-opus-5-5'


class AutoFlashSymbol(Symbol32):
    icon_id = 'auto-flash-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ('auto flash',)
    keywords = ('flash', 'auto', 'camera')

    def build(self) -> None:
        self.add_polyline('bolt', (10, 2), (2, 16), (13, 14), (4, 30))
        self.add_line('letter-0-0-0', (22, 28), (22, 20))
        self.add_bezier('letter-0-0-1', (22, 20), ((22, 17.79), (23.79, 16), (26, 16)), ((28.21, 16), (30, 17.79), (30, 20)))
        self.add_line('letter-0-0-2', (30, 20), (30, 28))
        self.add_contour('letter-0-0', 'letter-0-0-0', 'letter-0-0-1', 'letter-0-0-2')
        self.add_line('letter-0-1-0', (22, 24), (30, 24))
