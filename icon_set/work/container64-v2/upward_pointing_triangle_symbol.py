"""An empty upward triangle enclosure.

Keyshape HRECT_XL: (0, 4, 64, 60); chosen for the reference silhouette.
Construction reference: Lucide triangle: mirrored sloping sides and a horizontal base. Original and atomic-debug inspected.
Source sharp vertices retained as round stroke joins; 60 by 52 centerlines approximate an equilateral triangle.
Hosting measured with compose.py: plus does not pass, heart does not pass, check passes.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (upward-pointing-triangle-symbol HRECT_XL -> HRECT_L). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

AUTHOR = 'claude-opus-5-5'


class UpwardPointingTriangleSymbol(Container64):
    icon_id = 'upward-pointing-triangle-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'container'
    categories = ('container',)
    aliases = ()
    keywords = ('upward', 'pointing', 'triangle', 'symbol')

    def build(self) -> None:
        self.add_line('outline-1', (32, 10), (60, 54))
        self.add_line('outline-2', (60, 54), (4, 54))
        self.add_line('outline-3', (4, 54), (32, 10))
        self.add_contour('outline', 'outline-1', 'outline-2', 'outline-3', closed=True)
