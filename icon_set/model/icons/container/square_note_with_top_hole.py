"""A square hanging note with a circular eyelet centered on its top edge.

Keyshape SQUARE: visible (0,0)-(64,64), centerline extremes 2 and 62.
Reference: batch_16 supplied renders; Lucide square and circle: tangent rounded corners and complete circular eyelet.
All identity features retained.
Hosting (compose.py): plus does not fit, heart does not fit, check passes.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (square-note-with-top-hole SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'claude-opus-5-5'


class SquareNoteWithTopHole(Container64):
    icon_id = 'square-note-with-top-hole'
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ('square', 'note', 'with', 'top', 'hole')

    def build(self) -> None:
        self.add_arc('hole-0', (25, 13), (39, 13), radius_x=7)
        self.add_arc('hole-1', (39, 13), (25, 13), radius_x=7)
        self.add_line('frame-0', (25, 13), (12, 13))
        self.add_arc('frame-1', (12, 13), (6, 19), radius_x=6, sweep=False)
        self.add_line('frame-2', (6, 19), (6, 52))
        self.add_arc('frame-3', (6, 52), (12, 58), radius_x=6, sweep=False)
        self.add_line('frame-4', (12, 58), (52, 58))
        self.add_arc('frame-5', (52, 58), (58, 52), radius_x=6, sweep=False)
        self.add_line('frame-6', (58, 52), (58, 19))
        self.add_arc('frame-7', (58, 19), (52, 13), radius_x=6, sweep=False)
        self.add_line('frame-8', (52, 13), (39, 13))
        self.add_contour('hole', 'hole-0', 'hole-1', closed=True)
        self.add_contour('frame', 'frame-0', 'frame-1', 'frame-2', 'frame-3', 'frame-4', 'frame-5', 'frame-6', 'frame-7', 'frame-8')
        self.relate('connect', 'frame', 'hole')
