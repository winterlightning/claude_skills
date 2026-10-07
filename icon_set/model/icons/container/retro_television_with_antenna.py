"""A rounded television cabinet with paired aerials and splayed feet.

Keyshape SQUARE: (0, 0, 64, 64); preserves the reference proportions.
Reference: batch_11 source render; Lucide tv informs the V aerial and rounded cabinet.
Authored on the shared vertical axis except for directional subjects.
No decorative details added; all identifying source parts retained.
Hosting: plus does not clear, heart passes, check passes.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (retro-television-with-antenna SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.

v3 (2026-10-07): redrawn for symbol room on v2 (container-combination64): a symbol of at least 24 fits with a 4 px gap.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'claude-opus-5-5'


class RetroTelevisionWithAntenna(Container64):
    icon_id = 'retro-television-with-antenna'
    keyshape = Keyshape.SQUARE
    aliases = ('retro-tv', 'antenna-television')
    keywords = ('retro', 'television', 'with', 'antenna')

    def build(self) -> None:
        # Cabinet 12..52 (was 16..50) under a shorter aerial and on shorter feet, so the screen area holds a
        # symbol of 28 with a 4 px gap (was 22).
        self.add_line('cabinet0', (14, 12), (50, 12))
        self.add_arc('cabinet1', (50, 12), (58, 22), radius_x=8, radius_y=10)
        self.add_line('cabinet2', (58, 22), (58, 42))
        self.add_arc('cabinet3', (58, 42), (50, 52), radius_x=8, radius_y=10)
        self.add_line('cabinet4', (50, 52), (14, 52))
        self.add_arc('cabinet5', (14, 52), (6, 42), radius_x=8, radius_y=10)
        self.add_line('cabinet6', (6, 42), (6, 22))
        self.add_arc('cabinet7', (6, 22), (14, 12), radius_x=8, radius_y=10)
        self.add_line('aerial-1', (26, 6), (32, 12))
        self.add_line('aerial-2', (32, 12), (38, 6))
        self.add_line('foot-left', (20, 52), (17, 58))
        self.add_line('foot-right', (44, 52), (47, 58))
        self.add_contour('cabinet', 'cabinet0', 'cabinet1', 'cabinet2', 'cabinet3', 'cabinet4', 'cabinet5', 'cabinet6', 'cabinet7', closed=True)
        self.add_contour('aerial', 'aerial-1', 'aerial-2')
        self.relate('connect', 'aerial', 'cabinet')
        self.relate('connect', 'foot-left', 'cabinet')
        self.relate('connect', 'foot-right', 'cabinet')
