"""Height limit: chevrons pointing in from above and below to a limit bar (the figure 2.5 cannot hold the 8-unit stroke spacing at 32 px).

SYMBOL32 content symbol for a container combination; letters and digits are the official letter set
(Letters/official) grid-hinted to an even height with typeface_hinting, knots on whole units.
"""

from ...keyshapes import Keyshape
from ._base import Symbol32

SOURCE_ICON_ID = '38ba2a2e-533c-4f13-8799-64c05185a0e7'
SOURCE_PATH = 'published/gallery/combination-originals/38ba2a2e-533c-4f13-8799-64c05185a0e7.svg'
AUTHOR = 'claude-opus-5-5'


class HeightLimit25Symbol(Symbol32):
    icon_id = 'height-limit-2-5-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ('2.5m', 'clearance')
    keywords = ('height', 'limit', 'clearance')

    def build(self) -> None:
        self.add_polyline('arrow-top', (8, 2), (16, 10), (24, 2))
        self.add_line('limit', (2, 16), (30, 16))
        self.add_polyline('arrow-bottom', (8, 30), (16, 22), (24, 30))
