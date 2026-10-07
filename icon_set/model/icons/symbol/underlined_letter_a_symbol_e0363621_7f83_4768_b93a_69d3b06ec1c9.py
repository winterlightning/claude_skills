"""Text formatting: the letter A over an underline.

SYMBOL32 content symbol for a container combination; letters and digits are the official letter set
(Letters/official) grid-hinted to an even height with typeface_hinting, knots on whole units.
"""

from ...keyshapes import Keyshape
from ._base import Symbol32

SOURCE_ICON_ID = 'e0363621-7f83-4768-b93a-69d3b06ec1c9'
SOURCE_PATH = 'published/gallery/combination-originals/e0363621-7f83-4768-b93a-69d3b06ec1c9.svg'
AUTHOR = 'claude-opus-5-5'


class UnderlinedLetterASymbol(Symbol32):
    icon_id = 'underlined-letter-a-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ('underline',)
    keywords = ('text', 'format', 'underline')

    def build(self) -> None:
        self.add_line('letter-0-0-0', (9, 22), (9, 8))
        self.add_bezier('letter-0-0-1', (9, 8), ((9, 4.91), (12.14, 2), (16, 2)), ((19.86, 2), (23, 4.91), (23, 8)))
        self.add_line('letter-0-0-2', (23, 8), (23, 22))
        self.add_contour('letter-0-0', 'letter-0-0-0', 'letter-0-0-1', 'letter-0-0-2')
        self.add_line('letter-0-1-0', (9, 15), (23, 15))
        self.add_line('underline', (6, 30), (26, 30))
