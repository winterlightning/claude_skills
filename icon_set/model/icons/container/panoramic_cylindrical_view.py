"""An open panoramic enclosure with curved rims and inward-facing side panels.

Keyshape SQUARE: (0, 0, 64, 64); authored from its exact extremes.
Reference: batch_10 source render. Lucide cylinder uses elliptical rims and vertical walls.
Mirrored panels preserve the open wraparound view; the detached rear rim remains separate.
Hosting measured with compose.py: plus: does not clear; heart: does not clear; check: does not clear.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (panoramic-cylindrical-view SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'claude-opus-5-5'


class PanoramicCylindricalView(Container64):
    icon_id = 'panoramic-cylindrical-view'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'container'
    categories = ('container',)
    aliases = ()
    keywords = ('panoramic', 'cylindrical', 'view')

    def build(self) -> None:
        self.add_arc('rear-rim', (6, 16), (58, 16), radius_x=26, radius_y=10)
        self.add_line('left-wall', (6, 24), (6, 48))
        self.add_arc('bottom-left', (6, 48), (32, 58), radius_x=26, radius_y=10, sweep=False)
        self.add_arc('bottom-right', (32, 58), (58, 48), radius_x=26, radius_y=10, sweep=False)
        self.add_line('right-wall', (58, 48), (58, 24))
        self.add_line('left-return-1', (6, 24), (16, 28))
        self.add_line('left-return-2', (16, 28), (16, 56))
        self.add_line('right-return-1', (58, 24), (48, 28))
        self.add_line('right-return-2', (48, 28), (48, 56))
        self.add_contour('outer', 'left-wall', 'bottom-left', 'bottom-right', 'right-wall')
        self.add_contour('left-return', 'left-return-1', 'left-return-2')
        self.add_contour('right-return', 'right-return-1', 'right-return-2')
        self.relate('connect', 'outer', 'left-return')
        self.relate('connect', 'outer', 'right-return')
