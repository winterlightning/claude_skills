"""Clockwise Circular Arrow. Retains all identifying parts, reconstructed on the integer grid.

SQUARE visible extremes (4, 4, 44, 44); centerlines (6, 6, 42, 42).
Lucide rotate-cw and undo-2: coherent arcs, open arrowheads and explicit shaft joins.
Mirrored subjects use paired coordinates; directional parts preserve their
intentional asymmetry. Geometry is authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b4e2a04a-d4a8-40d4-a5ea-cc2cb10d5181'
SOURCE_PATH = 'pictographic-primitives/symbol/arrow circular_b4e2a04a-d4a8-40d4-a5ea-cc2cb10d5181.svg'
AUTHOR = 'gpt-6'


class ArrowCircularClockwise(Solo48):
    icon_id = 'arrow-circular-clockwise'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbols/standalone"
    aliases = ()
    keywords = ('refresh', 'redo', 'reload', 'rotate', 'clockwise', 'arrow', 'circle', 'repeat')

    def build(self) -> None:
        self.add_arc('se', (42, 30), (24, 42), radius_x=18, radius_y=12, sweep=True)
        self.add_arc('sw', (24, 42), (6, 24), radius_x=18, radius_y=18, sweep=True)
        self.add_arc('nw', (6, 24), (24, 6), radius_x=18, radius_y=18, sweep=True)
        self.add_arc('ne', (24, 6), (42, 18), radius_x=18, radius_y=12, sweep=True)
        self.add_contour('shaft', 'se', 'sw', 'nw', 'ne')
        self.add_polyline('head', (42, 6), (42, 18), (30, 18))
        self.relate("connect", 'shaft', 'head')
