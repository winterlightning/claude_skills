"""Left Right Arrow. Retains all identifying parts, reconstructed on the integer grid.

HRECT_L visible extremes (2, 6, 46, 42); centerlines (4, 8, 44, 40).
Lucide rotate-cw and undo-2: coherent arcs, open arrowheads and explicit shaft joins.
Mirrored subjects use paired coordinates; directional parts preserve their
intentional asymmetry. Geometry is authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '67bf7fb1-ed00-461a-9eb2-9b3fb1ab73b4'
SOURCE_PATH = 'pictographic-primitives/symbol/arrows left right_67bf7fb1-ed00-461a-9eb2-9b3fb1ab73b4.svg'
AUTHOR = 'gpt-6'


class ArrowLeftRight(Solo48):
    icon_id = 'arrow-left-right'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbols/standalone"
    aliases = ()
    keywords = ('arrows', 'left', 'right', 'horizontal', 'bidirectional', 'width', 'exchange', 'direction')

    def build(self) -> None:
        self.add_line('shaft', (4, 24), (44, 24))
        self.add_polyline('left-head', (20, 8), (4, 24), (20, 40))
        self.add_polyline('right-head', (28, 8), (44, 24), (28, 40))
        self.relate("connect", 'shaft', 'left-head')
        self.relate("connect", 'shaft', 'right-head')
