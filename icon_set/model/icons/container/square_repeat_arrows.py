"""Two opposing arrows form a square loop enclosure.

Keyshape SQUARE: visible (0,0)-(64,64), centerline extremes 2 and 62.
Reference: batch_16 supplied renders; Lucide repeat: quarter-circle turns and paired open arrowheads.
Rotational symmetry preserves the direction of the two arrows; duplicate references share one drawing.
Hosting (compose.py): plus passes, heart passes, check passes.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (square-repeat-arrows SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'claude-opus-5-5'


class SquareRepeatArrows(Container64):
    icon_id = 'square-repeat-arrows'
    keyshape = Keyshape.SQUARE
    aliases = ('square-repeating-loop-arrows',)
    keywords = ('square', 'repeat', 'arrows')

    def build(self) -> None:
        self.add_line('upper-0', (6, 38), (6, 20))
        self.add_arc('upper-1', (6, 20), (14, 12), radius_x=8)
        self.add_line('upper-2', (14, 12), (58, 12))
        self.add_line('lower-0', (58, 26), (58, 44))
        self.add_arc('lower-1', (58, 44), (50, 52), radius_x=8)
        self.add_line('lower-2', (50, 52), (6, 52))
        self.add_line('head-right-0', (52, 6), (58, 12))
        self.add_line('head-right-1', (58, 12), (52, 18))
        self.add_line('head-left-0', (12, 46), (6, 52))
        self.add_line('head-left-1', (6, 52), (12, 58))
        self.add_contour('upper', 'upper-0', 'upper-1', 'upper-2')
        self.add_contour('lower', 'lower-0', 'lower-1', 'lower-2')
        self.add_contour('head-right', 'head-right-0', 'head-right-1')
        self.add_contour('head-left', 'head-left-0', 'head-left-1')
        self.relate('connect', 'upper', 'head-right')
        self.relate('connect', 'lower', 'head-left')
