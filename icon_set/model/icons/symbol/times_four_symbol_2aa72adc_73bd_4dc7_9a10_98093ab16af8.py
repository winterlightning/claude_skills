"""Times four: a small multiplication cross beside a full-height digit 4.

SYMBOL32 content symbol for a container combination; letters and digits are the official letter set
(Letters/official) grid-hinted to an even height with typeface_hinting, knots on whole units.
"""

from ...keyshapes import Keyshape
from ._base import Symbol32

SOURCE_ICON_ID = '2aa72adc-73bd-4dc7-9a10-98093ab16af8'
SOURCE_PATH = 'published/gallery/combination-originals/2aa72adc-73bd-4dc7-9a10-98093ab16af8.svg'
AUTHOR = 'claude-opus-5-5'


class TimesFourSymbol(Symbol32):
    icon_id = 'times-four-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ('x4',)
    keywords = ('times', 'four', 'multiply')

    def build(self) -> None:
        self.add_line('times-a', (2, 12), (10, 20))
        self.add_line('times-b', (10, 12), (2, 20))
        self.relate('connect', 'times-a', 'times-b')
        self.add_line('four-0-0-0', (30, 2), (30, 30))
        self.add_line('four-0-0-1', (30, 21), (17, 21))
        self.add_bezier('four-0-0-2', (17, 21), ((16.31, 21), (16, 20.67), (16, 20)))
        self.add_line('four-0-0-3', (16, 20), (16, 2))
        self.add_contour('four-0-0', 'four-0-0-1', 'four-0-0-2', 'four-0-0-3')
