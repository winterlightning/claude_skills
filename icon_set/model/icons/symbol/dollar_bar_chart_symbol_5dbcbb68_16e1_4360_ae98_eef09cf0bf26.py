"""Finance: a dollar sign (the approved $ construction, half width) beside two rising chart bars.

SYMBOL32 content symbol for a container combination; letters and digits are the official letter set
(Letters/official) grid-hinted to an even height with typeface_hinting, knots on whole units.
"""

from ...keyshapes import Keyshape
from ._base import Symbol32

SOURCE_ICON_ID = '5dbcbb68-16e1-4360-ae98-eef09cf0bf26'
SOURCE_PATH = 'published/gallery/combination-originals/5dbcbb68-16e1-4360-ae98-eef09cf0bf26.svg'
AUTHOR = 'claude-opus-5-5'


class DollarBarChartSymbol(Symbol32):
    icon_id = 'dollar-bar-chart-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ('financial chart',)
    keywords = ('dollar', 'chart', 'finance')

    def build(self) -> None:
        self.add_bezier('s', (14, 9), ((13, 7), (11, 6), (8, 6)), ((5, 6), (2, 7), (2, 10)), ((2, 13), (5, 14), (8, 15)),
                        ((11, 16), (14, 17), (14, 20)), ((14, 23), (11, 24), (8, 24)), ((5, 24), (3, 23), (2, 21)))
        self.add_line('bar', (8, 2), (8, 28))
        self.relate('connect', 's', 'bar')
        self.add_line('bar-low', (22, 30), (22, 20))
        self.add_line('bar-high', (30, 30), (30, 10))
