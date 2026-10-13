"""Width limit: chevrons pointing in from the left and the right to an upright limit bar (the figure 4M / 2.5M
between them cannot hold the 8-unit stroke spacing at 32 px), the height-limit-2-5-symbol turned a quarter.

SYMBOL32 content symbol for a container combination (the >4M< and >2.5M< width limit road signs).
Plan: one vertical axis x 16; the bar spans the full centreline height (2..30); each chevron is 12 tall and
6 deep with its tip 8 from the bar (4 units of white), mirrored about x 16.
"""

from ...keyshapes import Keyshape
from ._base import Symbol32

SOURCE_ICON_ID = 'f92f1287-4d1f-4f11-b3d2-cf575c8bb3ec'
SOURCE_PATH = 'published/gallery/combination-originals/650f0f39-0037-444b-b3d2-cf575c8bb3ec.svg'
AUTHOR = 'claude-opus-5-5'


class WidthLimitSymbol(Symbol32):
    icon_id = 'width-limit-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ('4m-width', '2.5m-width', 'maximum-width')
    keywords = ('width', 'limit', 'road sign', 'maximum width')

    def build(self) -> None:
        self.add_polyline('arrow-left', (2, 10), (8, 16), (2, 22))
        self.add_line('limit', (16, 2), (16, 30))
        self.add_polyline('arrow-right', (30, 10), (24, 16), (30, 22))
