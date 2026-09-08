"""Two opposing arrows form a square loop enclosure.

Keyshape SQUARE: visible (0,0)-(64,64), centerline extremes 2 and 62.
Reference: batch_16 supplied renders; Lucide repeat: quarter-circle turns and paired open arrowheads.
Rotational symmetry preserves the direction of the two arrows; duplicate references share one drawing.
Hosting (compose.py): plus passes, heart passes, check passes.
"""

from ...keyshapes import Keyshape
from ._base import Container64


class SquareRepeatArrows(Container64):
    icon_id = 'square-repeat-arrows'
    keyshape = Keyshape.SQUARE
    aliases = ('square-repeating-loop-arrows',)
    keywords = ('square', 'repeat', 'arrows')

    def build(self) -> None:
        self.add_line('upper-0', (2, 42), (2, 16))
        self.add_arc('upper-1', (2, 16), (10, 8), radius_x=8, radius_y=8, sweep=True)
        self.add_line('upper-2', (10, 8), (62, 8))
        self.add_contour('upper', 'upper-0', 'upper-1', 'upper-2', closed=False)
        self.add_line('lower-0', (62, 22), (62, 48))
        self.add_arc('lower-1', (62, 48), (54, 56), radius_x=8, radius_y=8, sweep=True)
        self.add_line('lower-2', (54, 56), (2, 56))
        self.add_contour('lower', 'lower-0', 'lower-1', 'lower-2', closed=False)
        self.add_line('head-right-0', (56, 2), (62, 8))
        self.add_line('head-right-1', (62, 8), (56, 14))
        self.add_contour('head-right', 'head-right-0', 'head-right-1', closed=False)
        self.relate("connect", 'upper', 'head-right')
        self.add_line('head-left-0', (8, 50), (2, 56))
        self.add_line('head-left-1', (2, 56), (8, 62))
        self.add_contour('head-left', 'head-left-0', 'head-left-1', closed=False)
        self.relate("connect", 'lower', 'head-left')
