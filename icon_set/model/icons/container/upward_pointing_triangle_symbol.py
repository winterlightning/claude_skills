"""An empty upward triangle enclosure.

Keyshape HRECT_XL: (0, 4, 64, 60); chosen for the reference silhouette.
Construction reference: Lucide triangle: mirrored sloping sides and a horizontal base. Original and atomic-debug inspected.
Source sharp vertices retained as round stroke joins; 60 by 52 centerlines approximate an equilateral triangle.
Hosting measured with compose.py: plus does not pass, heart does not pass, check passes.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (upward-pointing-triangle-symbol HRECT_XL -> HRECT_L). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.

v3 (2026-10-07): redrawn for symbol room on v2 (container-combination64): the shape caps it below 24, now it takes a 16 symbol with a 4 px gap.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'claude-opus-5-5'


class UpwardPointingTriangleSymbol(Container64):
    icon_id = 'upward-pointing-triangle-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'container'
    categories = ('container',)
    aliases = ()
    keywords = ('upward', 'pointing', 'triangle', 'symbol')

    def build(self) -> None:
        # SQUARE (was HRECT_L): the triangle uses the full 52 x 52 square, apex (32,6), so its inscribed room
        # reaches 16 with a 4 px gap (was 15). A triangle cannot hold more inside the canvas.
        self.add_line('outline-1', (32, 6), (58, 58))
        self.add_line('outline-2', (58, 58), (6, 58))
        self.add_line('outline-3', (6, 58), (32, 6))
        self.add_contour('outline', 'outline-1', 'outline-2', 'outline-3', closed=True)
