"""A square hanging note with a circular eyelet centered on its top edge.

Keyshape SQUARE: visible (0,0)-(64,64), centerline extremes 2 and 62.
Reference: batch_16 supplied renders; Lucide square and circle: tangent rounded corners and complete circular eyelet.
All identity features retained.
Hosting (compose.py): plus does not fit, heart does not fit, check passes.
"""

from ...keyshapes import Keyshape
from ._base import Container64


class SquareNoteWithTopHole(Container64):
    icon_id = 'square-note-with-top-hole'
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ('square', 'note', 'with', 'top', 'hole')

    def build(self) -> None:
        self.add_arc('hole-0', (25, 9), (39, 9), radius_x=7, radius_y=7, sweep=True)
        self.add_arc('hole-1', (39, 9), (25, 9), radius_x=7, radius_y=7, sweep=True)
        self.add_contour('hole', 'hole-0', 'hole-1', closed=True)
        self.add_line('frame-0', (25, 9), (8, 9))
        self.add_arc('frame-1', (8, 9), (2, 15), radius_x=6, radius_y=6, sweep=False)
        self.add_line('frame-2', (2, 15), (2, 56))
        self.add_arc('frame-3', (2, 56), (8, 62), radius_x=6, radius_y=6, sweep=False)
        self.add_line('frame-4', (8, 62), (56, 62))
        self.add_arc('frame-5', (56, 62), (62, 56), radius_x=6, radius_y=6, sweep=False)
        self.add_line('frame-6', (62, 56), (62, 15))
        self.add_arc('frame-7', (62, 15), (56, 9), radius_x=6, radius_y=6, sweep=False)
        self.add_line('frame-8', (56, 9), (39, 9))
        self.add_contour('frame', 'frame-0', 'frame-1', 'frame-2', 'frame-3', 'frame-4', 'frame-5', 'frame-6', 'frame-7', 'frame-8', closed=False)
        self.relate("connect", 'frame', 'hole')
