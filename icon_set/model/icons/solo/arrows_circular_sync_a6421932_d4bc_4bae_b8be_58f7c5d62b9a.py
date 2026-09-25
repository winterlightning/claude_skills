"""Circular Sync Arrows. Retains all identifying parts, reconstructed on the integer grid.

SQUARE visible extremes (4, 4, 44, 44); centerlines (6, 6, 42, 42).
Lucide rotate-cw and undo-2: coherent arcs, open arrowheads and explicit shaft joins.
Mirrored subjects use paired coordinates; directional parts preserve their
intentional asymmetry. Geometry is authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a6421932-d4bc-4bae-b8be-58f7c5d62b9a'
SOURCE_PATH = 'pictographic-primitives/symbol/arrows spin_a6421932-d4bc-4bae-b8be-58f7c5d62b9a.svg'
AUTHOR = 'gpt-6'


class ArrowsCircularSync(Solo48):
    icon_id = 'arrows-circular-sync'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    aliases = ()
    keywords = ('sync', 'refresh', 'reload', 'rotate', 'circular', 'arrows', 'repeat', 'update')

    def build(self) -> None:
        self.add_arc('upper-shaft', (6, 18), (42, 18), radius_x=18, radius_y=12, sweep=True)
        self.add_polyline('upper-head', (42, 6), (42, 18), (30, 18))
        self.relate("connect", 'upper-shaft', 'upper-head')
        self.add_arc('lower-shaft', (42, 30), (6, 30), radius_x=18, radius_y=12, sweep=True)
        self.add_polyline('lower-head', (6, 42), (6, 30), (18, 30))
        self.relate("connect", 'lower-shaft', 'lower-head')
